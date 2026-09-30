from __future__ import annotations
import ast
from functools import lru_cache
import numpy as np
import pandas as pd
from . import indicators

ALLOWED_FUNCS = {
    name: getattr(indicators, name) for name in dir(indicators)
    if not name.startswith('_') and callable(getattr(indicators, name))
}

class UnsafeExpression(ValueError): pass

_ALLOWED_NODES=(ast.Expression, ast.BoolOp, ast.And, ast.Or, ast.Compare, ast.Gt, ast.GtE, ast.Lt, ast.LtE, ast.Eq, ast.NotEq,
                ast.BinOp, ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.Mod, ast.UnaryOp, ast.USub, ast.UAdd,
                ast.Name, ast.Load, ast.Call, ast.Constant, ast.BitAnd, ast.BitOr)


def _combine_bool(op, values):
    if not values: return True
    out=values[0]
    for v in values[1:]: out=(out & v) if isinstance(op,ast.And) else (out | v)
    return out


@lru_cache(maxsize=512)
def _compiled(expr: str) -> ast.Expression:
    tree=ast.parse(expr, mode='eval')
    for node in ast.walk(tree):
        if not isinstance(node,_ALLOWED_NODES):
            raise UnsafeExpression(f"Unsupported syntax: {type(node).__name__}")
        if isinstance(node,ast.Call):
            if not isinstance(node.func,ast.Name) or node.func.id not in ALLOWED_FUNCS:
                raise UnsafeExpression("Only whitelisted indicator functions are allowed")
    return tree


def evaluate(expr: str, df: pd.DataFrame) -> pd.Series:
    tree=_compiled(expr)
    env={c: df[c] for c in df.columns if c in {'open','high','low','close','volume'}}
    env.update(ALLOWED_FUNCS)

    def ev(n):
        if isinstance(n,ast.Expression): return ev(n.body)
        if isinstance(n,ast.Constant): return n.value
        if isinstance(n,ast.Name):
            if n.id not in env: raise UnsafeExpression(f"Unknown name {n.id}")
            return env[n.id]
        if isinstance(n,ast.Call): return env[n.func.id](*[ev(a) for a in n.args], **{kw.arg:ev(kw.value) for kw in n.keywords})
        if isinstance(n,ast.UnaryOp): return -ev(n.operand) if isinstance(n.op,ast.USub) else ev(n.operand)
        if isinstance(n,ast.BinOp):
            a,b=ev(n.left),ev(n.right)
            if isinstance(n.op,ast.Add): return a+b
            if isinstance(n.op,ast.Sub): return a-b
            if isinstance(n.op,ast.Mult): return a*b
            if isinstance(n.op,ast.Div): return a/b
            if isinstance(n.op,ast.Pow): return a**b
            if isinstance(n.op,ast.Mod): return a%b
            if isinstance(n.op,ast.BitAnd): return a & b
            if isinstance(n.op,ast.BitOr): return a | b
        if isinstance(n,ast.Compare):
            left=ev(n.left); out=None
            for op,rightn in zip(n.ops,n.comparators):
                right=ev(rightn)
                if isinstance(op,ast.Gt): cur=left>right
                elif isinstance(op,ast.GtE): cur=left>=right
                elif isinstance(op,ast.Lt): cur=left<right
                elif isinstance(op,ast.LtE): cur=left<=right
                elif isinstance(op,ast.Eq): cur=left==right
                elif isinstance(op,ast.NotEq): cur=left!=right
                out=cur if out is None else (out & cur)
                left=right
            return out
        if isinstance(n,ast.BoolOp): return _combine_bool(n.op,[ev(v) for v in n.values])
        raise UnsafeExpression(f"Unhandled node {type(n).__name__}")
    out=ev(tree).astype(bool)
    return out.fillna(False)

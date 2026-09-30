# Strategy performance cards

All 738 survivors. Headline per card = **combined OOS gain** `(1+eng_val)(1+eng_test)-1` at 40/10 bps. Full-history figures include data before 2024-08-01 (in-sample).


## 1111

### Z-Score RSI (1571) — Daily
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.043015824680755266 | 0.3424502324819869 |
| alpha | 0.43354579861646325 | 0.49443886884562327 |
| trades | 21 | 11 |
| winrate | 0.38095238095238093 | 0.5454545454545454 |
| sharpe | 0.247400540666677 | 1.9300725504657315 |
| maxdd | -0.2877036737262296 | -0.10777828839134407 |
| pf | 1.0828099481969977 | 5.046883435058199 |
| ann | 0.030201428348926473 | 0.5052993451336818 |

- **Combined OOS gain (stress):** 40.020%
- Full history @ stress: total 354.071%, CAGR 37.185%, benchmark 1.186%, sharpe 1.57, maxdd -0.288, trades 71

### EF Distance Reversal (2081) — 1h **(pick)**
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.0656738165600006 | 0.3110805641318257 |
| alpha | 0.44549837796350933 | 0.46666755140198135 |
| trades | 6 | 5 |
| winrate | 0.6666666666666666 | 0.6 |
| sharpe | 0.8333379190587471 | 2.205958607744648 |
| maxdd | -0.042141268223999995 | -0.07886044934292802 |
| pf | 3.733749169226677 | 20.580636053579152 |
| ann | 0.045962233185987245 | 0.4566718045010072 |

- **Combined OOS gain (stress):** 39.718%
- Full history @ stress: total 39.718%, CAGR 17.193%, benchmark -47.632%, sharpe 1.45, maxdd -0.079, trades 11

### Bull vs Medved (2510) — 1h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.14918463329200704 | 0.1873124719666417 |
| alpha | 0.5290091946955158 | 0.3428994592367973 |
| trades | 58 | 30 |
| winrate | 0.3793103448275862 | 0.43333333333333335 |
| sharpe | 0.6582815110992134 | 1.1317613293839326 |
| maxdd | -0.21983454759888998 | -0.11831640390166875 |
| pf | 1.3165875543168448 | 1.4734503360874334 |
| ann | 0.10322520209315988 | 0.2692719014027585 |

- **Combined OOS gain (stress):** 36.444%
- Full history @ stress: total 36.444%, CAGR 15.882%, benchmark -47.632%, sharpe 0.84, maxdd -0.220, trades 88

### Explosion Range Expansion (3263) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.039809807164005395 | 0.17421031165118905 |
| alpha | 0.4196343685675141 | 0.3303940572342279 |
| trades | 64 | 34 |
| winrate | 0.3125 | 0.23529411764705882 |
| sharpe | 0.25098392510307327 | 1.1015044610750697 |
| maxdd | -0.2612554827121101 | -0.1567308992007257 |
| pf | 1.0784003122464794 | 1.4480844594300009 |
| ann | 0.027963258952186987 | 0.2498615995092235 |

- **Combined OOS gain (stress):** 22.096%
- Full history @ stress: total 22.096%, CAGR 9.933%, benchmark -47.632%, sharpe 0.59, maxdd -0.261, trades 98

### Long Explosive V1 (992) — 1h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.08879089820800457 | 0.16973255932628017 |
| alpha | 0.4686154596115133 | 0.3253195465964358 |
| trades | 42 | 24 |
| winrate | 0.38095238095238093 | 0.4583333333333333 |
| sharpe | 0.4202502977294253 | 1.1055529164262898 |
| maxdd | -0.19982519608150884 | -0.1031980769588372 |
| pf | 1.1476869638362093 | 1.5217882810210503 |
| ann | 0.061941335970773004 | 0.24324723281065963 |

- **Combined OOS gain (stress):** 27.359%
- Full history @ stress: total 27.359%, CAGR 12.156%, benchmark -47.632%, sharpe 0.68, maxdd -0.200, trades 66

## 1182

### I Trend (2061) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.19167953565840623 | 0.01287376334108048 |
| alpha | 0.21945731343618402 | 0.2630995989327697 |
| trades | 50 | 28 |
| winrate | 0.42 | 0.4642857142857143 |
| sharpe | 0.8000862691537566 | 0.2010539152276679 |
| maxdd | -0.21017889592372907 | -0.06580604173010407 |
| pf | 1.3117055459381723 | 1.3147896128020315 |
| ann | 0.13189235558411516 | 0.017923493191802864 |

- **Combined OOS gain (stress):** 20.702%
- Full history @ stress: total 25.445%, CAGR 11.353%, benchmark -23.148%, sharpe 0.73, maxdd -0.210, trades 78

### Hercules A.T.C. 2006 (2485) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.21368798425240576 | 0.03632367349632881 |
| alpha | 0.24146576203018355 | 0.286549509088018 |
| trades | 47 | 20 |
| winrate | 0.40425531914893614 | 0.35 |
| sharpe | 1.0268851906540444 | 0.5866560682744945 |
| maxdd | -0.12699033598518772 | -0.04686009995784779 |
| pf | 1.4587196986680884 | 1.3436356701461487 |
| ann | 0.14662108672028396 | 0.05079930992896231 |

- **Combined OOS gain (stress):** 25.777%
- Full history @ stress: total 25.777%, CAGR 11.493%, benchmark -23.148%, sharpe 0.90, maxdd -0.127, trades 67

### The 20s Breakout (2986) — 4h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.4046716184964054 | 0.015222912375401298 |
| alpha | 0.4324493962741832 | 0.2654487479670905 |
| trades | 46 | 27 |
| winrate | 0.41304347826086957 | 0.4074074074074074 |
| sharpe | 1.656784019799953 | 0.2443844878177304 |
| maxdd | -0.11137679971113068 | -0.08261204494734897 |
| pf | 1.951966077458417 | 1.339305951923416 |
| ann | 0.27133090474530586 | 0.021203694729119205 |

- **Combined OOS gain (stress):** 42.605%
- Full history @ stress: total 48.209%, CAGR 20.519%, benchmark -23.148%, sharpe 1.36, maxdd -0.111, trades 73

### 5 EMA No-Touch Breakout (483) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.23617286870280885 | -0.01182935327767598 |
| alpha | 0.26395064648058664 | 0.23839648231401322 |
| trades | 55 | 30 |
| winrate | 0.4 | 0.43333333333333335 |
| sharpe | 1.0665292890828706 | -0.08538374466554705 |
| maxdd | -0.13788503029056165 | -0.1048207125716174 |
| pf | 1.4140697133005793 | 1.1371140345808084 |
| ann | 0.16158792839872427 | -0.016390538869337612 |

- **Combined OOS gain (stress):** 22.155%
- Full history @ stress: total 26.955%, CAGR 11.987%, benchmark -23.148%, sharpe 0.85, maxdd -0.152, trades 85

### Logistic RSI STOCH ROC AO (988) — 4h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.3036123723252053 | 0.007372666846096054 |
| alpha | 0.3313901501029831 | 0.25759850243778526 |
| trades | 38 | 21 |
| winrate | 0.42105263157894735 | 0.23809523809523808 |
| sharpe | 1.2069584062828296 | 0.14360524833263447 |
| maxdd | -0.0700842267389683 | -0.06924055647681138 |
| pf | 1.9196347312838742 | 1.0595895132253794 |
| ann | 0.20600763710171122 | 0.010253688824529705 |

- **Combined OOS gain (stress):** 31.322%
- Full history @ stress: total 31.322%, CAGR 13.798%, benchmark -23.148%, sharpe 0.90, maxdd -0.078, trades 59

## 1183

### Previous Candle Breakdown (2875) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.32624232446760426 | -0.023211593083757642 |
| alpha | 0.3274618366627262 | 0.21801150997399998 |
| trades | 25 | 9 |
| winrate | 0.44 | 0.3333333333333333 |
| sharpe | 1.1725669845200586 | -0.37493138376814905 |
| maxdd | -0.1526236551051966 | -0.07854067487442129 |
| pf | 1.9465705970792888 | 0.7580848115713628 |
| ann | 0.22076080453260793 | -0.0320897250192248 |

- **Combined OOS gain (stress):** 29.546%
- Full history @ stress: total 29.546%, CAGR 13.455%, benchmark -18.293%, sharpe 0.84, maxdd -0.172, trades 34

### Manual EA (3936) — 15min
> family: mean_reversion | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.095588651205603 | 0.0833709876485309 |
| alpha | 0.09068067574548033 | 0.290002130336512 |
| trades | 25 | 14 |
| winrate | 0.64 | 0.7142857142857143 |
| sharpe | 0.39140343353645923 | 0.5805728724072052 |
| maxdd | -0.20587086406652322 | -0.16672663287660272 |
| pf | 1.1381797779345757 | 1.5226104795607438 |
| ann | 0.06662110108614816 | 0.11762985662677528 |

- **Combined OOS gain (stress):** 18.693%
- Full history @ stress: total 22.403%, CAGR 10.360%, benchmark -17.791%, sharpe 0.51, maxdd -0.206, trades 39

### VmMatrix Double Zero (4213) — 4h **(pick)**
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.42641261694640176 | -0.011066202384126478 |
| alpha | 0.4276321291415237 | 0.23015690067363115 |
| trades | 17 | 6 |
| winrate | 0.47058823529411764 | 0.3333333333333333 |
| sharpe | 1.6815835467783324 | -0.1843857182716533 |
| maxdd | -0.05626170211603854 | -0.05510818041037424 |
| pf | 8.04256980606797 | 0.7169303124248138 |
| ann | 0.2852010778601457 | -0.015335421371742375 |

- **Combined OOS gain (stress):** 41.063%
- Full history @ stress: total 41.063%, CAGR 18.266%, benchmark -18.293%, sharpe 1.26, maxdd -0.056, trades 23

### 80-20 (488) — Daily
> family: pattern | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.603815644692048 | -0.02787791197795475 |
| alpha | 0.5502442161206194 | 0.20067706787236195 |
| trades | 20 | 7 |
| winrate | 0.6 | 0.42857142857142855 |
| sharpe | 1.3425266244009613 | -0.3239238798386402 |
| maxdd | -0.13563049103417857 | -0.061784522137080966 |
| pf | 2.1998450887542313 | 0.6149152333331482 |
| ann | 0.39616725867025027 | -0.038505359409115036 |

- **Combined OOS gain (stress):** 55.910%
- Full history @ stress: total 15.666%, CAGR 3.346%, benchmark -48.462%, sharpe 0.27, maxdd -0.317, trades 59

## 1202

### Timer (1788) — 1h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.0904869614843935 | 0.1937778699981776 |
| alpha | 0.3774716948463559 | 0.4145090129875344 |
| trades | 56 | 27 |
| winrate | 0.39285714285714285 | 0.5555555555555556 |
| sharpe | -0.22440732132935493 | 1.252513717750795 |
| maxdd | -0.2505787443956591 | -0.1156953596658119 |
| pf | 0.879076389249414 | 1.808706046198138 |
| ann | -0.0648110962649795 | 0.27888090477993654 |

- **Combined OOS gain (stress):** 8.576%
- Full history @ stress: total 10.602%, CAGR 4.896%, benchmark -56.486%, sharpe 0.33, maxdd -0.280, trades 83

### Expert MACD EURUSD 1 Hour (2431) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.012106274348793855 | 0.164952424554073 |
| alpha | 0.4474737781446445 | 0.40054025932484016 |
| trades | 48 | 26 |
| winrate | 0.3541666666666667 | 0.5 |
| sharpe | 0.041440990188957985 | 1.145985440953705 |
| maxdd | -0.14184074746076658 | -0.07242921634708921 |
| pf | 0.9779341362551754 | 1.7731260175856234 |
| ann | -0.008568112817264883 | 0.2361970542262284 |

- **Combined OOS gain (stress):** 15.085%
- Full history @ stress: total 19.237%, CAGR 8.704%, benchmark -55.801%, sharpe 0.53, maxdd -0.153, trades 74

### Hercules A.T.C. 2006 (2485) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.08566969765760479 | 0.1923580665778748 |
| alpha | 0.5452497501510432 | 0.42794590134864197 |
| trades | 47 | 22 |
| winrate | 0.3829787234042553 | 0.5454545454545454 |
| sharpe | 0.4251053423137116 | 1.681950375433178 |
| maxdd | -0.20690906724864133 | -0.0478629640080348 |
| pf | 1.1747203350894637 | 2.2671653113714356 |
| ann | 0.05978974208524512 | 0.2767690267620706 |

- **Combined OOS gain (stress):** 29.451%
- Full history @ stress: total 29.451%, CAGR 13.026%, benchmark -55.801%, sharpe 0.81, maxdd -0.207, trades 69

### Bull vs Medved (2510) — 1h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.031852130191193706 | 0.22480512729427526 |
| alpha | 0.4361065261395557 | 0.4455362702836321 |
| trades | 49 | 27 |
| winrate | 0.3673469387755102 | 0.4444444444444444 |
| sharpe | -0.03631743958347389 | 1.4621849739817143 |
| maxdd | -0.20171494703978943 | -0.15135993850581198 |
| pf | 1.0110321191707223 | 1.931034143564032 |
| ann | -0.022609547230796112 | 0.3252748926237634 |

- **Combined OOS gain (stress):** 18.579%
- Full history @ stress: total 24.477%, CAGR 10.945%, benchmark -56.486%, sharpe 0.63, maxdd -0.205, trades 76

### Demo GPT - Day Trading Scalping (675) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.0379118462703929 | 0.21532516668844104 |
| alpha | 0.42166820622304546 | 0.4509130014592082 |
| trades | 54 | 24 |
| winrate | 0.35185185185185186 | 0.5833333333333334 |
| sharpe | -0.045898538037478544 | 1.7098203587472924 |
| maxdd | -0.1920315497055668 | -0.05816673266998307 |
| pf | 0.9364831372136809 | 1.9860522400245963 |
| ann | -0.026935464288475708 | 0.3110507852334745 |

- **Combined OOS gain (stress):** 16.925%
- Full history @ stress: total 16.925%, CAGR 7.699%, benchmark -55.801%, sharpe 0.49, maxdd -0.192, trades 78

## 1210

### Renko RSI (1242) — Daily
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | -0.08173030528978742 | 0.06081150587385409 |
| alpha | 0.08504493900988686 | 0.15030566929797862 |
| trades | 12 | 5 |
| winrate | 0.75 | 0.4 |
| sharpe | -0.23690475865820695 | 0.5873321014971327 |
| maxdd | -0.2614134850758072 | -0.1376447728279977 |
| pf | 1.0516979020712467 | 0.5283116630890848 |
| ann | -0.05845900327030107 | 0.08544027813972588 |

- **Combined OOS gain (stress):** -2.589%
- Full history @ stress: total 12.333%, CAGR 0.639%, benchmark -68.207%, sharpe 0.16, maxdd -0.616, trades 156

### Smoothing Average (1968) — 4h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.135865405775202 | 0.13242773858619472 |
| alpha | 0.2640884022908815 | 0.22404264541849295 |
| trades | 14 | 9 |
| winrate | 0.7142857142857143 | 0.6666666666666666 |
| sharpe | 0.801283114548207 | 1.3856327561062285 |
| maxdd | -0.07202417287530405 | -0.04138399089160394 |
| pf | 2.441879709971485 | 5.490074792822911 |
| ann | 0.09417632084286631 | 0.1885265210155791 |

- **Combined OOS gain (stress):** 28.629%
- Full history @ stress: total 27.390%, CAGR 12.168%, benchmark -18.467%, sharpe 0.97, maxdd -0.110, trades 23

### I Gap (2145) — 4h
> family: volatility | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.068433065624391 | 0.09902240777087168 |
| alpha | 0.05978993089128848 | 0.1906373146031699 |
| trades | 81 | 31 |
| winrate | 0.4567901234567901 | 0.3225806451612903 |
| sharpe | -0.24051221137505274 | 0.9399593389211175 |
| maxdd | -0.15704529453979799 | -0.06700178837081538 |
| pf | 0.8932405472197685 | 1.3724275821351501 |
| ann | -0.04884704349552105 | 0.1401164366924923 |

- **Combined OOS gain (stress):** 2.381%
- Full history @ stress: total 2.381%, CAGR 1.123%, benchmark -18.467%, sharpe 0.15, maxdd -0.157, trades 112

### Expert MACD EURUSD 1 Hour (2431) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.06515605915000555 | 0.08415780942519535 |
| alpha | 0.19337905566568503 | 0.17577271625749358 |
| trades | 48 | 24 |
| winrate | 0.4166666666666667 | 0.4583333333333333 |
| sharpe | 0.3970858553786578 | 0.7838603380585031 |
| maxdd | -0.1482492746877787 | -0.11264533360950157 |
| pf | 1.161817357421899 | 1.3171064166521456 |
| ann | 0.045603188349881085 | 0.11875729533718449 |

- **Combined OOS gain (stress):** 15.480%
- Full history @ stress: total 14.368%, CAGR 6.575%, benchmark -18.467%, sharpe 0.51, maxdd -0.148, trades 72

### Explosion Range Expansion (3263) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.10438452130080833 | 0.04611323324997274 |
| alpha | 0.2326075178164878 | 0.13772814008227097 |
| trades | 67 | 41 |
| winrate | 0.3880597014925373 | 0.3170731707317073 |
| sharpe | 0.6406184870913139 | 0.4802353866291744 |
| maxdd | -0.14078518825219233 | -0.06600564399633235 |
| pf | 1.26522035053765 | 1.148412486276283 |
| ann | 0.07266379906503229 | 0.06461005910475182 |

- **Combined OOS gain (stress):** 15.531%
- Full history @ stress: total 15.531%, CAGR 7.088%, benchmark -18.467%, sharpe 0.57, maxdd -0.141, trades 108

## 1212

### Anubis (2676) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.15259550980800363 | 0.1796671706915285 |
| alpha | 0.2568701212069673 | 0.2622942893355962 |
| trades | 28 | 16 |
| winrate | 0.42857142857142855 | 0.25 |
| sharpe | 0.5277502972680113 | 1.4217143862942359 |
| maxdd | -0.26358761120001606 | -0.12318403402580103 |
| pf | 1.1994234218905024 | 2.1023583004651525 |
| ann | 0.10553753876146166 | 0.2579355305467106 |

- **Combined OOS gain (stress):** 35.968%
- Full history @ stress: total 39.222%, CAGR 16.995%, benchmark -15.868%, sharpe 0.79, maxdd -0.264, trades 44

### Crossing of Two iMA v2 (2810) — Daily
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.18223727488306873 | 0.14586955549156766 |
| alpha | 0.2739039415497355 | 0.22131439534921882 |
| trades | 25 | 8 |
| winrate | 0.44 | 0.5 |
| sharpe | 0.7143130332821847 | 1.668500394206675 |
| maxdd | -0.12561466459373583 | -0.10785779582688126 |
| pf | 1.3493920502249006 | 2.8097281032864343 |
| ann | 0.12554887265032222 | 0.20816416422800654 |

- **Combined OOS gain (stress):** 35.469%
- Full history @ stress: total 441.021%, CAGR 9.781%, benchmark 222.039%, sharpe 0.57, maxdd -0.403, trades 275

### Moving Average Shift (3901) — 4h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.20746412883600418 | 0.20809908905842867 |
| alpha | 0.31173874023496784 | 0.29072620770249635 |
| trades | 39 | 19 |
| winrate | 0.41025641025641024 | 0.3157894736842105 |
| sharpe | 0.7509754923110555 | 1.5749828913281358 |
| maxdd | -0.13776086260251763 | -0.12488121784964257 |
| pf | 1.4115867399022928 | 2.397226724985439 |
| ann | 0.14246390032528655 | 0.3002374103695611 |

- **Combined OOS gain (stress):** 45.874%
- Full history @ stress: total 49.366%, CAGR 20.964%, benchmark -15.868%, sharpe 1.05, maxdd -0.138, trades 58

### BONK Long Volatility (598) — Daily
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.06852148127863966 | 0.10889992079725852 |
| alpha | 0.16018814794530645 | 0.18434476065490968 |
| trades | 18 | 7 |
| winrate | 0.4444444444444444 | 0.42857142857142855 |
| sharpe | 0.3289684247445881 | 1.362129598868442 |
| maxdd | -0.23643200000292453 | -0.09408880772052863 |
| pf | 1.0850009922759591 | 2.2990881885512806 |
| ann | 0.047936064753298036 | 0.1543719040562328 |

- **Combined OOS gain (stress):** 18.488%
- Full history @ stress: total 536.729%, CAGR 10.774%, benchmark 222.039%, sharpe 0.59, maxdd -0.371, trades 215

## 1214

### Hoop Master (3162) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.2013547398944875 | 0.20929902723805194 |
| alpha | 0.4618585769745104 | 0.4807140736836276 |
| trades | 24 | 13 |
| winrate | 0.625 | 0.46153846153846156 |
| sharpe | 0.7968145309159899 | 1.0602879893253812 |
| maxdd | -0.11921333850087812 | -0.10381201238127391 |
| pf | 2.604439433248383 | 2.1304549132458805 |
| ann | 0.1383770495578054 | 0.3020313064313416 |

- **Combined OOS gain (stress):** 45.280%
- Full history @ stress: total 55.348%, CAGR 23.238%, benchmark -42.403%, sharpe 1.03, maxdd -0.119, trades 37

### Fast Slow RVI Crossover (3520) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.19438130401444864 | 0.15502237806382202 |
| alpha | 0.45488514109447153 | 0.4264374245093977 |
| trades | 60 | 30 |
| winrate | 0.43333333333333335 | 0.4 |
| sharpe | 0.7135354484337302 | 0.7954691768199083 |
| maxdd | -0.1779994373040783 | -0.1392019135624304 |
| pf | 1.320671538549517 | 1.5100665534349116 |
| ann | 0.13370473470529332 | 0.22158727017080393 |

- **Combined OOS gain (stress):** 37.954%
- Full history @ stress: total 41.317%, CAGR 17.827%, benchmark -42.403%, sharpe 0.78, maxdd -0.178, trades 90

### Balance of Power (546) — 1h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.172942289976721 | 0.2689511485582865 |
| alpha | 0.4530951793536546 | 0.5335857508931756 |
| trades | 52 | 20 |
| winrate | 0.4230769230769231 | 0.5 |
| sharpe | 0.6621304848696439 | 1.17756635862588 |
| maxdd | -0.19289697454833932 | -0.08219058909978172 |
| pf | 1.2513558696781266 | 2.0729826639484585 |
| ann | 0.1192897911132349 | 0.39207473314983887 |

- **Combined OOS gain (stress):** 48.841%
- Full history @ stress: total 53.619%, CAGR 22.586%, benchmark -43.934%, sharpe 0.93, maxdd -0.197, trades 72

### Futures Engulfing Candle Size (823) — 4h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.21036857983876778 | 0.17945888678823518 |
| alpha | 0.47087241691879067 | 0.45087393323381086 |
| trades | 69 | 28 |
| winrate | 0.42028985507246375 | 0.35714285714285715 |
| sharpe | 0.7661589781372485 | 0.8918823283854473 |
| maxdd | -0.10381984894053031 | -0.134017267488318 |
| pf | 1.3301445079798455 | 1.5973130673014106 |
| ann | 0.14440469147017243 | 0.2576270880798823 |

- **Combined OOS gain (stress):** 42.758%
- Full history @ stress: total 46.238%, CAGR 19.756%, benchmark -42.403%, sharpe 0.85, maxdd -0.134, trades 97

### Long Explosive V1 (992) — 4h **(pick)**
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.4883047682382591 | 0.24764269928990856 |
| alpha | 0.748808605318282 | 0.5190577457354842 |
| trades | 50 | 22 |
| winrate | 0.48 | 0.36363636363636365 |
| sharpe | 1.6112395806354471 | 1.1722583623493101 |
| maxdd | -0.0868534621588013 | -0.09310185963915929 |
| pf | 1.7815159286583018 | 2.0081420965787795 |
| ann | 0.32435160163958754 | 0.359716924583519 |

- **Combined OOS gain (stress):** 85.687%
- Full history @ stress: total 90.214%, CAGR 35.662%, benchmark -42.403%, sharpe 1.43, maxdd -0.093, trades 72

## 1301

### US Index First 30m Candle (1515) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.5055481519740097 | 0.2708890572662621 |
| alpha | 0.8014862564227525 | 0.39608549519187763 |
| trades | 51 | 32 |
| winrate | 0.45098039215686275 | 0.34375 |
| sharpe | 1.748719344864626 | 1.681567787382844 |
| maxdd | -0.13544374320641428 | -0.14794320593955712 |
| pf | 2.0417939926765816 | 2.0845752371300295 |
| ann | 0.3351733689512839 | 0.3950280789996903 |

- **Combined OOS gain (stress):** 91.338%
- Full history @ stress: total 91.338%, CAGR 36.042%, benchmark -35.397%, sharpe 1.72, maxdd -0.148, trades 83

### Exp Moving Average FN (1992) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.11907724474040493 | 0.3279717485993039 |
| alpha | 0.41501534918914773 | 0.4531681865249194 |
| trades | 36 | 16 |
| winrate | 0.3055555555555556 | 0.625 |
| sharpe | 0.5844014729619819 | 1.9724170287471787 |
| maxdd | -0.13838668765199313 | -0.07325658041667737 |
| pf | 1.3087871287944224 | 4.750658845168728 |
| ann | 0.08272619375246948 | 0.48280005802990966 |

- **Combined OOS gain (stress):** 48.610%
- Full history @ stress: total 48.610%, CAGR 20.673%, benchmark -35.397%, sharpe 1.13, maxdd -0.138, trades 52

### Anands (521) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.3189010392344047 | 0.29945832362772684 |
| alpha | 0.6148391436831475 | 0.42465476155334236 |
| trades | 32 | 20 |
| winrate | 0.375 | 0.55 |
| sharpe | 1.2547826122621253 | 1.8333347331990137 |
| maxdd | -0.16775768171007766 | -0.0552559018165969 |
| pf | 1.5890491838087115 | 3.273479104215341 |
| ann | 0.21598294932396578 | 0.43876960945904786 |

- **Combined OOS gain (stress):** 71.386%
- Full history @ stress: total 71.386%, CAGR 29.118%, benchmark -35.397%, sharpe 1.47, maxdd -0.173, trades 52

### Futures Engulfing Candle Size (823) — 4h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.5599184350448076 | 0.3034360631889226 |
| alpha | 0.8558565394935505 | 0.4286325011145381 |
| trades | 62 | 31 |
| winrate | 0.46774193548387094 | 0.41935483870967744 |
| sharpe | 1.8455486166428234 | 1.7567560106775997 |
| maxdd | -0.08831305182794558 | -0.08002635707300254 |
| pf | 2.2026241978126477 | 2.294717827444678 |
| ann | 0.3690602587659644 | 0.44488970087662927 |

- **Combined OOS gain (stress):** 103.325%
- Full history @ stress: total 106.545%, CAGR 41.068%, benchmark -35.397%, sharpe 1.83, maxdd -0.088, trades 93

### Long Explosive V1 (992) — 4h **(pick)**
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.20027135551720576 | 0.3269823734904451 |
| alpha | 0.49620945996594856 | 0.45217881141606064 |
| trades | 43 | 23 |
| winrate | 0.3488372093023256 | 0.43478260869565216 |
| sharpe | 0.8928704767485549 | 1.9614256627310789 |
| maxdd | -0.1379116505800848 | -0.09163652058183092 |
| pf | 1.3221187562640568 | 2.437450813671032 |
| ann | 0.13765168787164161 | 0.4812660546982215 |

- **Combined OOS gain (stress):** 59.274%
- Full history @ stress: total 61.796%, CAGR 25.639%, benchmark -35.397%, sharpe 1.35, maxdd -0.138, trades 66

## 1302

### Kalman Filter Candles (2152) — 1h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.6132436513816213 | 0.08903872493327336 |
| alpha | 0.3345034939013065 | 0.3859574924402761 |
| trades | 123 | 59 |
| winrate | 0.42276422764227645 | 0.4406779661016949 |
| sharpe | 1.5456377591124368 | 0.6952313009271337 |
| maxdd | -0.22254578283654047 | -0.16351643201954558 |
| pf | 1.480282935090211 | 1.231498107340953 |
| ann | 0.40196059410596763 | 0.1257582732267104 |

- **Combined OOS gain (stress):** 75.688%
- Full history @ stress: total 74.632%, CAGR 30.272%, benchmark -7.769%, sharpe 1.27, maxdd -0.224, trades 182

### Bull vs Medved (2510) — 1h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 1.0668976640924126 | 0.12672655278660216 |
| alpha | 0.7881575066120978 | 0.4236453202936049 |
| trades | 65 | 38 |
| winrate | 0.47692307692307695 | 0.47368421052631576 |
| sharpe | 2.429404309541994 | 0.9735768124048678 |
| maxdd | -0.12414851185891818 | -0.12446592465338224 |
| pf | 2.2204057563381125 | 1.4548363806209872 |
| ann | 0.6701922012807537 | 0.1802247189086088 |

- **Combined OOS gain (stress):** 132.883%
- Full history @ stress: total 131.626%, CAGR 48.949%, benchmark -7.769%, sharpe 1.97, maxdd -0.124, trades 103

### 5/8 MA Cross (2528) — 1h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.5583400581484173 | 0.06070366497038737 |
| alpha | 0.2795999006681025 | 0.3576224324773901 |
| trades | 104 | 47 |
| winrate | 0.375 | 0.425531914893617 |
| sharpe | 1.3988304892781098 | 0.4834573942657669 |
| maxdd | -0.2610712691379008 | -0.14453727511611325 |
| pf | 1.4704433582864964 | 1.1229147418100842 |
| ann | 0.3680814551055913 | 0.08528703638273649 |

- **Combined OOS gain (stress):** 65.294%
- Full history @ stress: total 64.072%, CAGR 26.474%, benchmark -7.769%, sharpe 1.10, maxdd -0.261, trades 151

### Fast Slow RVI Crossover (3520) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.8908630802136088 | 0.09837905530036317 |
| alpha | 0.5951183993625451 | 0.40664677183579623 |
| trades | 51 | 28 |
| winrate | 0.5882352941176471 | 0.5 |
| sharpe | 2.001426147786332 | 0.7237301135879511 |
| maxdd | -0.22134284272242122 | -0.11998516253838443 |
| pf | 2.3324409118066387 | 1.4319235654792963 |
| ann | 0.568392400256003 | 0.13918965663556793 |

- **Combined OOS gain (stress):** 107.688%
- Full history @ stress: total 109.759%, CAGR 42.105%, benchmark -6.543%, sharpe 1.62, maxdd -0.221, trades 79

### Adaptive KDJ (MTF) (492) — 4h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.7218532788400069 | 0.14081709013693655 |
| alpha | 0.4261085979889432 | 0.4490848066723696 |
| trades | 32 | 16 |
| winrate | 0.53125 | 0.5625 |
| sharpe | 2.4569894903898546 | 1.4013728351565693 |
| maxdd | -0.10043109648305482 | -0.07288040505653326 |
| pf | 3.155354877938959 | 2.7548234183566658 |
| ann | 0.4680014391074083 | 0.2007722682211628 |

- **Combined OOS gain (stress):** 96.432%
- Full history @ stress: total 98.390%, CAGR 38.398%, benchmark -6.543%, sharpe 2.16, maxdd -0.117, trades 48

## 1303

### ZeroLag MACD Cross (1627) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 1.039173389208011 | 0.9653858530081754 |
| alpha | 0.2689673670210062 | 0.5930644244367467 |
| trades | 70 | 38 |
| winrate | 0.4 | 0.5789473684210527 |
| sharpe | 2.145017197356481 | 3.55685642517235 |
| maxdd | -0.1788488074616521 | -0.07111737522393924 |
| pf | 2.117559862384978 | 3.800468883776113 |
| ann | 0.6543335436386895 | 1.5558504054073379 |

- **Combined OOS gain (stress):** 300.776%
- Full history @ stress: total 299.489%, CAGR 92.896%, benchmark 143.582%, sharpe 2.64, maxdd -0.179, trades 108

### Charles 1.3.7 (1747) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 1.2772815597480163 | 0.910971305431868 |
| alpha | 0.5070755375610114 | 0.5386498768604393 |
| trades | 114 | 63 |
| winrate | 0.35964912280701755 | 0.4444444444444444 |
| sharpe | 2.2448943165759343 | 2.820817549069086 |
| maxdd | -0.17907478164688428 | -0.13749214932029696 |
| pf | 1.8870942790705063 | 1.9989437884598065 |
| ann | 0.7885770771322385 | 1.4581086788272 |

- **Combined OOS gain (stress):** 335.182%
- Full history @ stress: total 333.784%, CAGR 100.582%, benchmark 143.582%, sharpe 2.45, maxdd -0.179, trades 177

### Bull vs Medved (2510) — 1h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 1.33580753346481 | 1.0018647423349738 |
| alpha | 0.5543083309129759 | 0.6319895195185747 |
| trades | 59 | 36 |
| winrate | 0.5423728813559322 | 0.5555555555555556 |
| sharpe | 2.7334460314323574 | 3.7363787349144557 |
| maxdd | -0.17204049082287043 | -0.11319603297378711 |
| pf | 3.0261377212758735 | 2.9393567623555645 |
| ann | 0.820930190501636 | 1.6219687481735234 |

- **Combined OOS gain (stress):** 367.597%
- Full history @ stress: total 367.597%, CAGR 107.852%, benchmark 145.136%, sharpe 3.10, maxdd -0.172, trades 95

### Explosion (3261) — 4h **(pick)**
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 1.362015268482013 | 0.9724107218389482 |
| alpha | 0.5918092462950082 | 0.6000892932675195 |
| trades | 61 | 33 |
| winrate | 0.39344262295081966 | 0.6060606060606061 |
| sharpe | 2.561078584920305 | 3.9246256348630704 |
| maxdd | -0.10527830624267553 | -0.07146654430040533 |
| pf | 3.09557501081902 | 4.581049206535549 |
| ann | 0.8353404942790585 | 1.5685462538744197 |

- **Combined OOS gain (stress):** 365.886%
- Full history @ stress: total 365.886%, CAGR 107.491%, benchmark 143.582%, sharpe 3.01, maxdd -0.105, trades 94

### Fast Slow RVI Crossover (3520) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 1.3393656284940092 | 0.9452639101689997 |
| alpha | 0.5691596063070044 | 0.572942481597571 |
| trades | 52 | 28 |
| winrate | 0.4807692307692308 | 0.6428571428571429 |
| sharpe | 2.423895307633788 | 3.510576806552503 |
| maxdd | -0.22405001555867232 | -0.10522321303922322 |
| pf | 3.0836913623348874 | 4.905933204981722 |
| ann | 0.8228893799330264 | 1.5195822908951384 |

- **Combined OOS gain (stress):** 355.068%
- Full history @ stress: total 355.068%, CAGR 105.191%, benchmark 143.582%, sharpe 2.80, maxdd -0.224, trades 80

## 1320

### Charles 1.3.7 (1747) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.051475748112783215 | 0.5731406556506473 |
| alpha | 0.3621385144479947 | 0.05794875799606314 |
| trades | 120 | 58 |
| winrate | 0.30833333333333335 | 0.46551724137931033 |
| sharpe | -0.01153298499189644 | 2.1028664797436143 |
| maxdd | -0.2589709616835112 | -0.18606069564270333 |
| pf | 0.9647701073423909 | 1.7989058450011015 |
| ann | -0.03664758911838406 | 0.8761497005616312 |

- **Combined OOS gain (stress):** 49.216%
- Full history @ stress: total 50.076%, CAGR 21.237%, benchmark -7.861%, sharpe 0.81, maxdd -0.326, trades 178

### ADX DMI (2303) — 1h
> family: trend | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.1497220081035937 | 0.6612049274901397 |
| alpha | 0.27139799189640634 | 0.1452049274901397 |
| trades | 74 | 35 |
| winrate | 0.22972972972972974 | 0.37142857142857144 |
| sharpe | -0.6014636531452359 | 2.721016667307265 |
| maxdd | -0.2960204928876615 | -0.1398386549761802 |
| pf | 0.7538029069029175 | 2.560786848082663 |
| ann | -0.10826413623541109 | 1.0235785501748929 |

- **Combined OOS gain (stress):** 41.249%
- Full history @ stress: total 41.680%, CAGR 17.971%, benchmark -9.040%, sharpe 0.89, maxdd -0.296, trades 109

### ColorJFatl Digit ReOpen (2412) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.13776346636840664 | 0.6823510660367418 |
| alpha | 0.5513777289291846 | 0.1671591683821576 |
| trades | 60 | 30 |
| winrate | 0.35 | 0.4 |
| sharpe | 0.5963233640360511 | 2.9187424395548955 |
| maxdd | -0.17416100696411085 | -0.1410916544110017 |
| pf | 1.2140005930992477 | 2.717064582734973 |
| ann | 0.09546772966983941 | 1.0594404232596872 |

- **Combined OOS gain (stress):** 91.412%
- Full history @ stress: total 92.515%, CAGR 36.438%, benchmark -7.861%, sharpe 1.56, maxdd -0.177, trades 90

### Futures Engulfing Candle Size (823) — 4h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.14768257336080648 | 0.7250951770039924 |
| alpha | 0.5612968359215844 | 0.20990327934940822 |
| trades | 54 | 33 |
| winrate | 0.42592592592592593 | 0.45454545454545453 |
| sharpe | 0.5968867145955786 | 3.0393427141794653 |
| maxdd | -0.19682631072803203 | -0.17620286347840908 |
| pf | 1.309641690457782 | 2.7056881998029056 |
| ann | 0.10220627137698912 | 1.1324655172530362 |

- **Combined OOS gain (stress):** 97.986%
- Full history @ stress: total 105.349%, CAGR 40.679%, benchmark -7.861%, sharpe 1.64, maxdd -0.197, trades 87

### Logistic RSI STOCH ROC AO (988) — Daily **(pick)**
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.07164716882096189 | 0.7591847737395021 |
| alpha | 0.5405043116781048 | 0.25282547326255456 |
| trades | 23 | 10 |
| winrate | 0.34782608695652173 | 0.5 |
| sharpe | 0.3428856573458271 | 3.0915492855761255 |
| maxdd | -0.16041286789319908 | -0.11376490114302384 |
| pf | 1.030344946920315 | 5.599717420775947 |
| ann | 0.05010082857283327 | 1.1912122541234234 |

- **Combined OOS gain (stress):** 88.523%
- Full history @ stress: total 8709.402%, CAGR 29.878%, benchmark 69.701%, sharpe 1.18, maxdd -0.354, trades 269

## 1321

### Sunil 2 Bar Breakout (1360) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.6287731775400032 | 0.8112211438404728 |
| alpha | 0.6338976284916868 | 0.29304580528024493 |
| trades | 39 | 20 |
| winrate | 0.46153846153846156 | 0.6 |
| sharpe | 1.557328918302483 | 3.3729463090339764 |
| maxdd | -0.15334119382064593 | -0.07928914909271079 |
| pf | 2.2747186561433916 | 5.526345951486085 |
| ann | 0.41148158784445577 | 1.2817416753034112 |

- **Combined OOS gain (stress):** 195.007%
- Full history @ stress: total 199.313%, CAGR 68.210%, benchmark 55.930%, sharpe 2.21, maxdd -0.153, trades 59

### Demo GPT - Day Trading Scalping (675) — 4h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.7193199728040081 | 0.9648781962455091 |
| alpha | 0.7244444237556917 | 0.4467028576852812 |
| trades | 52 | 27 |
| winrate | 0.4807692307692308 | 0.5925925925925926 |
| sharpe | 1.769842507593688 | 3.119844772456296 |
| maxdd | -0.10914335644736517 | -0.14596247898975767 |
| pf | 2.2660530528573233 | 4.0866356846901795 |
| ann | 0.4664752389200688 | 1.5549336141795065 |

- **Combined OOS gain (stress):** 237.825%
- Full history @ stress: total 237.825%, CAGR 78.150%, benchmark 55.930%, sharpe 2.30, maxdd -0.146, trades 79

### Futures Engulfing Candle Size (823) — 4h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.7896891388720089 | 0.7582346503973929 |
| alpha | 0.7948135898236925 | 0.240059311837165 |
| trades | 59 | 40 |
| winrate | 0.5423728813559322 | 0.475 |
| sharpe | 2.0101101643366572 | 3.006830475420329 |
| maxdd | -0.2085905828421668 | -0.0819580608292072 |
| pf | 2.2056616158867453 | 3.2924822079700244 |
| ann | 0.5086282725392288 | 1.1895688595422445 |

- **Combined OOS gain (stress):** 214.669%
- Full history @ stress: total 219.263%, CAGR 73.438%, benchmark 55.930%, sharpe 2.41, maxdd -0.209, trades 99

### Long Explosive V1 (992) — 1h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.5677222783240117 | 0.6711925818319724 |
| alpha | 0.5914291748757357 | 0.16376158395511475 |
| trades | 77 | 44 |
| winrate | 0.44155844155844154 | 0.5 |
| sharpe | 1.4638931604345016 | 2.752536032551772 |
| maxdd | -0.16714615336628802 | -0.08616863931985264 |
| pf | 1.5510532690922798 | 2.4723064105350883 |
| ann | 0.37389541602648824 | 1.0404946990159893 |

- **Combined OOS gain (stress):** 161.997%
- Full history @ stress: total 166.169%, CAGR 59.101%, benchmark 53.017%, sharpe 1.96, maxdd -0.167, trades 121

## 1322

### Futures Engulfing Candle Size (823) — Daily **(pick)**
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.6470000413185468 | 0.04694696339091786 |
| alpha | 0.19485482679709465 | 0.1756542941127981 |
| trades | 37 | 17 |
| winrate | 0.5675675675675675 | 0.35294117647058826 |
| sharpe | 1.5710293039200092 | 0.35889427804582474 |
| maxdd | -0.12664994555333842 | -0.2706885144983897 |
| pf | 2.6912967229674765 | 1.1582469595598421 |
| ann | 0.42262237362133903 | 0.06578858496133555 |

- **Combined OOS gain (stress):** 72.432%
- Full history @ stress: total 83.185%, CAGR 14.461%, benchmark 29.620%, sharpe 0.69, maxdd -0.271, trades 98

### Logistic RSI STOCH ROC AO (988) — Daily
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.5220573203152645 | 0.07800125968204763 |
| alpha | 0.06991210579381235 | 0.20670859040392786 |
| trades | 16 | 10 |
| winrate | 0.625 | 0.5 |
| sharpe | 1.4347852034346746 | 0.4778958647207202 |
| maxdd | -0.16978931215962667 | -0.3158435898870029 |
| pf | 3.060554996820995 | 1.2600176672469763 |
| ann | 0.34550031010142157 | 0.10994406712973381 |

- **Combined OOS gain (stress):** 64.078%
- Full history @ stress: total 48.303%, CAGR 9.191%, benchmark 29.620%, sharpe 0.44, maxdd -0.383, trades 69

## 1323

### Martingale with MACD and KDJ (1025) — 30min **(pick)**
> family: other | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.01887499503399681 | 0.16571358927992685 |
| alpha | 0.48368910753010574 | 0.18343315784695313 |
| trades | 19 | 18 |
| winrate | 0.2631578947368421 | 0.4444444444444444 |
| sharpe | -0.1223823427558965 | 1.2341593018767911 |
| maxdd | -0.113665227743864 | -0.08911406550456047 |
| pf | 0.9095510638079172 | 2.183160239702835 |
| ann | -0.01337204326029573 | 0.23731893781461677 |

- **Combined OOS gain (stress):** 14.371%
- Full history @ stress: total 14.371%, CAGR 10.711%, benchmark -49.704%, sharpe 0.67, maxdd -0.114, trades 37

### Order Block Finder (1145) — Daily
> family: other | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.13671878952959915 | 0.08375880410396497 |
| alpha | 0.3406416165617714 | 0.12149465316056873 |
| trades | 8 | 17 |
| winrate | 0.375 | 0.5294117647058824 |
| sharpe | -1.0835031469563445 | 0.7789905155015103 |
| maxdd | -0.22302762915999952 | -0.0835279260845796 |
| pf | 0.4257881939479786 | 1.876348353128997 |
| ann | -0.09865119241805798 | 0.11818551993554771 |

- **Combined OOS gain (stress):** -6.441%
- Full history @ stress: total -3.668%, CAGR -2.792%, benchmark -48.223%, sharpe -0.06, maxdd -0.223, trades 25

### EMA 5 Alert Candle Short (734) — Daily
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.03676941171440151 | 0.11560740377342205 |
| alpha | 0.514129817805772 | 0.1533432528300258 |
| trades | 8 | 5 |
| winrate | 0.25 | 0.8 |
| sharpe | 0.5508690274551206 | 1.4068208611774595 |
| maxdd | -0.05403339739189117 | -0.0784734363959696 |
| pf | 1.3806497769444057 | 4.220356669787386 |
| ann | 0.02583884081367538 | 0.16408051684926273 |

- **Combined OOS gain (stress):** 15.663%
- Full history @ stress: total 15.663%, CAGR 11.657%, benchmark -48.223%, sharpe 1.00, maxdd -0.078, trades 13

### IU Open Equal to High Low (942) — Daily
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.03767267736079882 | 0.1146296334916912 |
| alpha | 0.4396877287305717 | 0.15236548254829496 |
| trades | 10 | 14 |
| winrate | 0.2 | 0.35714285714285715 |
| sharpe | -0.5315228671881308 | 1.075940683238907 |
| maxdd | -0.08759708629785001 | -0.0907001773288072 |
| pf | 0.710433956016497 | 2.0604692416837067 |
| ann | -0.026764574804178376 | 0.1626638460895704 |

- **Combined OOS gain (stress):** 7.264%
- Full history @ stress: total 10.063%, CAGR 7.536%, benchmark -48.223%, sharpe 0.60, maxdd -0.149, trades 24

## 1830

### Heiken Ashi Simplified EA (1854) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.012775876247998585 | 0.13088799127487794 |
| alpha | 0.5149748540343773 | 0.37965888606347176 |
| trades | 13 | 11 |
| winrate | 0.3076923076923077 | 0.36363636363636365 |
| sharpe | -0.05421502635445484 | 1.0434294083031712 |
| maxdd | -0.08268827278993895 | -0.07492013086029226 |
| pf | 0.9263221249338933 | 2.0100802077683215 |
| ann | -0.009042914474414188 | 0.1862828071452447 |

- **Combined OOS gain (stress):** 11.644%
- Full history @ stress: total 11.644%, CAGR 5.364%, benchmark -62.804%, sharpe 0.47, maxdd -0.128, trades 24

### Ingrit (3195) — 4h **(pick)**
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.009958266736000754 | 0.14864524523491318 |
| alpha | 0.5377089970183766 | 0.397416140023507 |
| trades | 12 | 5 |
| winrate | 0.25 | 0.6 |
| sharpe | 0.12674531336648012 | 1.59706829400052 |
| maxdd | -0.0914738325359995 | -0.051359026174673694 |
| pf | 1.094917717156213 | 3.544678641568015 |
| ann | 0.007025075152563565 | 0.2122304745491923 |

- **Combined OOS gain (stress):** 16.008%
- Full history @ stress: total 16.008%, CAGR 7.298%, benchmark -62.804%, sharpe 0.75, maxdd -0.091, trades 17

### Explosion Range Expansion (3263) — 4h
> family: breakout | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.14565034003199295 | 0.0819258794990323 |
| alpha | 0.3821003902503829 | 0.3306967742876261 |
| trades | 67 | 39 |
| winrate | 0.3283582089552239 | 0.28205128205128205 |
| sharpe | -0.635174382348686 | 0.7064991190895697 |
| maxdd | -0.2636855277538982 | -0.14495609442787682 |
| pf | 0.7025064866716333 | 1.407293272170745 |
| ann | -0.10524944629919597 | 0.11555998713727922 |

- **Combined OOS gain (stress):** -7.566%
- Full history @ stress: total -3.071%, CAGR -1.468%, benchmark -62.804%, sharpe -0.01, maxdd -0.264, trades 106

### Demo GPT - Day Trading Scalping (675) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.0707292716759923 | 0.11999158836804735 |
| alpha | 0.45702145860638355 | 0.3687624831566412 |
| trades | 52 | 27 |
| winrate | 0.40384615384615385 | 0.3333333333333333 |
| sharpe | -0.21807944088816017 | 0.8854381057204526 |
| maxdd | -0.2305375491580558 | -0.11316205433042337 |
| pf | 0.9398048110872828 | 1.4177050824639452 |
| ann | -0.05050397318296296 | 0.170438601716274 |

- **Combined OOS gain (stress):** 4.078%
- Full history @ stress: total 9.141%, CAGR 4.237%, benchmark -62.804%, sharpe 0.32, maxdd -0.231, trades 79

## 1831

### Stochastic (1341) — 4h
> family: mean_reversion | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.21419881649333505 | 0.39487799497665765 |
| alpha | 0.28093475377194466 | 0.323847872254456 |
| trades | 29 | 15 |
| winrate | 0.5517241379310345 | 0.4 |
| sharpe | 0.7350033083077003 | 1.4823716177982504 |
| maxdd | -0.28134549617950555 | -0.08750993244423066 |
| pf | 1.2448172410001763 | 5.445653619781 |
| ann | 0.14696201578791057 | 0.5875575894855765 |

- **Combined OOS gain (stress):** 69.366%
- Full history @ stress: total 72.871%, CAGR 29.647%, benchmark 2.017%, sharpe 1.08, maxdd -0.281, trades 44

### Kalman Filter Candles (2152) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.2338070392853473 | 0.7207080147625808 |
| alpha | 0.3005429765639569 | 0.6496778920403792 |
| trades | 31 | 21 |
| winrate | 0.5161290322580645 | 0.5714285714285714 |
| sharpe | 0.7722138545953275 | 2.2682623066921708 |
| maxdd | -0.2718138688203656 | -0.06422371682840133 |
| pf | 1.2168114399981191 | 9.69818537021357 |
| ann | 0.16001692162520187 | 1.124937644612464 |

- **Combined OOS gain (stress):** 112.302%
- Full history @ stress: total 116.696%, CAGR 44.315%, benchmark 2.017%, sharpe 1.44, maxdd -0.272, trades 52

### N-Candles Sequence (2820) — 4h
> family: volatility | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.6141680893129782 | 0.5380892043603474 |
| alpha | 0.6809040265915878 | 0.4670590816381457 |
| trades | 15 | 9 |
| winrate | 0.6 | 0.7777777777777778 |
| sharpe | 1.7965805899838212 | 1.8257573653096182 |
| maxdd | -0.11378054972634088 | -0.073744963604787 |
| pf | 2.7570157226430005 | 14.25239514798784 |
| ann | 0.4025281083479957 | 0.818347200301971 |

- **Combined OOS gain (stress):** 148.273%
- Full history @ stress: total 153.412%, CAGR 55.437%, benchmark 2.017%, sharpe 1.77, maxdd -0.114, trades 24

### Demo GPT - Day Trading Scalping (675) — 4h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.5285467929664764 | 0.5802291607033974 |
| alpha | 0.595282730245086 | 0.5091990379811957 |
| trades | 42 | 25 |
| winrate | 0.5714285714285714 | 0.48 |
| sharpe | 1.8062565861010411 | 1.9563923085931978 |
| maxdd | -0.11596470186500929 | -0.09748065599968936 |
| pf | 2.4875726520995496 | 4.819534009597108 |
| ann | 0.3495506413707703 | 0.8879005417117554 |

- **Combined OOS gain (stress):** 141.545%
- Full history @ stress: total 140.667%, CAGR 51.679%, benchmark 2.017%, sharpe 1.77, maxdd -0.116, trades 67

### Futures Engulfing Candle Size (823) — 4h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.22772250631365742 | 0.3319833181751721 |
| alpha | 0.294458443592267 | 0.26095319545297047 |
| trades | 55 | 28 |
| winrate | 0.45454545454545453 | 0.5 |
| sharpe | 0.9304666100310776 | 2.523607425969376 |
| maxdd | -0.22108222743748618 | -0.04726925696604567 |
| pf | 1.437629601496305 | 2.677586257365288 |
| ann | 0.1559724770563835 | 0.4890244561040966 |

- **Combined OOS gain (stress):** 63.531%
- Full history @ stress: total 62.936%, CAGR 26.058%, benchmark 2.017%, sharpe 1.44, maxdd -0.221, trades 83

## 1832

### The 20s Breakout (2986) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.09525995270239462 | 0.118231499371936 |
| alpha | 0.10409696048088501 | 0.21053919167962842 |
| trades | 47 | 23 |
| winrate | 0.2978723404255319 | 0.391304347826087 |
| sharpe | -0.36296497229725483 | 1.1376311672098913 |
| maxdd | -0.19603329856078777 | -0.07569816651314487 |
| pf | 0.79163698932128 | 1.732229766813558 |
| ann | -0.06828098736916066 | 0.16788489955498775 |

- **Combined OOS gain (stress):** 1.171%
- Full history @ stress: total 2.244%, CAGR 1.058%, benchmark -24.116%, sharpe 0.15, maxdd -0.196, trades 70

### Rubberbands 3 (4116) — 4h
> family: trend | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.10113473124639338 | 0.09497850847844647 |
| alpha | 0.09822218193688625 | 0.1872862007861389 |
| trades | 48 | 24 |
| winrate | 0.3125 | 0.375 |
| sharpe | -0.3990329358755088 | 0.9418788495417518 |
| maxdd | -0.18876640361893648 | -0.07569773219039566 |
| pf | 0.7771766092191235 | 1.5440369252659067 |
| ann | -0.07255924719357643 | 0.13429451333475395 |

- **Combined OOS gain (stress):** -1.576%
- Full history @ stress: total -0.532%, CAGR -0.253%, benchmark -24.116%, sharpe 0.06, maxdd -0.189, trades 72

### CP Strat ORB (639) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.08704272710319261 | 0.09053279572087725 |
| alpha | 0.11231418608008703 | 0.18284048802856967 |
| trades | 47 | 23 |
| winrate | 0.3191489361702128 | 0.34782608695652173 |
| sharpe | -0.3299309726250052 | 0.9395508965463482 |
| maxdd | -0.17604826307542865 | -0.09070647410869115 |
| pf | 0.8036400523107567 | 1.5425431025734335 |
| ann | -0.06231051049589964 | 0.12790374719092723 |

- **Combined OOS gain (stress):** -0.439%
- Full history @ stress: total 0.617%, CAGR 0.292%, benchmark -24.116%, sharpe 0.10, maxdd -0.176, trades 70

### Demo GPT - Day Trading Scalping (675) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.06596553019559404 | 0.09517146285719091 |
| alpha | 0.1333913829876856 | 0.18747915516488334 |
| trades | 50 | 24 |
| winrate | 0.36 | 0.375 |
| sharpe | -0.197889707276907 | 0.8972205413266077 |
| maxdd | -0.14645505560946648 | -0.0791646901882328 |
| pf | 0.8653772628123774 | 1.610254265266625 |
| ann | -0.04706781916649527 | 0.13457211638060307 |

- **Combined OOS gain (stress):** 2.293%
- Full history @ stress: total 3.378%, CAGR 1.588%, benchmark -24.116%, sharpe 0.18, maxdd -0.146, trades 74

### Long Explosive V1 (992) — 4h **(pick)**
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.045949488563595375 | 0.16282601588420254 |
| alpha | 0.15340742461968426 | 0.25513370819189496 |
| trades | 49 | 19 |
| winrate | 0.30612244897959184 | 0.5263157894736842 |
| sharpe | -0.07179296800980564 | 1.3281066605567524 |
| maxdd | -0.21008204267687702 | -0.07350037184895353 |
| pf | 0.9258023562481812 | 1.9779228926624945 |
| ann | -0.032685747246338326 | 0.23306444270196147 |

- **Combined OOS gain (stress):** 10.939%
- Full history @ stress: total 12.117%, CAGR 5.575%, benchmark -24.116%, sharpe 0.38, maxdd -0.210, trades 68

## 1833

### Eugene Candle Pattern (1852) — Daily
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.21310966727837255 | 0.17528115840954528 |
| alpha | 0.12894300061170583 | 0.199236306217904 |
| trades | 36 | 17 |
| winrate | 0.3888888888888889 | 0.4117647058823529 |
| sharpe | 0.7089744267485355 | 1.2349952961100434 |
| maxdd | -0.1579275605480831 | -0.07765898782991287 |
| pf | 1.3874663579434048 | 1.7384737135205848 |
| ann | 0.14623506755395166 | 0.251444868872325 |

- **Combined OOS gain (stress):** 42.574%
- Full history @ stress: total 123.145%, CAGR 27.936%, benchmark 53.446%, sharpe 1.17, maxdd -0.165, trades 78

### Hercules A.T.C. 2006 (2485) — Daily **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.4558994899000095 | 0.17163628462656155 |
| alpha | 0.3717328232333428 | 0.19559143243492028 |
| trades | 29 | 14 |
| winrate | 0.4827586206896552 | 0.42857142857142855 |
| sharpe | 1.259184448201183 | 1.21614475117691 |
| maxdd | -0.1494222935524121 | -0.13038224439010115 |
| pf | 2.153672398792833 | 1.7803202885361615 |
| ann | 0.3039142051422705 | 0.2460581432663005 |

- **Combined OOS gain (stress):** 70.578%
- Full history @ stress: total 124.364%, CAGR 28.150%, benchmark 53.446%, sharpe 1.26, maxdd -0.199, trades 63

### 5 EMA No-Touch Breakout (483) — Daily
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.27311525117124846 | 0.25075095864329433 |
| alpha | 0.18894858450458174 | 0.27470610645165305 |
| trades | 30 | 13 |
| winrate | 0.43333333333333335 | 0.46153846153846156 |
| sharpe | 0.8774577777994027 | 1.7714872322878754 |
| maxdd | -0.14942646283994632 | -0.07173269366736401 |
| pf | 1.622877774965012 | 2.6031746038918944 |
| ann | 0.18600607860418616 | 0.3644236641170442 |

- **Combined OOS gain (stress):** 59.235%
- Full history @ stress: total 161.521%, CAGR 34.322%, benchmark 53.446%, sharpe 1.39, maxdd -0.158, trades 65

## 1834

### Reflex Oscillator (1235) — Daily
> family: other | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.018996860213200906 | 0.16706384486679027 |
| alpha | 0.5093443505606912 | 0.1298198970083173 |
| trades | 8 | 7 |
| winrate | 0.625 | 0.5714285714285714 |
| sharpe | 0.1637541981070854 | 1.2994840743757712 |
| maxdd | -0.10141594525439956 | -0.06703431750812938 |
| pf | 1.1070981472739843 | 4.752987528523803 |
| ann | 0.013383781891242563 | 0.23930978540515713 |

- **Combined OOS gain (stress):** 18.923%
- Full history @ stress: total 19.671%, CAGR 8.213%, benchmark -38.453%, sharpe 0.61, maxdd -0.101, trades 15

### EMA Sticker (1656) — Daily
> family: trend | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.291488316453848 | 0.03997220918979605 |
| alpha | 0.19885917389364227 | 0.0027282613313230897 |
| trades | 46 | 30 |
| winrate | 0.2826086956521739 | 0.4666666666666667 |
| sharpe | -1.0209782533740694 | 0.35849647502526283 |
| maxdd | -0.32786447758972814 | -0.1881563867721463 |
| pf | 0.496735864425414 | 1.11395132401578 |
| ann | -0.21607736154370083 | 0.055940626495758705 |

- **Combined OOS gain (stress):** -26.317%
- Full history @ stress: total -14.796%, CAGR -6.796%, benchmark -38.453%, sharpe -0.19, maxdd -0.410, trades 80

### Stochastic Breakout (248) — 1h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.20404930045080505 | 0.12957505742607722 |
| alpha | 0.6606653525115427 | 0.09039595294846525 |
| trades | 30 | 21 |
| winrate | 0.4666666666666667 | 0.47619047619047616 |
| sharpe | 1.0802330455585063 | 1.1336218709155355 |
| maxdd | -0.11526186958435314 | -0.13644023838529995 |
| pf | 1.785061804973683 | 1.750447044111174 |
| ann | 0.1401803149642582 | 0.18437054284484855 |

- **Combined OOS gain (stress):** 36.006%
- Full history @ stress: total 40.320%, CAGR 17.962%, benchmark -39.588%, sharpe 1.20, maxdd -0.136, trades 51

### 80-20 (488) — 4h **(pick)**
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.0053187010415973734 | 0.2384805899237865 |
| alpha | 0.45070735759032454 | 0.19930148544617454 |
| trades | 15 | 9 |
| winrate | 0.3333333333333333 | 0.6666666666666666 |
| sharpe | 0.04036551483802337 | 1.954767740167816 |
| maxdd | -0.12683602954716622 | -0.059051607237763704 |
| pf | 0.9642840979757342 | 6.599358095070941 |
| ann | -0.003760494059601771 | 0.3458695678099133 |

- **Combined OOS gain (stress):** 23.189%
- Full history @ stress: total 25.874%, CAGR 11.875%, benchmark -39.522%, sharpe 0.83, maxdd -0.127, trades 24

## 1835

### XMACD Modes (1781) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.04061394516166894 | 0.11459605523275784 |
| alpha | 0.22369086823859197 | 0.3044327158498178 |
| trades | 20 | 11 |
| winrate | 0.5 | 0.7272727272727273 |
| sharpe | 0.3300945651481733 | 1.3376426552761718 |
| maxdd | -0.09844043186006213 | -0.08915110546424321 |
| pf | 1.1465999241337077 | 2.0403451572454996 |
| ann | 0.028524829951009245 | 0.16261520383575312 |

- **Combined OOS gain (stress):** 15.986%
- Full history @ stress: total 15.986%, CAGR 8.513%, benchmark -31.323%, sharpe 0.69, maxdd -0.135, trades 31

### JS Sistem 2 (2743) — 30min
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.037724408310003454 | 0.035781529260849876 |
| alpha | 0.18948159680840604 | 0.22266677516248923 |
| trades | 23 | 14 |
| winrate | 0.5217391304347826 | 0.5714285714285714 |
| sharpe | 0.2588643310944979 | 0.3906085531712884 |
| maxdd | -0.26160539616672074 | -0.08558183960598853 |
| pf | 1.1169951939417018 | 1.2312753910798795 |
| ann | 0.026506323149753985 | 0.05003594973784775 |

- **Combined OOS gain (stress):** 7.486%
- Full history @ stress: total 7.046%, CAGR 3.822%, benchmark -28.690%, sharpe 0.27, maxdd -0.262, trades 37

### Explosion Range Expansion (3263) — Daily
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.005314348055998286 | 0.01387335535069023 |
| alpha | 0.1639164211747709 | 0.20001738452115514 |
| trades | 15 | 11 |
| winrate | 0.4666666666666667 | 0.6363636363636364 |
| sharpe | 0.12714451817949252 | 0.1958027109379596 |
| maxdd | -0.30627945461999884 | -0.11042157505415184 |
| pf | 0.984055001480961 | 1.216739120179451 |
| ann | -0.00375741394809026 | 0.019318898464105505 |

- **Combined OOS gain (stress):** 0.849%
- Full history @ stress: total 1.741%, CAGR 0.955%, benchmark -31.323%, sharpe 0.16, maxdd -0.306, trades 26

### 5 EMA No-Touch Breakout (483) — Daily **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.1379485355600023 | 0.06132043333729609 |
| alpha | 0.3071793047907715 | 0.247464462507761 |
| trades | 22 | 16 |
| winrate | 0.5454545454545454 | 0.5 |
| sharpe | 0.7647353394360804 | 0.5954870137297024 |
| maxdd | -0.1350270078679996 | -0.11934031050766591 |
| pf | 1.6371801261662475 | 1.4403598473563592 |
| ann | 0.09559361381836551 | 0.08616354500879275 |

- **Combined OOS gain (stress):** 20.773%
- Full history @ stress: total 22.681%, CAGR 11.920%, benchmark -31.323%, sharpe 0.75, maxdd -0.135, trades 38

### Balance of Power (546) — Daily
> family: momentum | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.21688811221200122 | 0.04013433875364569 |
| alpha | 0.3861188814427704 | 0.2262783679241106 |
| trades | 7 | 9 |
| winrate | 0.5714285714285714 | 0.5555555555555556 |
| sharpe | 1.0502079714084642 | 0.43736112002321376 |
| maxdd | -0.11632562783883837 | -0.08772263015013937 |
| pf | 3.4087449848173685 | 1.3250393431923988 |
| ann | 0.14875615614144122 | 0.05616925354789348 |

- **Combined OOS gain (stress):** 26.573%
- Full history @ stress: total 26.573%, CAGR 13.862%, benchmark -31.323%, sharpe 0.83, maxdd -0.116, trades 16

## 2010

### I Gap (2145) — 1h
> family: volatility | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.12603192654599504 | 0.016268111044166922 |
| alpha | 0.19311700962421774 | 0.09572547538525222 |
| trades | 59 | 53 |
| winrate | 0.2711864406779661 | 0.3018867924528302 |
| sharpe | -0.8303954645082725 | 0.21467434544725694 |
| maxdd | -0.20926050394024553 | -0.14118769545268706 |
| pf | 0.7066487404209978 | 1.033681354791478 |
| ann | -0.09078245649778816 | 0.022664092561732074 |

- **Combined OOS gain (stress):** -11.181%
- Full history @ stress: total -11.181%, CAGR -5.469%, benchmark -36.835%, sharpe -0.34, maxdd -0.209, trades 112

### Polarized Fractal Efficiency (2316) — Daily
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.03789675486930666 | 0.016371610550477644 |
| alpha | 0.31600752724656245 | 0.09224709693180055 |
| trades | 17 | 12 |
| winrate | 0.35294117647058826 | 0.5 |
| sharpe | -0.42407604644264113 | 0.28608901823154226 |
| maxdd | -0.06746159142272223 | -0.08341951134108128 |
| pf | 0.6525087187233225 | 1.1682615088601078 |
| ann | -0.026924680905721754 | 0.022808738439433762 |

- **Combined OOS gain (stress):** -2.215%
- Full history @ stress: total -62.401%, CAGR -2.860%, benchmark 1100.313%, sharpe -0.19, maxdd -0.739, trades 412

### Bull vs Medved (2510) — 4h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.007931467510001289 | 0.14711388301737904 |
| alpha | 0.3315774384479141 | 0.22567838350234504 |
| trades | 14 | 13 |
| winrate | 0.2857142857142857 | 0.38461538461538464 |
| sharpe | 0.10667243617385845 | 1.0994959716425972 |
| maxdd | -0.1009818230119992 | -0.12623809032918243 |
| pf | 1.047823202202242 | 1.734776258548512 |
| ann | 0.005596920404052685 | 0.2099865973529551 |

- **Combined OOS gain (stress):** 15.621%
- Full history @ stress: total 15.621%, CAGR 7.128%, benchmark -37.252%, sharpe 0.55, maxdd -0.126, trades 27

### Freeman (2953) — 4h
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | -0.012499136643999709 | 0.08062888814234515 |
| alpha | 0.3111468342939131 | 0.15919338862731114 |
| trades | 6 | 5 |
| winrate | 0.3333333333333333 | 0.4 |
| sharpe | -0.2483734027596511 | 1.1434867447130233 |
| maxdd | -0.046186081280745084 | -0.030847287498995346 |
| pf | 0.7073589425816037 | 3.0251003785218806 |
| ann | -0.00884667235767378 | 0.11370318453524142 |

- **Combined OOS gain (stress):** 6.712%
- Full history @ stress: total 6.712%, CAGR 3.130%, benchmark -37.252%, sharpe 0.51, maxdd -0.065, trades 11

### Explosion Range Expansion (3263) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.07218696504199451 | 0.032459914187524586 |
| alpha | 0.2514590058959183 | 0.11102441467249058 |
| trades | 55 | 35 |
| winrate | 0.3090909090909091 | 0.37142857142857144 |
| sharpe | -0.47213888922782515 | 0.35640739691986495 |
| maxdd | -0.10170200780083405 | -0.11895573853801489 |
| pf | 0.7646272832236448 | 1.131735455958209 |
| ann | -0.051556460304061136 | 0.04536237933860465 |

- **Combined OOS gain (stress):** -4.207%
- Full history @ stress: total -4.207%, CAGR -2.018%, benchmark -37.252%, sharpe -0.10, maxdd -0.119, trades 90

## 2020

### Renko Live Charts Pimped (1895) — 4h
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.20580458359200038 | 0.25659827736124496 |
| alpha | 0.24667414880939176 | 0.14948756629013782 |
| trades | 6 | 5 |
| winrate | 0.6666666666666666 | 0.6 |
| sharpe | 1.0742999812655614 | 1.908396306204014 |
| maxdd | -0.10152038271734332 | -0.13464528761530825 |
| pf | 4.862171393125861 | 3.7514955885631984 |
| ann | 0.14135435596386925 | 0.37329039994615076 |

- **Combined OOS gain (stress):** 51.521%
- Full history @ stress: total 51.521%, CAGR 21.789%, benchmark 6.957%, sharpe 1.40, maxdd -0.135, trades 11

### Bull vs Medved (2510) — 1h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.11515733435600306 | 0.18482456869014818 |
| alpha | 0.14930794731572294 | 0.07671646058204007 |
| trades | 43 | 34 |
| winrate | 0.46511627906976744 | 0.5 |
| sharpe | 0.641456578724621 | 1.402046806537582 |
| maxdd | -0.13525186032202086 | -0.11667141022657757 |
| pf | 1.3570403786244438 | 1.5932398219985349 |
| ann | 0.0800454337340053 | 0.26557974073396373 |

- **Combined OOS gain (stress):** 32.127%
- Full history @ stress: total 32.127%, CAGR 14.128%, benchmark 7.706%, sharpe 0.94, maxdd -0.135, trades 77

### Supertrend Distance Breakout (260) — 4h **(pick)**
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.14994150892000158 | 0.2792351904416204 |
| alpha | 0.19081107413739296 | 0.17212447937051323 |
| trades | 8 | 7 |
| winrate | 0.375 | 0.42857142857142855 |
| sharpe | 0.8958295504983003 | 2.121592319785192 |
| maxdd | -0.09339561373346938 | -0.0763619112842211 |
| pf | 3.0247431718953046 | 5.185153397496852 |
| ann | 0.1037384847591174 | 0.4077674628508594 |

- **Combined OOS gain (stress):** 47.105%
- Full history @ stress: total 47.105%, CAGR 20.092%, benchmark 6.957%, sharpe 1.39, maxdd -0.093, trades 15

### Hoop Master (3162) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.048048823996003076 | 0.35202607326455415 |
| alpha | 0.08891838921339446 | 0.244915362193447 |
| trades | 21 | 12 |
| winrate | 0.3333333333333333 | 0.5833333333333334 |
| sharpe | 0.3273773335204097 | 2.3508937397036194 |
| maxdd | -0.1284247060087771 | -0.06422270547622067 |
| pf | 1.5529306390064768 | 6.329376484644028 |
| ann | 0.03371097301069925 | 0.5202319984366348 |

- **Combined OOS gain (stress):** 41.699%
- Full history @ stress: total 42.731%, CAGR 18.385%, benchmark 6.957%, sharpe 1.19, maxdd -0.128, trades 33

### Parabolic SAR Bug 3 (4195) — 4h
> family: volatility | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.2090511663360004 | 0.26026106285112616 |
| alpha | 0.24992073155339178 | 0.153150351780019 |
| trades | 6 | 5 |
| winrate | 0.6666666666666666 | 0.6 |
| sharpe | 1.0741485708857437 | 1.9634405076344394 |
| maxdd | -0.09897672670000945 | -0.11018474234157716 |
| pf | 4.936134877751104 | 3.751303214195267 |
| ann | 0.1435245485877168 | 0.37885274274192615 |

- **Combined OOS gain (stress):** 52.372%
- Full history @ stress: total 52.372%, CAGR 22.113%, benchmark 6.957%, sharpe 1.41, maxdd -0.110, trades 11

## 2030

### Sunil 2 Bar Breakout (1360) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.1885516141060053 | 0.2968697683314352 |
| alpha | 0.4978212770273537 | 0.2517717291157491 |
| trades | 38 | 24 |
| winrate | 0.2631578947368421 | 0.4583333333333333 |
| sharpe | 0.7927377404612649 | 1.3596839048660119 |
| maxdd | -0.12444525968759568 | -0.07593209088317088 |
| pf | 1.4648141669004264 | 2.577359163657304 |
| ann | 0.1297926005358343 | 0.4347908054287659 |

- **Combined OOS gain (stress):** 54.140%
- Full history @ stress: total 54.140%, CAGR 22.783%, benchmark -25.140%, sharpe 1.02, maxdd -0.159, trades 62

### ZeroLag MACD Cross (1627) — Daily
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.01454727812587675 | 0.30221081977712894 |
| alpha | 0.32506311148451283 | 0.25402989549001 |
| trades | 39 | 23 |
| winrate | 0.3333333333333333 | 0.4782608695652174 |
| sharpe | 0.05505879824878032 | 1.381990613046763 |
| maxdd | -0.13846328415763676 | -0.10444407318011972 |
| pf | 0.8944138103028807 | 2.3724714625553474 |
| ann | -0.010299437088087338 | 0.4430037844922201 |

- **Combined OOS gain (stress):** 28.327%
- Full history @ stress: total 186832.683%, CAGR 25.491%, benchmark 2079.870%, sharpe 0.58, maxdd -0.813, trades 717

### Explosion (3261) — 4h **(pick)**
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.35307587074000524 | 0.372524338224101 |
| alpha | 0.6623455336613536 | 0.3274262990084149 |
| trades | 47 | 27 |
| winrate | 0.3404255319148936 | 0.4074074074074074 |
| sharpe | 1.3032335909133796 | 1.8637572144817713 |
| maxdd | -0.1206876392819215 | -0.05772295645129155 |
| pf | 2.2027396890783217 | 3.4348554239177234 |
| ann | 0.2381590360039445 | 0.5523353617202666 |

- **Combined OOS gain (stress):** 85.713%
- Full history @ stress: total 92.612%, CAGR 36.471%, benchmark -25.140%, sharpe 1.59, maxdd -0.121, trades 74

### Breakthrough Volatility (3271) — 4h
> family: breakout | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.10716491354398827 | 0.20059925389628686 |
| alpha | 0.20210474937736012 | 0.15550121468060074 |
| trades | 101 | 49 |
| winrate | 0.297029702970297 | 0.3877551020408163 |
| sharpe | -0.31793260974934323 | 1.1183851575700343 |
| maxdd | -0.26104989571796877 | -0.18232740192480013 |
| pf | 0.9057287597198375 | 1.4557226117870696 |
| ann | -0.07695922330985483 | 0.2890409378949754 |

- **Combined OOS gain (stress):** 7.194%
- Full history @ stress: total 11.175%, CAGR 5.153%, benchmark -25.140%, sharpe 0.34, maxdd -0.292, trades 150

### Chart Patterns (617) — 1h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.07028465538856443 | 0.2717052892152507 |
| alpha | 0.23703928827340737 | 0.2266072499995646 |
| trades | 63 | 35 |
| winrate | 0.3333333333333333 | 0.4857142857142857 |
| sharpe | -0.20594048403367748 | 1.456317199243223 |
| maxdd | -0.17465456544423597 | -0.11605305146352807 |
| pf | 0.886742444186323 | 1.7799710027438849 |
| ann | -0.05018304677609886 | 0.39627252938197 |

- **Combined OOS gain (stress):** 18.232%
- Full history @ stress: total 18.232%, CAGR 8.269%, benchmark -24.930%, sharpe 0.49, maxdd -0.226, trades 98

## 2040

### Hercules A.T.C. 2006 (2485) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.3190993427156057 | 0.21804771051596017 |
| alpha | 0.31986562624051007 | 0.3824163607336669 |
| trades | 50 | 21 |
| winrate | 0.44 | 0.5714285714285714 |
| sharpe | 1.2913324899698417 | 2.0727656505280785 |
| maxdd | -0.1326250328875085 | -0.055950260268127994 |
| pf | 1.6555009820288193 | 3.081494298029351 |
| ann | 0.21611211160670596 | 0.3151313979174353 |

- **Combined OOS gain (stress):** 60.673%
- Full history @ stress: total 63.077%, CAGR 26.110%, benchmark -11.762%, sharpe 1.56, maxdd -0.143, trades 71

### Explosion Range Expansion (3263) — 4h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.586218266766809 | 0.1858314432506043 |
| alpha | 0.5869845502917134 | 0.35020009346831105 |
| trades | 61 | 33 |
| winrate | 0.4426229508196721 | 0.42424242424242425 |
| sharpe | 1.7936806874271514 | 1.6359946972241286 |
| maxdd | -0.10537068510577141 | -0.07829448205767875 |
| pf | 2.0224066107047127 | 1.9028402315143889 |
| ann | 0.3853271722605818 | 0.2670736252725634 |

- **Combined OOS gain (stress):** 88.099%
- Full history @ stress: total 90.914%, CAGR 35.899%, benchmark -11.762%, sharpe 1.77, maxdd -0.105, trades 94

### 5 EMA No-Touch Breakout (483) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.29941218080320775 | 0.12431034848518419 |
| alpha | 0.3001784643281121 | 0.28867899870289093 |
| trades | 65 | 32 |
| winrate | 0.4153846153846154 | 0.46875 |
| sharpe | 1.1584795292082841 | 1.1099314454225764 |
| maxdd | -0.11865183214689734 | -0.11779240223535481 |
| pf | 1.4720012802926479 | 1.4981717571564865 |
| ann | 0.20326116016944895 | 0.17671127399696984 |

- **Combined OOS gain (stress):** 46.094%
- Full history @ stress: total 48.281%, CAGR 20.546%, benchmark -11.762%, sharpe 1.18, maxdd -0.119, trades 97

### Futures Engulfing Candle Size (823) — 4h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.2774524644304066 | 0.13005291074543845 |
| alpha | 0.278218747955311 | 0.2944215609631452 |
| trades | 62 | 33 |
| winrate | 0.3548387096774194 | 0.5454545454545454 |
| sharpe | 0.9858879223727974 | 1.0971769093562802 |
| maxdd | -0.15303968457464745 | -0.07697769161995571 |
| pf | 1.3954066878303721 | 1.529732251947071 |
| ann | 0.1888591509138997 | 0.18506642755797853 |

- **Combined OOS gain (stress):** 44.359%
- Full history @ stress: total 46.519%, CAGR 19.865%, benchmark -11.762%, sharpe 1.05, maxdd -0.153, trades 95

### Long Explosive V1 (992) — 4h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.46868055688920696 | 0.135813455186081 |
| alpha | 0.46944684041411133 | 0.30018210540378776 |
| trades | 54 | 23 |
| winrate | 0.42592592592592593 | 0.4782608695652174 |
| sharpe | 1.4989708949343938 | 1.1807199770172963 |
| maxdd | -0.15458743982033551 | -0.08236276389254982 |
| pf | 1.6276797790400075 | 1.8609512921823053 |
| ann | 0.3119907689502648 | 0.1934643453750855 |

- **Combined OOS gain (stress):** 66.815%
- Full history @ stress: total 69.311%, CAGR 28.374%, benchmark -11.762%, sharpe 1.43, maxdd -0.155, trades 77

## 2060

### Rally Base Drop SND Pivots (1215) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.19770054445760388 | 0.2741988016655079 |
| alpha | 0.387355716871397 | 0.35853615106309844 |
| trades | 29 | 11 |
| winrate | 0.4482758620689655 | 0.5454545454545454 |
| sharpe | 1.1375749679075737 | 2.121339602516989 |
| maxdd | -0.11827558295084672 | -0.0852260932726161 |
| pf | 2.149006621803718 | 4.343830599491507 |
| ann | 0.1359296752298076 | 0.4000761322792885 |

- **Combined OOS gain (stress):** 52.611%
- Full history @ stress: total 52.611%, CAGR 22.204%, benchmark -24.138%, sharpe 1.53, maxdd -0.118, trades 40

### Bull vs Medved (2510) — 4h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.3150756817168012 | 0.2854421095867772 |
| alpha | 0.5047308541305944 | 0.3697794589843677 |
| trades | 17 | 12 |
| winrate | 0.5294117647058824 | 0.4166666666666667 |
| sharpe | 1.6142838993985194 | 2.0626561577183327 |
| maxdd | -0.08593135688744402 | -0.12186272687484168 |
| pf | 4.696468672943576 | 2.569282213816053 |
| ann | 0.2134902376768204 | 0.41726257544072287 |

- **Combined OOS gain (stress):** 69.045%
- Full history @ stress: total 67.281%, CAGR 27.641%, benchmark -24.138%, sharpe 1.74, maxdd -0.122, trades 29

### Explosion Range Expansion (3263) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.29075212259680683 | 0.2400138773761873 |
| alpha | 0.4804072950106 | 0.3243512267737778 |
| trades | 52 | 34 |
| winrate | 0.4807692307692308 | 0.47058823529411764 |
| sharpe | 1.4582426655299172 | 1.6565381685229132 |
| maxdd | -0.09874025691631538 | -0.14045246185858073 |
| pf | 1.9073570145185523 | 1.8562142396367913 |
| ann | 0.1975901652765799 | 0.34818416971779675 |

- **Combined OOS gain (stress):** 60.055%
- Full history @ stress: total 60.055%, CAGR 24.996%, benchmark -24.138%, sharpe 1.52, maxdd -0.140, trades 86

### NRTR Reversal (3795) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.19770054445760388 | 0.2741988016655079 |
| alpha | 0.387355716871397 | 0.35853615106309844 |
| trades | 29 | 11 |
| winrate | 0.4482758620689655 | 0.5454545454545454 |
| sharpe | 1.1375749679075737 | 2.121339602516989 |
| maxdd | -0.11827558295084672 | -0.0852260932726161 |
| pf | 2.149006621803718 | 4.343830599491507 |
| ann | 0.1359296752298076 | 0.4000761322792885 |

- **Combined OOS gain (stress):** 52.611%
- Full history @ stress: total 52.611%, CAGR 22.204%, benchmark -24.138%, sharpe 1.53, maxdd -0.118, trades 40

### Gann Swing Multi Layer (830) — 4h
> family: other | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.15802114339760398 | 0.27420373584852364 |
| alpha | 0.34767631581139713 | 0.35854108524611417 |
| trades | 29 | 11 |
| winrate | 0.41379310344827586 | 0.5454545454545454 |
| sharpe | 0.9553708803786518 | 2.1213558308213547 |
| maxdd | -0.11827496056008402 | -0.08522585802140148 |
| pf | 1.857569714690565 | 4.343914660986051 |
| ann | 0.10921160672876007 | 0.40008366175118826 |

- **Combined OOS gain (stress):** 47.555%
- Full history @ stress: total 47.555%, CAGR 20.266%, benchmark -24.138%, sharpe 1.42, maxdd -0.118, trades 40

## 2070

### The 20s Breakout (2986) — 4h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.31531330081280795 | 0.5407328759300138 |
| alpha | 0.3895363355477257 | 0.3113121442226967 |
| trades | 58 | 28 |
| winrate | 0.3448275862068966 | 0.5714285714285714 |
| sharpe | 1.13368884460605 | 3.0860383426777145 |
| maxdd | -0.23070440824362093 | -0.08897117233868146 |
| pf | 1.4633900227762724 | 3.250425013411573 |
| ann | 0.21364513897054604 | 0.8226891250962995 |

- **Combined OOS gain (stress):** 102.655%
- Full history @ stress: total 103.983%, CAGR 40.235%, benchmark 17.952%, sharpe 1.84, maxdd -0.231, trades 86

### 5 EMA No-Touch Breakout (483) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.22049722990080878 | 0.35542269809234983 |
| alpha | 0.29472026463572654 | 0.1260019663850327 |
| trades | 63 | 36 |
| winrate | 0.36507936507936506 | 0.5 |
| sharpe | 0.8689892277110383 | 2.2352145802709793 |
| maxdd | -0.22161379979553641 | -0.12032900364657273 |
| pf | 1.3429677930354564 | 1.9760792974841763 |
| ann | 0.1511621199701847 | 0.5255386282228369 |

- **Combined OOS gain (stress):** 65.429%
- Full history @ stress: total 66.513%, CAGR 27.363%, benchmark 17.952%, sharpe 1.37, maxdd -0.222, trades 99

### CP Strat ORB (639) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.1154153489012093 | 0.3600578042493514 |
| alpha | 0.18963838363612706 | 0.13063707254203427 |
| trades | 64 | 35 |
| winrate | 0.359375 | 0.5142857142857142 |
| sharpe | 0.5059323231325898 | 2.2543352791738482 |
| maxdd | -0.24129772716799114 | -0.11731598699172963 |
| pf | 1.1559881909684546 | 2.0036431818018134 |
| ann | 0.0802219704345013 | 0.5327885115823685 |

- **Combined OOS gain (stress):** 51.703%
- Full history @ stress: total 52.697%, CAGR 22.236%, benchmark 17.952%, sharpe 1.13, maxdd -0.241, trades 99

### Futures Engulfing Candle Size (823) — 4h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.3340518155404075 | 0.45317766648987345 |
| alpha | 0.4082748502753253 | 0.22375693478255632 |
| trades | 64 | 32 |
| winrate | 0.453125 | 0.5 |
| sharpe | 1.1585224523047477 | 2.6103028837018045 |
| maxdd | -0.1552147228088251 | -0.07754759453330051 |
| pf | 1.4898124696957051 | 2.899395605445895 |
| ann | 0.22583486436405176 | 0.6804496917085594 |

- **Combined OOS gain (stress):** 93.861%
- Full history @ stress: total 95.132%, CAGR 37.315%, benchmark 17.952%, sharpe 1.68, maxdd -0.155, trades 96

### Intraday Volume Swings (931) — 1h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.12047682067480747 | 0.4481716262919573 |
| alpha | 0.19469985540972523 | 0.21968723939172885 |
| trades | 66 | 26 |
| winrate | 0.3333333333333333 | 0.5384615384615384 |
| sharpe | 0.5432264518278384 | 2.453394153082751 |
| maxdd | -0.25434779355132986 | -0.09459716507993898 |
| pf | 1.1525518759273972 | 3.1875882950515835 |
| ann | 0.08368267189299017 | 0.6724154576712233 |

- **Combined OOS gain (stress):** 62.264%
- Full history @ stress: total 63.453%, CAGR 26.247%, benchmark 17.952%, sharpe 1.29, maxdd -0.254, trades 92

## 2080

### Volume Climax Reversal (115) — 1h
> family: volume | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.22004247721023873 | 0.18933212412340827 |
| alpha | 0.37623471380912976 | 0.5420225876290022 |
| trades | 5 | 5 |
| winrate | 0.6 | 0.4 |
| sharpe | 1.3577089027667177 | 1.5072060670892693 |
| maxdd | -0.03676154302721668 | -0.05287620424764827 |
| pf | 8.115579985696009 | 5.442600746472472 |
| ann | 0.15085908105515844 | 0.27227136933173646 |

- **Combined OOS gain (stress):** 45.104%
- Full history @ stress: total 45.104%, CAGR 19.314%, benchmark -43.854%, sharpe 1.39, maxdd -0.064, trades 10

### EM VOL (1748) — 1h
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.1581304965540018 | -0.008044772185622495 |
| alpha | 0.31432273315289283 | 0.34464569131997147 |
| trades | 18 | 7 |
| winrate | 0.4444444444444444 | 0.2857142857142857 |
| sharpe | 0.8227986988356932 | -0.0732359124248403 |
| maxdd | -0.11318257194399906 | -0.04214643789591144 |
| pf | 1.7571559548445836 | 0.8475451117899303 |
| ann | 0.10928560522640485 | -0.011154944415468937 |

- **Combined OOS gain (stress):** 14.881%
- Full history @ stress: total 14.881%, CAGR 6.802%, benchmark -43.854%, sharpe 0.58, maxdd -0.113, trades 25

### Bull vs Medved (2510) — 4h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.44385082633200224 | 0.11537942705295867 |
| alpha | 0.6123389866234412 | 0.4652991702311289 |
| trades | 17 | 9 |
| winrate | 0.35294117647058826 | 0.5555555555555556 |
| sharpe | 1.5595302804492877 | 1.473294103130695 |
| maxdd | -0.10210722417467721 | -0.034052696713545605 |
| pf | 2.5801806306515016 | 6.135920796716301 |
| ann | 0.29628138157818285 | 0.1637501630106264 |

- **Combined OOS gain (stress):** 61.044%
- Full history @ stress: total 68.074%, CAGR 27.928%, benchmark -44.672%, sharpe 1.61, maxdd -0.102, trades 26

### Explosion Range Expansion (3263) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.03830979983800664 | 0.0577137284714031 |
| alpha | 0.20679796012944562 | 0.4076334716495733 |
| trades | 64 | 36 |
| winrate | 0.328125 | 0.2777777777777778 |
| sharpe | 0.24523331755102062 | 0.5601623065383394 |
| maxdd | -0.22681826826871732 | -0.08888308950387125 |
| pf | 1.0835514629633214 | 1.3611605859647815 |
| ann | 0.02691538573983343 | 0.08104075459894644 |

- **Combined OOS gain (stress):** 9.823%
- Full history @ stress: total 14.617%, CAGR 6.685%, benchmark -44.672%, sharpe 0.47, maxdd -0.227, trades 100

## 2081

### PowerZone (1179) — 1h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.08757129959600252 | 0.008994487158345166 |
| alpha | 0.3490391895042594 | 0.3230685612324192 |
| trades | 20 | 12 |
| winrate | 0.5 | 0.4166666666666667 |
| sharpe | 0.6168389626949622 | 0.1750238150412634 |
| maxdd | -0.09834643923573394 | -0.06806839052760993 |
| pf | 1.5335455733932961 | 1.1042387950109553 |
| ann | 0.06110082367631042 | 0.01251319402308293 |

- **Combined OOS gain (stress):** 9.735%
- Full history @ stress: total 9.735%, CAGR 4.505%, benchmark -46.904%, sharpe 0.47, maxdd -0.098, trades 32

### Timer (1788) — 4h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.11929995267600213 | 0.032785155034667834 |
| alpha | 0.37046274337367646 | 0.34328403813221076 |
| trades | 19 | 11 |
| winrate | 0.47368421052631576 | 0.36363636363636365 |
| sharpe | 0.583905795780086 | 0.383987737317446 |
| maxdd | -0.1334067025390967 | -0.09241650012276903 |
| pf | 1.5115398431418068 | 1.2302596408826376 |
| ann | 0.08287841710023702 | 0.04581974106596354 |

- **Combined OOS gain (stress):** 15.600%
- Full history @ stress: total 16.238%, CAGR 7.398%, benchmark -46.163%, sharpe 0.54, maxdd -0.133, trades 30

### The 20s Breakout (2986) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.14113457105200444 | -0.02498488209401284 |
| alpha | 0.3922973617496788 | 0.2855140010035301 |
| trades | 58 | 33 |
| winrate | 0.41379310344827586 | 0.24242424242424243 |
| sharpe | 0.7110617019544819 | -0.16930276345121717 |
| maxdd | -0.1301785629678328 | -0.10287922011827166 |
| pf | 1.2933303527605198 | 0.9219426844011335 |
| ann | 0.09775981550036139 | -0.034529193742387276 |

- **Combined OOS gain (stress):** 11.262%
- Full history @ stress: total 11.876%, CAGR 5.468%, benchmark -46.163%, sharpe 0.43, maxdd -0.130, trades 91

### Fast Slow RVI Crossover (3520) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.07392538902400725 | 0.031018832435651067 |
| alpha | 0.3250881797216816 | 0.341517715533194 |
| trades | 62 | 32 |
| winrate | 0.45161290322580644 | 0.3125 |
| sharpe | 0.39664320637559 | 0.32766654540010676 |
| maxdd | -0.11237603621522174 | -0.16597334641181516 |
| pf | 1.1386847657457324 | 1.1241865802061324 |
| ann | 0.05167749261981003 | 0.04333656856126966 |

- **Combined OOS gain (stress):** 10.724%
- Full history @ stress: total 11.335%, CAGR 5.225%, benchmark -46.163%, sharpe 0.39, maxdd -0.166, trades 94

### Long Explosive V1 (992) — 1h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.03083006649999387 | 0.01895180618348613 |
| alpha | 0.230637823408263 | 0.3330258802575602 |
| trades | 64 | 24 |
| winrate | 0.390625 | 0.4583333333333333 |
| sharpe | -0.006381825039747681 | 0.2486864645489312 |
| maxdd | -0.2271417374830571 | -0.09944022048967793 |
| pf | 0.9919202807020076 | 1.150776072396484 |
| ann | -0.021880699545608784 | 0.026416544403004893 |

- **Combined OOS gain (stress):** -1.246%
- Full history @ stress: total 3.523%, CAGR 1.656%, benchmark -46.904%, sharpe 0.18, maxdd -0.227, trades 88

## 2083

### Adaptive Trend Flow (496) — Daily **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.004724256890576761 | 0.1428187901707736 |
| alpha | 0.3998064874459928 | 0.010489580918487285 |
| trades | 32 | 22 |
| winrate | 0.46875 | 0.5 |
| sharpe | 0.07085619592896975 | 0.9094202323758378 |
| maxdd | -0.1603047345765477 | -0.10813080595376567 |
| pf | 0.9950199611773496 | 1.657029142951934 |
| ann | -0.003339910333758911 | 0.20369929136160692 |

- **Combined OOS gain (stress):** 13.742%
- Full history @ stress: total 102.895%, CAGR 20.320%, benchmark -11.555%, sharpe 1.06, maxdd -0.236, trades 96

## 2084

### Bollinger Band Width Breakout (256) — 30min
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.019082377655595284 | 0.05382104132600274 |
| alpha | 0.4340177813269166 | 0.5054164983297885 |
| trades | 37 | 16 |
| winrate | 0.32432432432432434 | 0.375 |
| sharpe | 0.0280378109743187 | 0.5246122447605632 |
| maxdd | -0.2113178771305293 | -0.14008514813258643 |
| pf | 0.9605283211291143 | 1.3846834643765857 |
| ann | -0.013519381198456304 | 0.07551938453032991 |

- **Combined OOS gain (stress):** 3.371%
- Full history @ stress: total 3.371%, CAGR 1.630%, benchmark -67.758%, sharpe 0.18, maxdd -0.211, trades 53

### EMA Crossover with Volume + Stacked TP & Trailing SL (742) — 30min **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.13498873725560112 | 0.049155958481583495 |
| alpha | 0.588088896238113 | 0.5007514154853693 |
| trades | 14 | 9 |
| winrate | 0.42857142857142855 | 0.3333333333333333 |
| sharpe | 0.755606630225998 | 0.583161926687252 |
| maxdd | -0.1217060329852182 | -0.07067942914377912 |
| pf | 1.8764120679356178 | 1.6186545998811792 |
| ann | 0.09357963636711308 | 0.0689128914053343 |

- **Combined OOS gain (stress):** 19.078%
- Full history @ stress: total 19.078%, CAGR 8.888%, benchmark -67.758%, sharpe 0.70, maxdd -0.122, trades 23

### IU Range Trading (944) — 30min
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.0023915268847951587 | 0.028613414879352872 |
| alpha | 0.4507086320977167 | 0.48020887188313865 |
| trades | 39 | 28 |
| winrate | 0.28205128205128205 | 0.35714285714285715 |
| sharpe | 0.07627597174983389 | 0.3119380736733382 |
| maxdd | -0.20585547949966354 | -0.16412267129762903 |
| pf | 0.9945310825871391 | 1.110898023291975 |
| ann | -0.0016901587908005888 | 0.03995758808846439 |

- **Combined OOS gain (stress):** 2.615%
- Full history @ stress: total 2.615%, CAGR 1.267%, benchmark -67.758%, sharpe 0.16, maxdd -0.227, trades 67

### Long Term Profitable Swing (994) — 30min
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.021283062676794917 | 0.0058745248162643815 |
| alpha | 0.43181709630571696 | 0.45746998182005016 |
| trades | 44 | 26 |
| winrate | 0.20454545454545456 | 0.3076923076923077 |
| sharpe | -0.01626807107330126 | 0.13657241437289075 |
| maxdd | -0.19360334541280644 | -0.20343478691102057 |
| pf | 0.9577173670830136 | 1.0208350593972646 |
| ann | -0.015083453043372774 | 0.008167747261164537 |

- **Combined OOS gain (stress):** -1.553%
- Full history @ stress: total -1.553%, CAGR -0.761%, benchmark -67.758%, sharpe 0.04, maxdd -0.203, trades 70

## 2090

### Hercules A.T.C. 2006 (2485) — 4h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.07013477896359588 | 0.06680556564894125 |
| alpha | 0.3053007611060906 | 0.26425779494830426 |
| trades | 49 | 28 |
| winrate | 0.32653061224489793 | 0.4642857142857143 |
| sharpe | -0.20766770197575476 | 0.6579640343051169 |
| maxdd | -0.20328768930823415 | -0.10456810934469385 |
| pf | 0.8635717698309648 | 1.4015624613740918 |
| ann | -0.05007487532627497 | 0.09396734124747907 |

- **Combined OOS gain (stress):** -0.801%
- Full history @ stress: total 2.030%, CAGR 0.973%, benchmark -45.122%, sharpe 0.14, maxdd -0.203, trades 77

### Explosion (3261) — 4h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.04618412237280611 | 0.028192227988418805 |
| alpha | 0.4216196624424926 | 0.22564445728778182 |
| trades | 57 | 28 |
| winrate | 0.3684210526315789 | 0.4642857142857143 |
| sharpe | 0.25750170285388985 | 0.29472765592452044 |
| maxdd | -0.21070328896845225 | -0.10486770395408507 |
| pf | 1.099017748929494 | 1.4041446170977603 |
| ann | 0.03241128199762611 | 0.039366246814113826 |

- **Combined OOS gain (stress):** 7.568%
- Full history @ stress: total 17.811%, CAGR 8.218%, benchmark -45.122%, sharpe 0.47, maxdd -0.211, trades 85

### 5 EMA No-Touch Breakout (483) — 4h
> family: breakout | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.14639458899479463 | -0.0007975829426792869 |
| alpha | 0.22904095107489186 | 0.19665464635668373 |
| trades | 66 | 36 |
| winrate | 0.30303030303030304 | 0.3888888888888889 |
| sharpe | -0.47485824786095215 | 0.08018525047846527 |
| maxdd | -0.2454585433178874 | -0.1339659418836877 |
| pf | 0.7796358039854148 | 0.9976714320818537 |
| ann | -0.10580017763141825 | -0.0011074980823270186 |

- **Combined OOS gain (stress):** -14.708%
- Full history @ stress: total -14.708%, CAGR -7.379%, benchmark -45.122%, sharpe -0.30, maxdd -0.245, trades 102

### Futures Engulfing Candle Size (823) — 4h
> family: pattern | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.12652607515679282 | 0.015407688993795965 |
| alpha | 0.24890946491289367 | 0.21285991829315898 |
| trades | 68 | 35 |
| winrate | 0.35294117647058826 | 0.4 |
| sharpe | -0.33936256190129593 | 0.20976566970733204 |
| maxdd | -0.22506723554950026 | -0.10564290165587964 |
| pf | 0.8298081855698847 | 1.1522994400888857 |
| ann | -0.09114567297678411 | 0.021461830281103156 |

- **Combined OOS gain (stress):** -11.307%
- Full history @ stress: total -8.776%, CAGR -4.329%, benchmark -45.122%, sharpe -0.10, maxdd -0.225, trades 103

### Hull MA Reversal (89) — 4h
> family: trend | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.11263020904599619 | 0.09758821244971916 |
| alpha | 0.2628053310236903 | 0.29504044174908217 |
| trades | 55 | 29 |
| winrate | 0.38181818181818183 | 0.4827586206896552 |
| sharpe | -0.3005600115001988 | 0.7964205380546072 |
| maxdd | -0.20027000192843625 | -0.09737926176385492 |
| pf | 0.8562243247711634 | 1.709052134248586 |
| ann | -0.0809545654758137 | 0.13805069876363074 |

- **Combined OOS gain (stress):** -2.603%
- Full history @ stress: total 6.671%, CAGR 3.161%, benchmark -45.122%, sharpe 0.25, maxdd -0.200, trades 84

## 2100

### Exp Moving Average FN (1992) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.04442178414880482 | 0.4873841748376868 |
| alpha | 0.5450538954003851 | 0.4806888137664289 |
| trades | 37 | 21 |
| winrate | 0.32432432432432434 | 0.47619047619047616 |
| sharpe | 0.3032199548041528 | 2.1733642700947446 |
| maxdd | -0.12922041931326078 | -0.07071892725756346 |
| pf | 1.1444874861831074 | 3.072088962523747 |
| ann | 0.03118231281689554 | 0.7356349828992939 |

- **Combined OOS gain (stress):** 55.346%
- Full history @ stress: total 56.599%, CAGR 23.708%, benchmark -46.776%, sharpe 1.21, maxdd -0.129, trades 58

### Hercules A.T.C. 2006 (2485) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.19531400838160518 | 0.48349196771648684 |
| alpha | 0.6959461196331854 | 0.47679660664522894 |
| trades | 39 | 29 |
| winrate | 0.38461538461538464 | 0.4827586206896552 |
| sharpe | 1.173309066963491 | 2.395573544296036 |
| maxdd | -0.09392590681601587 | -0.09113989564319835 |
| pf | 1.858673272971762 | 2.533988301715746 |
| ann | 0.1343301246532571 | 0.7293305712389733 |

- **Combined OOS gain (stress):** 77.324%
- Full history @ stress: total 80.955%, CAGR 32.489%, benchmark -46.776%, sharpe 1.74, maxdd -0.094, trades 68

### Color XMUV Time (2621) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.036276103183194186 | 0.4542752794983642 |
| alpha | 0.46435600806838606 | 0.4475799184271063 |
| trades | 49 | 31 |
| winrate | 0.32653061224489793 | 0.41935483870967744 |
| sharpe | -0.12959749648984756 | 2.0538859733372328 |
| maxdd | -0.1621113484107085 | -0.08136511735304686 |
| pf | 0.9070383337952849 | 2.5427932109623854 |
| ann | -0.025766952084742445 | 0.6822126996730697 |

- **Combined OOS gain (stress):** 40.152%
- Full history @ stress: total 43.022%, CAGR 18.499%, benchmark -46.776%, sharpe 0.97, maxdd -0.162, trades 80

### Explosion (3261) — 4h **(pick)**
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.08356818177960745 | 0.521149290039292 |
| alpha | 0.5842002930311877 | 0.5144539289680341 |
| trades | 57 | 33 |
| winrate | 0.3508771929824561 | 0.42424242424242425 |
| sharpe | 0.43582937531474725 | 2.378541193145647 |
| maxdd | -0.1609028367010269 | -0.11106682609995255 |
| pf | 1.1490792163852612 | 2.8268813866572153 |
| ann | 0.058340043172988354 | 0.7905943193635676 |

- **Combined OOS gain (stress):** 64.827%
- Full history @ stress: total 68.202%, CAGR 27.974%, benchmark -46.776%, sharpe 1.32, maxdd -0.161, trades 90

### Breakthrough Volatility (3271) — 4h
> family: breakout | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.19135792564798848 | 0.391593146318689 |
| alpha | 0.30927418560359177 | 0.3848977852474311 |
| trades | 108 | 56 |
| winrate | 0.3425925925925926 | 0.44642857142857145 |
| sharpe | -0.7199392067352961 | 1.8311777663927495 |
| maxdd | -0.2902667002673376 | -0.12836873587384057 |
| pf | 0.7794994593749253 | 1.5913906625320342 |
| ann | -0.13933979305393196 | 0.5823678667685637 |

- **Combined OOS gain (stress):** 12.530%
- Full history @ stress: total 14.834%, CAGR 6.781%, benchmark -46.776%, sharpe 0.41, maxdd -0.290, trades 164

## 2110

### EMA Sticker (1656) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 1.446136785836012 | 0.3734412891811394 |
| alpha | 0.27973176228813124 | 0.096995591014708 |
| trades | 64 | 35 |
| winrate | 0.46875 | 0.45714285714285713 |
| sharpe | 2.264874504404457 | 1.6711267732137804 |
| maxdd | -0.15727074325619916 | -0.14538484096907456 |
| pf | 2.1961549196765424 | 2.083358882575228 |
| ann | 0.881281358349411 | 0.5537758259244558 |

- **Combined OOS gain (stress):** 235.963%
- Full history @ stress: total 235.963%, CAGR 77.683%, benchmark 184.144%, sharpe 2.07, maxdd -0.157, trades 99

### Bull vs Medved (2510) — 1h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 1.8984218066720175 | 0.37507661557524097 |
| alpha | 0.7488890963916437 | 0.09138867231282966 |
| trades | 68 | 43 |
| winrate | 0.5 | 0.46511627906976744 |
| sharpe | 2.3833899389001716 | 1.8305129351604434 |
| maxdd | -0.13277455629254653 | -0.09042226911886819 |
| pf | 2.3620555894966393 | 1.8213263968363882 |
| ann | 1.1208393662858875 | 0.5563457344687781 |

- **Combined OOS gain (stress):** 298.555%
- Full history @ stress: total 298.555%, CAGR 92.682%, benchmark 181.931%, sharpe 2.21, maxdd -0.133, trades 111

### The 20s Breakout (2986) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 1.4193368106800106 | 0.42627985527379986 |
| alpha | 0.25293178713212994 | 0.14983415710736847 |
| trades | 57 | 30 |
| winrate | 0.45614035087719296 | 0.4666666666666667 |
| sharpe | 2.442577747315874 | 2.1439621724516496 |
| maxdd | -0.16157066563061873 | -0.09550803336516722 |
| pf | 2.5156749620915706 | 2.854825884448156 |
| ann | 0.8666963008252673 | 0.6374082512977726 |

- **Combined OOS gain (stress):** 245.065%
- Full history @ stress: total 248.270%, CAGR 80.742%, benchmark 184.144%, sharpe 2.36, maxdd -0.162, trades 87

### Demo GPT - Day Trading Scalping (675) — 4h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 1.7308690305880137 | 0.4326027466552045 |
| alpha | 0.564464007040133 | 0.1561570484887731 |
| trades | 54 | 24 |
| winrate | 0.5555555555555556 | 0.5416666666666666 |
| sharpe | 2.4933656952610095 | 2.028703965920165 |
| maxdd | -0.10602089847772034 | -0.13590795527568855 |
| pf | 2.563087421268411 | 3.425246911355869 |
| ann | 1.0334696988710461 | 0.6474979032412795 |

- **Combined OOS gain (stress):** 291.225%
- Full history @ stress: total 291.225%, CAGR 90.993%, benchmark 184.144%, sharpe 2.34, maxdd -0.136, trades 78

### Long Explosive V1 (992) — 4h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 1.271890145284011 | 0.3820251921240534 |
| alpha | 0.10548512173613034 | 0.105579493957622 |
| trades | 75 | 31 |
| winrate | 0.52 | 0.45161290322580644 |
| sharpe | 2.045866248140895 | 1.8318238415277417 |
| maxdd | -0.15499325776160544 | -0.1131272175877388 |
| pf | 1.9416783159946807 | 2.0558016152733996 |
| ann | 0.7855845068688114 | 0.5672786367928357 |

- **Combined OOS gain (stress):** 213.981%
- Full history @ stress: total 216.898%, CAGR 72.827%, benchmark 184.144%, sharpe 1.99, maxdd -0.155, trades 106

## 2120

### Bull vs Medved (2510) — 1h **(pick)**
> family: trend | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.13522183389839304 | 0.13503924220203434 |
| alpha | 0.4182287750325948 | 0.3045894152124149 |
| trades | 61 | 35 |
| winrate | 0.4262295081967213 | 0.34285714285714286 |
| sharpe | -0.5231982639222748 | 0.9709589457788873 |
| maxdd | -0.23705404070582736 | -0.08131533075656994 |
| pf | 0.7605487363731884 | 1.4472014843942167 |
| ann | -0.09754726948307091 | 0.19233470603456015 |

- **Combined OOS gain (stress):** -1.844%
- Full history @ stress: total -0.079%, CAGR -0.038%, benchmark -61.028%, sharpe 0.09, maxdd -0.237, trades 96

### Explosion Range Expansion (3263) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.0548878101839918 | -0.0028625050045879563 |
| alpha | 0.49552090916205727 | 0.17568855032912567 |
| trades | 69 | 35 |
| winrate | 0.34782608695652173 | 0.34285714285714286 |
| sharpe | -0.1514354351340603 | 0.05898159969333291 |
| maxdd | -0.2122329712674702 | -0.09616352209613843 |
| pf | 0.8975250317582422 | 1.0969872890229169 |
| ann | -0.03909712004322774 | -0.00397318566996796 |

- **Combined OOS gain (stress):** -5.759%
- Full history @ stress: total -2.894%, CAGR -1.384%, benchmark -60.763%, sharpe 0.00, maxdd -0.212, trades 104

### Expert AML MFI (3443) — 4h
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | -0.0027818331903968208 | 0.1008814552982451 |
| alpha | 0.5476268861556522 | 0.27943251063195873 |
| trades | 22 | 7 |
| winrate | 0.36363636363636365 | 0.5714285714285714 |
| sharpe | 0.03316865247328782 | 1.3116813143918578 |
| maxdd | -0.08103616436689409 | -0.03699978472732124 |
| pf | 0.9850361553147479 | 2.735280787008289 |
| ann | -0.0019661119767385715 | 0.1427956689392389 |

- **Combined OOS gain (stress):** 9.782%
- Full history @ stress: total 9.782%, CAGR 4.526%, benchmark -60.763%, sharpe 0.47, maxdd -0.099, trades 29

### Resonance Hunter (3617) — 4h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.01466990522239564 | 0.038091175950200507 |
| alpha | 0.5357388141236534 | 0.21664223128391413 |
| trades | 40 | 13 |
| winrate | 0.375 | 0.38461538461538464 |
| sharpe | -0.0016432678494899431 | 0.44588110114892865 |
| maxdd | -0.14523527609525533 | -0.1013633500852621 |
| pf | 0.9591771247111535 | 1.285636694987329 |
| ann | -0.010386445668400857 | 0.05328910025674238 |

- **Combined OOS gain (stress):** 2.286%
- Full history @ stress: total 2.286%, CAGR 1.078%, benchmark -60.763%, sharpe 0.15, maxdd -0.155, trades 53

### IU Range Trading (944) — 1h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.05027964798679696 | 0.07175117443219592 |
| alpha | 0.5031709609441909 | 0.24130134744257647 |
| trades | 29 | 14 |
| winrate | 0.20689655172413793 | 0.42857142857142855 |
| sharpe | -0.22502120349766852 | 0.7291000388728487 |
| maxdd | -0.13994226808760113 | -0.07011603982244718 |
| pf | 0.8209455694993504 | 1.8870738821585442 |
| ann | -0.03578951731759461 | 0.10101693600331374 |

- **Combined OOS gain (stress):** 1.786%
- Full history @ stress: total 3.740%, CAGR 1.757%, benchmark -61.028%, sharpe 0.20, maxdd -0.140, trades 43

## 2140

### PowerZone (1179) — 1h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.10407648577160167 | 0.0814951900836105 |
| alpha | 0.3278264857716017 | 0.36499635197361824 |
| trades | 20 | 8 |
| winrate | 0.45 | 0.625 |
| sharpe | 0.6362856443525325 | 1.0038332847332014 |
| maxdd | -0.1328461379724455 | -0.05175640566972506 |
| pf | 1.5475607336412087 | 2.348126015095156 |
| ann | 0.07245242018851328 | 0.11494330625746274 |

- **Combined OOS gain (stress):** 19.405%
- Full history @ stress: total 19.405%, CAGR 8.777%, benchmark -42.188%, sharpe 0.75, maxdd -0.133, trades 28

### Explosion Range Expansion (3263) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.011362575176007583 | -0.0019275892352377255 |
| alpha | 0.2351125751760076 | 0.27878780734330033 |
| trades | 60 | 34 |
| winrate | 0.3333333333333333 | 0.4117647058823529 |
| sharpe | 0.13191910647189226 | 0.06882110720535695 |
| maxdd | -0.18066005245947625 | -0.1405095303885172 |
| pf | 1.1424121548415982 | 0.8503245322981404 |
| ann | 0.00801410742708697 | -0.0026760001943959555 |

- **Combined OOS gain (stress):** 0.941%
- Full history @ stress: total 4.252%, CAGR 1.995%, benchmark -42.188%, sharpe 0.20, maxdd -0.192, trades 94

### Futures Engulfing Candle Size (823) — 4h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.22631083627160664 | -0.052945984044407535 |
| alpha | 0.45006083627160665 | 0.22776941253413052 |
| trades | 52 | 32 |
| winrate | 0.4230769230769231 | 0.4375 |
| sharpe | 0.8671596433460008 | -0.3063706777478989 |
| maxdd | -0.13393574335039915 | -0.14755640704945894 |
| pf | 1.3856316804011979 | 0.8267221941104208 |
| ann | 0.15503328702685204 | -0.07276535938338247 |

- **Combined OOS gain (stress):** 16.138%
- Full history @ stress: total 15.881%, CAGR 7.242%, benchmark -42.188%, sharpe 0.46, maxdd -0.173, trades 84

### ICT NY Kill Zone Auto Trading (915) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.04304152816240103 | -0.0023338633240109763 |
| alpha | 0.26679152816240104 | 0.2783815332545271 |
| trades | 16 | 9 |
| winrate | 0.3125 | 0.4444444444444444 |
| sharpe | 0.3475430521106305 | 0.020226721126083647 |
| maxdd | -0.0662721476143997 | -0.05270351351730007 |
| pf | 1.2583655690409632 | 0.9745934987144931 |
| ann | 0.030219364172166863 | -0.0032397591461403863 |

- **Combined OOS gain (stress):** 4.061%
- Full history @ stress: total 4.061%, CAGR 1.906%, benchmark -42.188%, sharpe 0.23, maxdd -0.068, trades 25

### Long Explosive V1 (992) — 1h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.07978614317920862 | 0.07302753985382271 |
| alpha | 0.30353614317920863 | 0.35652870174383045 |
| trades | 59 | 19 |
| winrate | 0.4067796610169492 | 0.5263157894736842 |
| sharpe | 0.36732456112468526 | 0.5626095117302113 |
| maxdd | -0.20618024062162998 | -0.10805365530206301 |
| pf | 1.1089314931120118 | 1.4126590457803527 |
| ann | 0.05572898007660165 | 0.10283835575770528 |

- **Combined OOS gain (stress):** 15.864%
- Full history @ stress: total 17.199%, CAGR 7.819%, benchmark -42.188%, sharpe 0.46, maxdd -0.206, trades 78

## 2150

### HSI1 First 30m Candle (1413) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.09313839745039554 | 0.14918416359325493 |
| alpha | 0.1308083874719992 | 0.15526487116649978 |
| trades | 46 | 16 |
| winrate | 0.391304347826087 | 0.4375 |
| sharpe | -0.29528084907465785 | 1.2018135753884638 |
| maxdd | -0.20350398971888883 | -0.10671896279583015 |
| pf | 0.8160210746319837 | 2.4226916496970388 |
| ann | -0.0667379876835904 | 0.21302041860711363 |

- **Combined OOS gain (stress):** 4.215%
- Full history @ stress: total 4.215%, CAGR 1.978%, benchmark -20.266%, sharpe 0.20, maxdd -0.229, trades 62

### Kalman Filter Candles (2152) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.05609586837919256 | 0.16084415889239145 |
| alpha | 0.16785091654320217 | 0.1669248664656363 |
| trades | 51 | 25 |
| winrate | 0.49019607843137253 | 0.44 |
| sharpe | -0.0714101758271675 | 1.3223501610523027 |
| maxdd | -0.24600493586039196 | -0.09275975428797678 |
| pf | 0.9059589533229989 | 1.8223090192971727 |
| ann | -0.03996501102351091 | 0.23014678819455425 |

- **Combined OOS gain (stress):** 9.573%
- Full history @ stress: total 9.573%, CAGR 4.432%, benchmark -20.266%, sharpe 0.31, maxdd -0.251, trades 76

### RSI Threshold (2406) — 4h **(pick)**
> family: mean_reversion | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.14126087065800053 | 0.1900532475866632 |
| alpha | 0.36520765558039525 | 0.19613395515990806 |
| trades | 11 | 6 |
| winrate | 0.7272727272727273 | 0.6666666666666666 |
| sharpe | 0.5758501499315641 | 1.560771924751571 |
| maxdd | -0.26977470546897675 | -0.07467143706416002 |
| pf | 2.03701351527329 | 6.068840783548694 |
| ann | 0.09784565063436568 | 0.2733428192744103 |

- **Combined OOS gain (stress):** 35.816%
- Full history @ stress: total 40.414%, CAGR 17.469%, benchmark -20.266%, sharpe 0.94, maxdd -0.270, trades 17

### Hercules A.T.C. 2006 (2485) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.13532758195680716 | 0.17215677692593823 |
| alpha | 0.3592743668792019 | 0.17823748449918309 |
| trades | 53 | 22 |
| winrate | 0.3584905660377358 | 0.45454545454545453 |
| sharpe | 0.6537832484578651 | 1.474810742786761 |
| maxdd | -0.12956105722649358 | -0.0779153001190529 |
| pf | 1.2740593844613308 | 2.0450651784633727 |
| ann | 0.09381027933423902 | 0.24682697584674385 |

- **Combined OOS gain (stress):** 33.078%
- Full history @ stress: total 33.078%, CAGR 14.517%, benchmark -20.266%, sharpe 0.93, maxdd -0.130, trades 75

### The 20s Breakout (2986) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.02482689207760913 | 0.1398719154035888 |
| alpha | 0.24877367700000386 | 0.14595262297683365 |
| trades | 65 | 24 |
| winrate | 0.3230769230769231 | 0.4166666666666667 |
| sharpe | 0.18818371169660558 | 1.1418814047644932 |
| maxdd | -0.1278237048694384 | -0.09014483143302376 |
| pf | 1.0366834679097128 | 1.6894941424974674 |
| ann | 0.017476461954222033 | 0.19939086250837312 |

- **Combined OOS gain (stress):** 16.817%
- Full history @ stress: total 16.817%, CAGR 7.652%, benchmark -20.266%, sharpe 0.51, maxdd -0.156, trades 89

## 2160

### Sunil 2 Bar Breakout (1360) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.22174513158320552 | 0.3301656748684405 |
| alpha | 0.6338782039902505 | 0.6002207881568666 |
| trades | 39 | 17 |
| winrate | 0.3076923076923077 | 0.5882352941176471 |
| sharpe | 0.783983732349594 | 1.8675773933958104 |
| maxdd | -0.1827743203936144 | -0.061952837133562144 |
| pf | 1.376404795455047 | 3.7872681106311457 |
| ann | 0.15199352873688743 | 0.4862032752344667 |

- **Combined OOS gain (stress):** 62.512%
- Full history @ stress: total 69.296%, CAGR 28.369%, benchmark -53.346%, sharpe 1.25, maxdd -0.183, trades 56

### US Index First 30m Candle (1515) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.18116401199040943 | 0.2959057803440295 |
| alpha | 0.5932970843974544 | 0.5659608936324556 |
| trades | 67 | 34 |
| winrate | 0.29850746268656714 | 0.4411764705882353 |
| sharpe | 0.7065425291140749 | 1.9014276019018435 |
| maxdd | -0.15135281170440318 | -0.07546416516999788 |
| pf | 1.2510112438328576 | 2.2772686768709587 |
| ann | 0.12482689561166138 | 0.43330987195644344 |

- **Combined OOS gain (stress):** 53.068%
- Full history @ stress: total 59.458%, CAGR 24.774%, benchmark -53.346%, sharpe 1.21, maxdd -0.151, trades 101

### The 20s Breakout (2986) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.4293004056356111 | 0.2728450268474678 |
| alpha | 0.8414334780426561 | 0.5429001401358939 |
| trades | 58 | 32 |
| winrate | 0.3448275862068966 | 0.46875 |
| sharpe | 1.4193963583199884 | 1.734764171546986 |
| maxdd | -0.12879863555261606 | -0.06958414816242098 |
| pf | 1.711770229362658 | 2.2521647821580486 |
| ann | 0.28703872472872005 | 0.3980107252869365 |

- **Combined OOS gain (stress):** 81.928%
- Full history @ stress: total 89.523%, CAGR 35.428%, benchmark -53.346%, sharpe 1.61, maxdd -0.129, trades 90

### Rubberbands 3 (4116) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.29188670077401224 | 0.22935155941521046 |
| alpha | 0.7040197731810572 | 0.4994066727036366 |
| trades | 69 | 37 |
| winrate | 0.3333333333333333 | 0.40540540540540543 |
| sharpe | 0.993678049144395 | 1.5175406929790327 |
| maxdd | -0.13041429250839753 | -0.07546450707229169 |
| pf | 1.3755295570775392 | 1.8631337832183588 |
| ann | 0.1983337722824141 | 0.33211176052105684 |

- **Combined OOS gain (stress):** 58.818%
- Full history @ stress: total 65.449%, CAGR 26.976%, benchmark -53.346%, sharpe 1.25, maxdd -0.130, trades 106

### Long Explosive V1 (992) — 4h **(pick)**
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.31576001326040704 | 0.3397426125539167 |
| alpha | 0.727893085667452 | 0.6097977258423428 |
| trades | 55 | 24 |
| winrate | 0.38181818181818183 | 0.7083333333333334 |
| sharpe | 1.095003795930194 | 2.090184976926562 |
| maxdd | -0.11298038252346743 | -0.054995452446644055 |
| pf | 1.5013501619164944 | 3.6489696979252075 |
| ann | 0.2139363237033285 | 0.5010845499260188 |

- **Combined OOS gain (stress):** 76.278%
- Full history @ stress: total 83.637%, CAGR 33.416%, benchmark -53.346%, sharpe 1.52, maxdd -0.113, trades 79

## 2170

### Explosion Range Expansion (3263) — 4h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.19660315634200587 | 0.41263400020021535 |
| alpha | 0.49738237712122657 | 0.44891847044694977 |
| trades | 54 | 32 |
| winrate | 0.46296296296296297 | 0.5625 |
| sharpe | 0.9329764929894578 | 2.301632472583223 |
| maxdd | -0.0727049416215294 | -0.05663859435297636 |
| pf | 1.540771343701497 | 3.2867573262736482 |
| ann | 0.13519427874359757 | 0.6156923726100614 |

- **Combined OOS gain (stress):** 69.036%
- Full history @ stress: total 69.036%, CAGR 28.275%, benchmark -31.013%, sharpe 1.49, maxdd -0.111, trades 86

### Rubberbands 3 (4116) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.0763702439051942 | 0.2571057541775743 |
| alpha | 0.2244089768740265 | 0.29339022442430873 |
| trades | 66 | 32 |
| winrate | 0.3333333333333333 | 0.53125 |
| sharpe | -0.27046315496449924 | 1.5208235136486652 |
| maxdd | -0.22274807010471387 | -0.06456514389661727 |
| pf | 0.8755927528416482 | 2.0231875815130604 |
| ann | -0.05457958005278429 | 0.37406068362692846 |

- **Combined OOS gain (stress):** 16.110%
- Full history @ stress: total 16.110%, CAGR 7.342%, benchmark -31.013%, sharpe 0.47, maxdd -0.255, trades 98

### Futures Engulfing Candle Size (823) — 4h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.07181699490039306 | 0.36717295829288754 |
| alpha | 0.22896222587882764 | 0.40345742853962197 |
| trades | 60 | 31 |
| winrate | 0.35 | 0.5806451612903226 |
| sharpe | -0.2601090163592184 | 2.156141095345989 |
| maxdd | -0.1921056057506907 | -0.06335823181552525 |
| pf | 0.8549173507614393 | 2.6080387319891294 |
| ann | -0.05128928767846408 | 0.5439361948280395 |

- **Combined OOS gain (stress):** 26.899%
- Full history @ stress: total 26.899%, CAGR 11.963%, benchmark -31.013%, sharpe 0.72, maxdd -0.227, trades 91

### HSI First 30m Candle (893) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.0763702439051942 | 0.2571057541775743 |
| alpha | 0.2244089768740265 | 0.29339022442430873 |
| trades | 66 | 32 |
| winrate | 0.3333333333333333 | 0.53125 |
| sharpe | -0.27046315496449924 | 1.5208235136486652 |
| maxdd | -0.22274807010471387 | -0.06456514389661727 |
| pf | 0.8755927528416482 | 2.0231875815130604 |
| ann | -0.05457958005278429 | 0.37406068362692846 |

- **Combined OOS gain (stress):** 16.110%
- Full history @ stress: total 16.110%, CAGR 7.342%, benchmark -31.013%, sharpe 0.47, maxdd -0.255, trades 98

### Long Explosive V1 (992) — 4h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.014340910934003137 | 0.32514745550972046 |
| alpha | 0.31512013171322384 | 0.3614319257564549 |
| trades | 28 | 22 |
| winrate | 0.32142857142857145 | 0.6363636363636364 |
| sharpe | 0.1437761469844101 | 1.7106150413264214 |
| maxdd | -0.14715452209094992 | -0.06428475061055128 |
| pf | 1.0442110194216414 | 3.1664948508956092 |
| ann | 0.0101103694585023 | 0.4784222336648487 |

- **Combined OOS gain (stress):** 34.415%
- Full history @ stress: total 34.415%, CAGR 15.061%, benchmark -31.013%, sharpe 0.86, maxdd -0.184, trades 50

## 2180

### Parabolic SAR Bug5 (1626) — 4h **(pick)**
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.06779441142880183 | 0.5051858328007075 |
| alpha | 0.3817532214974517 | 0.39580071953209894 |
| trades | 14 | 8 |
| winrate | 0.5 | 0.625 |
| sharpe | 0.3648513529795432 | 2.9439931507932497 |
| maxdd | -0.15399849760942197 | -0.06378701520869845 |
| pf | 1.3265813853291528 | 13.913889060625596 |
| ann | 0.0474322501788671 | 0.7645508993162651 |

- **Combined OOS gain (stress):** 60.723%
- Full history @ stress: total 60.723%, CAGR 25.243%, benchmark -21.556%, sharpe 1.34, maxdd -0.154, trades 22

### EMA Prediction (2034) — Daily
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.040369654735148974 | 0.4884989498374903 |
| alpha | 0.34613588403625084 | 0.36456452360798197 |
| trades | 39 | 20 |
| winrate | 0.48717948717948717 | 0.7 |
| sharpe | -0.04330113989742995 | 2.9249421850106128 |
| maxdd | -0.2150842510214036 | -0.08644904159330846 |
| pf | 0.9006859874948898 | 3.8191143775432694 |
| ann | -0.028692325563837495 | 0.7374418249738641 |

- **Combined OOS gain (stress):** 42.841%
- Full history @ stress: total 117966.752%, CAGR 28.411%, benchmark 539.183%, sharpe 0.81, maxdd -0.659, trades 711

### Kalman Filter Candles (2152) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.025202900688403584 | 0.5904723607683116 |
| alpha | 0.3391617107570535 | 0.481087247499703 |
| trades | 40 | 24 |
| winrate | 0.525 | 0.625 |
| sharpe | 0.19097305235322812 | 3.290313897275317 |
| maxdd | -0.20580261730490623 | -0.07440786194753346 |
| pf | 1.0562802389088204 | 4.212821223144633 |
| ann | 0.01774018491823437 | 0.9049172418425382 |

- **Combined OOS gain (stress):** 63.056%
- Full history @ stress: total 63.056%, CAGR 26.102%, benchmark -21.556%, sharpe 1.38, maxdd -0.206, trades 64

### Explosion (3261) — 4h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.15614159134880556 | 0.47528459939836276 |
| alpha | 0.47010040141745546 | 0.3658994861297542 |
| trades | 50 | 22 |
| winrate | 0.44 | 0.5 |
| sharpe | 0.830287054952078 | 2.9366612558550504 |
| maxdd | -0.10504830692297995 | -0.09649924161326673 |
| pf | 1.411910267055074 | 3.3362280300967675 |
| ann | 0.1079394065132302 | 0.7160577461464828 |

- **Combined OOS gain (stress):** 70.564%
- Full history @ stress: total 70.564%, CAGR 28.824%, benchmark -21.556%, sharpe 1.68, maxdd -0.105, trades 72

### Fast Slow RVI Crossover (3520) — Daily
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.11833702912838096 | 0.42229155551503106 |
| alpha | 0.5048425678997808 | 0.2983571292855227 |
| trades | 24 | 9 |
| winrate | 0.375 | 0.6666666666666666 |
| sharpe | 0.5673099517177408 | 3.0426893915451267 |
| maxdd | -0.15505204091874736 | -0.09974446323232611 |
| pf | 1.3524773387477909 | 4.701056424781228 |
| ann | 0.08222018425330657 | 0.6310529195810832 |

- **Combined OOS gain (stress):** 59.060%
- Full history @ stress: total 77267.983%, CAGR 26.507%, benchmark 539.183%, sharpe 0.80, maxdd -0.666, trades 401

## 2190

### Sunil 2 Bar Breakout (1360) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.2532891215256057 | 0.6751557426809718 |
| alpha | 0.3313901935011033 | 0.45594233197819944 |
| trades | 43 | 16 |
| winrate | 0.4186046511627907 | 0.5625 |
| sharpe | 0.8860478699576694 | 2.8131274985947186 |
| maxdd | -0.11791599993949697 | -0.07042261286683915 |
| pf | 1.6005163160244988 | 4.475207634654867 |
| ann | 0.1729276680068923 | 1.047218041119803 |

- **Combined OOS gain (stress):** 109.945%
- Full history @ stress: total 109.945%, CAGR 42.165%, benchmark 15.835%, sharpe 1.64, maxdd -0.158, trades 59

### Timer (1788) — 1h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.4123554472768092 | 0.5339984252950776 |
| alpha | 0.5029898883644225 | 0.31948333216726765 |
| trades | 68 | 33 |
| winrate | 0.45588235294117646 | 0.42424242424242425 |
| sharpe | 1.2398498306685615 | 2.520515032062914 |
| maxdd | -0.11953142645616655 | -0.09134337161758732 |
| pf | 1.5565873395819727 | 2.3651020402331437 |
| ann | 0.27624013252450874 | 0.8116342864624952 |

- **Combined OOS gain (stress):** 116.655%
- Full history @ stress: total 118.103%, CAGR 44.759%, benchmark 14.260%, sharpe 1.72, maxdd -0.120, trades 101

### Last Price (2126) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.26614593963640587 | 0.721560240444397 |
| alpha | 0.3442470116119035 | 0.5023468297416247 |
| trades | 42 | 18 |
| winrate | 0.42857142857142855 | 0.5 |
| sharpe | 0.9018984339275343 | 3.095235952178429 |
| maxdd | -0.15297809545015384 | -0.07042862325855248 |
| pf | 1.7864055394994773 | 4.160762270148164 |
| ann | 0.18141559595344425 | 1.1263993838638586 |

- **Combined OOS gain (stress):** 117.975%
- Full history @ stress: total 124.665%, CAGR 46.808%, benchmark 15.835%, sharpe 1.79, maxdd -0.153, trades 60

### The 20s Breakout (2986) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.3312371126412086 | 0.5343248530619942 |
| alpha | 0.40933818461670624 | 0.31511144235922184 |
| trades | 62 | 28 |
| winrate | 0.4032258064516129 | 0.5 |
| sharpe | 1.2046833747386605 | 2.5767330016459384 |
| maxdd | -0.0941101158984925 | -0.06890003446043558 |
| pf | 1.570875241619431 | 3.213437536072262 |
| ann | 0.2240070752231229 | 0.8121696948266963 |

- **Combined OOS gain (stress):** 104.255%
- Full history @ stress: total 104.425%, CAGR 40.379%, benchmark 15.835%, sharpe 1.74, maxdd -0.094, trades 90

### Futures Engulfing Candle Size (823) — 4h **(pick)**
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.4356601821376087 | 0.7980151679635532 |
| alpha | 0.5137612541131064 | 0.5788017572607809 |
| trades | 60 | 31 |
| winrate | 0.5333333333333333 | 0.45161290322580644 |
| sharpe | 1.5875197283102664 | 3.145321515353402 |
| maxdd | -0.10595355144320473 | -0.09393105828796433 |
| pf | 2.05291366776742 | 3.0948084936778786 |
| ann | 0.2910819364165016 | 1.2586697907741766 |

- **Combined OOS gain (stress):** 158.134%
- Full history @ stress: total 158.349%, CAGR 56.866%, benchmark 15.835%, sharpe 2.23, maxdd -0.106, trades 91

## 2210

### RSI Adaptive T3 (1281) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.010851744179208866 | -0.02846481190865624 |
| alpha | 0.022640362065387887 | 0.19167667789575504 |
| trades | 71 | 15 |
| winrate | 0.3380281690140845 | 0.4666666666666667 |
| sharpe | 0.14160379038097778 | -0.47206112045837195 |
| maxdd | -0.23196766420786263 | -0.06907054735268892 |
| pf | 1.017429556938014 | 0.7136630432770581 |
| ann | 0.007654383891013028 | -0.0393114309958813 |

- **Combined OOS gain (stress):** -1.792%
- Full history @ stress: total -1.792%, CAGR -1.051%, benchmark -23.821%, sharpe 0.05, maxdd -0.232, trades 86

### Stochastic RSI OHLC (1340) — 1h
> family: momentum | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.0797602721216013 | -0.00014509128928386072 |
| alpha | 0.09554974580581188 | 0.2299288610525404 |
| trades | 9 | 5 |
| winrate | 0.3333333333333333 | 0.6 |
| sharpe | 0.3931899961607096 | 0.08260385540839968 |
| maxdd | -0.13269634214666715 | -0.06926786384902939 |
| pf | 1.6331464166622665 | 0.998203667379309 |
| ann | 0.055711109848954665 | -0.0002014946717832089 |

- **Combined OOS gain (stress):** 7.960%
- Full history @ stress: total 7.960%, CAGR 4.578%, benchmark -24.130%, sharpe 0.34, maxdd -0.133, trades 14

### JK BullP AutoTrader (2482) — 1h **(pick)**
> family: volatility | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.13974198386440295 | -0.0016970462316217017 |
| alpha | 0.15553145754861353 | 0.22837690611020256 |
| trades | 19 | 6 |
| winrate | 0.3684210526315789 | 0.6666666666666666 |
| sharpe | 0.6570018218520515 | 0.06329752432931898 |
| maxdd | -0.12443490176622918 | -0.08375745970878101 |
| pf | 0.7376258400203117 | 0.9436490979316922 |
| ann | 0.09681320708989216 | -0.002356051647614099 |

- **Combined OOS gain (stress):** 13.781%
- Full history @ stress: total 13.257%, CAGR 7.546%, benchmark -24.130%, sharpe 0.52, maxdd -0.124, trades 26

### Time Zone Pivots Open System (3062) — 1h
> family: breakout | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.05252983062960315 | -0.011018351488871092 |
| alpha | 0.06831930431381372 | 0.21905560085295317 |
| trades | 19 | 5 |
| winrate | 0.47368421052631576 | 0.2 |
| sharpe | 0.5071899280211386 | -0.3012587712125993 |
| maxdd | -0.07350410328587587 | -0.055062032946402995 |
| pf | 1.6746333165671288 | 0.805622028250509 |
| ann | 0.03683144855376441 | -0.015269253110221537 |

- **Combined OOS gain (stress):** 4.093%
- Full history @ stress: total 4.093%, CAGR 2.372%, benchmark -24.130%, sharpe 0.32, maxdd -0.074, trades 24

### CorrTime (3319) — 15min
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.06551154021280192 | -0.01338395542440629 |
| alpha | 0.07970456535473225 | 0.2185832576903478 |
| trades | 18 | 10 |
| winrate | 0.2777777777777778 | 0.3 |
| sharpe | 0.40597291551091436 | -0.15616762418957342 |
| maxdd | -0.1184380723845857 | -0.08874968755979218 |
| pf | 1.3912121147316976 | 0.7847327063845834 |
| ann | 0.04584970629517282 | -0.01853892138338653 |

- **Combined OOS gain (stress):** 5.125%
- Full history @ stress: total 5.125%, CAGR 2.964%, benchmark -24.006%, sharpe 0.28, maxdd -0.118, trades 28

## 2220

### Sunil 2 Bar Breakout (1360) — 4h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.4963855889824056 | 0.12021018891736879 |
| alpha | 0.6304826240228368 | 0.3725946349922038 |
| trades | 37 | 19 |
| winrate | 0.4594594594594595 | 0.47368421052631576 |
| sharpe | 1.3537861279562646 | 0.9016661444810995 |
| maxdd | -0.1166382670180085 | -0.10031225164932511 |
| pf | 2.087219762335609 | 1.5820365064495674 |
| ann | 0.3294275966795699 | 0.1707558768804851 |

- **Combined OOS gain (stress):** 67.627%
- Full history @ stress: total 67.627%, CAGR 27.767%, benchmark -31.334%, sharpe 1.21, maxdd -0.132, trades 56

### Timer (1788) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.31351627574680374 | 0.10110685427336308 |
| alpha | 0.447613310787235 | 0.3534913003481981 |
| trades | 18 | 13 |
| winrate | 0.5 | 0.6923076923076923 |
| sharpe | 0.8931771738425924 | 0.7894999425843732 |
| maxdd | -0.14898767053474404 | -0.09913819864809337 |
| pf | 1.9721293500996637 | 2.008484082730405 |
| ann | 0.21247347399509242 | 0.14312063030177957 |

- **Combined OOS gain (stress):** 44.632%
- Full history @ stress: total 46.170%, CAGR 19.729%, benchmark -31.334%, sharpe 0.88, maxdd -0.149, trades 31

### Bull vs Medved (2510) — 1h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.3660798057884067 | 0.0971656748284202 |
| alpha | 0.5048197521691038 | 0.35715115050017043 |
| trades | 60 | 25 |
| winrate | 0.38333333333333336 | 0.6 |
| sharpe | 1.0126281112356488 | 0.7075225265262295 |
| maxdd | -0.14490660208098216 | -0.09619097331262194 |
| pf | 1.4369533417987455 | 1.6530101789492029 |
| ann | 0.24655398952081842 | 0.13744229830802213 |

- **Combined OOS gain (stress):** 49.882%
- Full history @ stress: total 54.891%, CAGR 23.066%, benchmark -31.702%, sharpe 0.98, maxdd -0.145, trades 85

### Lbs V12 (3880) — 1h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.41350488616480385 | 0.08054869755569083 |
| alpha | 0.5522448325455009 | 0.34053417322744106 |
| trades | 33 | 17 |
| winrate | 0.42424242424242425 | 0.5294117647058824 |
| sharpe | 1.0298065279764763 | 0.6252735153150566 |
| maxdd | -0.19288876622430795 | -0.093271356332007 |
| pf | 1.6108020574341226 | 1.7189419403367356 |
| ann | 0.27697383857180724 | 0.11358841027821898 |

- **Combined OOS gain (stress):** 52.736%
- Full history @ stress: total 57.841%, CAGR 24.173%, benchmark -31.702%, sharpe 0.97, maxdd -0.193, trades 50

### Gann Swing Multi Layer (830) — 4h
> family: other | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.4101857452652047 | 0.10734096971767082 |
| alpha | 0.5442827803056359 | 0.35972541579250583 |
| trades | 27 | 15 |
| winrate | 0.4444444444444444 | 0.4666666666666667 |
| sharpe | 1.2236150132630215 | 0.9145402675963719 |
| maxdd | -0.18455853989991555 | -0.07448056700775763 |
| pf | 2.1641540611074834 | 1.7163706421604459 |
| ann | 0.2748546976045736 | 0.15211869430606884 |

- **Combined OOS gain (stress):** 56.156%
- Full history @ stress: total 56.156%, CAGR 23.542%, benchmark -31.334%, sharpe 1.13, maxdd -0.185, trades 42

## 2223

### VIDYA Auto-Trading (Reversal Logic) (1523) — 30min
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.008067547458000979 | 0.4819061714316737 |
| alpha | 0.2971065864970399 | 0.09249807174320002 |
| trades | 9 | 8 |
| winrate | 0.3333333333333333 | 0.875 |
| sharpe | 0.1121732559501652 | 2.6307651257460036 |
| maxdd | -0.1521554548199997 | -0.08452532045626404 |
| pf | 1.0446750774559632 | 13.709849165956328 |
| ann | 0.005692833551335541 | 0.7267638162325902 |

- **Combined OOS gain (stress):** 49.386%
- Full history @ stress: total 49.386%, CAGR 21.619%, benchmark 0.450%, sharpe 1.25, maxdd -0.152, trades 17

### Daily Range (3167) — 1h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.15214600466000117 | 0.48350887629245753 |
| alpha | 0.4411850436990401 | 0.10127747133377962 |
| trades | 8 | 8 |
| winrate | 0.625 | 0.875 |
| sharpe | 0.8853215633498327 | 2.4239939600936142 |
| maxdd | -0.11325339425208325 | -0.09312961897198746 |
| pf | 2.6932328483617773 | 7.859206913566101 |
| ann | 0.10523292060719314 | 0.7293579450516718 |

- **Combined OOS gain (stress):** 70.922%
- Full history @ stress: total 70.922%, CAGR 29.874%, benchmark 0.450%, sharpe 1.58, maxdd -0.113, trades 16

### Lbs V12 (3880) — 1h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.11207067394600201 | 0.5243126560803002 |
| alpha | 0.40110971298504094 | 0.1420812511216223 |
| trades | 18 | 15 |
| winrate | 0.3888888888888889 | 0.6666666666666666 |
| sharpe | 0.6061286839639008 | 2.6648782280111445 |
| maxdd | -0.1421577007953002 | -0.12149347118589948 |
| pf | 1.4239747995809708 | 3.35636504752707 |
| ann | 0.07793257234334683 | 0.7957678228177725 |

- **Combined OOS gain (stress):** 69.514%
- Full history @ stress: total 70.345%, CAGR 29.661%, benchmark 0.450%, sharpe 1.51, maxdd -0.142, trades 33

### Adaptive KDJ (MTF) (492) — Daily
> family: trend | params: `{}` | flags: thin_trades;win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.15835594218324267 | 0.39722240106191276 |
| alpha | 0.09974590966860908 | 0.0020190642527364577 |
| trades | 16 | 7 |
| winrate | 0.25 | 0.7142857142857143 |
| sharpe | -1.0598247972966244 | 2.7042244538294216 |
| maxdd | -0.1759427577245778 | -0.14948228856048795 |
| pf | 0.35519720898664714 | 28.55409568473599 |
| ann | -0.11467081976969185 | 0.5912644172052568 |

- **Combined OOS gain (stress):** 17.596%
- Full history @ stress: total 71.935%, CAGR 15.630%, benchmark 40.842%, sharpe 1.15, maxdd -0.311, trades 39

### Balance of Power (546) — Daily
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.08001096163388044 | 0.5150119445383439 |
| alpha | 0.3381128134857322 | 0.11980860772916757 |
| trades | 13 | 10 |
| winrate | 0.38461538461538464 | 0.7 |
| sharpe | 0.43979601941829144 | 2.9073832383257647 |
| maxdd | -0.1339769236111672 | -0.0765198425085778 |
| pf | 1.1975087237772724 | 11.798910926257342 |
| ann | 0.055884266348525946 | 0.7805689732000598 |

- **Combined OOS gain (stress):** 63.623%
- Full history @ stress: total 108.897%, CAGR 21.824%, benchmark 40.842%, sharpe 1.19, maxdd -0.281, trades 35

## 2230

### Nadaraya-Watson Envelope (1109) — 4h **(pick)**
> family: other | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.009390412967596462 | 0.4981669434623175 |
| alpha | 0.3936806043068757 | 0.3662651029715198 |
| trades | 36 | 23 |
| winrate | 0.3055555555555556 | 0.6086956521739131 |
| sharpe | 0.09012768986591316 | 2.3202889236084236 |
| maxdd | -0.22253122163759909 | -0.10251561967204892 |
| pf | 0.9825310900574161 | 4.1010958859301 |
| ann | -0.006643316023899337 | 0.7531338807049366 |

- **Combined OOS gain (stress):** 48.410%
- Full history @ stress: total 48.410%, CAGR 20.596%, benchmark -29.175%, sharpe 0.88, maxdd -0.223, trades 59

### The 20s Breakout (2986) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.7270212875808089 | 0.47635046225901423 |
| alpha | 1.130092304855281 | 0.34444862176821656 |
| trades | 49 | 31 |
| winrate | 0.40816326530612246 | 0.41935483870967744 |
| sharpe | 2.051695055419763 | 2.4414552104240554 |
| maxdd | -0.11671287781188189 | -0.16402649361982602 |
| pf | 2.074279441392522 | 2.490993920429618 |
| ann | 0.4711128843580976 | 0.717779824373536 |

- **Combined OOS gain (stress):** 154.969%
- Full history @ stress: total 158.876%, CAGR 57.018%, benchmark -29.175%, sharpe 2.22, maxdd -0.164, trades 80

### Rubberbands 3 (4116) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.4733558766744095 | 0.4283826148581025 |
| alpha | 0.8764268939488816 | 0.2964807743673048 |
| trades | 58 | 34 |
| winrate | 0.3793103448275862 | 0.4117647058823529 |
| sharpe | 1.4756294365223268 | 2.24572297941845 |
| maxdd | -0.15648563315787056 | -0.17047382683038448 |
| pf | 1.6490869141994657 | 2.2396775818677965 |
| ann | 0.3149400201860544 | 0.6407617700040791 |

- **Combined OOS gain (stress):** 110.452%
- Full history @ stress: total 113.677%, CAGR 43.358%, benchmark -29.175%, sharpe 1.79, maxdd -0.170, trades 92

### 5 EMA No-Touch Breakout (483) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.38686169109560753 | 0.4688030182013403 |
| alpha | 0.7899327083700797 | 0.3369011777105426 |
| trades | 56 | 31 |
| winrate | 0.375 | 0.45161290322580644 |
| sharpe | 1.3068152406887974 | 2.4338884391528275 |
| maxdd | -0.15648598118347268 | -0.1651790538509258 |
| pf | 1.5728184199849358 | 2.466798320470463 |
| ann | 0.2599216455661246 | 0.7055960974766229 |

- **Combined OOS gain (stress):** 103.703%
- Full history @ stress: total 106.824%, CAGR 41.158%, benchmark -29.175%, sharpe 1.76, maxdd -0.165, trades 87

### CP Strat ORB (639) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.41744225881880936 | 0.45554786240056355 |
| alpha | 0.8205132760932815 | 0.3236460219097659 |
| trades | 56 | 30 |
| winrate | 0.375 | 0.4666666666666667 |
| sharpe | 1.3903956664131405 | 2.396967254875114 |
| maxdd | -0.14195034324093403 | -0.15142928440358117 |
| pf | 1.637927156804474 | 2.6070271428005416 |
| ann | 0.27948580321644667 | 0.684257395458344 |

- **Combined OOS gain (stress):** 106.316%
- Full history @ stress: total 109.477%, CAGR 42.014%, benchmark -29.175%, sharpe 1.80, maxdd -0.151, trades 86

## 2240

### Sunil 2 Bar Breakout (1360) — 4h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 1.81804318765281 | 0.2653130455113175 |
| alpha | 0.9567657425430296 | 0.5778774121436554 |
| trades | 36 | 18 |
| winrate | 0.5555555555555556 | 0.5555555555555556 |
| sharpe | 2.4937662496553523 | 1.6450980352635884 |
| maxdd | -0.12486462338145121 | -0.16127285154885274 |
| pf | 3.8584144262309166 | 2.3395521252973346 |
| ann | 1.07911672819088 | 0.38653505073067373 |

- **Combined OOS gain (stress):** 256.571%
- Full history @ stress: total 260.377%, CAGR 83.695%, benchmark 33.234%, sharpe 2.25, maxdd -0.161, trades 54

### Eugene Candle Pattern (1852) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 1.9885661183924106 | 0.2580898760651187 |
| alpha | 1.1272886732826302 | 0.5706542426974566 |
| trades | 44 | 20 |
| winrate | 0.5681818181818182 | 0.45 |
| sharpe | 2.6445208543007053 | 1.6444187135508712 |
| maxdd | -0.13529424176323313 | -0.11864312985232428 |
| pf | 3.651605355637862 | 1.9902961397855898 |
| ann | 1.1672292833546254 | 0.3755547969585262 |

- **Combined OOS gain (stress):** 275.988%
- Full history @ stress: total 280.002%, CAGR 88.374%, benchmark 33.234%, sharpe 2.36, maxdd -0.135, trades 64

### Explosion (3261) — 4h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 1.6183728365192125 | 0.24240303850931832 |
| alpha | 0.757095391409432 | 0.5549674051416562 |
| trades | 63 | 28 |
| winrate | 0.42857142857142855 | 0.5 |
| sharpe | 2.39516802459193 | 1.6354999772782912 |
| maxdd | -0.09714934688206633 | -0.16822441277923206 |
| pf | 3.036521609460492 | 1.783276158285945 |
| ann | 0.9739254908940018 | 0.35179298921787616 |

- **Combined OOS gain (stress):** 225.307%
- Full history @ stress: total 228.780%, CAGR 75.871%, benchmark 33.234%, sharpe 2.18, maxdd -0.168, trades 91

### BONK Long Volatility (598) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 1.2760391006124086 | 0.28699300723763876 |
| alpha | 0.4147616555026281 | 0.5995573738699767 |
| trades | 36 | 18 |
| winrate | 0.5277777777777778 | 0.5555555555555556 |
| sharpe | 1.9606926075939934 | 1.744532417778369 |
| maxdd | -0.14737798644459477 | -0.13347131378004407 |
| pf | 2.7043856756865474 | 2.299353961899576 |
| ann | 0.7878876196211682 | 0.41963786867160446 |

- **Combined OOS gain (stress):** 192.925%
- Full history @ stress: total 192.925%, CAGR 66.497%, benchmark 33.234%, sharpe 1.87, maxdd -0.147, trades 54

## 2270

### I Gap (2145) — 1h
> family: volatility | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.16937165431199097 | -0.047115465081030816 |
| alpha | 0.12053444897439403 | 0.18262521563209733 |
| trades | 111 | 51 |
| winrate | 0.32432432432432434 | 0.35294117647058826 |
| sharpe | -0.7918482721995161 | -0.2644967871478897 |
| maxdd | -0.2765455692460377 | -0.14096139377111572 |
| pf | 0.7638456117356842 | 0.9301079555539173 |
| ann | -0.12287295118109132 | -0.06482801221961132 |

- **Combined OOS gain (stress):** -20.851%
- Full history @ stress: total -19.277%, CAGR -9.659%, benchmark -44.219%, sharpe -0.53, maxdd -0.289, trades 162

### Bull vs Medved (2510) — 1h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.06893953700799305 | 0.10510008161382234 |
| alpha | 0.22096656627839195 | 0.3348407623269505 |
| trades | 56 | 28 |
| winrate | 0.3392857142857143 | 0.39285714285714285 |
| sharpe | -0.2831459604763564 | 0.8707969362393211 |
| maxdd | -0.2325118816311963 | -0.09136920107884927 |
| pf | 0.8049277253906041 | 1.6217256604564454 |
| ann | -0.04921240732443832 | 0.14888201587386884 |

- **Combined OOS gain (stress):** 2.891%
- Full history @ stress: total 4.939%, CAGR 2.313%, benchmark -44.219%, sharpe 0.22, maxdd -0.233, trades 84

### Rollback Rebound (2856) — Daily **(pick)**
> family: volatility | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.046524812495692514 | 0.03126874466452079 |
| alpha | 0.3448202670411471 | 0.26100942537764893 |
| trades | 22 | 15 |
| winrate | 0.36363636363636365 | 0.26666666666666666 |
| sharpe | 0.38123769231582877 | 0.47398399269908337 |
| maxdd | -0.07762693713168278 | -0.06778294901804127 |
| pf | 1.3494112929742517 | 1.1942976911569054 |
| ann | 0.032648792647531844 | 0.043687805576152705 |

- **Combined OOS gain (stress):** 7.925%
- Full history @ stress: total 352.810%, CAGR 7.337%, benchmark 88.032%, sharpe 0.50, maxdd -0.349, trades 404

## 2280

### FT CCI (1619) — 4h
> family: volume | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.006227474819202827 | 0.14591819832253505 |
| alpha | 0.25869226355159713 | 0.11612901408788812 |
| trades | 19 | 14 |
| winrate | 0.3684210526315789 | 0.6428571428571429 |
| sharpe | 0.10532201854851624 | 1.1343390311722197 |
| maxdd | -0.1554897320106019 | -0.06734077962863416 |
| pf | 1.1323506900182403 | 2.4531269209937143 |
| ann | 0.004395574262448632 | 0.20823539172308703 |

- **Combined OOS gain (stress):** 15.305%
- Full history @ stress: total 18.522%, CAGR 8.394%, benchmark -20.880%, sharpe 0.57, maxdd -0.155, trades 33

### Hercules A.T.C. 2006 (2485) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.08249219274119413 | 0.1468551058089851 |
| alpha | 0.16997259599120018 | 0.11706592157433815 |
| trades | 43 | 27 |
| winrate | 0.27906976744186046 | 0.5185185185185185 |
| sharpe | -0.5108226202062119 | 1.1686354138039141 |
| maxdd | -0.21523485293091604 | -0.12345717580404136 |
| pf | 0.7699267154626191 | 1.805549556153413 |
| ann | -0.05901096934245398 | 0.20960753079019145 |

- **Combined OOS gain (stress):** 5.225%
- Full history @ stress: total 6.114%, CAGR 2.855%, benchmark -20.880%, sharpe 0.27, maxdd -0.215, trades 70

### Bull vs Medved (2510) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.25973508212560215 | 0.12302854709985467 |
| alpha | 0.5121998708579965 | 0.09323936286520773 |
| trades | 17 | 12 |
| winrate | 0.6470588235294118 | 0.5833333333333334 |
| sharpe | 1.2078652859162498 | 1.1355667297094882 |
| maxdd | -0.07353515966255775 | -0.05010437470635798 |
| pf | 3.2739721531824078 | 2.395189010514368 |
| ann | 0.17718639769854416 | 0.17484857518736674 |

- **Combined OOS gain (stress):** 41.472%
- Full history @ stress: total 42.668%, CAGR 18.360%, benchmark -20.880%, sharpe 1.21, maxdd -0.087, trades 29

### Multi Stochastic (2681) — 4h
> family: mean_reversion | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.014011650359598282 | 0.13868757669466714 |
| alpha | 0.23845313837279603 | 0.1088983924600202 |
| trades | 19 | 13 |
| winrate | 0.47368421052631576 | 0.5384615384615384 |
| sharpe | 0.01898556003760078 | 1.0433513976098376 |
| maxdd | -0.1638087229298668 | -0.05751427867684267 |
| pf | 0.9565033596081136 | 2.9113024779173267 |
| ann | -0.009919426103053297 | 0.19766053887940815 |

- **Combined OOS gain (stress):** 12.273%
- Full history @ stress: total 12.273%, CAGR 5.645%, benchmark -20.880%, sharpe 0.40, maxdd -0.164, trades 32

### WPR Custom Cloud Simple (3555) — 4h **(pick)**
> family: mean_reversion | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.02535581043239854 | 0.1820273434140025 |
| alpha | 0.22710897829999577 | 0.15223815917935557 |
| trades | 17 | 11 |
| winrate | 0.4117647058823529 | 0.7272727272727273 |
| sharpe | -0.029940927973759933 | 1.4272884869832332 |
| maxdd | -0.14219733757486008 | -0.06626039402356709 |
| pf | 1.5679326131087485 | 1.4577688375236957 |
| ann | -0.017980764276027905 | 0.2614321305866414 |

- **Combined OOS gain (stress):** 15.206%
- Full history @ stress: total 18.421%, CAGR 8.350%, benchmark -20.880%, sharpe 0.56, maxdd -0.142, trades 28

## 2281

### Live Alligator (1660) — 1h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.07435695535799391 | 0.209401977422083 |
| alpha | 0.510477879476841 | 0.24035640562500638 |
| trades | 41 | 14 |
| winrate | 0.3170731707317073 | 0.5 |
| sharpe | -0.37968094120694396 | 1.756259782437686 |
| maxdd | -0.17585414736676752 | -0.12783139299234647 |
| pf | 0.9201642449171867 | 2.1976841346076457 |
| ann | -0.053124141268649505 | 0.30218524821473314 |

- **Combined OOS gain (stress):** 11.947%
- Full history @ stress: total 17.738%, CAGR 8.054%, benchmark -57.695%, sharpe 0.62, maxdd -0.176, trades 55

### Bull vs Medved (2510) — 1h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.08869009179199272 | 0.4251003258960795 |
| alpha | 0.4961447430428422 | 0.45605475409900287 |
| trades | 64 | 38 |
| winrate | 0.390625 | 0.39473684210526316 |
| sharpe | -0.24767931134057988 | 1.70356618159765 |
| maxdd | -0.2394555744319331 | -0.12192896887302462 |
| pf | 0.9272166903534905 | 2.088248309878066 |
| ann | -0.06350618539688913 | 0.6355279578646389 |

- **Combined OOS gain (stress):** 29.871%
- Full history @ stress: total 36.959%, CAGR 16.089%, benchmark -57.695%, sharpe 0.73, maxdd -0.239, trades 103

### CorrTime (3319) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.014210834079998791 | 0.15932465372656224 |
| alpha | 0.5791715188611777 | 0.22015798705989553 |
| trades | 10 | 8 |
| winrate | 0.4 | 0.5 |
| sharpe | -0.07558043667682927 | 1.3084304642351607 |
| maxdd | -0.06969979665599968 | -0.0628258988876138 |
| pf | 0.8650710923921208 | 3.867131338885838 |
| ann | -0.010060733583952208 | 0.2279111108650438 |

- **Combined OOS gain (stress):** 14.285%
- Full history @ stress: total 14.285%, CAGR 6.539%, benchmark -58.566%, sharpe 0.58, maxdd -0.070, trades 18

### Butterfly Pattern (3727) — 4h
> family: volatility | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.08797281575400051 | 0.1346318270447675 |
| alpha | 0.681355168695177 | 0.1954651603781008 |
| trades | 9 | 12 |
| winrate | 0.4444444444444444 | 0.4166666666666667 |
| sharpe | 0.6238668089639694 | 0.9997226511736214 |
| maxdd | -0.09746117351076844 | -0.13104831055999944 |
| pf | 1.6474568630575608 | 1.8504240723218959 |
| ann | 0.06137756760005675 | 0.19174037465541094 |

- **Combined OOS gain (stress):** 23.445%
- Full history @ stress: total 23.445%, CAGR 10.507%, benchmark -58.566%, sharpe 0.77, maxdd -0.131, trades 21

## 2282

### SuperTrend AI Oscillator (1371) — Daily
> family: trend | params: `{}` | flags: thin_trades;win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.10775519989712246 | 0.03425180566914032 |
| alpha | 0.0599139730352084 | 0.008096618223630392 |
| trades | 7 | 8 |
| winrate | 0.2857142857142857 | 0.5 |
| sharpe | -1.2548954793635834 | 0.5194390869614628 |
| maxdd | -0.14434901336309947 | -0.049406065105175645 |
| pf | 0.12940470376342753 | 1.3625528948044525 |
| ann | -0.07739039894484223 | 0.04788287696837701 |

- **Combined OOS gain (stress):** -7.719%
- Full history @ stress: total 3.747%, CAGR 0.901%, benchmark -32.278%, sharpe 0.14, maxdd -0.206, trades 25

### Futures Engulfing Candle Size (823) — Daily **(pick)**
> family: pattern | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.1369482890416589 | 0.1070966065203296 |
| alpha | 0.030720883890671957 | 0.08094141907481966 |
| trades | 40 | 17 |
| winrate | 0.425 | 0.5882352941176471 |
| sharpe | -0.44253910719380923 | 0.9038850008934168 |
| maxdd | -0.1978869490411086 | -0.06929024463296096 |
| pf | 0.7451217087433168 | 1.5080751052554295 |
| ann | -0.098820485415265 | 0.15176561887428575 |

- **Combined OOS gain (stress):** -4.452%
- Full history @ stress: total -8.256%, CAGR -2.079%, benchmark -32.278%, sharpe -0.01, maxdd -0.273, trades 98

## 2283

### Maximus vX Lite (1751) — 30min **(pick)**
> family: breakout | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | -0.010356518437599105 | 0.05933648511673173 |
| alpha | 0.33575459267351204 | 0.02275111926307316 |
| trades | 6 | 5 |
| winrate | 0.5 | 0.4 |
| sharpe | -0.04792932500217912 | 0.6400114594773595 |
| maxdd | -0.07938636191439996 | -0.1333589608712853 |
| pf | 0.8595923165643446 | 1.6745940397513548 |
| ann | -0.007327840681026765 | 0.08334480121371479 |

- **Combined OOS gain (stress):** 4.837%
- Full history @ stress: total 4.998%, CAGR 2.407%, benchmark -29.167%, sharpe 0.27, maxdd -0.133, trades 11

### Explosion Range Expansion (3263) — Daily
> family: breakout | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.21334329351169978 | 0.06019745577976954 |
| alpha | 0.09554246107222131 | 0.019381129249157247 |
| trades | 25 | 11 |
| winrate | 0.32 | 0.45454545454545453 |
| sharpe | -1.0077223743313424 | 0.5594802437398615 |
| maxdd | -0.286224814889408 | -0.136776961000322 |
| pf | 0.4737768637159539 | 1.4999553392399232 |
| ann | -0.15593790919648087 | 0.08456779485949983 |

- **Combined OOS gain (stress):** -16.599%
- Full history @ stress: total -13.175%, CAGR -4.254%, benchmark -27.660%, sharpe -0.14, maxdd -0.304, trades 54

## 2284

### ZeroLag MACD Cross (1627) — Daily **(pick)**
> family: trend | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.11593378248040287 | 0.1163716908466288 |
| alpha | 0.312808732489657 | 0.1825737814389632 |
| trades | 42 | 22 |
| winrate | 0.38095238095238093 | 0.36363636363636365 |
| sharpe | -0.3945421777172319 | 1.1310820330470586 |
| maxdd | -0.2025051232192716 | -0.062390736573931904 |
| pf | 0.8021148706399803 | 1.5987075201684382 |
| ann | -0.08337310723991587 | 0.16518821249432136 |

- **Combined OOS gain (stress):** -1.305%
- Full history @ stress: total -19.825%, CAGR -8.505%, benchmark -57.051%, sharpe -0.35, maxdd -0.310, trades 73

### Polarized Fractal Efficiency (2316) — Daily
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.1064195727824202 | -0.018225662560541478 |
| alpha | 0.5351620877524801 | 0.04797642803179292 |
| trades | 15 | 11 |
| winrate | 0.4666666666666667 | 0.5454545454545454 |
| sharpe | 0.9732015841475058 | -0.2233692196551413 |
| maxdd | -0.07344100079597493 | -0.09385590644564712 |
| pf | 1.9243372074145841 | 0.8806430164419463 |
| ann | 0.07405984922758879 | -0.025221483276006262 |

- **Combined OOS gain (stress):** 8.625%
- Full history @ stress: total 12.045%, CAGR 4.681%, benchmark -57.051%, sharpe 0.61, maxdd -0.094, trades 30

### Exp Fisher CG Oscillator (3054) — Daily
> family: momentum | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.10422757908025548 | 0.09650374882394153 |
| alpha | 0.3245149358898044 | 0.16270583941627592 |
| trades | 46 | 23 |
| winrate | 0.34782608695652173 | 0.43478260869565216 |
| sharpe | -0.40766644863009677 | 0.9420765443782556 |
| maxdd | -0.16801601457346071 | -0.07731844881828553 |
| pf | 0.8099619042629529 | 1.3902685437356912 |
| ann | -0.07481488512830825 | 0.13648939213722477 |

- **Combined OOS gain (stress):** -1.778%
- Full history @ stress: total 3.759%, CAGR 1.495%, benchmark -57.051%, sharpe 0.17, maxdd -0.175, trades 75

## 2285

### Projection (1196) — Daily
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.06006097148159617 | 0.15750329823478038 |
| alpha | 0.3517931318618688 | 0.15903079314313073 |
| trades | 28 | 21 |
| winrate | 0.32142857142857145 | 0.5238095238095238 |
| sharpe | -0.35193800578593104 | 1.2653385565855018 |
| maxdd | -0.18648849857871352 | -0.08605540442668147 |
| pf | 0.8397457945582829 | 1.945204170589503 |
| ann | -0.04281590776297084 | 0.2252328161915531 |

- **Combined OOS gain (stress):** 8.798%
- Full history @ stress: total 10.435%, CAGR 5.216%, benchmark -40.395%, sharpe 0.43, maxdd -0.186, trades 49

### XMA Candles (2374) — Daily
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.021758563214798632 | 0.15337707259432798 |
| alpha | 0.3900955401286663 | 0.15490456750267834 |
| trades | 10 | 8 |
| winrate | 0.4 | 0.5 |
| sharpe | -0.07386846393807964 | 1.1977455476751933 |
| maxdd | -0.15828370856994411 | -0.06875263401230758 |
| pf | 1.098075795848847 | 2.159201270312136 |
| ann | -0.01542153655861278 | 0.21917128198265767 |

- **Combined OOS gain (stress):** 12.828%
- Full history @ stress: total 14.526%, CAGR 7.195%, benchmark -40.395%, sharpe 0.54, maxdd -0.158, trades 18

### Bull vs Medved (2510) — Daily **(pick)**
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.15974090718640133 | 0.24895024978246405 |
| alpha | 0.5715950105298663 | 0.2504777446908144 |
| trades | 6 | 5 |
| winrate | 0.3333333333333333 | 0.8 |
| sharpe | 1.0672587716815851 | 2.016721400112655 |
| maxdd | -0.1104814368653495 | -0.04142679918525494 |
| pf | 3.3705157326065978 | 8.38276982821474 |
| ann | 0.11037512121070359 | 0.36169635239304987 |

- **Combined OOS gain (stress):** 44.846%
- Full history @ stress: total 47.025%, CAGR 21.829%, benchmark -40.395%, sharpe 1.52, maxdd -0.110, trades 11

### Alexav SpeedUp M1 (2790) — Daily
> family: volatility | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.05141261592000146 | 0.16654603560752346 |
| alpha | 0.4632667192634664 | 0.16807353051587381 |
| trades | 11 | 10 |
| winrate | 0.45454545454545453 | 0.7 |
| sharpe | 0.49634596123900404 | 2.0392481195601184 |
| maxdd | -0.09133618926945641 | -0.02886878626156464 |
| pf | 1.509833925243301 | 4.143210333144643 |
| ann | 0.03605381005240216 | 0.23854620972156804 |

- **Combined OOS gain (stress):** 22.652%
- Full history @ stress: total 24.497%, CAGR 11.879%, benchmark -40.395%, sharpe 1.20, maxdd -0.091, trades 21

### Explosion Range Expansion (3263) — Daily
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.09709633583559873 | 0.11973771773941588 |
| alpha | 0.3147577675078662 | 0.12126521264776624 |
| trades | 19 | 14 |
| winrate | 0.2631578947368421 | 0.5 |
| sharpe | -0.5097707778120115 | 1.0544133553216712 |
| maxdd | -0.1917478528159995 | -0.13807246221464797 |
| pf | 0.6781337968937473 | 1.6823918845457342 |
| ann | -0.06961744004160175 | 0.17007016604383374 |

- **Combined OOS gain (stress):** 1.102%
- Full history @ stress: total 1.102%, CAGR 0.563%, benchmark -40.395%, sharpe 0.11, maxdd -0.192, trades 33

## 2286

### Smoothing Average (1968) — 4h
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | -0.007804482597999152 | 0.13147432899457234 |
| alpha | 0.3559980768169917 | 0.038516582515699005 |
| trades | 10 | 5 |
| winrate | 0.4 | 0.6 |
| sharpe | 0.0011057559570210663 | 1.371207746724662 |
| maxdd | -0.14832514810177522 | -0.0664609637454705 |
| pf | 1.2131127060769484 | 3.397680323755233 |
| ann | -0.00552004512812676 | 0.18713707628554177 |

- **Combined OOS gain (stress):** 12.264%
- Full history @ stress: total 14.532%, CAGR 7.424%, benchmark -29.068%, sharpe 0.64, maxdd -0.157, trades 15

### NRTR ATR Stop (2624) — 4h **(pick)**
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.003664133904000666 | 0.1651799219030956 |
| alpha | 0.3674666933189915 | 0.07222217542422227 |
| trades | 10 | 7 |
| winrate | 0.2 | 0.5714285714285714 |
| sharpe | 0.07935109682605491 | 1.4841042309693615 |
| maxdd | -0.10269871593308999 | -0.05299181986450563 |
| pf | 1.0253382756067997 | 5.79227730551684 |
| ann | 0.002587246345012284 | 0.23653233358464032 |

- **Combined OOS gain (stress):** 16.945%
- Full history @ stress: total 16.945%, CAGR 8.613%, benchmark -29.068%, sharpe 0.78, maxdd -0.131, trades 17

## 2287

### Bearish Abandoned Baby (114) — 1h
> family: pattern | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.038948275080800565 | 0.04149734910359015 |
| alpha | 0.5727944289269544 | 0.3348727434253568 |
| trades | 6 | 5 |
| winrate | 0.5 | 0.6 |
| sharpe | 0.8089676590353119 | 0.7089586589704022 |
| maxdd | -0.030870343355602903 | -0.048170915423481175 |
| pf | 2.173202474318121 | 3.2185359615839513 |
| ann | 0.027361465241246163 | 0.05809185073234224 |

- **Combined OOS gain (stress):** 8.206%
- Full history @ stress: total 8.206%, CAGR 5.347%, benchmark -65.538%, sharpe 0.74, maxdd -0.048, trades 11

### MA2CCI (1659) — 1h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.0009747272672016027 | 0.06875065314374362 |
| alpha | 0.5348208811133555 | 0.36212604746551025 |
| trades | 12 | 13 |
| winrate | 0.25 | 0.5384615384615384 |
| sharpe | 0.055760350569595225 | 0.6380987992037107 |
| maxdd | -0.05579143225199945 | -0.08014568728797034 |
| pf | 1.0081771989127362 | 1.6966624364293024 |
| ann | 0.000688526550870705 | 0.09673840517538257 |

- **Combined OOS gain (stress):** 6.979%
- Full history @ stress: total 6.979%, CAGR 4.557%, benchmark -65.538%, sharpe 0.41, maxdd -0.094, trades 25

### V1N1 Lonny Breakout (2529) — 30min
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.00015894051399822917 | 0.06109060194527616 |
| alpha | 0.5336872133321556 | 0.3463490575930107 |
| trades | 20 | 20 |
| winrate | 0.35 | 0.35 |
| sharpe | 0.06894483319334842 | 0.6217334791147967 |
| maxdd | -0.09106344056179827 | -0.12142586909329123 |
| pf | 0.9990831052773697 | 1.3031101513530918 |
| ann | -0.00011229086457109627 | 0.08583690134581845 |

- **Combined OOS gain (stress):** 6.092%
- Full history @ stress: total 6.092%, CAGR 3.983%, benchmark -65.538%, sharpe 0.34, maxdd -0.121, trades 40

### Plan X (3202) — 15min
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.016960868101598803 | 0.03232482580813967 |
| alpha | 0.5168852857445551 | 0.3175832814558742 |
| trades | 17 | 10 |
| winrate | 0.35294117647058826 | 0.1 |
| sharpe | -0.1069386150231236 | 0.4113659222530367 |
| maxdd | -0.09115065525444688 | -0.08355993974653264 |
| pf | 0.8876307532902091 | 1.2522219691098362 |
| ann | -0.012012555733875052 | 0.04517243117950742 |

- **Combined OOS gain (stress):** 1.482%
- Full history @ stress: total 1.482%, CAGR 0.976%, benchmark -65.538%, sharpe 0.14, maxdd -0.118, trades 27

### Bullish & Bearish Harami Stochastic (3422) — 30min **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.01792450854000105 | 0.08110548625105363 |
| alpha | 0.5517706623861549 | 0.3663639418987882 |
| trades | 11 | 15 |
| winrate | 0.36363636363636365 | 0.2 |
| sharpe | 0.21311013314595642 | 0.5500421819000928 |
| maxdd | -0.13083761844799968 | -0.1779004167671805 |
| pf | 1.0711360409878368 | 1.3935732136533299 |
| ann | 0.012630243959664611 | 0.11438539269223802 |

- **Combined OOS gain (stress):** 10.048%
- Full history @ stress: total 10.048%, CAGR 6.528%, benchmark -65.538%, sharpe 0.39, maxdd -0.246, trades 26

## 2288

### MA Crossover with TP/SL and 5 EMA Filter (1002) — 30min
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.7824787653096013 | 0.05734223230235691 |
| alpha | 0.7182005777437426 | 0.36734223230235685 |
| trades | 19 | 8 |
| winrate | 0.42105263157894735 | 0.375 |
| sharpe | 0.7857453006666643 | 0.6545244316621587 |
| maxdd | -0.1081742417568079 | -0.056212037540315785 |
| pf | 5.261427838310676 | 1.7572938074832973 |
| ann | 0.5043317287259559 | 0.08051348456913332 |

- **Combined OOS gain (stress):** 88.469%
- Full history @ stress: total 88.469%, CAGR 36.214%, benchmark -27.292%, sharpe 0.67, maxdd -0.112, trades 27

### Bull vs Medved (2510) — 30min
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.645642328243212 | 0.048660192825277226 |
| alpha | 0.5813641406773533 | 0.35866019282527717 |
| trades | 83 | 44 |
| winrate | 0.5421686746987951 | 0.36363636363636365 |
| sharpe | 0.7933014532395266 | 0.3725443928381272 |
| maxdd | -0.5380370104457424 | -0.16344008724686732 |
| pf | 1.586820597959455 | 0.9838990937955214 |
| ann | 0.4217937519946573 | 0.06821147926462912 |

- **Combined OOS gain (stress):** 72.572%
- Full history @ stress: total 63.500%, CAGR 27.093%, benchmark -27.292%, sharpe 0.64, maxdd -0.538, trades 127

### e-TurboFx Classic (3760) — 4h **(pick)**
> family: momentum | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.5270248010272023 | 0.08319176390360283 |
| alpha | 0.4627466134613436 | 0.3993463724268932 |
| trades | 10 | 5 |
| winrate | 0.9 | 0.6 |
| sharpe | 0.7148750703329971 | 0.6111922253704412 |
| maxdd | -0.5155788989977683 | -0.18253027608810368 |
| pf | 26.90467481770257 | 1.723254741801215 |
| ann | 0.34860116104962335 | 0.11737309101971927 |

- **Combined OOS gain (stress):** 65.406%
- Full history @ stress: total 65.406%, CAGR 27.813%, benchmark -27.292%, sharpe 0.63, maxdd -0.516, trades 15

### BB Breakout Momentum Squeeze (553) — 4h
> family: breakout | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.1219094188568004 | -0.034913607166532246 |
| alpha | 0.05763123129094172 | 0.2812410013567581 |
| trades | 6 | 9 |
| winrate | 0.5 | 0.2222222222222222 |
| sharpe | 0.6502143865417397 | -0.10804417884588773 |
| maxdd | -0.1010480672400248 | -0.07985387005030076 |
| pf | 3.108559273849419 | 0.633694710881764 |
| ann | 0.08466135451083212 | -0.04815597916044512 |

- **Combined OOS gain (stress):** 8.274%
- Full history @ stress: total 8.274%, CAGR 3.953%, benchmark -27.292%, sharpe 0.30, maxdd -0.146, trades 15

## 2290

### EMA Prediction (2034) — Daily
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.039633028356369726 | 0.39482846287657725 |
| alpha | 0.35004708105398585 | 0.28554274859086304 |
| trades | 43 | 21 |
| winrate | 0.4186046511627907 | 0.6190476190476191 |
| sharpe | 0.2532938487701604 | 2.0250043809909686 |
| maxdd | -0.19253876077700727 | -0.12445600312686145 |
| pf | 1.0936462974466667 | 3.36161928443209 |
| ann | 0.02783978811247234 | 0.5874792985495509 |

- **Combined OOS gain (stress):** 45.011%
- Full history @ stress: total 1578.152%, CAGR 14.685%, benchmark -74.583%, sharpe 0.63, maxdd -0.625, trades 584

### Kalman Filter Candles (2152) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.00805932478360516 | 0.4530491757685917 |
| alpha | 0.31269850004133704 | 0.33898891751895044 |
| trades | 42 | 21 |
| winrate | 0.2619047619047619 | 0.5238095238095238 |
| sharpe | 0.11703265744074852 | 1.9982491203736654 |
| maxdd | -0.17525006055796166 | -0.13251865295776388 |
| pf | 1.0230076878866423 | 3.098031053270185 |
| ann | 0.0056870380766087525 | 0.680243341183216 |

- **Combined OOS gain (stress):** 46.476%
- Full history @ stress: total 47.766%, CAGR 20.348%, benchmark -19.948%, sharpe 0.98, maxdd -0.175, trades 63

### Explosion (3261) — 4h **(pick)**
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.05564662586320579 | 0.6513313903111944 |
| alpha | 0.36028580112093767 | 0.5372711320615531 |
| trades | 43 | 31 |
| winrate | 0.4186046511627907 | 0.5483870967741935 |
| sharpe | 0.36096732681969146 | 2.8107418413549285 |
| maxdd | -0.10887738140392544 | -0.13189689329709453 |
| pf | 1.1536458202013185 | 3.544851472958525 |
| ann | 0.03899961769656568 | 1.0068945025491374 |

- **Combined OOS gain (stress):** 74.322%
- Full history @ stress: total 74.322%, CAGR 30.162%, benchmark -19.948%, sharpe 1.50, maxdd -0.132, trades 74

### 5 EMA No-Touch Breakout (483) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.0715535152535951 | 0.5177372525133317 |
| alpha | 0.23308566000413677 | 0.4036769942636904 |
| trades | 55 | 32 |
| winrate | 0.2727272727272727 | 0.53125 |
| sharpe | -0.3425912114828054 | 2.456597959428325 |
| maxdd | -0.16542954346239758 | -0.08956179616735871 |
| pf | 0.8295481037504336 | 2.5514581191616097 |
| ann | -0.05109903584303177 | 0.785018815211219 |

- **Combined OOS gain (stress):** 40.914%
- Full history @ stress: total 43.200%, CAGR 18.569%, benchmark -19.948%, sharpe 1.03, maxdd -0.165, trades 87

## 2300

### Sunil 2 Bar Breakout (1360) — 4h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.4813052544380052 | 0.30670751772678306 |
| alpha | 0.5755420145626159 | 0.31314874155931127 |
| trades | 44 | 17 |
| winrate | 0.38636363636363635 | 0.5882352941176471 |
| sharpe | 1.3669888022149845 | 1.671838954811358 |
| maxdd | -0.14428554786929992 | -0.1383029221347526 |
| pf | 1.8391267913017184 | 2.728759863034446 |
| ann | 0.3199482918006713 | 0.4499285581797723 |

- **Combined OOS gain (stress):** 93.563%
- Full history @ stress: total 106.761%, CAGR 41.138%, benchmark -3.894%, sharpe 1.58, maxdd -0.144, trades 61

### Hull Ma Volume (144) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.1609336253580036 | 0.28398173939634086 |
| alpha | 0.2551703854826143 | 0.29042296322886907 |
| trades | 36 | 16 |
| winrate | 0.3611111111111111 | 0.6875 |
| sharpe | 0.6904957285823983 | 2.034887087419621 |
| maxdd | -0.14518502717136517 | -0.06696560663853102 |
| pf | 1.465606970426148 | 3.995930987566274 |
| ann | 0.1111817630388654 | 0.4150269487431799 |

- **Combined OOS gain (stress):** 49.062%
- Full history @ stress: total 59.226%, CAGR 24.688%, benchmark -3.894%, sharpe 1.29, maxdd -0.145, trades 52

### ZeroLag MACD Cross (1627) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.718176392473211 | 0.22817063612142463 |
| alpha | 0.8124131525978217 | 0.23461185995395284 |
| trades | 77 | 41 |
| winrate | 0.42857142857142855 | 0.4146341463414634 |
| sharpe | 1.6712789132882657 | 1.316614466888085 |
| maxdd | -0.15372379517729484 | -0.10325417193690656 |
| pf | 1.7722426812551844 | 1.6676854764032154 |
| ann | 0.46578606824641544 | 0.3303349561646529 |

- **Combined OOS gain (stress):** 111.021%
- Full history @ stress: total 110.648%, CAGR 42.390%, benchmark -3.894%, sharpe 1.55, maxdd -0.154, trades 118

### Labouchere EA (2147) — 4h
> family: volume | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.6074563201800047 | 0.28745394447100847 |
| alpha | 0.7016930803046154 | 0.2938951683035367 |
| trades | 31 | 20 |
| winrate | 0.45161290322580644 | 0.6 |
| sharpe | 1.6858531562308885 | 1.5641961974140044 |
| maxdd | -0.12480310783232962 | -0.15087234480732592 |
| pf | 2.417808843688075 | 3.362085284996851 |
| ann | 0.3984055679150833 | 0.4203440364351927 |

- **Combined OOS gain (stress):** 106.953%
- Full history @ stress: total 106.586%, CAGR 41.081%, benchmark -3.894%, sharpe 1.63, maxdd -0.151, trades 51

### Bezier ReOpen (2414) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.6599125369480039 | 0.1939696220821927 |
| alpha | 0.7541492970726146 | 0.20041084591472091 |
| trades | 51 | 26 |
| winrate | 0.47058823529411764 | 0.46153846153846156 |
| sharpe | 1.6679347913548757 | 1.1467968557302077 |
| maxdd | -0.1292725844309034 | -0.17924560441622028 |
| pf | 2.5822378439520897 | 1.7992017354011793 |
| ann | 0.43049296906428336 | 0.2791662001395556 |

- **Combined OOS gain (stress):** 98.189%
- Full history @ stress: total 97.838%, CAGR 38.215%, benchmark -3.894%, sharpe 1.48, maxdd -0.179, trades 77

## 2310

### Timer (1788) — 4h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.02063575816560248 | 0.08796447289771958 |
| alpha | 0.490653711486967 | 0.29363355661558377 |
| trades | 21 | 13 |
| winrate | 0.47619047619047616 | 0.6153846153846154 |
| sharpe | 0.16993355111692232 | 0.7751190265368562 |
| maxdd | -0.15844872445857727 | -0.08613142306301957 |
| pf | 1.0785020502311382 | 1.8000121209784057 |
| ann | 0.014534980472224346 | 0.12421636266241398 |

- **Combined OOS gain (stress):** 11.042%
- Full history @ stress: total 11.042%, CAGR 5.094%, benchmark -56.732%, sharpe 0.38, maxdd -0.158, trades 34

### Eugene Candle Pattern (1852) — 4h
> family: breakout | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.10061413320239543 | 0.06815537486638723 |
| alpha | 0.3694038201189691 | 0.2738244585842514 |
| trades | 47 | 28 |
| winrate | 0.23404255319148937 | 0.32142857142857145 |
| sharpe | -0.40129557650622094 | 0.5968874827080299 |
| maxdd | -0.25200134276220965 | -0.13142108587063317 |
| pf | 0.7993795083162387 | 1.3276946519001782 |
| ann | -0.07217979516256046 | 0.09589013511466993 |

- **Combined OOS gain (stress):** -3.932%
- Full history @ stress: total -3.647%, CAGR -1.747%, benchmark -56.732%, sharpe -0.02, maxdd -0.252, trades 75

### Genie (1875) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.028764453375596744 | 0.08133338322567552 |
| alpha | 0.4412534999457678 | 0.2870024669435397 |
| trades | 23 | 13 |
| winrate | 0.34782608695652173 | 0.38461538461538464 |
| sharpe | -0.07603658692424746 | 0.7353218597099471 |
| maxdd | -0.20415558806748124 | -0.077492210668341 |
| pf | 0.888917204858966 | 1.81508571634319 |
| ann | -0.020408370699355416 | 0.11471164843941861 |

- **Combined OOS gain (stress):** 5.023%
- Full history @ stress: total 5.023%, CAGR 2.352%, benchmark -56.732%, sharpe 0.23, maxdd -0.204, trades 36

### Explosion Range Expansion (3263) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.035974967598007224 | 0.029356161293082605 |
| alpha | 0.5059929209193718 | 0.2350252450109468 |
| trades | 65 | 34 |
| winrate | 0.3076923076923077 | 0.35294117647058826 |
| sharpe | 0.23656594358712604 | 0.3172848039363972 |
| maxdd | -0.1511493115379492 | -0.0899544610070967 |
| pf | 1.070397365812869 | 1.0881100858146997 |
| ann | 0.02528343700870428 | 0.04100062440813779 |

- **Combined OOS gain (stress):** 6.639%
- Full history @ stress: total 6.639%, CAGR 3.096%, benchmark -56.732%, sharpe 0.26, maxdd -0.152, trades 99

### Anands (521) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.08227096310399662 | 0.08648685451556637 |
| alpha | 0.3877469902173679 | 0.29215593823343056 |
| trades | 36 | 21 |
| winrate | 0.3333333333333333 | 0.38095238095238093 |
| sharpe | -0.30485334421289045 | 0.7448806969580468 |
| maxdd | -0.30160478255754086 | -0.07518035247698962 |
| pf | 0.8021092385630421 | 1.5794563507952364 |
| ann | -0.05885068082427525 | 0.12209645354194443 |

- **Combined OOS gain (stress):** -0.290%
- Full history @ stress: total 0.006%, CAGR 0.003%, benchmark -56.732%, sharpe 0.08, maxdd -0.302, trades 57

## 2320

### Charles 1.3.7 (1747) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.569783134786018 | 0.22143746366501693 |
| alpha | 0.06311646811935145 | 0.3319475100328686 |
| trades | 111 | 61 |
| winrate | 0.4144144144144144 | 0.36065573770491804 |
| sharpe | 1.2515638378175118 | 1.1315692637084567 |
| maxdd | -0.19655342083250182 | -0.14973438109269532 |
| pf | 1.3546067186168946 | 1.3003347911980578 |
| ann | 0.37517111505224787 | 0.3202169972773039 |

- **Combined OOS gain (stress):** 91.739%
- Full history @ stress: total 98.800%, CAGR 38.533%, benchmark 39.515%, sharpe 1.27, maxdd -0.197, trades 172

### Timer (1788) — 1h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.7202450890140093 | 0.725911868107372 |
| alpha | 0.19133979996111883 | 0.8329716043370075 |
| trades | 70 | 28 |
| winrate | 0.5285714285714286 | 0.5357142857142857 |
| sharpe | 1.720741781114691 | 3.618237853634404 |
| maxdd | -0.1037263361640055 | -0.07153496631495271 |
| pf | 1.8621949436900724 | 4.439805220980837 |
| ann | 0.4670326552787534 | 1.1338676890215824 |

- **Combined OOS gain (stress):** 196.899%
- Full history @ stress: total 195.876%, CAGR 67.290%, benchmark 41.574%, sharpe 2.30, maxdd -0.106, trades 98

### Bull vs Medved (2510) — 1h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 1.235145357676012 | 0.6639370886437315 |
| alpha | 0.7062400686231216 | 0.770996824873367 |
| trades | 61 | 27 |
| winrate | 0.6229508196721312 | 0.5925925925925926 |
| sharpe | 2.4169645614839816 | 3.4983030559945085 |
| maxdd | -0.11173120928989744 | -0.11858434326271972 |
| pf | 2.9557395873759535 | 4.509430317840915 |
| ann | 0.7651329966014013 | 1.0282021094092335 |

- **Combined OOS gain (stress):** 271.914%
- Full history @ stress: total 270.633%, CAGR 86.157%, benchmark 41.574%, sharpe 2.72, maxdd -0.119, trades 88

### Explosion Range Expansion (3263) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.8409021398900123 | 0.4855769778777621 |
| alpha | 0.3342354732233457 | 0.5960870242456138 |
| trades | 65 | 33 |
| winrate | 0.5076923076923077 | 0.5454545454545454 |
| sharpe | 2.157324496002486 | 2.790831427604038 |
| maxdd | -0.09245381900424388 | -0.06184517514679799 |
| pf | 2.553429746637643 | 3.0764975705870246 |
| ann | 0.5390006693557476 | 0.732706972675113 |

- **Combined OOS gain (stress):** 173.480%
- Full history @ stress: total 173.599%, CAGR 61.193%, benchmark 39.515%, sharpe 2.36, maxdd -0.092, trades 98

### Long Explosive V1 (992) — 1h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.7385901285160141 | 0.4941358326589085 |
| alpha | 0.20968483946312366 | 0.601195568888544 |
| trades | 92 | 30 |
| winrate | 0.4673913043478261 | 0.5666666666666667 |
| sharpe | 1.6925517316623426 | 3.0605023731864867 |
| maxdd | -0.11128838610976288 | -0.07479119436855819 |
| pf | 1.6477925191848082 | 2.732825768000087 |
| ann | 0.4780681208566955 | 0.7465862113046962 |

- **Combined OOS gain (stress):** 159.769%
- Full history @ stress: total 164.865%, CAGR 58.731%, benchmark 41.574%, sharpe 2.08, maxdd -0.111, trades 122

## 2330

### Parabolic Sar Volume (188) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.05138172986440548 | 0.11571269214472268 |
| alpha | 0.3248092009812219 | 0.37029517686977365 |
| trades | 52 | 27 |
| winrate | 0.3076923076923077 | 0.48148148148148145 |
| sharpe | 0.3108353126062476 | 0.9059916962548741 |
| maxdd | -0.1364569046279278 | -0.07158301172929815 |
| pf | 1.103903762261778 | 1.5458884066629397 |
| ann | 0.03603230833591842 | 0.16423309575079337 |

- **Combined OOS gain (stress):** 17.304%
- Full history @ stress: total 18.494%, CAGR 8.382%, benchmark -43.620%, sharpe 0.57, maxdd -0.168, trades 79

### Bull vs Medved (2510) — 1h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.0563534332236062 | 0.2733987312285844 |
| alpha | 0.32414127280963456 | 0.5289919515675674 |
| trades | 60 | 31 |
| winrate | 0.4166666666666667 | 0.5161290322580645 |
| sharpe | 0.3033684652982336 | 1.6437804396558593 |
| maxdd | -0.23017749393012754 | -0.1006940557169419 |
| pf | 1.088562388261318 | 1.837690914774716 |
| ann | 0.039491040045941395 | 0.39885538956857447 |

- **Combined OOS gain (stress):** 34.516%
- Full history @ stress: total 37.685%, CAGR 16.381%, benchmark -43.182%, sharpe 0.86, maxdd -0.230, trades 91

### The 20s Breakout (2986) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.21628051375920454 | 0.12164560157153881 |
| alpha | 0.48970798487602096 | 0.37622808629658977 |
| trades | 50 | 32 |
| winrate | 0.38 | 0.4375 |
| sharpe | 0.9750430466767014 | 0.8081497587654526 |
| maxdd | -0.18740645376438803 | -0.1131534983381065 |
| pf | 1.5164379439840323 | 1.4240958907086465 |
| ann | 0.14835090394811679 | 0.17283982168007417 |

- **Combined OOS gain (stress):** 36.424%
- Full history @ stress: total 37.808%, CAGR 16.430%, benchmark -43.620%, sharpe 0.91, maxdd -0.187, trades 82

### Aftershock Playbook (509) — 4h
> family: volatility | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.16909289607840106 | 0.22222200574126005 |
| alpha | 0.4425203671952175 | 0.476804490466311 |
| trades | 6 | 5 |
| winrate | 0.5 | 0.6 |
| sharpe | 0.8477368263308044 | 1.2254111997384343 |
| maxdd | -0.08656019684451488 | -0.1759399677230803 |
| pf | 3.5706445864399075 | 3.1305646063847763 |
| ann | 0.11669341650553178 | 0.3213948175235164 |

- **Combined OOS gain (stress):** 42.889%
- Full history @ stress: total 42.889%, CAGR 18.447%, benchmark -43.620%, sharpe 0.99, maxdd -0.176, trades 11

### Function Logistic Equation (816) — 4h **(pick)**
> family: other | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.1712565039888021 | 0.1882353186025163 |
| alpha | 0.4446839751056185 | 0.44281780332756726 |
| trades | 12 | 7 |
| winrate | 0.5 | 0.42857142857142855 |
| sharpe | 0.9035381284404443 | 1.6746546442744512 |
| maxdd | -0.08235732937305618 | -0.07614768869785327 |
| pf | 3.0090406331188473 | 3.275976043296323 |
| ann | 0.118153054964655 | 0.27064221273345646 |

- **Combined OOS gain (stress):** 39.173%
- Full history @ stress: total 39.173%, CAGR 16.976%, benchmark -43.620%, sharpe 1.18, maxdd -0.082, trades 19

## 2340

### Swing Breakout Strategy PRO (1388) — 1h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.07015169645040364 | 0.3425950713896677 |
| alpha | 0.395672529783737 | 0.3661134156982284 |
| trades | 32 | 15 |
| winrate | 0.4375 | 0.7333333333333333 |
| sharpe | 0.34072034033658455 | 1.8051449255678322 |
| maxdd | -0.15366723261803827 | -0.06941369647792606 |
| pf | 1.1229012196851162 | 6.949880492163093 |
| ann | 0.04906533777364186 | 0.5055249006762652 |

- **Combined OOS gain (stress):** 43.678%
- Full history @ stress: total 43.678%, CAGR 18.757%, benchmark -32.422%, sharpe 0.90, maxdd -0.171, trades 47

### The 20s Breakout (2986) — 4h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.10149396170560454 | 0.4858832783116389 |
| alpha | 0.42436977869906867 | 0.508482148368136 |
| trades | 53 | 21 |
| winrate | 0.32075471698113206 | 0.6190476190476191 |
| sharpe | 0.4534843200160359 | 2.64459104337217 |
| maxdd | -0.17958619668911235 | -0.0549222764801518 |
| pf | 1.1516322957010703 | 5.651471651176874 |
| ann | 0.0706795695703859 | 0.7332031414804354 |

- **Combined OOS gain (stress):** 63.669%
- Full history @ stress: total 64.562%, CAGR 26.653%, benchmark -32.157%, sharpe 1.26, maxdd -0.188, trades 74

### Adaptive EMA Breakout (301) — 1h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.07015169645040364 | 0.3425950713896677 |
| alpha | 0.395672529783737 | 0.3661134156982284 |
| trades | 32 | 15 |
| winrate | 0.4375 | 0.7333333333333333 |
| sharpe | 0.34072034033658455 | 1.8051449255678322 |
| maxdd | -0.15366723261803827 | -0.06941369647792606 |
| pf | 1.1229012196851162 | 6.949880492163093 |
| ann | 0.04906533777364186 | 0.5055249006762652 |

- **Combined OOS gain (stress):** 43.678%
- Full history @ stress: total 43.678%, CAGR 18.757%, benchmark -32.422%, sharpe 0.90, maxdd -0.171, trades 47

### JS Signal Baes (3192) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.0038649405451960384 | 0.3253484717631627 |
| alpha | 0.3190108764482681 | 0.3479473418196598 |
| trades | 41 | 18 |
| winrate | 0.3170731707317073 | 0.4444444444444444 |
| sharpe | 0.10320598106179345 | 1.962646057887564 |
| maxdd | -0.20299292085710097 | -0.08126626928708902 |
| pf | 0.9942951605494609 | 2.7725489297482873 |
| ann | -0.002732053380351096 | 0.4787337011630417 |

- **Combined OOS gain (stress):** 32.023%
- Full history @ stress: total 31.736%, CAGR 13.968%, benchmark -32.157%, sharpe 0.69, maxdd -0.233, trades 59

### IU Open Equal to High Low (942) — Daily
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.12285554645834407 | 0.34990603209981774 |
| alpha | 0.4856714309348784 | 0.37708503866026755 |
| trades | 38 | 20 |
| winrate | 0.39473684210526316 | 0.5 |
| sharpe | 0.4936196370407487 | 1.788060892549773 |
| maxdd | -0.1494103847243512 | -0.07625701449725808 |
| pf | 1.2179697642739067 | 2.712872851037973 |
| ann | 0.08530750255221342 | 0.5169224317965169 |

- **Combined OOS gain (stress):** 51.575%
- Full history @ stress: total 353.020%, CAGR 8.000%, benchmark -70.908%, sharpe 0.48, maxdd -0.504, trades 442

## 2350

### Previous Day High Low Long (1184) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.1851139170416023 | 0.7425761852167254 |
| alpha | 0.6228406401371283 | 0.7027439001014213 |
| trades | 25 | 19 |
| winrate | 0.32 | 0.5789473684210527 |
| sharpe | 0.9729792713034333 | 3.2451472771298957 |
| maxdd | -0.12229018019536453 | -0.04575724447914964 |
| pf | 2.0342842180757943 | 7.558851485227343 |
| ann | 0.12748302322043026 | 1.1625347815812113 |

- **Combined OOS gain (stress):** 106.515%
- Full history @ stress: total 106.515%, CAGR 41.058%, benchmark -40.024%, sharpe 1.98, maxdd -0.122, trades 44

### US Index First 30m Candle (1515) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.1866655306464069 | 0.664495925585705 |
| alpha | 0.6243922537419329 | 0.6246636404704009 |
| trades | 58 | 30 |
| winrate | 0.3620689655172414 | 0.36666666666666664 |
| sharpe | 0.7781061230463978 | 2.774208338325814 |
| maxdd | -0.15356334059167187 | -0.09568042629741325 |
| pf | 1.3949769321924723 | 2.8153146427161913 |
| ann | 0.12852570015062703 | 1.0291481772116629 |

- **Combined OOS gain (stress):** 97.520%
- Full history @ stress: total 99.046%, CAGR 38.615%, benchmark -40.024%, sharpe 1.63, maxdd -0.154, trades 88

### Hercules A.T.C. 2006 (2485) — 4h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.23522037402280493 | 0.7332176035830613 |
| alpha | 0.6729470971183309 | 0.6933853184677572 |
| trades | 41 | 25 |
| winrate | 0.34146341463414637 | 0.44 |
| sharpe | 1.0560863498103936 | 3.1565906072726833 |
| maxdd | -0.11957411788799743 | -0.0726740952660403 |
| pf | 1.841598017069043 | 4.908440113206268 |
| ann | 0.1609555394863067 | 1.1464223271248088 |

- **Combined OOS gain (stress):** 114.091%
- Full history @ stress: total 115.745%, CAGR 44.014%, benchmark -40.024%, sharpe 1.97, maxdd -0.120, trades 66

### The 20s Breakout (2986) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.15910454044480593 | 0.8333796684350745 |
| alpha | 0.5968312635403319 | 0.7935473833197704 |
| trades | 52 | 27 |
| winrate | 0.38461538461538464 | 0.4074074074074074 |
| sharpe | 0.7103045760149279 | 3.368470047867363 |
| maxdd | -0.12818873879253379 | -0.09260467925058602 |
| pf | 1.344209533003373 | 4.023537490115955 |
| ann | 0.10994464328903786 | 1.3206013682934317 |

- **Combined OOS gain (stress):** 112.508%
- Full history @ stress: total 114.150%, CAGR 43.508%, benchmark -40.024%, sharpe 1.85, maxdd -0.139, trades 79

### Rubberbands 3 (4116) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.19962274888520803 | 0.6598251181281594 |
| alpha | 0.637349471980734 | 0.6199928330128552 |
| trades | 60 | 31 |
| winrate | 0.38333333333333336 | 0.3548387096774194 |
| sharpe | 0.8197925404432973 | 2.7519413381781397 |
| maxdd | -0.12900109125018877 | -0.09568037237800908 |
| pf | 1.4109787560857494 | 2.750083212894142 |
| ann | 0.13721733230735977 | 1.0212446607297943 |

- **Combined OOS gain (stress):** 99.116%
- Full history @ stress: total 100.655%, CAGR 39.145%, benchmark -40.024%, sharpe 1.64, maxdd -0.130, trades 91

## 2360

### Hercules A.T.C. 2006 (2485) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.07480748609520393 | 0.4875006381091882 |
| alpha | 0.5835356656463262 | 0.681813434317719 |
| trades | 42 | 26 |
| winrate | 0.42857142857142855 | 0.5769230769230769 |
| sharpe | 0.45017183433188795 | 2.0995425410791086 |
| maxdd | -0.11349658677108188 | -0.09570961205941786 |
| pf | 1.196069947154768 | 2.966057771105592 |
| ann | 0.052287692607470904 | 0.7358237234902016 |

- **Combined OOS gain (stress):** 59.878%
- Full history @ stress: total 63.352%, CAGR 26.211%, benchmark -57.606%, sharpe 1.27, maxdd -0.120, trades 68

### Explosion Range Expansion (3263) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.025591551475608654 | 0.5807205987572004 |
| alpha | 0.5343197310267309 | 0.7750333949657312 |
| trades | 69 | 31 |
| winrate | 0.34782608695652173 | 0.41935483870967744 |
| sharpe | 0.19230757135736354 | 2.0596334980361 |
| maxdd | -0.14450085610613517 | -0.11573419878219338 |
| pf | 1.036575239077902 | 2.9876602098598206 |
| ann | 0.018012744949518877 | 0.8887159752135236 |

- **Combined OOS gain (stress):** 62.117%
- Full history @ stress: total 65.641%, CAGR 27.046%, benchmark -57.606%, sharpe 1.12, maxdd -0.165, trades 100

### Rubberbands 3 (4116) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.027290874072007032 | 0.4122348246205163 |
| alpha | 0.5360190536231293 | 0.6065476208290471 |
| trades | 67 | 37 |
| winrate | 0.373134328358209 | 0.43243243243243246 |
| sharpe | 0.20031973530163358 | 1.6669950978736228 |
| maxdd | -0.12869757538642057 | -0.11492199702021855 |
| pf | 1.0432215738550543 | 1.9489211481607565 |
| ann | 0.019204120682458026 | 0.6150583516686454 |

- **Combined OOS gain (stress):** 45.078%
- Full history @ stress: total 48.231%, CAGR 20.527%, benchmark -57.606%, sharpe 0.93, maxdd -0.131, trades 104

### 5 EMA No-Touch Breakout (483) — 4h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.09192470660640795 | 0.4270795591082517 |
| alpha | 0.6006528861575302 | 0.6213923553167825 |
| trades | 60 | 37 |
| winrate | 0.4166666666666667 | 0.40540540540540543 |
| sharpe | 0.4868179537053522 | 1.743627258576262 |
| maxdd | -0.12869543207937761 | -0.11492374309997311 |
| pf | 1.1710263226718673 | 2.0743663316244016 |
| ann | 0.06409980043664221 | 0.6386834069733636 |

- **Combined OOS gain (stress):** 55.826%
- Full history @ stress: total 59.214%, CAGR 24.684%, benchmark -57.606%, sharpe 1.11, maxdd -0.129, trades 97

### Long Explosive V1 (992) — 4h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.09089443813800657 | 0.49099723768657455 |
| alpha | 0.5996226176891288 | 0.6853100338951054 |
| trades | 48 | 33 |
| winrate | 0.3333333333333333 | 0.48484848484848486 |
| sharpe | 0.43419977268785787 | 1.73340107546216 |
| maxdd | -0.1557123096149019 | -0.1716002801851707 |
| pf | 1.2043573594703718 | 1.9585252992997444 |
| ann | 0.06339038617119752 | 0.7414929935481107 |

- **Combined OOS gain (stress):** 62.652%
- Full history @ stress: total 74.256%, CAGR 30.139%, benchmark -57.606%, sharpe 1.15, maxdd -0.172, trades 81

## 2370

### EMA Sticker (1656) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.07978504321920754 | 0.7638447821028596 |
| alpha | 0.39463652836772234 | 0.2363218463230432 |
| trades | 66 | 35 |
| winrate | 0.4090909090909091 | 0.45714285714285713 |
| sharpe | 0.3387031638956456 | 2.575208494181766 |
| maxdd | -0.2677511202038749 | -0.12324830679416976 |
| pf | 1.0811240109996565 | 3.4763204526161253 |
| ann | 0.055728220290521824 | 1.1992775001223248 |

- **Combined OOS gain (stress):** 90.457%
- Full history @ stress: total 95.259%, CAGR 37.357%, benchmark 9.901%, sharpe 1.23, maxdd -0.268, trades 101

### Timer (1788) — 1h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.3708585960152093 | 0.8176464046694043 |
| alpha | 0.6957366447956971 | 0.2615716383142641 |
| trades | 68 | 33 |
| winrate | 0.39705882352941174 | 0.45454545454545453 |
| sharpe | 1.039794561813816 | 2.885564960828769 |
| maxdd | -0.1735541665878938 | -0.10820795364260205 |
| pf | 1.3369635533088806 | 2.780409029515643 |
| ann | 0.2496331334144184 | 1.2929908174243288 |

- **Combined OOS gain (stress):** 149.174%
- Full history @ stress: total 151.467%, CAGR 54.870%, benchmark 8.293%, sharpe 1.76, maxdd -0.205, trades 101

### Daily Range (3167) — 4h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.06415027936760254 | 0.9830783623825177 |
| alpha | 0.37900176451611733 | 0.4555554266027013 |
| trades | 18 | 8 |
| winrate | 0.5 | 0.75 |
| sharpe | 0.31820498457768825 | 2.9081321108029887 |
| maxdd | -0.18429807857519698 | -0.09539580437992567 |
| pf | 1.1601828447693163 | 14.32253135021688 |
| ann | 0.0449055723315408 | 1.587859209429841 |

- **Combined OOS gain (stress):** 111.029%
- Full history @ stress: total 111.029%, CAGR 42.512%, benchmark 9.901%, sharpe 1.47, maxdd -0.214, trades 26

### Balance of Power (546) — 1h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.5902226713964072 | 0.7166232910351547 |
| alpha | 0.9151007201768949 | 0.16054852468001446 |
| trades | 56 | 32 |
| winrate | 0.5178571428571429 | 0.5 |
| sharpe | 1.6197035198348064 | 2.582287219290357 |
| maxdd | -0.14841731907966638 | -0.1609446712735494 |
| pf | 1.901169337841716 | 2.6169680498430163 |
| ann | 0.38779699783341415 | 1.1179354267235202 |

- **Combined OOS gain (stress):** 172.981%
- Full history @ stress: total 172.981%, CAGR 61.020%, benchmark 8.293%, sharpe 1.99, maxdd -0.178, trades 88

### Hull MA Reversal (89) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.33424212568040756 | 0.7117540413917542 |
| alpha | 0.6490936108289224 | 0.1842311056119379 |
| trades | 59 | 36 |
| winrate | 0.4406779661016949 | 0.4444444444444444 |
| sharpe | 0.9090315372621011 | 2.472472584529042 |
| maxdd | -0.22494608374354608 | -0.14360557008871055 |
| pf | 1.361661457246951 | 3.273124041331853 |
| ann | 0.22595840555655688 | 1.109596799524991 |

- **Combined OOS gain (stress):** 128.389%
- Full history @ stress: total 134.148%, CAGR 49.716%, benchmark 9.901%, sharpe 1.54, maxdd -0.225, trades 95

## 2381

### Order Block Finder (1145) — Daily
> family: other | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.23167179102204627 | 0.13668977222201928 |
| alpha | 0.46139097978959687 | 0.1942185366042104 |
| trades | 40 | 17 |
| winrate | 0.525 | 0.5294117647058824 |
| sharpe | 0.9403330312875808 | 0.8996507957524148 |
| maxdd | -0.11452793752953871 | -0.17928539912726815 |
| pf | 1.7796868454141388 | 1.5654472645408521 |
| ann | 0.15859827080800026 | 0.19474332401300054 |

- **Combined OOS gain (stress):** 40.003%
- Full history @ stress: total 144.662%, CAGR 26.000%, benchmark -23.415%, sharpe 1.35, maxdd -0.203, trades 97

### EMA Sticker (1656) — Daily
> family: trend | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.18081731343797414 | -0.008911528698214877 |
| alpha | 0.04890187532957646 | 0.048617235683976245 |
| trades | 53 | 25 |
| winrate | 0.49056603773584906 | 0.48 |
| sharpe | -0.42976661048722514 | 0.07600984248084693 |
| maxdd | -0.32764731315206264 | -0.2660891632030866 |
| pf | 0.7115737320440236 | 0.980107402375685 |
| ann | -0.131429110735805 | -0.012354703309580772 |

- **Combined OOS gain (stress):** -18.812%
- Full history @ stress: total 15.654%, CAGR 3.828%, benchmark -23.415%, sharpe 0.28, maxdd -0.521, trades 140

### Logistic RSI STOCH ROC AO (988) — Daily **(pick)**
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.1351060133479669 | 0.30874645543405665 |
| alpha | 0.3648252021155175 | 0.3662752198162478 |
| trades | 23 | 11 |
| winrate | 0.34782608695652173 | 0.45454545454545453 |
| sharpe | 0.5008401785707661 | 1.6666163254932083 |
| maxdd | -0.26109623100005475 | -0.09953322044453117 |
| pf | 1.4250164681726991 | 4.969299414650558 |
| ann | 0.09365946550615845 | 0.45307151429454007 |

- **Combined OOS gain (stress):** 48.557%
- Full history @ stress: total 129.126%, CAGR 23.883%, benchmark -23.415%, sharpe 1.05, maxdd -0.281, trades 60

## 2382

### Up Gap Strategy With Delay (1511) — 1h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.1789627655152053 | 0.19547218968301916 |
| alpha | 0.35015578200405106 | 0.23380170913382015 |
| trades | 38 | 31 |
| winrate | 0.42105263157894735 | 0.5483870967741935 |
| sharpe | 1.0779987167232197 | 1.5703201898122439 |
| maxdd | -0.06794789382314304 | -0.11365137114844659 |
| pf | 1.6713419829155722 | 1.8622963171719678 |
| ann | 0.12334552848704905 | 0.28140238857763933 |

- **Combined OOS gain (stress):** 40.942%
- Full history @ stress: total 40.942%, CAGR 18.217%, benchmark -18.477%, sharpe 1.27, maxdd -0.114, trades 69

### I Trend (2061) — Daily
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.14571236019678224 | 0.14778938809811626 |
| alpha | 0.28319999620073866 | 0.1844656058631593 |
| trades | 26 | 12 |
| winrate | 0.4230769230769231 | 0.5833333333333334 |
| sharpe | 0.5632236671280081 | 0.881056017087776 |
| maxdd | -0.17900565360211806 | -0.1866508414043212 |
| pf | 1.4682771383212354 | 1.5701295457243585 |
| ann | 0.10086917265861373 | 0.21097625919504415 |

- **Combined OOS gain (stress):** 31.504%
- Full history @ stress: total 146.441%, CAGR 35.821%, benchmark -4.162%, sharpe 1.46, maxdd -0.187, trades 50

### I Gap (2145) — 30min
> family: volatility | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.15005071553718985 | 0.05568063461502826 |
| alpha | 0.017914230908769202 | 0.0923568523800713 |
| trades | 107 | 80 |
| winrate | 0.3644859813084112 | 0.4125 |
| sharpe | -0.5227554205372907 | 0.4308277268830043 |
| maxdd | -0.2582022350955986 | -0.16271214167575665 |
| pf | 0.8201953271340822 | 1.0744472812833645 |
| ann | -0.10850769801903071 | 0.07815603595771692 |

- **Combined OOS gain (stress):** -10.272%
- Full history @ stress: total -10.451%, CAGR -5.240%, benchmark -18.160%, sharpe -0.15, maxdd -0.258, trades 188

### WPR Custom Cloud Simple (3555) — 1h
> family: mean_reversion | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.02412903942400413 | 0.18429910774583358 |
| alpha | 0.1953220559128499 | 0.22262862719663457 |
| trades | 47 | 29 |
| winrate | 0.425531914893617 | 0.5862068965517241 |
| sharpe | 0.18861835784484368 | 1.1013650971126863 |
| maxdd | -0.35935183466482334 | -0.16745129482237164 |
| pf | 1.0477480874057814 | 1.6194544576011598 |
| ann | 0.016986930405336942 | 0.2648003182407175 |

- **Combined OOS gain (stress):** 21.288%
- Full history @ stress: total 21.029%, CAGR 9.754%, benchmark -18.477%, sharpe 0.54, maxdd -0.359, trades 76

### Dynamic Support and Resistance Pivot (717) — 4h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.1570966831712024 | 0.2483948679582837 |
| alpha | 0.32506162961716145 | 0.2861739177579402 |
| trades | 19 | 16 |
| winrate | 0.21052631578947367 | 0.375 |
| sharpe | 0.7289588701982593 | 1.5848353077313933 |
| maxdd | -0.14590671680799816 | -0.14307068730254002 |
| pf | 1.7659864798680547 | 2.2700935564839435 |
| ann | 0.10858594912717567 | 0.36085549232728065 |

- **Combined OOS gain (stress):** 44.451%
- Full history @ stress: total 46.851%, CAGR 20.609%, benchmark -18.160%, sharpe 1.11, maxdd -0.146, trades 35

## 3002

### Adaptive Renko (1899) — 4h
> family: volatility | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.039338790031598014 | 0.036601791299096575 |
| alpha | 0.1890937737594106 | 0.2045644662602163 |
| trades | 24 | 12 |
| winrate | 0.2916666666666667 | 0.4166666666666667 |
| sharpe | -0.3786296788429753 | 0.6434713903854196 |
| maxdd | -0.09581862358035098 | -0.07004936375683979 |
| pf | 0.7951474212788932 | 1.614612020568766 |
| ann | -0.027955294560911392 | 0.05119097088554647 |

- **Combined OOS gain (stress):** -0.418%
- Full history @ stress: total -0.418%, CAGR -0.198%, benchmark -34.994%, sharpe 0.01, maxdd -0.122, trades 36

### Alexav SpeedUp M1 (2790) — 4h **(pick)**
> family: volatility | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.007157414777598015 | 0.04704680423466945 |
| alpha | 0.2212751490134106 | 0.21500947919578917 |
| trades | 22 | 13 |
| winrate | 0.36363636363636365 | 0.46153846153846156 |
| sharpe | -0.011044007715377297 | 0.8115075825101121 |
| maxdd | -0.09826915782023382 | -0.06512637744359595 |
| pf | 0.9651288630841637 | 1.8371682777936835 |
| ann | -0.005061896173505165 | 0.06592974024926268 |

- **Combined OOS gain (stress):** 3.955%
- Full history @ stress: total 3.955%, CAGR 1.857%, benchmark -34.994%, sharpe 0.25, maxdd -0.116, trades 35

### 5 EMA No-Touch Breakout (483) — Daily
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.0680278869012304 | 0.027980215734057623 |
| alpha | 0.18518098124346039 | 0.19852285139297243 |
| trades | 29 | 12 |
| winrate | 0.3103448275862069 | 0.4166666666666667 |
| sharpe | -0.3145846199340127 | 0.42693167325769465 |
| maxdd | -0.1555027521649608 | -0.06511116385394045 |
| pf | 0.7679644589982032 | 1.4074964067672013 |
| ann | -0.04855479324476031 | 0.03906861981645804 |

- **Combined OOS gain (stress):** -4.195%
- Full history @ stress: total 252.048%, CAGR 9.160%, benchmark -76.063%, sharpe 0.61, maxdd -0.372, trades 306

## 3003

### RSI Buy Sell Force (1264) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.06972017527040753 | 0.0015385735579460658 |
| alpha | 0.37323093404730445 | 0.21189964106187065 |
| trades | 49 | 24 |
| winrate | 0.3673469387755102 | 0.2916666666666667 |
| sharpe | 0.3704888166819327 | 0.088041656714428 |
| maxdd | -0.296480599061953 | -0.14873433711970663 |
| pf | 1.1186099582186797 | 1.0768186393633898 |
| ann | 0.04876646614079272 | 0.002137384086893457 |

- **Combined OOS gain (stress):** 7.137%
- Full history @ stress: total 8.308%, CAGR 3.858%, benchmark -43.035%, sharpe 0.31, maxdd -0.304, trades 73

### Sunil 2 Bar Breakout (1360) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.08420506511000303 | 0.026768605463837192 |
| alpha | 0.38771582388689996 | 0.23712967296776177 |
| trades | 35 | 20 |
| winrate | 0.45714285714285713 | 0.4 |
| sharpe | 0.4326558237813836 | 0.3118476297984971 |
| maxdd | -0.19402034621819386 | -0.12915378976769532 |
| pf | 1.1757649051750214 | 1.2907140153912933 |
| ann | 0.05877947457985 | 0.037368195308836505 |

- **Combined OOS gain (stress):** 11.323%
- Full history @ stress: total 12.540%, CAGR 5.764%, benchmark -43.035%, sharpe 0.42, maxdd -0.207, trades 55

### FX-CHAOS Scalp (2822) — 1h
> family: volume | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.005909859611194945 | 0.03509856215947105 |
| alpha | 0.2920353458682571 | 0.24172316783770442 |
| trades | 36 | 19 |
| winrate | 0.3333333333333333 | 0.3684210526315789 |
| sharpe | 0.039675807190681804 | 0.4269435417353115 |
| maxdd | -0.23311184094880344 | -0.11613175068989312 |
| pf | 0.985682020595871 | 1.2798137466842912 |
| ann | -0.004178826328735341 | 0.04907452655789535 |

- **Combined OOS gain (stress):** 2.898%
- Full history @ stress: total 2.954%, CAGR 1.391%, benchmark -42.580%, sharpe 0.17, maxdd -0.254, trades 55

### DreamBot (3432) — 4h **(pick)**
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.06458168443040191 | 0.06351348743387208 |
| alpha | 0.36809244320729884 | 0.27387455493779667 |
| trades | 15 | 8 |
| winrate | 0.4 | 0.375 |
| sharpe | 0.40058962303989587 | 0.6849809338803523 |
| maxdd | -0.1134581167521338 | -0.11473658722688707 |
| pf | 1.4535790187484434 | 1.8975555052976145 |
| ann | 0.04520482164702244 | 0.0892817657547742 |

- **Combined OOS gain (stress):** 13.220%
- Full history @ stress: total 13.220%, CAGR 6.066%, benchmark -43.035%, sharpe 0.50, maxdd -0.115, trades 23

### Futures Engulfing Candle Size (823) — 4h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.11516345836680619 | 0.04317085450110336 |
| alpha | 0.4186742171437031 | 0.25353192200502794 |
| trades | 54 | 29 |
| winrate | 0.3888888888888889 | 0.3448275862068966 |
| sharpe | 0.6042442608477095 | 0.53420018574573 |
| maxdd | -0.16263904019709785 | -0.08466191324781602 |
| pf | 1.2750282829782915 | 1.335959436249701 |
| ann | 0.08004962399582394 | 0.060453755495957884 |

- **Combined OOS gain (stress):** 16.331%
- Full history @ stress: total 20.509%, CAGR 9.252%, benchmark -43.035%, sharpe 0.70, maxdd -0.163, trades 83

## 3004

### Rejection Candle (104) — 4h **(pick)**
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.04209204512159337 | 0.01015061696931796 |
| alpha | 0.25214791104338097 | 0.10131083796379314 |
| trades | 26 | 19 |
| winrate | 0.3076923076923077 | 0.42105263157894735 |
| sharpe | 0.30789799068524826 | 0.19283655961737478 |
| maxdd | -0.11059258556536089 | -0.06074974695111435 |
| pf | 1.220079400822248 | 1.083575591007006 |
| ann | 0.029556731201701547 | 0.014124765879043544 |

- **Combined OOS gain (stress):** 5.267%
- Full history @ stress: total 5.267%, CAGR 2.465%, benchmark -26.480%, sharpe 0.27, maxdd -0.112, trades 45

### Overnight Gap (129) — 4h
> family: pattern | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | -0.004340658602332015 | 0.0068159509762386605 |
| alpha | 0.20571520731945558 | 0.09797617197071384 |
| trades | 15 | 5 |
| winrate | 0.3333333333333333 | 0.4 |
| sharpe | 0.01230605529915703 | 0.3025665623919051 |
| maxdd | -0.07165714966924674 | -0.029907289245897695 |
| pf | 0.9644549930924998 | 1.2924077091630803 |
| ann | -0.0030685443369123933 | 0.009478403262753732 |

- **Combined OOS gain (stress):** 0.245%
- Full history @ stress: total 0.245%, CAGR 0.116%, benchmark -26.480%, sharpe 0.05, maxdd -0.072, trades 20

### ColorMaRsi Trigger MMRec Duplex (3161) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.03137634506800291 | -0.025082428547806623 |
| alpha | 0.2414322109897905 | 0.06607779244666856 |
| trades | 25 | 15 |
| winrate | 0.4 | 0.4 |
| sharpe | 0.2608383642960894 | -0.27143756857874235 |
| maxdd | -0.07068447117967047 | -0.0649068480134648 |
| pf | 1.1711898497998579 | 0.7872909396221673 |
| ann | 0.022066033734801538 | -0.03466333590753845 |

- **Combined OOS gain (stress):** 0.551%
- Full history @ stress: total 1.029%, CAGR 0.487%, benchmark -26.480%, sharpe 0.10, maxdd -0.071, trades 40

### Weekly Rebound Corridor (3885) — 4h
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.03480397747000086 | -0.0018059764905121733 |
| alpha | 0.24485984339178846 | 0.08935424450396301 |
| trades | 8 | 6 |
| winrate | 0.375 | 0.3333333333333333 |
| sharpe | 0.3250757198006191 | -0.05135039736940507 |
| maxdd | -0.05079959386543853 | -0.04091573443021368 |
| pf | 1.491067178236314 | 0.9434262699983356 |
| ann | 0.024464558132499592 | -0.0025072290978135348 |

- **Combined OOS gain (stress):** 3.294%
- Full history @ stress: total 3.294%, CAGR 1.549%, benchmark -26.480%, sharpe 0.24, maxdd -0.051, trades 14

## 3005

### MA Crossover with TP/SL and 5 EMA Filter (1002) — 4h **(pick)**
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.026887614271600135 | 0.1201836136437795 |
| alpha | 0.23356283891858354 | 0.23138361364377957 |
| trades | 7 | 5 |
| winrate | 0.42857142857142855 | 0.2 |
| sharpe | 0.5434491362737071 | 1.108983708174056 |
| maxdd | -0.03172432290335325 | -0.03289541926127837 |
| pf | 1.6481564254161327 | 4.568455009368955 |
| ann | 0.018921452207091072 | 0.17071730444640343 |

- **Combined OOS gain (stress):** 15.030%
- Full history @ stress: total 15.030%, CAGR 6.868%, benchmark -28.691%, sharpe 0.75, maxdd -0.060, trades 12

### Butterfly Pattern (3727) — 4h
> family: volatility | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.054085606583201384 | 0.1117602341007804 |
| alpha | 0.2607608312301848 | 0.22296023410078047 |
| trades | 12 | 10 |
| winrate | 0.5833333333333334 | 0.3 |
| sharpe | 0.5785390701067661 | 0.950686059398306 |
| maxdd | -0.06366199848432663 | -0.0847227435739002 |
| pf | 1.6797108621290888 | 2.296404703170788 |
| ann | 0.03791394460874886 | 0.1585092236640382 |

- **Combined OOS gain (stress):** 17.189%
- Full history @ stress: total 17.189%, CAGR 7.814%, benchmark -28.691%, sharpe 0.72, maxdd -0.085, trades 22

### ASCPlusPlus (3890) — 30min
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.05663854824919612 | 0.1390608225745642 |
| alpha | 0.1510537594431116 | 0.2566144365539129 |
| trades | 36 | 15 |
| winrate | 0.2777777777777778 | 0.5333333333333333 |
| sharpe | -0.325266567835364 | 1.1419701426256512 |
| maxdd | -0.11282350409567143 | -0.061779266374084374 |
| pf | 0.8282200771331727 | 2.243960958029727 |
| ann | -0.04035498822655592 | 0.19820577714366516 |

- **Combined OOS gain (stress):** 7.455%
- Full history @ stress: total 7.455%, CAGR 3.469%, benchmark -28.782%, sharpe 0.32, maxdd -0.145, trades 51

## 3008

### Order Block Finder (1145) — 4h **(pick)**
> family: other | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.15801776867840545 | 0.08148907785024484 |
| alpha | 0.4572303671036023 | 0.4868944832556502 |
| trades | 35 | 27 |
| winrate | 0.3142857142857143 | 0.3333333333333333 |
| sharpe | 0.8511217230221447 | 0.6387371576902835 |
| maxdd | -0.10137078659861876 | -0.0944616878493445 |
| pf | 1.5327871703363412 | 1.321920949462744 |
| ann | 0.10920932304782704 | 0.1149345551681038 |

- **Combined OOS gain (stress):** 25.238%
- Full history @ stress: total 25.980%, CAGR 11.578%, benchmark -56.693%, sharpe 0.76, maxdd -0.113, trades 62

### I Gap (2145) — 4h
> family: volatility | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | 0.0915084364380101 | -0.15382506739901847 |
| alpha | 0.390721034863207 | 0.2515803380063869 |
| trades | 73 | 54 |
| winrate | 0.3698630136986301 | 0.2222222222222222 |
| sharpe | 0.43730429188416603 | -0.8349144060613036 |
| maxdd | -0.18249563829981497 | -0.3249331967886435 |
| pf | 1.125232192863396 | 0.7639440205481774 |
| ann | 0.06381319201940339 | -0.2070279544086896 |

- **Combined OOS gain (stress):** -7.639%
- Full history @ stress: total -6.054%, CAGR -2.919%, benchmark -56.693%, sharpe -0.04, maxdd -0.359, trades 127

### Polarized Fractal Efficiency (2316) — 4h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.0419623385264043 | 0.1400540751185504 |
| alpha | 0.34117493695160117 | 0.5454594805239558 |
| trades | 31 | 15 |
| winrate | 0.3548387096774194 | 0.4666666666666667 |
| sharpe | 0.3195117626931337 | 1.193829034005897 |
| maxdd | -0.12297658882828355 | -0.0838073803916457 |
| pf | 1.1356392732583684 | 2.3924097236544144 |
| ann | 0.029466196749960982 | 0.19965706063042243 |

- **Combined OOS gain (stress):** 18.789%
- Full history @ stress: total 19.492%, CAGR 8.814%, benchmark -56.693%, sharpe 0.70, maxdd -0.123, trades 46

### Bull vs Medved (2510) — 1h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.11850532091560462 | -0.016432367001748327 |
| alpha | 0.41494800866264014 | 0.39216978353588605 |
| trades | 43 | 28 |
| winrate | 0.4186046511627907 | 0.39285714285714285 |
| sharpe | 0.5168562396070369 | 0.06625762072072043 |
| maxdd | -0.16385142301501898 | -0.2753207920914389 |
| pf | 1.247252497574617 | 0.9899855779078521 |
| ann | 0.08233523672093135 | -0.022747853250306926 |

- **Combined OOS gain (stress):** 10.013%
- Full history @ stress: total 11.264%, CAGR 5.193%, benchmark -56.522%, sharpe 0.33, maxdd -0.275, trades 71

### Long Explosive V1 (992) — 4h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.054666671256004884 | 0.014480917075106348 |
| alpha | 0.35387926968120176 | 0.4198863224805117 |
| trades | 38 | 24 |
| winrate | 0.39473684210526316 | 0.375 |
| sharpe | 0.3101513613936971 | 0.20050477331066602 |
| maxdd | -0.13990002489502573 | -0.16795291188364858 |
| pf | 1.1046834422887704 | 1.0578961635105548 |
| ann | 0.038318124301427 | 0.020167300749700745 |

- **Combined OOS gain (stress):** 6.994%
- Full history @ stress: total 7.627%, CAGR 3.548%, benchmark -56.693%, sharpe 0.27, maxdd -0.168, trades 62

## 3010

### CorrTime (3319) — 4h
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.040597595385600815 | 0.05554018828977236 |
| alpha | 0.19524503128303672 | 0.10362155675949036 |
| trades | 12 | 5 |
| winrate | 0.25 | 0.8 |
| sharpe | 0.48392693227914846 | 1.1678910066698147 |
| maxdd | -0.04747613003039952 | -0.017773208060835488 |
| pf | 1.4860171170673033 | 21.8131161498257 |
| ann | 0.028513413328776993 | 0.07795683900597195 |

- **Combined OOS gain (stress):** 9.839%
- Full history @ stress: total 9.839%, CAGR 4.552%, benchmark -17.508%, sharpe 0.72, maxdd -0.047, trades 17

### AML CCI Meeting Lines (3440) — 4h **(pick)**
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.04310247817680146 | 0.08019371420515586 |
| alpha | 0.19774991407423737 | 0.12827508267487386 |
| trades | 13 | 6 |
| winrate | 0.3076923076923077 | 0.6666666666666666 |
| sharpe | 0.516387647170388 | 1.2237146260832947 |
| maxdd | -0.06749351281742177 | -0.02744811512157097 |
| pf | 1.66961907051804 | 5.0300942606967 |
| ann | 0.03026189441656646 | 0.11308037358460266 |

- **Combined OOS gain (stress):** 12.675%
- Full history @ stress: total 12.675%, CAGR 5.824%, benchmark -17.508%, sharpe 0.81, maxdd -0.067, trades 19

### Expert AML MFI (3443) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.026842219638401055 | 0.05955008469395984 |
| alpha | 0.18148965553583696 | 0.10763145316367784 |
| trades | 12 | 8 |
| winrate | 0.25 | 0.75 |
| sharpe | 0.3502624250472581 | 1.2324587367491842 |
| maxdd | -0.06240965586159919 | -0.027447255730844056 |
| pf | 1.4332266821173407 | 4.051270182335957 |
| ann | 0.01888963040278946 | 0.08364817961599602 |

- **Combined OOS gain (stress):** 8.799%
- Full history @ stress: total 8.799%, CAGR 4.081%, benchmark -17.508%, sharpe 0.67, maxdd -0.062, trades 20

### Resonance Hunter (3617) — 4h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.003963803200801808 | 0.027262146924361463 |
| alpha | 0.1586112390982377 | 0.07534351539407946 |
| trades | 20 | 9 |
| winrate | 0.4 | 0.4444444444444444 |
| sharpe | 0.07773969429366949 | 0.5413166318807754 |
| maxdd | -0.15725378751389607 | -0.03852463192899136 |
| pf | 1.0208046157411739 | 1.4503098480003596 |
| ann | 0.00279872019547045 | 0.038060757916784205 |

- **Combined OOS gain (stress):** 3.133%
- Full history @ stress: total 3.133%, CAGR 1.474%, benchmark -17.508%, sharpe 0.21, maxdd -0.157, trades 29

### Adaptive KDJ (MTF) (492) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.013084963212396827 | 0.058150149496173364 |
| alpha | 0.14156247268503908 | 0.10623151796589136 |
| trades | 30 | 14 |
| winrate | 0.3333333333333333 | 0.5714285714285714 |
| sharpe | -0.031135146890345532 | 0.862902785615005 |
| maxdd | -0.09023254949696591 | -0.06722335117020906 |
| pf | 0.9692073413373575 | 1.995114973416378 |
| ann | -0.009262113902336555 | 0.08166026541889093 |

- **Combined OOS gain (stress):** 4.430%
- Full history @ stress: total 7.064%, CAGR 3.291%, benchmark -17.508%, sharpe 0.36, maxdd -0.090, trades 44

## 3020

### Time Session Filter - MACD example (1436) — 4h
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.1394119604532018 | 0.2815201444847175 |
| alpha | 0.3842564776381445 | 0.34685743765400046 |
| trades | 21 | 7 |
| winrate | 0.5238095238095238 | 0.5714285714285714 |
| sharpe | 0.6592532985376898 | 2.286652645279794 |
| maxdd | -0.12134031729153538 | -0.0849589487055129 |
| pf | 1.5989042790406465 | 5.129435595168835 |
| ann | 0.09658882457411955 | 0.4112608215855902 |

- **Combined OOS gain (stress):** 46.018%
- Full history @ stress: total 46.018%, CAGR 19.670%, benchmark -27.889%, sharpe 1.20, maxdd -0.121, trades 28

### Live Alligator (1660) — 4h **(pick)**
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.16825151264000127 | 0.2890243572562343 |
| alpha | 0.413096029824944 | 0.35436165042551726 |
| trades | 12 | 6 |
| winrate | 0.5833333333333334 | 0.6666666666666666 |
| sharpe | 1.279373780046128 | 2.6503383496703976 |
| maxdd | -0.06721803102036272 | -0.03739602639795225 |
| pf | 3.8268726557744395 | 13.80992567005447 |
| ann | 0.11612557849861949 | 0.4227506872846549 |

- **Combined OOS gain (stress):** 50.590%
- Full history @ stress: total 50.590%, CAGR 21.433%, benchmark -27.889%, sharpe 1.84, maxdd -0.067, trades 18

### Ergodic Ticks Volume Indicator (2036) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.13508409657240228 | 0.2765434907491713 |
| alpha | 0.379928613757345 | 0.3418807839184542 |
| trades | 21 | 8 |
| winrate | 0.47619047619047616 | 0.75 |
| sharpe | 0.6540623699230605 | 2.2737646999659544 |
| maxdd | -0.1186883427158828 | -0.08630718822787509 |
| pf | 1.6203352722599664 | 5.63903400798998 |
| ann | 0.09364454707123504 | 0.40365536107616395 |

- **Combined OOS gain (stress):** 44.898%
- Full history @ stress: total 44.898%, CAGR 19.234%, benchmark -27.889%, sharpe 1.19, maxdd -0.119, trades 29

### Bull vs Medved (2510) — 1h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.26751293422800715 | 0.2222106791178986 |
| alpha | 0.5111194916050563 | 0.28952651315684863 |
| trades | 60 | 32 |
| winrate | 0.4666666666666667 | 0.40625 |
| sharpe | 1.1323507331130922 | 1.8128006386200128 |
| maxdd | -0.16577694983991487 | -0.17541220743274888 |
| pf | 1.414964233836254 | 1.6557557967059597 |
| ann | 0.18231657900956488 | 0.32137781095655105 |

- **Combined OOS gain (stress):** 54.917%
- Full history @ stress: total 55.731%, CAGR 23.382%, benchmark -27.770%, sharpe 1.37, maxdd -0.175, trades 92

### Intraday Volume Swings (931) — 1h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.05175738914600547 | 0.22334812065070997 |
| alpha | 0.29536394652305464 | 0.29066395468966 |
| trades | 55 | 24 |
| winrate | 0.34545454545454546 | 0.4583333333333333 |
| sharpe | 0.31224743821103457 | 1.9040783671143349 |
| maxdd | -0.12553534970161917 | -0.09152204518254925 |
| pf | 1.0958622089767696 | 2.313442829277848 |
| ann | 0.03629381569075152 | 0.32308594929264367 |

- **Combined OOS gain (stress):** 28.667%
- Full history @ stress: total 29.343%, CAGR 12.981%, benchmark -27.770%, sharpe 0.87, maxdd -0.126, trades 79

## 3030

### Sunil 2 Bar Breakout (1360) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.03498706063839696 | -0.0008762201912008161 |
| alpha | 0.13776233108909697 | 0.2090717265988512 |
| trades | 37 | 14 |
| winrate | 0.2972972972972973 | 0.2857142857142857 |
| sharpe | -0.12546537011834064 | 0.06287957264510616 |
| maxdd | -0.11856329616623529 | -0.12483866708051283 |
| pf | 0.8829045123958678 | 0.9995181495434649 |
| ann | -0.02484651957233408 | -0.0012166726343183498 |

- **Combined OOS gain (stress):** -3.583%
- Full history @ stress: total -3.505%, CAGR -1.678%, benchmark -33.528%, sharpe -0.05, maxdd -0.144, trades 51

### Bull vs Medved (2510) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.0014167675263976331 | 0.029434180835352874 |
| alpha | 0.1713326242010963 | 0.2393821276254049 |
| trades | 18 | 8 |
| winrate | 0.3333333333333333 | 0.25 |
| sharpe | 0.03312563519318091 | 0.5154823400275609 |
| maxdd | -0.10103390565175263 | -0.03698599879067477 |
| pf | 0.9876669481690767 | 1.496077108100057 |
| ann | -0.0010011257266161477 | 0.04111020397878651 |

- **Combined OOS gain (stress):** 2.798%
- Full history @ stress: total 2.881%, CAGR 1.356%, benchmark -33.528%, sharpe 0.20, maxdd -0.101, trades 26

### Bullish & Bearish Engulfing (2626) — 30min **(pick)**
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.01990154086760043 | 0.002769940237169477 |
| alpha | 0.196656988809489 | 0.2127178870272215 |
| trades | 11 | 7 |
| winrate | 0.36363636363636365 | 0.5714285714285714 |
| sharpe | 0.18717065620894785 | 0.0879657779303154 |
| maxdd | -0.1655134118715058 | -0.059811095012342386 |
| pf | 1.130844416343822 | 1.062515265709103 |
| ann | 0.014019316960143247 | 0.003848916839462646 |

- **Combined OOS gain (stress):** 2.273%
- Full history @ stress: total 2.273%, CAGR 1.072%, benchmark -33.850%, sharpe 0.16, maxdd -0.166, trades 18

### Three MA Cross Channel (3966) — 1h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.03756492377999765 | -0.014466564831658646 |
| alpha | 0.13919052416189093 | 0.19548138195839337 |
| trades | 18 | 8 |
| winrate | 0.3888888888888889 | 0.25 |
| sharpe | -0.22221818026493467 | -0.21186105846965045 |
| maxdd | -0.11319892908297513 | -0.05958186023344958 |
| pf | 0.812105675508471 | 0.7867131530993531 |
| ann | -0.026687587458180118 | -0.020034256431995967 |

- **Combined OOS gain (stress):** -5.149%
- Full history @ stress: total -5.149%, CAGR -2.476%, benchmark -33.850%, sharpe -0.22, maxdd -0.149, trades 26

### Gann Swing Multi Layer (830) — 4h
> family: other | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.060666592289597365 | -0.011020006997973786 |
| alpha | 0.11208279943789656 | 0.19892793979207823 |
| trades | 30 | 11 |
| winrate | 0.3 | 0.2727272727272727 |
| sharpe | -0.3057096589578578 | -0.04125942588858329 |
| maxdd | -0.11397683204745379 | -0.11119746814072662 |
| pf | 0.7943316778242667 | 0.8935010377945405 |
| ann | -0.04325165770271755 | -0.015271542370502655 |

- **Combined OOS gain (stress):** -7.102%
- Full history @ stress: total -7.102%, CAGR -3.434%, benchmark -33.528%, sharpe -0.21, maxdd -0.139, trades 41

## 3050

### MM Fibonacci (1055) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.024582974937199298 | 0.02113060833782643 |
| alpha | 0.3535109084198419 | 0.21568661012274382 |
| trades | 12 | 9 |
| winrate | 0.4166666666666667 | 0.3333333333333333 |
| sharpe | -0.16128755473699882 | 0.30978014269626175 |
| maxdd | -0.05434553745529591 | -0.06953294276669097 |
| pf | 0.7913508641156571 | 1.3251487299835092 |
| ann | -0.017430704214357773 | 0.0294658621162478 |

- **Combined OOS gain (stress):** -0.397%
- Full history @ stress: total -0.180%, CAGR -0.085%, benchmark -48.649%, sharpe 0.04, maxdd -0.075, trades 21

### Octopus Nest (1132) — 1h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.03307694107119952 | 0.03813796583502893 |
| alpha | 0.34413103613677776 | 0.22763055676453048 |
| trades | 14 | 10 |
| winrate | 0.2857142857142857 | 0.7 |
| sharpe | -0.2533645441766702 | 0.561576400520746 |
| maxdd | -0.09840583720676688 | -0.061894714943026785 |
| pf | 0.6979504429758975 | 1.9757387634929378 |
| ann | -0.023483274290374112 | 0.05335503318252188 |

- **Combined OOS gain (stress):** 0.380%
- Full history @ stress: total 0.467%, CAGR 0.221%, benchmark -48.575%, sharpe 0.07, maxdd -0.098, trades 24

### Crypto Analysis (3301) — 1h
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.02846429054800015 | -0.0013371821736911649 |
| alpha | 0.4056722677559774 | 0.18815540875581038 |
| trades | 6 | 6 |
| winrate | 0.5 | 0.3333333333333333 |
| sharpe | 0.3456469469602323 | 0.003697217195919376 |
| maxdd | -0.05235895913980504 | -0.03964495114500899 |
| pf | 1.7650330921084114 | 0.9713225206870368 |
| ann | 0.02002645200075137 | -0.0018565733824534858 |

- **Combined OOS gain (stress):** 2.709%
- Full history @ stress: total 2.709%, CAGR 1.276%, benchmark -48.575%, sharpe 0.23, maxdd -0.052, trades 12

### IU Range Trading (944) — 4h **(pick)**
> family: breakout | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | -0.015374596540399632 | 0.056720423218180605 |
| alpha | 0.36271928681664156 | 0.251276425003098 |
| trades | 7 | 5 |
| winrate | 0.2857142857142857 | 0.4 |
| sharpe | -0.11647935889150565 | 0.8324554374384179 |
| maxdd | -0.05383930562530548 | -0.03983074576126133 |
| pf | 0.684098856666245 | 3.4400781654129893 |
| ann | -0.010886512540967397 | 0.07963110286688924 |

- **Combined OOS gain (stress):** 4.047%
- Full history @ stress: total 4.047%, CAGR 1.900%, benchmark -48.649%, sharpe 0.27, maxdd -0.054, trades 12

## 3060

### VininI Trend LRMA (2050) — 4h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.030321126209601923 | 0.15070487557229706 |
| alpha | 0.43903481915566 | 0.1315267933805162 |
| trades | 12 | 10 |
| winrate | 0.5 | 0.7 |
| sharpe | 0.264186513907057 | 1.7453514902890837 |
| maxdd | -0.09433587304936475 | -0.0527076991996408 |
| pf | 1.2987288838402 | 5.933340737444495 |
| ann | 0.02132716166643478 | 0.21525024778727642 |

- **Combined OOS gain (stress):** 18.560%
- Full history @ stress: total 19.445%, CAGR 8.794%, benchmark -38.257%, sharpe 0.84, maxdd -0.094, trades 22

### I Gap (2145) — 1h
> family: volatility | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.11284806565119143 | 0.039151731730600936 |
| alpha | 0.29586562729486665 | 0.010817246588928464 |
| trades | 68 | 31 |
| winrate | 0.38235294117647056 | 0.41935483870967744 |
| sharpe | -0.5976669320831735 | 0.4968740088407695 |
| maxdd | -0.1858850402679043 | -0.1246371966555152 |
| pf | 0.7922478629307191 | 1.1645519646117182 |
| ann | -0.08111397651940333 | 0.05478384249071899 |

- **Combined OOS gain (stress):** -7.811%
- Full history @ stress: total -6.383%, CAGR -3.080%, benchmark -38.257%, sharpe -0.18, maxdd -0.186, trades 99

### CCI MA v1.5 (3993) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.002750112650404146 | 0.08011546430198946 |
| alpha | 0.41146380559646223 | 0.060937382110208604 |
| trades | 29 | 12 |
| winrate | 0.4482758620689655 | 0.5833333333333334 |
| sharpe | 0.07093308694736632 | 1.1766145746925127 |
| maxdd | -0.1307973826053468 | -0.06814236479239122 |
| pf | 1.0526526349059644 | 2.6010588526441856 |
| ann | 0.0019421154950938213 | 0.11296839446505347 |

- **Combined OOS gain (stress):** 8.309%
- Full history @ stress: total 9.871%, CAGR 4.566%, benchmark -38.257%, sharpe 0.49, maxdd -0.131, trades 42

### 80-20 (488) — 4h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.07912109250799704 | 0.07218375072943983 |
| alpha | 0.32959260043806105 | 0.05300566853765898 |
| trades | 40 | 20 |
| winrate | 0.325 | 0.4 |
| sharpe | -0.3569653837526676 | 0.8723388650905834 |
| maxdd | -0.157443932791821 | -0.08878957349836603 |
| pf | 0.8125166162824644 | 1.4588169799850053 |
| ann | -0.05656971929763899 | 0.10163414364825063 |

- **Combined OOS gain (stress):** -1.265%
- Full history @ stress: total -1.265%, CAGR -0.602%, benchmark -38.257%, sharpe 0.02, maxdd -0.188, trades 60

### Balance of Power (546) — 4h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.0005724800843975864 | 0.09331636797981901 |
| alpha | 0.4081412128616605 | 0.07413828578803816 |
| trades | 29 | 15 |
| winrate | 0.3793103448275862 | 0.4666666666666667 |
| sharpe | 0.061845741969912923 | 1.1772693795404254 |
| maxdd | -0.11610612584994862 | -0.05484289785734309 |
| pf | 1.0617434207264074 | 2.069694443118314 |
| ann | -0.0004044795416552338 | 0.13190398314094476 |

- **Combined OOS gain (stress):** 9.269%
- Full history @ stress: total 11.964%, CAGR 5.507%, benchmark -38.257%, sharpe 0.49, maxdd -0.116, trades 44

## 3080

### HSI1 First 30m Candle (1413) — Daily
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.0303195408171818 | 0.09519154473179747 |
| alpha | 0.24266182564244554 | 0.09770832325528733 |
| trades | 17 | 9 |
| winrate | 0.4117647058823529 | 0.4444444444444444 |
| sharpe | -0.08169338036463694 | 0.9461405219972927 |
| maxdd | -0.12572268659500574 | -0.06291880285947327 |
| pf | 0.8667585005652875 | 2.358259459425588 |
| ann | -0.021516721151828122 | 0.13460100922258333 |

- **Combined OOS gain (stress):** 6.199%
- Full history @ stress: total 4290.773%, CAGR 11.871%, benchmark 30.609%, sharpe 0.77, maxdd -0.326, trades 386

### Last Price (2126) — Daily
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.006671395696985272 | 0.09519135859601069 |
| alpha | 0.26630997076264207 | 0.09770813711950055 |
| trades | 17 | 9 |
| winrate | 0.4117647058823529 | 0.4444444444444444 |
| sharpe | 0.0460671445762576 | 0.9461391575754456 |
| maxdd | -0.10592206004348226 | -0.06291887078923875 |
| pf | 0.9674964782714025 | 2.3582555322743306 |
| ann | -0.004717833568917973 | 0.13460074141835832 |

- **Combined OOS gain (stress):** 8.788%
- Full history @ stress: total 3199.890%, CAGR 10.927%, benchmark 30.609%, sharpe 0.69, maxdd -0.350, trades 389

### Futures Engulfing Candle Size (823) — Daily **(pick)**
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.07947614702508954 | 0.1872469278514337 |
| alpha | 0.1935052194345378 | 0.18976370637492357 |
| trades | 29 | 14 |
| winrate | 0.3793103448275862 | 0.6428571428571429 |
| sharpe | -0.24751706747512142 | 1.6397570888166915 |
| maxdd | -0.20007671615027312 | -0.05191960247049565 |
| pf | 0.8172888899638882 | 3.5221660516684135 |
| ann | -0.056826715429928454 | 0.2691745923697404 |

- **Combined OOS gain (stress):** 9.289%
- Full history @ stress: total 456.435%, CAGR 5.222%, benchmark 30.609%, sharpe 0.34, maxdd -0.457, trades 647

### FVG Breakout Lite (825) — Daily
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.06221456113222135 | 0.1395305995287004 |
| alpha | 0.3351959275918487 | 0.14204737805219025 |
| trades | 18 | 10 |
| winrate | 0.5 | 0.6 |
| sharpe | 0.34606034475394226 | 1.2782696815280266 |
| maxdd | -0.10440141501956446 | -0.05419367515672113 |
| pf | 1.3233014871274877 | 2.755496032381411 |
| ann | 0.043562399434861954 | 0.19889212691325353 |

- **Combined OOS gain (stress):** 21.043%
- Full history @ stress: total 2545.070%, CAGR 10.202%, benchmark 30.609%, sharpe 0.63, maxdd -0.351, trades 472

## 3090

### Genie Stoch RSI (1888) — 4h **(pick)**
> family: mean_reversion | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.036227952187601 | -0.003658894672735835 |
| alpha | 0.30016237841710913 | 0.2291279905731659 |
| trades | 9 | 6 |
| winrate | 0.5555555555555556 | 0.3333333333333333 |
| sharpe | 0.3901581767633894 | -0.1357677376809236 |
| maxdd | -0.0871723277626919 | -0.02056940147438191 |
| pf | 1.3881631021065501 | 0.8348491894357968 |
| ann | 0.025460314620380675 | -0.005077794812474279 |

- **Combined OOS gain (stress):** 3.244%
- Full history @ stress: total 3.244%, CAGR 1.526%, benchmark -42.459%, sharpe 0.27, maxdd -0.087, trades 15

## 3091

### PowerZone (1179) — 30min
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.041281312064397335 | -0.0037432432231432333 |
| alpha | 0.37260757682449164 | 0.24270225440718862 |
| trades | 30 | 17 |
| winrate | 0.3 | 0.4117647058823529 |
| sharpe | -0.20714148921795092 | 0.03549526506353423 |
| maxdd | -0.15753491829450117 | -0.08560659318424202 |
| pf | 0.8478815671362085 | 0.8741587249197298 |
| ann | -0.02934432125891595 | -0.005194767920066901 |

- **Combined OOS gain (stress):** -4.487%
- Full history @ stress: total -5.712%, CAGR -2.751%, benchmark -55.833%, sharpe -0.16, maxdd -0.197, trades 47

### Consecutive Close High1 Mean Reversion (1601) — 30min **(pick)**
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.007423525479600457 | 0.09410803348955632 |
| alpha | 0.42131241436848943 | 0.3405535311198882 |
| trades | 8 | 5 |
| winrate | 0.625 | 0.4 |
| sharpe | 0.1764745632438737 | 1.0867200656969187 |
| maxdd | -0.02334147077720039 | -0.0331187843057541 |
| pf | 1.2975589475147196 | 6.454652230434051 |
| ann | 0.00523887435266901 | 0.1330423993116534 |

- **Combined OOS gain (stress):** 10.223%
- Full history @ stress: total 10.223%, CAGR 4.725%, benchmark -55.833%, sharpe 0.64, maxdd -0.033, trades 13

### Heiken Ashi Simplified EA (1854) — 1h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.06738588763320319 | 0.019154401796088738 |
| alpha | 0.48018737186325877 | 0.2655998994264206 |
| trades | 19 | 9 |
| winrate | 0.2631578947368421 | 0.3333333333333333 |
| sharpe | 0.5236964448850477 | 0.2684844567212567 |
| maxdd | -0.11806114110232291 | -0.05632709760083454 |
| pf | 1.3581108234327806 | 1.2672650627271502 |
| ann | 0.04714912419655137 | 0.0266999779795436 |

- **Combined OOS gain (stress):** 8.783%
- Full history @ stress: total 8.783%, CAGR 4.074%, benchmark -55.751%, sharpe 0.42, maxdd -0.167, trades 28

### 5 EMA No-Touch Breakout (483) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.0930822090196044 | -0.02264620622029745 |
| alpha | 0.5047922461943256 | 0.22498786318033348 |
| trades | 42 | 22 |
| winrate | 0.2857142857142857 | 0.3181818181818182 |
| sharpe | 0.5427135646885095 | -0.15331071640410865 |
| maxdd | -0.12083227077871983 | -0.10733597690370256 |
| pf | 1.2762290235888643 | 0.8618914805102105 |
| ann | 0.06489659014560867 | -0.03131157442947474 |

- **Combined OOS gain (stress):** 6.833%
- Full history @ stress: total 6.833%, CAGR 3.185%, benchmark -55.669%, sharpe 0.29, maxdd -0.121, trades 64

### Adaptive KDJ (MTF) (492) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.006855814559995288 | 0.03238122757021289 |
| alpha | 0.4048542226147259 | 0.2800152969708438 |
| trades | 35 | 16 |
| winrate | 0.2857142857142857 | 0.3125 |
| sharpe | 0.011559687179418235 | 0.3772716166375036 |
| maxdd | -0.15263577700364728 | -0.06417391710083142 |
| pf | 1.0820554141334162 | 1.2326487554312129 |
| ann | -0.004848381542932545 | 0.04525173668449023 |

- **Combined OOS gain (stress):** 2.530%
- Full history @ stress: total 1.667%, CAGR 0.787%, benchmark -55.669%, sharpe 0.12, maxdd -0.189, trades 52

## 3092

### Stoch TP TS V3103 (1791) — Daily
> family: other | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.051262479617131484 | 0.03317748395186859 |
| alpha | 0.0956531172281081 | 0.15760144708550927 |
| trades | 47 | 26 |
| winrate | 0.425531914893617 | 0.4230769230769231 |
| sharpe | 0.2753855612477845 | 0.4128682190073852 |
| maxdd | -0.30338423501984935 | -0.11164702490184586 |
| pf | 1.0621486273936325 | 1.1628658798762639 |
| ann | 0.03594928903493422 | 0.04637151821492291 |

- **Combined OOS gain (stress):** 8.614%
- Full history @ stress: total -21.580%, CAGR -8.282%, benchmark -39.943%, sharpe -0.43, maxdd -0.303, trades 93

### Fisher Org Signal (2292) — Daily
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.13283522924196456 | 0.05906485149868712 |
| alpha | 0.17722586685294117 | 0.1834888146323278 |
| trades | 13 | 9 |
| winrate | 0.6153846153846154 | 0.7777777777777778 |
| sharpe | 0.5898167516277862 | 0.5443525231973219 |
| maxdd | -0.18609992355801075 | -0.1190003767464628 |
| pf | 1.4245157507826336 | 1.423651847279124 |
| ann | 0.09211332550323603 | 0.08295903062098642 |

- **Combined OOS gain (stress):** 19.975%
- Full history @ stress: total -1.298%, CAGR -0.464%, benchmark -39.943%, sharpe 0.06, maxdd -0.273, trades 26

### Bull vs Medved (2510) — 4h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.1827071538376026 | 0.08191295412939037 |
| alpha | 0.26286432476098176 | 0.20523510178039717 |
| trades | 19 | 12 |
| winrate | 0.47368421052631576 | 0.5833333333333334 |
| sharpe | 0.8321981144583888 | 0.9353322964742017 |
| maxdd | -0.10609896789029338 | -0.06080801432281924 |
| pf | 1.986161734605692 | 2.354532977105735 |
| ann | 0.1258648966430964 | 0.11554147861018871 |

- **Combined OOS gain (stress):** 27.959%
- Full history @ stress: total 27.959%, CAGR 12.406%, benchmark -17.878%, sharpe 0.86, maxdd -0.106, trades 31

### Stochastic RSI Cross (25) — Daily
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.10589260506675657 | 0.08647915603175726 |
| alpha | 0.1502832426777332 | 0.21090311916539795 |
| trades | 15 | 6 |
| winrate | 0.4666666666666667 | 0.8333333333333334 |
| sharpe | 0.9664733101709452 | 2.203835524238464 |
| maxdd | -0.10475799186787094 | -0.01088723296613947 |
| pf | 1.6014496905819262 | 13.27459731530626 |
| ann | 0.07369842048664954 | 0.12208541161696163 |

- **Combined OOS gain (stress):** 20.153%
- Full history @ stress: total -4.254%, CAGR -1.534%, benchmark -39.943%, sharpe -0.17, maxdd -0.206, trades 39

## 4001

### Shooting Star Reversal (60) — 4h **(pick)**
> family: pattern | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | -0.0056844593100005 | 0.01998086865461346 |
| alpha | 0.4652662449153516 | 0.30915695912311103 |
| trades | 8 | 6 |
| winrate | 0.5 | 0.5 |
| sharpe | -0.08597164884047012 | 0.3866227191505659 |
| maxdd | -0.04817668967879474 | -0.053308885354067415 |
| pf | 0.8934450456939913 | 1.3693033862596362 |
| ann | -0.0040193136116214445 | 0.02785644148470645 |

- **Combined OOS gain (stress):** 1.418%
- Full history @ stress: total 1.418%, CAGR 0.670%, benchmark -61.268%, sharpe 0.15, maxdd -0.053, trades 14

## 4002

### Trendline Breaks with Multi Fibonacci Supertrend (1475) — 1h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.03853344984999707 | 0.16155716216208127 |
| alpha | 0.329508776637527 | 0.21348594554487066 |
| trades | 22 | 12 |
| winrate | 0.2727272727272727 | 0.5 |
| sharpe | -0.2466780430946506 | 1.592880295627647 |
| maxdd | -0.10464686172216009 | -0.07639568545258768 |
| pf | 0.8209858496726598 | 2.9585530309473893 |
| ann | -0.027379666949227888 | 0.2311962360351305 |

- **Combined OOS gain (stress):** 11.680%
- Full history @ stress: total 11.680%, CAGR 5.380%, benchmark -38.676%, sharpe 0.53, maxdd -0.105, trades 34

### NRTR ATR Stop (2624) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.004684303248002397 | 0.15454080233368006 |
| alpha | 0.3822835471043351 | 0.20364794519082297 |
| trades | 16 | 11 |
| winrate | 0.5 | 0.45454545454545453 |
| sharpe | 0.08527470472019617 | 1.369445191289745 |
| maxdd | -0.1279365454651853 | -0.06625959356318611 |
| pf | 1.0340150487057966 | 3.7072847826069166 |
| ann | 0.0033070946056037442 | 0.2208799794445142 |

- **Combined OOS gain (stress):** 15.995%
- Full history @ stress: total 15.995%, CAGR 7.292%, benchmark -39.603%, sharpe 0.62, maxdd -0.128, trades 27

### Plan X (3202) — 1h **(pick)**
> family: breakout | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.0446182200560008 | 0.18305664436309455 |
| alpha | 0.41266044654352485 | 0.23498542774588393 |
| trades | 6 | 5 |
| winrate | 0.5 | 0.4 |
| sharpe | 0.5659810137233368 | 1.7579832891707792 |
| maxdd | -0.07244827584659241 | -0.054071537075896514 |
| pf | 1.8256341600422095 | 5.756672155251252 |
| ann | 0.03131932781376445 | 0.262957892294273 |

- **Combined OOS gain (stress):** 23.584%
- Full history @ stress: total 23.584%, CAGR 10.566%, benchmark -38.676%, sharpe 1.12, maxdd -0.073, trades 11

### Fast Slow RVI Crossover (3520) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.0031394119579931656 | 0.09618668773141836 |
| alpha | 0.37445983189833953 | 0.14529383058856127 |
| trades | 62 | 28 |
| winrate | 0.4838709677419355 | 0.39285714285714285 |
| sharpe | 0.07977800157233435 | 0.7752685268882737 |
| maxdd | -0.16782946211231808 | -0.10448963543986256 |
| pf | 1.0810903300090633 | 1.2673231546470913 |
| ann | -0.0022189540649913964 | 0.13603303139283507 |

- **Combined OOS gain (stress):** 9.275%
- Full history @ stress: total 11.524%, CAGR 5.310%, benchmark -39.603%, sharpe 0.37, maxdd -0.175, trades 90

### T3MA(MTC) (3898) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.02303882504599586 | 0.11002318199089367 |
| alpha | 0.35456041881033684 | 0.15913032484803658 |
| trades | 40 | 21 |
| winrate | 0.325 | 0.3333333333333333 |
| sharpe | -0.01657312880793939 | 0.9077343100029492 |
| maxdd | -0.14962446904933924 | -0.10062461370510278 |
| pf | 0.9347382483070314 | 1.6026006699344124 |
| ann | -0.016332049683936534 | 0.15599615870106498 |

- **Combined OOS gain (stress):** 8.445%
- Full history @ stress: total 8.445%, CAGR 3.921%, benchmark -39.603%, sharpe 0.31, maxdd -0.150, trades 61

## 4003

### RSI Failure Swing (110) — 1h
> family: other | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.061378076174885665 | -0.013146817891845908 |
| alpha | 0.12443611188917125 | 0.21348040104306543 |
| trades | 19 | 12 |
| winrate | 0.5263157894736842 | 0.3333333333333333 |
| sharpe | 0.5079269479192301 | -0.06471224425166562 |
| maxdd | -0.05712859096629419 | -0.12087082107558722 |
| pf | 1.3799015048325207 | 0.8680365115339279 |
| ann | 0.042981749748778775 | -0.01821129416795464 |

- **Combined OOS gain (stress):** 4.742%
- Full history @ stress: total 4.742%, CAGR 2.222%, benchmark -27.065%, sharpe 0.25, maxdd -0.121, trades 31

### Stochastic Failure Swing (111) — 1h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.061378076174885665 | -0.013146817891845908 |
| alpha | 0.12443611188917125 | 0.21348040104306543 |
| trades | 19 | 12 |
| winrate | 0.5263157894736842 | 0.3333333333333333 |
| sharpe | 0.5079269479192301 | -0.06471224425166562 |
| maxdd | -0.05712859096629419 | -0.12087082107558722 |
| pf | 1.3799015048325207 | 0.8680365115339279 |
| ann | 0.042981749748778775 | -0.01821129416795464 |

- **Combined OOS gain (stress):** 4.742%
- Full history @ stress: total 4.742%, CAGR 2.222%, benchmark -27.065%, sharpe 0.25, maxdd -0.121, trades 31

### Stochastic RSI OHLC (1340) — 1h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.07046414922600208 | 0.05236263056593682 |
| alpha | 0.13352218494028767 | 0.27898984950084815 |
| trades | 15 | 9 |
| winrate | 0.6 | 0.5555555555555556 |
| sharpe | 0.44522635181216036 | 0.5391590737590374 |
| maxdd | -0.09931012587047228 | -0.08522136800139235 |
| pf | 1.8789857018595502 | 1.6669116967434408 |
| ann | 0.049281720532895035 | 0.07345282067941583 |

- **Combined OOS gain (stress):** 12.652%
- Full history @ stress: total 12.652%, CAGR 5.814%, benchmark -27.065%, sharpe 0.48, maxdd -0.099, trades 24

### JK BullP AutoTrader (2482) — 1h **(pick)**
> family: volatility | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.13126497917000268 | -0.02927528293530013 |
| alpha | 0.19432301488428827 | 0.1973519359996112 |
| trades | 20 | 12 |
| winrate | 0.6 | 0.3333333333333333 |
| sharpe | 0.9487723872100523 | -0.24008041331847596 |
| maxdd | -0.05152645327340666 | -0.12731573633627857 |
| pf | 2.697768687109807 | 0.7045555432136498 |
| ann | 0.09104363570294405 | -0.04042425276643269 |

- **Combined OOS gain (stress):** 9.815%
- Full history @ stress: total 9.815%, CAGR 4.541%, benchmark -27.065%, sharpe 0.45, maxdd -0.127, trades 32

## 4005

### Order Block Finder (1145) — 4h
> family: other | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.1923454417000079 | 0.3704834048345742 |
| alpha | 0.48505273440730057 | 0.5592945936457631 |
| trades | 56 | 27 |
| winrate | 0.4107142857142857 | 0.4074074074074074 |
| sharpe | 0.7824801581389712 | 2.2113778153532406 |
| maxdd | -0.13405878715997166 | -0.09410514006837656 |
| pf | 1.414640672687488 | 2.3260957945708114 |
| ann | 0.1323391653667536 | 0.5491305449069623 |

- **Combined OOS gain (stress):** 63.409%
- Full history @ stress: total 63.409%, CAGR 26.231%, benchmark -42.058%, sharpe 1.31, maxdd -0.134, trades 83

### Explosion Range Expansion (3263) — 4h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.45632063753201013 | 0.4258588301141788 |
| alpha | 0.7490279302393028 | 0.6146700189253677 |
| trades | 66 | 43 |
| winrate | 0.3787878787878788 | 0.4418604651162791 |
| sharpe | 1.423619986430405 | 2.020897992586337 |
| maxdd | -0.1372385547471121 | -0.12575160566654908 |
| pf | 1.7389456254540647 | 2.018082818051933 |
| ann | 0.30418066588376846 | 0.6367370236628822 |

- **Combined OOS gain (stress):** 107.651%
- Full history @ stress: total 109.711%, CAGR 42.089%, benchmark -42.058%, sharpe 1.67, maxdd -0.137, trades 109

### Breakthrough Volatility (3271) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.13345093090401416 | 0.5362057163114218 |
| alpha | 0.42615822361130684 | 0.7250169051226106 |
| trades | 101 | 50 |
| winrate | 0.3564356435643564 | 0.48 |
| sharpe | 0.5038524064607488 | 2.303319937768816 |
| maxdd | -0.14780618124014577 | -0.1519604691555413 |
| pf | 1.1291883084643195 | 2.0378172002772876 |
| ann | 0.0925326365775423 | 0.8152555581951764 |

- **Combined OOS gain (stress):** 74.121%
- Full history @ stress: total 75.848%, CAGR 30.702%, benchmark -42.058%, sharpe 1.20, maxdd -0.152, trades 151

### Futures Engulfing Candle Size (823) — 4h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.5055573186720093 | 0.4002202146649776 |
| alpha | 0.7982646113793019 | 0.5890314034761664 |
| trades | 64 | 33 |
| winrate | 0.4375 | 0.5151515151515151 |
| sharpe | 1.5087747113119239 | 1.9529057420676024 |
| maxdd | -0.12342549540069814 | -0.09309398762648935 |
| pf | 1.769977525542083 | 2.1447769021366665 |
| ann | 0.33517911216831675 | 0.5960078956482642 |

- **Combined OOS gain (stress):** 110.811%
- Full history @ stress: total 112.903%, CAGR 43.111%, benchmark -42.058%, sharpe 1.69, maxdd -0.123, trades 97

### Long Explosive V1 (992) — 4h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.5235060838360095 | 0.41858086409286854 |
| alpha | 0.8162133765433022 | 0.6073920529040574 |
| trades | 63 | 32 |
| winrate | 0.4126984126984127 | 0.5 |
| sharpe | 1.5185315599092752 | 2.032925272508545 |
| maxdd | -0.15131701917652973 | -0.11339675072097755 |
| pf | 1.809142651214902 | 1.8570315650752836 |
| ann | 0.34640497831325834 | 0.6251461734221833 |

- **Combined OOS gain (stress):** 116.122%
- Full history @ stress: total 116.561%, CAGR 44.272%, benchmark -42.058%, sharpe 1.71, maxdd -0.151, trades 95

## 4006

### WarriorTrading Momentum (1554) — 4h **(pick)**
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.039484561801600426 | 0.025383558896026504 |
| alpha | 0.3926183316799914 | 0.2601784669582613 |
| trades | 8 | 7 |
| winrate | 0.375 | 0.42857142857142855 |
| sharpe | 0.4915443489449717 | 0.5177630862924258 |
| maxdd | -0.06044798236152893 | -0.038477382050532194 |
| pf | 1.5431251693480947 | 1.707531408312008 |
| ann | 0.027736087153660716 | 0.03542531846897368 |

- **Combined OOS gain (stress):** 6.587%
- Full history @ stress: total 6.587%, CAGR 3.072%, benchmark -49.392%, sharpe 0.50, maxdd -0.067, trades 15

### Polarized Fractal Efficiency (2316) — Daily
> family: momentum | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.02700809881014621 | -0.12596553642553698 |
| alpha | 0.3896585678565204 | 0.11044942476006636 |
| trades | 18 | 12 |
| winrate | 0.5 | 0.5 |
| sharpe | -0.1130446989236779 | -1.8023980150533456 |
| maxdd | -0.145233338627073 | -0.1478177237222349 |
| pf | 0.8530380486612642 | 0.2912044665963343 |
| ann | -0.019157198211640525 | -0.17053925253718283 |

- **Combined OOS gain (stress):** -14.957%
- Full history @ stress: total 72.961%, CAGR 4.446%, benchmark -11.469%, sharpe 0.43, maxdd -0.265, trades 136

### Bull vs Medved (2510) — 1h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.036683966062006856 | -0.001872925388260449 |
| alpha | 0.4045998709980214 | 0.23400278082642878 |
| trades | 54 | 23 |
| winrate | 0.5185185185185185 | 0.391304347826087 |
| sharpe | 0.25061986116653856 | 0.03559214098616235 |
| maxdd | -0.17234405706641642 | -0.08820071559226383 |
| pf | 1.1901870373842383 | 0.8956965525345474 |
| ann | 0.025779110902677038 | -0.0026001400768721483 |

- **Combined OOS gain (stress):** 3.474%
- Full history @ stress: total 5.953%, CAGR 2.781%, benchmark -50.548%, sharpe 0.27, maxdd -0.172, trades 77

## 4007

### Big Dog Range Breakout (2496) — 1h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.00038860573199839266 | 0.05776692660880056 |
| alpha | 0.36866451205091144 | 0.25989458618326866 |
| trades | 13 | 9 |
| winrate | 0.23076923076923078 | 0.4444444444444444 |
| sharpe | 0.06083989673041721 | 0.6561132590005799 |
| maxdd | -0.15542702690378285 | -0.08320603768845714 |
| pf | 0.9981525154035166 | 1.4529676390476878 |
| ann | -0.0002745577175394809 | 0.08111626539949746 |

- **Combined OOS gain (stress):** 5.736%
- Full history @ stress: total 5.736%, CAGR 2.681%, benchmark -48.037%, sharpe 0.27, maxdd -0.155, trades 22

### Bull vs Medved (2510) — 1h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.07705711112239544 | 0.1780687775648353 |
| alpha | 0.2919960066605144 | 0.3801964371393034 |
| trades | 57 | 28 |
| winrate | 0.3333333333333333 | 0.35714285714285715 |
| sharpe | -0.3446345495151004 | 1.587314999705172 |
| maxdd | -0.1524543099618869 | -0.06489062669144896 |
| pf | 0.8114150483931956 | 1.983015895646086 |
| ann | -0.05507634042542453 | 0.2555690522062697 |

- **Combined OOS gain (stress):** 8.729%
- Full history @ stress: total 9.275%, CAGR 4.297%, benchmark -48.037%, sharpe 0.36, maxdd -0.152, trades 85

### Daily BreakPoint (2717) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.026244460467998887 | 0.053372911573358994 |
| alpha | 0.3478677961184845 | 0.2583199080397901 |
| trades | 14 | 11 |
| winrate | 0.2857142857142857 | 0.36363636363636365 |
| sharpe | -0.19589546014304318 | 0.6806167381341915 |
| maxdd | -0.06649945586073425 | -0.05496445837651032 |
| pf | 0.8217414942600791 | 1.8409325389527953 |
| ann | -0.018613412762477077 | 0.07488426754628352 |

- **Combined OOS gain (stress):** 2.573%
- Full history @ stress: total 3.529%, CAGR 1.659%, benchmark -48.454%, sharpe 0.22, maxdd -0.071, trades 25

### ASCPlusPlus (3890) — 1h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.013673382467998985 | 0.03314885640966714 |
| alpha | 0.35537973531491085 | 0.23527651598413524 |
| trades | 17 | 13 |
| winrate | 0.29411764705882354 | 0.38461538461538464 |
| sharpe | -0.016687157625114996 | 0.39797905094835306 |
| maxdd | -0.13665900892703786 | -0.07857956326091331 |
| pf | 0.9367271216010844 | 1.1748827433320672 |
| ann | -0.009679466933582237 | 0.04633125326370702 |

- **Combined OOS gain (stress):** 1.902%
- Full history @ stress: total 1.902%, CAGR 0.898%, benchmark -48.037%, sharpe 0.13, maxdd -0.137, trades 30

## 4008

### True Scalper Profit Lock (2511) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.22858004706280188 | 0.05943147809356275 |
| alpha | 0.4453465141286701 | 0.3823082952320479 |
| trades | 14 | 12 |
| winrate | 0.7142857142857143 | 0.3333333333333333 |
| sharpe | 1.800920885831068 | 0.8595024804893268 |
| maxdd | -0.053968237733019064 | -0.05639651066557849 |
| pf | 4.537988877149042 | 1.5719364922081402 |
| ann | 0.1565428477678379 | 0.08347971810232502 |

- **Combined OOS gain (stress):** 30.160%
- Full history @ stress: total 30.160%, CAGR 13.319%, benchmark -47.006%, sharpe 1.44, maxdd -0.056, trades 26

### The 20s Breakout (2986) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.1665564504992052 | 0.062310537439075775 |
| alpha | 0.3833229175650734 | 0.3851873545775609 |
| trades | 50 | 30 |
| winrate | 0.32 | 0.4 |
| sharpe | 0.6793438741591483 | 0.6554396771988878 |
| maxdd | -0.1312235610388598 | -0.09442421162764636 |
| pf | 1.3173161824940893 | 1.2031345710983148 |
| ann | 0.114981239914834 | 0.08757102674728023 |

- **Combined OOS gain (stress):** 23.925%
- Full history @ stress: total 23.829%, CAGR 10.670%, benchmark -47.006%, sharpe 0.66, maxdd -0.168, trades 80

### CorrTime (3319) — 4h **(pick)**
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.18877059776000227 | 0.0771140757541755 |
| alpha | 0.4055370648258705 | 0.39999089289266065 |
| trades | 15 | 6 |
| winrate | 0.4666666666666667 | 0.3333333333333333 |
| sharpe | 1.1444706993225116 | 1.0003595832663705 |
| maxdd | -0.0965060069911644 | -0.08309446623811068 |
| pf | 2.1212746880164026 | 2.116433299923224 |
| ann | 0.12993965571247812 | 0.10867565475363139 |

- **Combined OOS gain (stress):** 28.044%
- Full history @ stress: total 28.044%, CAGR 12.441%, benchmark -47.006%, sharpe 1.10, maxdd -0.097, trades 21

### Demo GPT - Day Trading Scalping (675) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.06358946434320423 | 0.08033916854920098 |
| alpha | 0.28035593140907245 | 0.40321598568768613 |
| trades | 51 | 26 |
| winrate | 0.3333333333333333 | 0.4230769230769231 |
| sharpe | 0.3321836255482479 | 0.7744621073925037 |
| maxdd | -0.2041004411240177 | -0.11533593726758817 |
| pf | 1.1175547197103397 | 1.3865154665269703 |
| ann | 0.04451650299929222 | 0.11328853365171754 |

- **Combined OOS gain (stress):** 14.904%
- Full history @ stress: total 14.064%, CAGR 6.441%, benchmark -47.006%, sharpe 0.44, maxdd -0.204, trades 78

## 4009

### Parabolic SAR Bug5 (1626) — 4h **(pick)**
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.4245195947596021 | 0.31986017466000094 |
| alpha | 0.9252900107842554 | 0.45239029514192874 |
| trades | 13 | 8 |
| winrate | 0.5384615384615384 | 0.5 |
| sharpe | 1.4474327610959272 | 1.6803447919365402 |
| maxdd | -0.12643969683450784 | -0.1003033209426476 |
| pf | 6.890150484479745 | 4.294624196162544 |
| ann | 0.28399585899188984 | 0.47023638174607796 |

- **Combined OOS gain (stress):** 88.017%
- Full history @ stress: total 88.017%, CAGR 34.917%, benchmark -55.624%, sharpe 1.53, maxdd -0.126, trades 21

### Parabolic Sar Volume (188) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.1709320976076063 | 0.2926830797422124 |
| alpha | 0.6717025136322596 | 0.4252132002241402 |
| trades | 56 | 31 |
| winrate | 0.375 | 0.41935483870967744 |
| sharpe | 0.7961849128014793 | 1.7402082489927762 |
| maxdd | -0.12220005652719779 | -0.11279176423896087 |
| pf | 1.3479227246483205 | 2.239660840474916 |
| ann | 0.11793425060841978 | 0.4283620849279748 |

- **Combined OOS gain (stress):** 51.364%
- Full history @ stress: total 51.364%, CAGR 21.729%, benchmark -55.624%, sharpe 1.17, maxdd -0.149, trades 87

### Fisher Cyber Cycle (1946) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.07233142125879177 | 0.25081493242154496 |
| alpha | 0.42843899476586156 | 0.38334505290347276 |
| trades | 69 | 31 |
| winrate | 0.391304347826087 | 0.3870967741935484 |
| sharpe | -0.11579426138191701 | 1.5167831243058791 |
| maxdd | -0.2198133620482149 | -0.1365136567534988 |
| pf | 0.923580410147923 | 1.9606947270423711 |
| ann | -0.05166078733681945 | 0.36452058540873145 |

- **Combined OOS gain (stress):** 16.034%
- Full history @ stress: total 18.910%, CAGR 8.563%, benchmark -55.624%, sharpe 0.47, maxdd -0.220, trades 100

### Hercules A.T.C. 2006 (2485) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.27015828137160414 | 0.2905048613367669 |
| alpha | 0.7709286973962575 | 0.4230349818186947 |
| trades | 41 | 24 |
| winrate | 0.4634146341463415 | 0.5 |
| sharpe | 1.231298509238543 | 1.9397259066292518 |
| maxdd | -0.060843842739123355 | -0.07009536306098485 |
| pf | 2.031249922018795 | 2.7350755497472092 |
| ann | 0.18405931183078805 | 0.4250205975848813 |

- **Combined OOS gain (stress):** 63.915%
- Full history @ stress: total 63.915%, CAGR 26.417%, benchmark -55.624%, sharpe 1.50, maxdd -0.101, trades 65

### Morse Code (2597) — Daily
> family: volatility | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.2369233085128608 | 0.2807739332939345 |
| alpha | 0.3424048568618162 | 0.4069875255269443 |
| trades | 46 | 25 |
| winrate | 0.391304347826087 | 0.52 |
| sharpe | -1.172077307031376 | 1.6744039414929068 |
| maxdd | -0.2962071576466695 | -0.09942812246490962 |
| pf | 0.5907041012105365 | 2.1103822521711266 |
| ann | -0.17389203432470746 | 0.41011970789831276 |

- **Combined OOS gain (stress):** -2.267%
- Full history @ stress: total 3.470%, CAGR 0.326%, benchmark -59.004%, sharpe 0.11, maxdd -0.477, trades 354

## 4011

### RSI (1276) — 30min **(pick)**
> family: mean_reversion | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.13094193646760055 | 0.008129398639705965 |
| alpha | 0.2874701263785798 | 0.21454743853562952 |
| trades | 7 | 7 |
| winrate | 0.8571428571428571 | 0.5714285714285714 |
| sharpe | 0.5253877140396398 | 0.15010250193504635 |
| maxdd | -0.1606676738516395 | -0.16462368861987164 |
| pf | 5.611729686267009 | 0.6320423032896875 |
| ann | 0.0908235176836083 | 0.011307784770108187 |

- **Combined OOS gain (stress):** 14.014%
- Full history @ stress: total 15.625%, CAGR 7.129%, benchmark -32.122%, sharpe 0.44, maxdd -0.165, trades 14

### Keltner RSI Divergence (311) — 4h
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.24986571626160115 | -0.008106151005845663 |
| alpha | 0.4013582535750341 | 0.20850343803525018 |
| trades | 10 | 7 |
| winrate | 0.8 | 0.5714285714285714 |
| sharpe | 1.0492337848091762 | -0.10129287175514945 |
| maxdd | -0.09531095427465086 | -0.054280389045270216 |
| pf | 4.45813555756156 | 0.9968544150512215 |
| ann | 0.1706632727985289 | -0.011239918004986249 |

- **Combined OOS gain (stress):** 23.973%
- Full history @ stress: total 24.965%, CAGR 11.150%, benchmark -31.716%, sharpe 0.80, maxdd -0.095, trades 17

### Resonance Hunter (3617) — 4h
> family: momentum | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.18780636245680293 | -0.007616354893475563 |
| alpha | 0.33929889977023586 | 0.20899323414762028 |
| trades | 23 | 5 |
| winrate | 0.5217391304347826 | 0.4 |
| sharpe | 1.160870537187966 | -0.16196976308316485 |
| maxdd | -0.05911011543471789 | -0.0331113876078688 |
| pf | 2.1251109947178604 | 0.8217202200563309 |
| ann | 0.12929207840947288 | -0.010561781350364008 |

- **Combined OOS gain (stress):** 17.876%
- Full history @ stress: total 17.876%, CAGR 8.114%, benchmark -31.716%, sharpe 0.85, maxdd -0.089, trades 28

### Manual EA (3936) — 30min
> family: mean_reversion | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.20036559063240023 | -0.04279105385434656 |
| alpha | 0.3568937805433795 | 0.163626986041577 |
| trades | 9 | 11 |
| winrate | 0.6666666666666666 | 0.5454545454545454 |
| sharpe | 0.7126038919329345 | -0.22967317845807445 |
| maxdd | -0.16083524698299623 | -0.16376593279397922 |
| pf | 9.3508679231566 | 0.6177247862935697 |
| ann | 0.1377147890278665 | -0.05892878283986158 |

- **Combined OOS gain (stress):** 14.900%
- Full history @ stress: total 16.524%, CAGR 7.524%, benchmark -32.122%, sharpe 0.45, maxdd -0.185, trades 20

## 4012

### Three Candle Bullish Engulfing (1424) — 1h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.009662301751601765 | 0.11873634097977348 |
| alpha | 0.1983877919476802 | 0.1451293028566064 |
| trades | 24 | 10 |
| winrate | 0.25 | 0.5 |
| sharpe | 0.12273060532849092 | 1.493587366200206 |
| maxdd | -0.07274136325726455 | -0.06213768400335329 |
| pf | 1.0691179223670948 | 2.7584186206551946 |
| ann | 0.006816580197640976 | 0.16861721138121832 |

- **Combined OOS gain (stress):** 12.955%
- Full history @ stress: total 12.955%, CAGR 5.949%, benchmark -18.627%, sharpe 0.66, maxdd -0.073, trades 34

### Rampok Scalp (1725) — 4h
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | -0.01380289135519841 | 0.11173849368330457 |
| alpha | 0.1729292953769883 | 0.12948997297324538 |
| trades | 15 | 6 |
| winrate | 0.5333333333333333 | 0.3333333333333333 |
| sharpe | 0.022865871665129225 | 1.0405291852588778 |
| maxdd | -0.18555584855818585 | -0.08142585716469775 |
| pf | 0.9464758485186974 | 2.6199169263778836 |
| ann | -0.009771334593263625 | 0.15847776146569603 |

- **Combined OOS gain (stress):** 9.639%
- Full history @ stress: total 9.639%, CAGR 4.462%, benchmark -18.428%, sharpe 0.35, maxdd -0.186, trades 21

### Heiken Ashi Simplified EA (1854) — 30min
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.006540898110397708 | 0.06561620516431321 |
| alpha | 0.1761751512723183 | 0.08336768445425402 |
| trades | 21 | 10 |
| winrate | 0.2857142857142857 | 0.4 |
| sharpe | -0.0001532253082040495 | 0.9772440948484983 |
| maxdd | -0.10075245099056129 | -0.06935781907500682 |
| pf | 0.9591103168110637 | 1.7056864347416807 |
| ann | -0.004625460139136006 | 0.09227388916554768 |

- **Combined OOS gain (stress):** 5.865%
- Full history @ stress: total 5.335%, CAGR 2.496%, benchmark -18.025%, sharpe 0.30, maxdd -0.101, trades 31

### Bull vs Medved (2510) — 4h
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.01081963638240202 | 0.08222335848489992 |
| alpha | 0.19755182311458874 | 0.09997483777484073 |
| trades | 17 | 5 |
| winrate | 0.47058823529411764 | 0.4 |
| sharpe | 0.13069777905429894 | 0.7626443603675302 |
| maxdd | -0.11491928056697964 | -0.08701866002439729 |
| pf | 1.136137895591095 | 1.9871586822938467 |
| ann | 0.007631772027997474 | 0.115985986940351 |

- **Combined OOS gain (stress):** 9.393%
- Full history @ stress: total 11.716%, CAGR 5.396%, benchmark -18.428%, sharpe 0.40, maxdd -0.115, trades 22

### ColorMaRsi Trigger MMRec Duplex (3161) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.032664286184796776 | 0.05976668464103274 |
| alpha | 0.15406790054738995 | 0.07751816393097355 |
| trades | 22 | 16 |
| winrate | 0.4090909090909091 | 0.3125 |
| sharpe | -0.28722832702234535 | 0.7367677798925731 |
| maxdd | -0.135060833072966 | -0.09888757320156916 |
| pf | 0.802072174511956 | 1.3673918731457024 |
| ann | -0.02318886789116925 | 0.08395584376667542 |

- **Combined OOS gain (stress):** 2.515%
- Full history @ stress: total 2.515%, CAGR 1.185%, benchmark -18.428%, sharpe 0.17, maxdd -0.135, trades 38

## 4013

### Pivot Point SuperTrend TrendFilter (1169) — 30min
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.11234702077600178 | 0.12335999059023295 |
| alpha | 0.20424282395979332 | 0.24148547471106951 |
| trades | 14 | 5 |
| winrate | 0.35714285714285715 | 0.8 |
| sharpe | 1.0591265618172367 | 1.9961010306558984 |
| maxdd | -0.06431657452038897 | -0.03215241155094184 |
| pf | 1.8452305728100415 | 8.475374510945437 |
| ann | 0.07812180563272864 | 0.17533014580624284 |

- **Combined OOS gain (stress):** 24.957%
- Full history @ stress: total 24.957%, CAGR 11.147%, benchmark -17.619%, sharpe 1.40, maxdd -0.064, trades 19

### Eugene Candle Pattern (1852) — Daily
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.25998107518819613 | 0.0624807558238627 |
| alpha | 0.3550514977234074 | 0.17648853792503005 |
| trades | 29 | 12 |
| winrate | 0.4482758620689655 | 0.3333333333333333 |
| sharpe | 1.0808996337152734 | 0.8442576625949263 |
| maxdd | -0.15092181820624528 | -0.0804961103656131 |
| pf | 1.940429468585399 | 1.5547280355954605 |
| ann | 0.1773487939898002 | 0.08781305195860045 |

- **Combined OOS gain (stress):** 33.871%
- Full history @ stress: total 478.126%, CAGR 30.916%, benchmark 314.000%, sharpe 1.50, maxdd -0.266, trades 142

### The 20s Breakout (2986) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.11368559094000674 | 0.05947051665396552 |
| alpha | 0.20492382410438037 | 0.1762276927594737 |
| trades | 53 | 28 |
| winrate | 0.2830188679245283 | 0.39285714285714285 |
| sharpe | 0.6438725866065957 | 0.6332732187932999 |
| maxdd | -0.11090337952158924 | -0.10852971468042738 |
| pf | 1.2629239284974967 | 1.3243513389947004 |
| ann | 0.07903821957834123 | 0.08353516526079052 |

- **Combined OOS gain (stress):** 17.992%
- Full history @ stress: total 17.861%, CAGR 8.107%, benchmark -17.560%, sharpe 0.64, maxdd -0.111, trades 81

### Futures Engulfing Candle Size (823) — 4h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.05372522499200616 | 0.051240160722283656 |
| alpha | 0.1449634581563798 | 0.16799733682779183 |
| trades | 57 | 31 |
| winrate | 0.2807017543859649 | 0.45161290322580644 |
| sharpe | 0.3392234430420295 | 0.5256256801772099 |
| maxdd | -0.13386358162949508 | -0.125806385184284 |
| pf | 1.1206180827745376 | 1.2015793308737983 |
| ann | 0.03766323583224107 | 0.07186304215686001 |

- **Combined OOS gain (stress):** 10.772%
- Full history @ stress: total 10.649%, CAGR 4.917%, benchmark -17.560%, sharpe 0.40, maxdd -0.134, trades 88

### Long Explosive V1 (992) — 4h **(pick)**
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.19807175129600463 | 0.10131918069429569 |
| alpha | 0.28930998446037826 | 0.21807635679980386 |
| trades | 36 | 19 |
| winrate | 0.3888888888888889 | 0.3684210526315789 |
| sharpe | 0.9748414981753241 | 0.9836714109724033 |
| maxdd | -0.10697065794481919 | -0.11946521461747672 |
| pf | 1.4964504863916395 | 1.588354734545988 |
| ann | 0.13617838857912035 | 0.1434267684072572 |

- **Combined OOS gain (stress):** 31.946%
- Full history @ stress: total 31.800%, CAGR 13.994%, benchmark -17.560%, sharpe 0.97, maxdd -0.119, trades 55

## 4014

### RSI Failure Swing (110) — 4h **(pick)**
> family: other | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.1632276344175334 | 0.12264074374121914 |
| alpha | 0.5533069994968985 | 0.260164079148811 |
| trades | 17 | 6 |
| winrate | 0.4117647058823529 | 0.6666666666666666 |
| sharpe | 0.7525501549227185 | 1.30132926858802 |
| maxdd | -0.14379002688875187 | -0.06425809793823167 |
| pf | 1.5291371773946054 | 3.908874368487874 |
| ann | 0.11273253046151166 | 0.17428518667854664 |

- **Combined OOS gain (stress):** 30.589%
- Full history @ stress: total 31.746%, CAGR 13.972%, benchmark -45.000%, sharpe 0.93, maxdd -0.144, trades 23

### Stochastic Failure Swing (111) — 4h
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.1632276344175334 | 0.12264074374121914 |
| alpha | 0.5533069994968985 | 0.260164079148811 |
| trades | 17 | 6 |
| winrate | 0.4117647058823529 | 0.6666666666666666 |
| sharpe | 0.7525501549227185 | 1.30132926858802 |
| maxdd | -0.14379002688875187 | -0.06425809793823167 |
| pf | 1.5291371773946054 | 3.908874368487874 |
| ann | 0.11273253046151166 | 0.17428518667854664 |

- **Combined OOS gain (stress):** 30.589%
- Full history @ stress: total 31.746%, CAGR 13.972%, benchmark -45.000%, sharpe 0.93, maxdd -0.144, trades 23

### Bull vs Medved (2510) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.26795408756560235 | 0.11837494351764022 |
| alpha | 0.6580334526449675 | 0.2558982789252321 |
| trades | 15 | 9 |
| winrate | 0.6 | 0.5555555555555556 |
| sharpe | 1.1558098889024622 | 1.1382585695130398 |
| maxdd | -0.11414371385645117 | -0.10223175149671782 |
| pf | 3.3779285492539506 | 2.4853279373918236 |
| ann | 0.18260728129749748 | 0.16809296332102597 |

- **Combined OOS gain (stress):** 41.805%
- Full history @ stress: total 43.062%, CAGR 18.515%, benchmark -45.000%, sharpe 1.17, maxdd -0.114, trades 24

### The 20s Breakout (2986) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.08576824049400833 | 0.020616063916180538 |
| alpha | 0.47584760557337347 | 0.1581393993237724 |
| trades | 59 | 29 |
| winrate | 0.3559322033898305 | 0.3448275862068966 |
| sharpe | 0.46034138991346213 | 0.2542916926961849 |
| maxdd | -0.19051398343759463 | -0.12185545504568118 |
| pf | 1.160311543685507 | 1.133121761635599 |
| ann | 0.05985770014177039 | 0.028745508967914946 |

- **Combined OOS gain (stress):** 10.815%
- Full history @ stress: total 11.798%, CAGR 5.432%, benchmark -45.000%, sharpe 0.41, maxdd -0.191, trades 88

### CP Strat ORB (639) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.03652695237960857 | 0.016173529575364443 |
| alpha | 0.4266063174589737 | 0.15369686498295632 |
| trades | 65 | 32 |
| winrate | 0.36923076923076925 | 0.3125 |
| sharpe | 0.24158533075045335 | 0.2197389215774219 |
| maxdd | -0.21139995570501158 | -0.10846926181046324 |
| pf | 1.0692944799733635 | 1.111143596259908 |
| ann | 0.025669348323393626 | 0.02253191510778252 |

- **Combined OOS gain (stress):** 5.329%
- Full history @ stress: total 6.263%, CAGR 2.923%, benchmark -45.000%, sharpe 0.26, maxdd -0.211, trades 97

## 4015

### Up Gap Strategy With Delay (1511) — 1h **(pick)**
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.1960717300280077 | 0.024871700682456144 |
| alpha | 0.41186705817038816 | 0.09298967821054616 |
| trades | 59 | 19 |
| winrate | 0.4406779661016949 | 0.47368421052631576 |
| sharpe | 0.8326044925041237 | 0.45306075207898694 |
| maxdd | -0.15900997623199753 | -0.04809521032349462 |
| pf | 1.372687565920398 | 1.213655461101958 |
| ann | 0.13483808105488704 | 0.03470756643143691 |

- **Combined OOS gain (stress):** 22.582%
- Full history @ stress: total 22.582%, CAGR 10.439%, benchmark -26.196%, sharpe 0.72, maxdd -0.159, trades 78

## 4016

### Expert MACD EURUSD 1 Hour (2431) — Daily
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.08600547529780811 | 0.1419025477978395 |
| alpha | 0.18778247341352006 | 0.15230034000925197 |
| trades | 28 | 12 |
| winrate | 0.32142857142857145 | 0.6666666666666666 |
| sharpe | 0.4240117884755406 | 0.6326664956682486 |
| maxdd | -0.2246828346677241 | -0.4685205061585481 |
| pf | 1.2634803537158095 | 1.9335959371736986 |
| ann | 0.06002129685898949 | 0.2023592513087924 |

- **Combined OOS gain (stress):** 24.011%
- Full history @ stress: total 35.846%, CAGR 12.684%, benchmark 4.901%, sharpe 0.47, maxdd -0.469, trades 47

### Adaptive KDJ (MTF) (492) — Daily **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.13968408985235925 | 0.35125199289068343 |
| alpha | 0.2414610879680712 | 0.3616497851020959 |
| trades | 15 | 9 |
| winrate | 0.6666666666666666 | 0.8888888888888888 |
| sharpe | 0.7133583190959232 | 2.9253064599710306 |
| maxdd | -0.09242400487506408 | -0.061039653060857235 |
| pf | 2.14129656893755 | 42.49682005412575 |
| ann | 0.09677384640096864 | 0.5190233583571306 |

- **Combined OOS gain (stress):** 54.000%
- Full history @ stress: total 51.782%, CAGR 17.663%, benchmark 4.901%, sharpe 1.28, maxdd -0.120, trades 24

## 4017

### Kalman Filter Candles (2152) — Daily **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.02372662992902108 | 0.25273002727617766 |
| alpha | 0.40219929599690485 | 0.1951718877412938 |
| trades | 20 | 10 |
| winrate | 0.3 | 0.5 |
| sharpe | -0.004758269750464726 | 1.721861044984449 |
| maxdd | -0.2117368591068446 | -0.13642060606394502 |
| pf | 1.0913508078539782 | 2.7173923220304905 |
| ann | -0.016821356242134988 | 0.36742287670329277 |

- **Combined OOS gain (stress):** 22.301%
- Full history @ stress: total 23.698%, CAGR 9.713%, benchmark -42.528%, sharpe 0.59, maxdd -0.229, trades 33

### Hercules A.T.C. 2006 (2485) — Daily
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.07914909175887042 | 0.22698603366344017 |
| alpha | 0.5050750176847963 | 0.1694278941285563 |
| trades | 27 | 11 |
| winrate | 0.37037037037037035 | 0.7272727272727273 |
| sharpe | 0.4140884525117447 | 1.9344958164798745 |
| maxdd | -0.15797947238541832 | -0.04450906391204468 |
| pf | 1.252711668495859 | 4.898270725366378 |
| ann | 0.055288905302520286 | 0.32855328337808243 |

- **Combined OOS gain (stress):** 32.410%
- Full history @ stress: total 39.215%, CAGR 15.512%, benchmark -42.528%, sharpe 0.98, maxdd -0.168, trades 41

### 5 EMA No-Touch Breakout (483) — Daily
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.09505296886085435 | 0.21230261703777753 |
| alpha | 0.5209788947867803 | 0.15474447750289366 |
| trades | 29 | 11 |
| winrate | 0.3448275862068966 | 0.7272727272727273 |
| sharpe | 0.46719102849674216 | 1.7718966344916771 |
| maxdd | -0.10155863974670354 | -0.06292924912571074 |
| pf | 1.3146872408310093 | 5.446927424137693 |
| ann | 0.06625263219275168 | 0.3065246781671018 |

- **Combined OOS gain (stress):** 32.754%
- Full history @ stress: total 39.576%, CAGR 15.642%, benchmark -42.528%, sharpe 0.96, maxdd -0.155, trades 43

## 4019

### RSI Buy Sell Force (1264) — Daily
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.09720739282920055 | 0.12328814678080291 |
| alpha | 0.35051865110734626 | 0.2348308770804698 |
| trades | 6 | 11 |
| winrate | 0.6666666666666666 | 0.5454545454545454 |
| sharpe | 0.9735636468561832 | 0.8718294217926561 |
| maxdd | -0.12552348832658577 | -0.15963709584653918 |
| pf | 3.133276558622832 | 1.1678529269132254 |
| ann | 0.0677342307064226 | 0.17522575569693144 |

- **Combined OOS gain (stress):** 23.248%
- Full history @ stress: total 23.111%, CAGR 18.251%, benchmark -33.733%, sharpe 0.91, maxdd -0.160, trades 17

### PSAR Trader v2 (1772) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.1451955967532006 | 0.16930720977246905 |
| alpha | 0.4072561037033232 | 0.2773852042014383 |
| trades | 12 | 12 |
| winrate | 0.5 | 0.5 |
| sharpe | 1.796502400404488 | 1.5519031458819925 |
| maxdd | -0.06162115400056234 | -0.08123237228624458 |
| pf | 2.7473948668669865 | 2.7797594695168177 |
| ann | 0.1005183559013374 | 0.2426194337259362 |

- **Combined OOS gain (stress):** 33.909%
- Full history @ stress: total 33.909%, CAGR 26.545%, benchmark -34.546%, sharpe 1.65, maxdd -0.081, trades 24

### RoNz Rapid-Fire (1923) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.038846354792801074 | 0.18192969988569385 |
| alpha | 0.3009068617429237 | 0.2900076943146631 |
| trades | 9 | 11 |
| winrate | 0.3333333333333333 | 0.5454545454545454 |
| sharpe | 0.5984243128981903 | 1.6794531493773848 |
| maxdd | -0.06365606498516219 | -0.06633404744634619 |
| pf | 1.303989632217239 | 3.3663960744176307 |
| ann | 0.027290262629821704 | 0.26128741765823293 |

- **Combined OOS gain (stress):** 22.784%
- Full history @ stress: total 22.784%, CAGR 17.998%, benchmark -34.546%, sharpe 1.23, maxdd -0.068, trades 20

### JS Signal Baes (3192) — Daily **(pick)**
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.08667027798480076 | 0.18032341490170256 |
| alpha | 0.33998153626294647 | 0.29186614520136944 |
| trades | 6 | 9 |
| winrate | 0.6666666666666666 | 0.4444444444444444 |
| sharpe | 0.9202137527998011 | 1.4110047694275514 |
| maxdd | -0.13647709358799953 | -0.08988634258724326 |
| pf | 1.6431542506444325 | 2.6889912977490757 |
| ann | 0.06047968778825652 | 0.25890748476260605 |

- **Combined OOS gain (stress):** 28.262%
- Full history @ stress: total 28.262%, CAGR 22.225%, benchmark -33.733%, sharpe 1.19, maxdd -0.136, trades 15

### Tweezer Bottom (99) — 4h
> family: pattern | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.028264161174114788 | 0.1592412215396415 |
| alpha | 0.2903246681242374 | 0.26731921596861075 |
| trades | 7 | 9 |
| winrate | 0.42857142857142855 | 0.4444444444444444 |
| sharpe | 0.48708967845978396 | 1.8170541536036475 |
| maxdd | -0.0688588863777615 | -0.0564576834499122 |
| pf | 1.2374228971098287 | 3.3390301360562162 |
| ann | 0.019886220643028363 | 0.22778838845217075 |

- **Combined OOS gain (stress):** 19.201%
- Full history @ stress: total 19.201%, CAGR 15.213%, benchmark -34.546%, sharpe 1.23, maxdd -0.069, trades 16

## 4020

### Parabolic SAR Bug5 (1626) — 1h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.1435835782572068 | 0.4049860871426869 |
| alpha | 0.4978812721775422 | 0.24801824640761816 |
| trades | 46 | 23 |
| winrate | 0.41304347826086957 | 0.5217391304347826 |
| sharpe | 0.5119349628460281 | 2.0630388111104794 |
| maxdd | -0.28897605837005136 | -0.13053959814224925 |
| pf | 1.193689050054403 | 3.1321774896630004 |
| ann | 0.09942370135001832 | 0.6035571253517655 |

- **Combined OOS gain (stress):** 60.672%
- Full history @ stress: total 64.940%, CAGR 26.791%, benchmark -20.807%, sharpe 1.08, maxdd -0.289, trades 69

### Explosion Range Expansion (3263) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.4710285426440102 | 0.36701068792235425 |
| alpha | 0.8219242223068132 | 0.19841053324331326 |
| trades | 68 | 29 |
| winrate | 0.4264705882352941 | 0.3793103448275862 |
| sharpe | 1.5548756593083082 | 2.115876470443701 |
| maxdd | -0.09527548392364316 | -0.08551295941157921 |
| pf | 1.7115738879364286 | 2.4516817955061736 |
| ann | 0.3134722521625466 | 0.5436817055016419 |

- **Combined OOS gain (stress):** 101.091%
- Full history @ stress: total 102.922%, CAGR 39.888%, benchmark -20.390%, sharpe 1.78, maxdd -0.095, trades 97

### Fast Slow RVI Crossover (3520) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.020621974371592522 | 0.40156719388560425 |
| alpha | 0.3302737052912105 | 0.23296703920656325 |
| trades | 60 | 23 |
| winrate | 0.45 | 0.5217391304347826 |
| sharpe | 0.03357271135862143 | 2.195734492644163 |
| maxdd | -0.19304957686215218 | -0.084664708056993 |
| pf | 0.9718360186906104 | 3.4468268339958836 |
| ann | -0.014613495695881218 | 0.5981405243715625 |

- **Combined OOS gain (stress):** 37.266%
- Full history @ stress: total 38.516%, CAGR 16.713%, benchmark -20.390%, sharpe 0.82, maxdd -0.193, trades 83

### Alert MACD Slow (3923) — 4h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.24419961522560518 | 0.42107440139725205 |
| alpha | 0.5950952948884082 | 0.25247424671821106 |
| trades | 41 | 19 |
| winrate | 0.4634146341463415 | 0.5263157894736842 |
| sharpe | 0.8318341634822093 | 2.2752976671358764 |
| maxdd | -0.17952874086648252 | -0.05490596120216573 |
| pf | 1.388002766138515 | 3.980333449788195 |
| ann | 0.16691145233793114 | 0.6291147703921394 |

- **Combined OOS gain (stress):** 76.810%
- Full history @ stress: total 78.420%, CAGR 31.605%, benchmark -20.390%, sharpe 1.35, maxdd -0.183, trades 60

### 5 EMA No-Touch Breakout (483) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.04615755392999166 | 0.3685606122643674 |
| alpha | 0.30473812573281134 | 0.19996045758532643 |
| trades | 72 | 33 |
| winrate | 0.3611111111111111 | 0.3939393939393939 |
| sharpe | -0.07677179968757879 | 2.1639792473953 |
| maxdd | -0.25086150175317323 | -0.0900747891695729 |
| pf | 0.939205337645029 | 2.3685996584221263 |
| ann | -0.03283478956440089 | 0.5461129380944143 |

- **Combined OOS gain (stress):** 30.539%
- Full history @ stress: total 31.728%, CAGR 13.964%, benchmark -20.390%, sharpe 0.75, maxdd -0.251, trades 105

## 4021

### Timer (1788) — 4h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.6010226232476026 | 0.23101884145650442 |
| alpha | 0.5459604562849028 | 0.4210349445160857 |
| trades | 20 | 9 |
| winrate | 0.5 | 0.5555555555555556 |
| sharpe | 1.3836832643248858 | 1.2514599563216482 |
| maxdd | -0.23679296366696345 | -0.11431775582151582 |
| pf | 2.4373663431195953 | 2.1582748522663158 |
| ann | 0.39444908119283006 | 0.3346214648797958 |

- **Combined OOS gain (stress):** 97.089%
- Full history @ stress: total 106.087%, CAGR 40.919%, benchmark -10.657%, sharpe 1.41, maxdd -0.243, trades 29

### The 20s Breakout (2986) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.4057203980316064 | 0.20530324584504744 |
| alpha | 0.3506582310689066 | 0.3953193489046287 |
| trades | 51 | 33 |
| winrate | 0.39215686274509803 | 0.5151515151515151 |
| sharpe | 1.216730667742511 | 1.347280227301736 |
| maxdd | -0.1436789983097463 | -0.061954194421891096 |
| pf | 1.7214620582353573 | 1.9620333565494772 |
| ann | 0.27200143766904805 | 0.29606033917786556 |

- **Combined OOS gain (stress):** 69.432%
- Full history @ stress: total 72.775%, CAGR 29.613%, benchmark -10.657%, sharpe 1.30, maxdd -0.144, trades 84

### 5 EMA No-Touch Breakout (483) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.39887890602680676 | 0.249747756371703 |
| alpha | 0.3438167390641069 | 0.43976385943128427 |
| trades | 55 | 34 |
| winrate | 0.38181818181818183 | 0.5294117647058824 |
| sharpe | 1.1646571744688583 | 1.5910075219288242 |
| maxdd | -0.17307330823400502 | -0.07099934868006141 |
| pf | 1.665496070642718 | 2.0863317247815103 |
| ann | 0.26762470617571066 | 0.36290404883948035 |

- **Combined OOS gain (stress):** 74.825%
- Full history @ stress: total 78.274%, CAGR 31.554%, benchmark -10.657%, sharpe 1.34, maxdd -0.173, trades 89

### CP Strat ORB (639) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.3785773413900071 | 0.2242774321661991 |
| alpha | 0.32351517442730726 | 0.4142935352257804 |
| trades | 52 | 33 |
| winrate | 0.40384615384615385 | 0.5454545454545454 |
| sharpe | 1.12128086621085 | 1.4138856986805615 |
| maxdd | -0.1730734764584666 | -0.0709990744368375 |
| pf | 1.6249814145016044 | 1.8837267691316937 |
| ann | 0.25459994987142553 | 0.32448198944734297 |

- **Combined OOS gain (stress):** 68.776%
- Full history @ stress: total 72.106%, CAGR 29.375%, benchmark -10.657%, sharpe 1.25, maxdd -0.173, trades 85

### Futures Engulfing Candle Size (823) — 4h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.3474946202860101 | 0.17673409151767583 |
| alpha | 0.29243245332331025 | 0.3667501945772571 |
| trades | 63 | 30 |
| winrate | 0.42857142857142855 | 0.5333333333333333 |
| sharpe | 0.9887130043491178 | 1.1347542939050599 |
| maxdd | -0.13207830708708734 | -0.11729407617203358 |
| pf | 1.4843451873544766 | 1.5578646844303015 |
| ann | 0.23454869045278026 | 0.2535939577339037 |

- **Combined OOS gain (stress):** 58.564%
- Full history @ stress: total 58.564%, CAGR 24.442%, benchmark -10.657%, sharpe 1.03, maxdd -0.143, trades 93

## 4030

### Timer (1788) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.8212389810188025 | 0.4728964510380811 |
| alpha | 0.28186153587507046 | 0.2673144224472028 |
| trades | 20 | 10 |
| winrate | 0.45 | 0.5 |
| sharpe | 1.617187242458246 | 2.423685016074757 |
| maxdd | -0.0863211643079479 | -0.08031864833542413 |
| pf | 4.771824407676666 | 5.109561614689658 |
| ann | 0.5273689347247681 | 0.7122010525211928 |

- **Combined OOS gain (stress):** 168.250%
- Full history @ stress: total 168.250%, CAGR 59.690%, benchmark 88.276%, sharpe 1.84, maxdd -0.086, trades 30

### Bull vs Medved (2510) — 4h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.8196275394098591 | 0.6563022259802205 |
| alpha | 0.280250094266127 | 0.4507201973893422 |
| trades | 23 | 8 |
| winrate | 0.391304347826087 | 0.625 |
| sharpe | 1.6179908594027517 | 3.431694500563807 |
| maxdd | -0.12378206887404652 | -0.06320685925800884 |
| pf | 4.317692998449126 | 11.991990599532938 |
| ann | 0.5264140571728888 | 1.0152892587834468 |

- **Combined OOS gain (stress):** 201.385%
- Full history @ stress: total 201.385%, CAGR 68.761%, benchmark 88.276%, sharpe 2.09, maxdd -0.124, trades 31

### Demo GPT - Day Trading Scalping (675) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.8093924869599249 | 0.33262321252442906 |
| alpha | 0.27001504181619285 | 0.1270411839335508 |
| trades | 39 | 31 |
| winrate | 0.4358974358974359 | 0.5161290322580645 |
| sharpe | 1.5471641164656469 | 1.7496176203183524 |
| maxdd | -0.12151289707728807 | -0.0960750458760844 |
| pf | 3.264065087272631 | 2.155768507127793 |
| ann | 0.5203433561805748 | 0.4900179983719395 |

- **Combined OOS gain (stress):** 141.124%
- Full history @ stress: total 143.412%, CAGR 52.497%, benchmark 88.276%, sharpe 1.61, maxdd -0.122, trades 70

### Long Explosive V1 (992) — 4h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 1.0605498156937525 | 0.2898530811339395 |
| alpha | 0.5211723705500204 | 0.08427105254306122 |
| trades | 44 | 27 |
| winrate | 0.4772727272727273 | 0.5185185185185185 |
| sharpe | 1.9132111990557705 | 1.5634052021884568 |
| maxdd | -0.10634210771721297 | -0.10327649414144846 |
| pf | 3.9118290434064655 | 1.8160992054724678 |
| ann | 0.6665666865881255 | 0.424021162725956 |

- **Combined OOS gain (stress):** 165.781%
- Full history @ stress: total 165.781%, CAGR 58.991%, benchmark 88.276%, sharpe 1.80, maxdd -0.106, trades 71

## 4031

### PowerZone (1179) — 1h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.050565551689203625 | -0.017941470743345733 |
| alpha | 0.30272117734640647 | 0.4135653785717227 |
| trades | 30 | 12 |
| winrate | 0.4 | 0.5 |
| sharpe | 0.3423755572226052 | -0.1318030421765557 |
| maxdd | -0.07828031331168983 | -0.08517701909465913 |
| pf | 1.1869768879484368 | 0.8434188419802305 |
| ann | 0.03546404841791628 | -0.024829592759438635 |

- **Combined OOS gain (stress):** 3.172%
- Full history @ stress: total 3.172%, CAGR 1.492%, benchmark -56.362%, sharpe 0.18, maxdd -0.089, trades 42

### ZeroLag MACD Cross (1627) — Daily
> family: trend | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.11167702521864498 | -0.1729493395825369 |
| alpha | 0.18619531520688704 | 0.258868842235645 |
| trades | 39 | 22 |
| winrate | 0.46153846153846156 | 0.36363636363636365 |
| sharpe | -0.2750560685096124 | -1.1842007694481764 |
| maxdd | -0.22140284207115102 | -0.23115513280822575 |
| pf | 0.7673749142529872 | 0.5247647108074658 |
| ann | -0.08025723242307958 | -0.23180765006956638 |

- **Combined OOS gain (stress):** -26.531%
- Full history @ stress: total 229.038%, CAGR 11.176%, benchmark -62.273%, sharpe 0.57, maxdd -0.416, trades 317

### Polarized Fractal Efficiency (2316) — Daily **(pick)**
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.1509583802684782 | 0.05299452953015549 |
| alpha | 0.4488307206940102 | 0.48481271134833737 |
| trades | 15 | 9 |
| winrate | 0.6666666666666666 | 0.7777777777777778 |
| sharpe | 0.9276321426023665 | 0.6725673852271573 |
| maxdd | -0.0711278012159916 | -0.053002156246364396 |
| pf | 2.613820651399101 | 2.178712197058757 |
| ann | 0.1044279300084674 | 0.07434808308278051 |

- **Combined OOS gain (stress):** 21.195%
- Full history @ stress: total 113.363%, CAGR 6.974%, benchmark -62.273%, sharpe 0.61, maxdd -0.372, trades 115

### Explosion Range Expansion (3263) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.004481348549991049 | 0.0963402100924069 |
| alpha | 0.23406254866628307 | 0.5290903467791209 |
| trades | 64 | 34 |
| winrate | 0.375 | 0.5 |
| sharpe | 0.06080920792698809 | 1.0796363393586759 |
| maxdd | -0.18428724805790597 | -0.07788284528731859 |
| pf | 0.9923776423656465 | 1.583690152751248 |
| ann | -0.003168067984075873 | 0.13625399684405592 |

- **Combined OOS gain (stress):** 9.143%
- Full history @ stress: total 9.143%, CAGR 4.237%, benchmark -55.567%, sharpe 0.35, maxdd -0.229, trades 98

### Futures Engulfing Candle Size (823) — 4h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.0032411216987920932 | 0.10981865244417133 |
| alpha | 0.23530277551748202 | 0.5425687891308854 |
| trades | 59 | 30 |
| winrate | 0.3728813559322034 | 0.4666666666666667 |
| sharpe | 0.0673630497777657 | 1.2524616014525949 |
| maxdd | -0.22041900284987304 | -0.055109093203040804 |
| pf | 0.9948695057563882 | 1.6654521763036516 |
| ann | -0.002290877356795673 | 0.15570035791911518 |

- **Combined OOS gain (stress):** 10.622%
- Full history @ stress: total 10.622%, CAGR 4.905%, benchmark -55.567%, sharpe 0.39, maxdd -0.239, trades 89

## 4040

### Rally Base Drop SND Pivots (1215) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.10469402990760446 | 0.47797570273507817 |
| alpha | 0.570051997575041 | 0.3879961526328286 |
| trades | 30 | 17 |
| winrate | 0.3333333333333333 | 0.47058823529411764 |
| sharpe | 0.5139272719560869 | 2.149130900667514 |
| maxdd | -0.16514032150603453 | -0.1439323423800879 |
| pf | 1.2374939943671153 | 3.1889934866657317 |
| ann | 0.07287617136185398 | 0.7204066004096052 |

- **Combined OOS gain (stress):** 63.271%
- Full history @ stress: total 66.383%, CAGR 27.316%, benchmark -38.453%, sharpe 1.26, maxdd -0.171, trades 47

### True Scalper Profit Lock (2511) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.05566352295760191 | 0.559544861805862 |
| alpha | 0.5210214906250384 | 0.4695653117036125 |
| trades | 14 | 11 |
| winrate | 0.42857142857142855 | 0.45454545454545453 |
| sharpe | 0.6370526747622031 | 2.9179204787232806 |
| maxdd | -0.06901207517681907 | -0.02681095650961174 |
| pf | 1.701198807789997 | 7.680000947309062 |
| ann | 0.03901136687543216 | 0.853669123679689 |

- **Combined OOS gain (stress):** 64.635%
- Full history @ stress: total 64.635%, CAGR 26.680%, benchmark -38.453%, sharpe 1.77, maxdd -0.069, trades 25

### ColorMaRsi Trigger MMRec Duplex (3161) — Daily
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.11327230827834556 | 0.5741179604221585 |
| alpha | 0.5739022295381881 | 0.48968255859102916 |
| trades | 14 | 9 |
| winrate | 0.42857142857142855 | 0.5555555555555556 |
| sharpe | 0.7034271933118302 | 2.839464048155086 |
| maxdd | -0.07818534392017074 | -0.036682925319880266 |
| pf | 1.6564182540406143 | 13.443025826351342 |
| ann | 0.07875531189008345 | 0.8777685887944657 |

- **Combined OOS gain (stress):** 75.242%
- Full history @ stress: total 1028.318%, CAGR 7.452%, benchmark 22.517%, sharpe 0.60, maxdd -0.560, trades 401

### Explosion Range Expansion (3263) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.23386548102520788 | 0.4851712695348718 |
| alpha | 0.6992234486926444 | 0.3951917194326222 |
| trades | 63 | 34 |
| winrate | 0.38095238095238093 | 0.5294117647058824 |
| sharpe | 0.9595244256761206 | 2.11750407004211 |
| maxdd | -0.19623030009839126 | -0.13724546437163387 |
| pf | 1.4484513563900911 | 2.453154691440745 |
| ann | 0.16005573995809597 | 0.7320498365848864 |

- **Combined OOS gain (stress):** 83.250%
- Full history @ stress: total 86.547%, CAGR 34.415%, benchmark -38.453%, sharpe 1.48, maxdd -0.196, trades 97

### Lbs V12 (3880) — 1h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.1158059399656024 | 0.669163701580177 |
| alpha | 0.5830096223591582 | 0.5791841514779275 |
| trades | 28 | 17 |
| winrate | 0.42857142857142855 | 0.5294117647058824 |
| sharpe | 0.51402164066662 | 2.605057605304173 |
| maxdd | -0.18196076643900871 | -0.1636083898891011 |
| pf | 1.2572997540899389 | 4.9431759776421895 |
| ann | 0.08048919480240424 | 1.0370551830258083 |

- **Combined OOS gain (stress):** 86.246%
- Full history @ stress: total 91.001%, CAGR 35.928%, benchmark -38.665%, sharpe 1.46, maxdd -0.233, trades 45

## 4050

### EMA Prediction (2034) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.15908860227801225 | 0.07788927682503055 |
| alpha | 0.21811638005579004 | 0.34188927682503056 |
| trades | 79 | 36 |
| winrate | 0.3924050632911392 | 0.4444444444444444 |
| sharpe | 0.5187965336073969 | 0.5370103188921335 |
| maxdd | -0.2838448138751839 | -0.1817292283718871 |
| pf | 1.1263763303402232 | 1.2009180707714062 |
| ann | 0.10993386083444578 | 0.10978394215463672 |

- **Combined OOS gain (stress):** 24.937%
- Full history @ stress: total 26.342%, CAGR 11.730%, benchmark -28.125%, sharpe 0.54, maxdd -0.289, trades 115

### Big Dog Range Breakout (2496) — 30min **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.6034874510080039 | 0.23444762553001497 |
| alpha | 0.6848433832113937 | 0.4977928212595524 |
| trades | 23 | 12 |
| winrate | 0.391304347826087 | 0.4166666666666667 |
| sharpe | 1.6887268581123225 | 1.5902992456637903 |
| maxdd | -0.10838585278280155 | -0.08138519274482581 |
| pf | 2.830495621606159 | 2.926667502259335 |
| ann | 0.395965409974379 | 0.3397868530884891 |

- **Combined OOS gain (stress):** 97.942%
- Full history @ stress: total 97.942%, CAGR 38.249%, benchmark -29.831%, sharpe 1.65, maxdd -0.108, trades 35

### Plan X (3202) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.5029618325960017 | 0.19438925977871757 |
| alpha | 0.5619896103737795 | 0.4583892597787176 |
| trades | 12 | 8 |
| winrate | 0.4166666666666667 | 0.875 |
| sharpe | 1.5945791681784764 | 1.6909514339780862 |
| maxdd | -0.12392844391162894 | -0.0747630136549583 |
| pf | 4.4061347833996685 | 5.630240068598437 |
| ann | 0.333552550375634 | 0.2797906137160411 |

- **Combined OOS gain (stress):** 79.512%
- Full history @ stress: total 79.512%, CAGR 31.987%, benchmark -28.125%, sharpe 1.61, maxdd -0.124, trades 20

### Macd Pattern Trader v03 (StockSharp port) (3954) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.30088510695600346 | 0.1402548129683061 |
| alpha | 0.35991288473378125 | 0.4042548129683061 |
| trades | 29 | 18 |
| winrate | 0.27586206896551724 | 0.5555555555555556 |
| sharpe | 0.857295296483809 | 0.982732484903974 |
| maxdd | -0.1772482750191008 | -0.11602706644697491 |
| pf | 1.438386000734009 | 1.9608029436430434 |
| ann | 0.2042245929100328 | 0.19995042696271081 |

- **Combined OOS gain (stress):** 48.334%
- Full history @ stress: total 53.965%, CAGR 22.717%, benchmark -28.125%, sharpe 0.96, maxdd -0.177, trades 47

### CP Strat ORB (639) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.5314237527180063 | 0.17640068277017162 |
| alpha | 0.5904515304957841 | 0.44040068277017164 |
| trades | 60 | 31 |
| winrate | 0.4 | 0.45161290322580644 |
| sharpe | 1.4150121521728354 | 1.232749255012996 |
| maxdd | -0.21512112035646458 | -0.12562930366936853 |
| pf | 1.8203807920671302 | 1.8540335630000415 |
| ann | 0.35134464795686426 | 0.2531007088643107 |

- **Combined OOS gain (stress):** 80.157%
- Full history @ stress: total 86.999%, CAGR 34.570%, benchmark -28.125%, sharpe 1.43, maxdd -0.215, trades 91

## 4051

### PowerZone (1179) — 1h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.2033241493104021 | -4.903485867213675e-05 |
| alpha | 0.22048483573785926 | 0.22348037690603373 |
| trades | 21 | 11 |
| winrate | 0.42857142857142855 | 0.45454545454545453 |
| sharpe | 1.0744284581409616 | 0.061080703436088624 |
| maxdd | -0.14391305431102885 | -0.0943608218867682 |
| pf | 1.8544513460803802 | 0.9996020765646285 |
| ann | 0.1396951427963622 | -6.809814224695288e-05 |

- **Combined OOS gain (stress):** 20.327%
- Full history @ stress: total 20.327%, CAGR 9.174%, benchmark -17.629%, sharpe 0.74, maxdd -0.144, trades 32

### Parabolic SAR Bug5 (1626) — 4h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.2996598720984016 | 0.00893173511583445 |
| alpha | 0.3213990025331843 | 0.21613894232304165 |
| trades | 17 | 8 |
| winrate | 0.47058823529411764 | 0.25 |
| sharpe | 1.1223738019167253 | 0.1598225247015899 |
| maxdd | -0.1268689272755451 | -0.07750058700067386 |
| pf | 2.6649061695282263 | 0.9937811976962527 |
| ann | 0.2034231960680255 | 0.012425742175433463 |

- **Combined OOS gain (stress):** 31.127%
- Full history @ stress: total 29.884%, CAGR 13.205%, benchmark -18.012%, sharpe 0.83, maxdd -0.127, trades 25

### Bull vs Medved (2510) — 4h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.28106795242280214 | 0.10941811456657313 |
| alpha | 0.30280708285758484 | 0.31662532177378033 |
| trades | 21 | 8 |
| winrate | 0.6190476190476191 | 0.5 |
| sharpe | 1.0628206863959027 | 0.9887418469572324 |
| maxdd | -0.12929720187693194 | -0.07545110561673785 |
| pf | 2.139152680429506 | 1.6688989008378714 |
| ann | 0.1912352910656081 | 0.15512114155314105 |

- **Combined OOS gain (stress):** 42.124%
- Full history @ stress: total 40.777%, CAGR 17.613%, benchmark -18.012%, sharpe 1.01, maxdd -0.129, trades 29

### Explosion (3261) — 4h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.30023578394200556 | 0.05193594756273501 |
| alpha | 0.32197491437678827 | 0.2591431547699422 |
| trades | 44 | 19 |
| winrate | 0.45454545454545453 | 0.3684210526315789 |
| sharpe | 1.131733088108548 | 0.5494325722872938 |
| maxdd | -0.1202887511101629 | -0.06730699947004681 |
| pf | 1.7119792560495606 | 1.3160568489075262 |
| ann | 0.20379991385018825 | 0.07284842252545265 |

- **Combined OOS gain (stress):** 36.776%
- Full history @ stress: total 36.776%, CAGR 16.016%, benchmark -18.012%, sharpe 0.95, maxdd -0.120, trades 63

### IU Open Equal to High Low (942) — 4h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.19697012264080715 | -0.05505303792811622 |
| alpha | 0.21870925307558986 | 0.15215416927909098 |
| trades | 51 | 29 |
| winrate | 0.37254901960784315 | 0.1724137931034483 |
| sharpe | 0.8548718414295241 | -0.44726574524911766 |
| maxdd | -0.14452800298268353 | -0.16483654746307175 |
| pf | 1.446709534685635 | 0.8002099376256068 |
| ann | 0.1354402171578064 | -0.07562912230117902 |

- **Combined OOS gain (stress):** 13.107%
- Full history @ stress: total 12.035%, CAGR 5.539%, benchmark -18.012%, sharpe 0.41, maxdd -0.165, trades 80

## 4071

### VininI Trend (2049) — 4h
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.21054783391799425 | 0.05655114583323306 |
| alpha | 0.5630327520449693 | 0.6292007184828057 |
| trades | 15 | 5 |
| winrate | 0.4666666666666667 | 0.4 |
| sharpe | 0.6471540768941113 | 0.5864410708216651 |
| maxdd | -0.22154284933226098 | -0.0803633797533495 |
| pf | 1.6918351999248054 | 1.790853577773974 |
| ann | 0.14452442651426267 | 0.07939092378555879 |

- **Combined OOS gain (stress):** 27.901%
- Full history @ stress: total 27.901%, CAGR 12.382%, benchmark -71.273%, sharpe 0.61, maxdd -0.222, trades 20

### ColorMaRsi Trigger MMRec Duplex (3161) — 4h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.3209114120673784 | 0.036756431948765655 |
| alpha | 0.6733963301943534 | 0.6094060045983383 |
| trades | 21 | 10 |
| winrate | 0.47619047619047616 | 0.3 |
| sharpe | 1.1090486425884805 | 0.6545653033624611 |
| maxdd | -0.17288219749115186 | -0.062045105296303915 |
| pf | 2.185172920266353 | 1.4214822133655287 |
| ann | 0.21729211455549247 | 0.05140876212290557 |

- **Combined OOS gain (stress):** 36.946%
- Full history @ stress: total 36.946%, CAGR 16.084%, benchmark -71.273%, sharpe 0.97, maxdd -0.173, trades 31

### Explosion Range Expansion (3263) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.3889649114719842 | -0.02646136184246406 |
| alpha | 0.7414498295989592 | 0.5461882108071086 |
| trades | 69 | 31 |
| winrate | 0.391304347826087 | 0.2903225806451613 |
| sharpe | 1.0428166281890983 | -0.1056890796061552 |
| maxdd | -0.19100127509604237 | -0.215117239100178 |
| pf | 1.5500696968693597 | 0.9661485612079783 |
| ann | 0.26127122434429384 | -0.03655903401875482 |

- **Combined OOS gain (stress):** 35.221%
- Full history @ stress: total 37.253%, CAGR 16.207%, benchmark -71.273%, sharpe 0.75, maxdd -0.215, trades 100

### Straddle Trail v2.40 (3986) — Daily
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.3345860398401641 | -0.007543388762275005 |
| alpha | 0.7183931736051878 | 0.5614221284791043 |
| trades | 11 | 5 |
| winrate | 0.5454545454545454 | 0.4 |
| sharpe | 1.0788883854421254 | 0.00918580131902577 |
| maxdd | -0.16545602739862086 | -0.0886891776490264 |
| pf | 2.6836438492563337 | 0.9254737912834189 |
| ann | 0.22618164678234876 | -0.010460746527025333 |

- **Combined OOS gain (stress):** 32.452%
- Full history @ stress: total 164.251%, CAGR 22.190%, benchmark -41.827%, sharpe 1.03, maxdd -0.221, trades 54

### 80-20 (488) — Daily
> family: pattern | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.10709166747019949 | -0.012561680712877 |
| alpha | 0.27671546629482424 | 0.5564038365285023 |
| trades | 20 | 10 |
| winrate | 0.35 | 0.3 |
| sharpe | -0.13084706212212832 | -0.011232863734966009 |
| maxdd | -0.45039514539194214 | -0.1257351923611587 |
| pf | 0.7859387105176031 | 0.8903885074627895 |
| ann | -0.07690572643144689 | -0.017402742636572377 |

- **Combined OOS gain (stress):** -11.831%
- Full history @ stress: total 232.539%, CAGR 28.122%, benchmark -41.827%, sharpe 1.08, maxdd -0.463, trades 68

## 4080

### The 20s Breakout (2986) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.0763826049632057 | 0.11381446941076101 |
| alpha | 0.47162777583987736 | 0.1914615282342904 |
| trades | 45 | 22 |
| winrate | 0.4 | 0.45454545454545453 |
| sharpe | 0.40414881328468816 | 1.0755791712433227 |
| maxdd | -0.1618786506300306 | -0.07194718241339049 |
| pf | 1.1395072769261299 | 1.5434469515498939 |
| ann | 0.053376932319206594 | 0.16148314126204122 |

- **Combined OOS gain (stress):** 19.889%
- Full history @ stress: total 19.714%, CAGR 8.910%, benchmark -41.753%, sharpe 0.61, maxdd -0.162, trades 67

### Fast Slow RVI Crossover (3520) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.06292738738839454 | 0.08269664464187287 |
| alpha | 0.3323177834882771 | 0.16034370346540228 |
| trades | 58 | 29 |
| winrate | 0.29310344827586204 | 0.4827586206896552 |
| sharpe | -0.14125635491066826 | 0.6813598151254494 |
| maxdd | -0.23610933727770989 | -0.09009527878546952 |
| pf | 0.9181617445036014 | 1.27134927117685 |
| ann | -0.04487905042605311 | 0.11666384229625937 |

- **Combined OOS gain (stress):** 1.457%
- Full history @ stress: total 1.308%, CAGR 0.618%, benchmark -41.753%, sharpe 0.13, maxdd -0.270, trades 87

### Rubberbands 3 (4116) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.0740569957175935 | 0.06639652366033633 |
| alpha | 0.32118817515907816 | 0.14404358248386573 |
| trades | 59 | 25 |
| winrate | 0.3389830508474576 | 0.4 |
| sharpe | -0.2565922779615312 | 0.6499040310149148 |
| maxdd | -0.17282349715846335 | -0.07746668076814589 |
| pf | 0.8885157259717142 | 1.2753222993357238 |
| ann | -0.05290737517276334 | 0.09338485043790934 |

- **Combined OOS gain (stress):** -1.258%
- Full history @ stress: total -1.402%, CAGR -0.668%, benchmark -41.753%, sharpe 0.04, maxdd -0.189, trades 84

### 5 EMA No-Touch Breakout (483) — 4h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.02190778206799393 | 0.11578129484633015 |
| alpha | 0.37333738880867773 | 0.19342835366985955 |
| trades | 56 | 22 |
| winrate | 0.35714285714285715 | 0.45454545454545453 |
| sharpe | -0.034828338791683726 | 1.0789025358557887 |
| maxdd | -0.1519168888747926 | -0.06702445043790939 |
| pf | 0.9642276291020803 | 1.6008774930271201 |
| ann | -0.01552764193230205 | 0.16433251453619735 |

- **Combined OOS gain (stress):** 9.134%
- Full history @ stress: total 8.974%, CAGR 4.161%, benchmark -41.753%, sharpe 0.35, maxdd -0.172, trades 78

### CP Strat ORB (639) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.042163828607994835 | 0.07846710468440987 |
| alpha | 0.3530813422686768 | 0.15611416350793927 |
| trades | 53 | 24 |
| winrate | 0.33962264150943394 | 0.4166666666666667 |
| sharpe | -0.15290032909576054 | 0.7526127234286343 |
| maxdd | -0.1825967173301325 | -0.06840193450193255 |
| pf | 0.9261490527206173 | 1.3427600277563807 |
| ann | -0.029975649524787817 | 0.11061025116419465 |

- **Combined OOS gain (stress):** 3.299%
- Full history @ stress: total 3.149%, CAGR 1.481%, benchmark -41.753%, sharpe 0.17, maxdd -0.183, trades 77

## 4081

### Bull vs Medved (2510) — 1h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.18209491012760792 | -0.05975779196143072 |
| alpha | 0.21821047995104303 | 0.1466304144267757 |
| trades | 57 | 26 |
| winrate | 0.40350877192982454 | 0.34615384615384615 |
| sharpe | 0.7871214923222613 | -0.5568417474421467 |
| maxdd | -0.13573091223226075 | -0.16060645446326505 |
| pf | 1.3006019063773149 | 0.784920081987729 |
| ann | 0.12545311586612984 | -0.08201453922038604 |

- **Combined OOS gain (stress):** 11.146%
- Full history @ stress: total 13.004%, CAGR 5.978%, benchmark -22.231%, sharpe 0.44, maxdd -0.224, trades 83

### e-TurboFx Classic (3760) — 4h **(pick)**
> family: momentum | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.1214591412608017 | -0.0004648093840187162 |
| alpha | 0.17875898427493042 | 0.2065728338238373 |
| trades | 10 | 7 |
| winrate | 0.7 | 0.2857142857142857 |
| sharpe | 0.6973794772304045 | 0.0442812398887549 |
| maxdd | -0.0916070169405152 | -0.054148049205014925 |
| pf | 5.025255718712003 | 0.4713489226086647 |
| ann | 0.08435378592372667 | -0.0006454611647717101 |

- **Combined OOS gain (stress):** 12.094%
- Full history @ stress: total 14.062%, CAGR 6.449%, benchmark -23.940%, sharpe 0.57, maxdd -0.108, trades 17

### Lbs V12 (3880) — 1h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.25623200742720487 | -0.04809362913796156 |
| alpha | 0.29234757725064 | 0.15829457725024487 |
| trades | 30 | 18 |
| winrate | 0.3333333333333333 | 0.3888888888888889 |
| sharpe | 1.021396496062692 | -0.4630717324371644 |
| maxdd | -0.1757169464535715 | -0.1622745801348725 |
| pf | 1.797259832454287 | 0.7820434200183699 |
| ann | 0.1748727751526813 | -0.06616095251719833 |

- **Combined OOS gain (stress):** 19.582%
- Full history @ stress: total 21.581%, CAGR 9.726%, benchmark -22.231%, sharpe 0.65, maxdd -0.200, trades 48

### Adaptive KDJ (MTF) (492) — Daily
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.15383620741064874 | -0.03900038517742699 |
| alpha | 0.2340177505271389 | 0.16738782121077944 |
| trades | 19 | 5 |
| winrate | 0.42105263157894735 | 0.4 |
| sharpe | 0.8350872237112199 | -0.4974516480468339 |
| maxdd | -0.1449305137935808 | -0.11271702669259753 |
| pf | 1.6521310428155473 | 0.46320182298762597 |
| ann | 0.10637814694233705 | -0.05374913810156556 |

- **Combined OOS gain (stress):** 10.884%
- Full history @ stress: total 37.471%, CAGR 6.811%, benchmark -60.415%, sharpe 0.54, maxdd -0.145, trades 46

## 4082

### Fast Slow RVI Crossover (3520) — Daily
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.05904081672051431 | 0.018135122767849676 |
| alpha | 0.18085899853869614 | 0.16689545334636202 |
| trades | 17 | 14 |
| winrate | 0.5882352941176471 | 0.35714285714285715 |
| sharpe | 0.4110835943471657 | 0.23597384217921638 |
| maxdd | -0.1251017166535794 | -0.1625442586451925 |
| pf | 1.3048824590020702 | 1.1042737357169095 |
| ann | 0.04135861838603394 | 0.025274217166593616 |

- **Combined OOS gain (stress):** 7.825%
- Full history @ stress: total 21.514%, CAGR 6.174%, benchmark -44.846%, sharpe 0.53, maxdd -0.250, trades 40

### SwingTrader (3601) — Daily
> family: mean_reversion | params: `{}` | flags: thin_trades;win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | 0.05127480829330833 | -0.11115216823754503 |
| alpha | 0.17309299011149015 | 0.03760816234096731 |
| trades | 11 | 5 |
| winrate | 0.6363636363636364 | 0.2 |
| sharpe | 0.33495769867578795 | -1.0500691960385256 |
| maxdd | -0.08764338009807182 | -0.14428427280919698 |
| pf | 2.915864384891788 | 0.011287706571793028 |
| ann | 0.03595787210607049 | -0.1509517457962889 |

- **Combined OOS gain (stress):** -6.558%
- Full history @ stress: total -30.545%, CAGR -10.601%, benchmark -44.846%, sharpe -0.74, maxdd -0.332, trades 25

### Manual EA (3936) — 15min **(pick)**
> family: mean_reversion | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.06401003597360155 | 0.05563863086783005 |
| alpha | 0.18095294573419085 | 0.20877326601685375 |
| trades | 14 | 13 |
| winrate | 0.42857142857142855 | 0.5384615384615384 |
| sharpe | 0.3530008365505524 | 0.43212908051550597 |
| maxdd | -0.17463138707566883 | -0.11226192327171136 |
| pf | 1.359247008564861 | 1.289884198150908 |
| ann | 0.04480828314389851 | 0.07809646038628482 |

- **Combined OOS gain (stress):** 12.321%
- Full history @ stress: total 12.321%, CAGR 5.830%, benchmark -24.125%, sharpe 0.38, maxdd -0.246, trades 27

### 80-20 (488) — Daily
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.04442859434413737 | 0.13286339722288965 |
| alpha | 0.1662467761623192 | 0.281623727801402 |
| trades | 17 | 8 |
| winrate | 0.5882352941176471 | 0.625 |
| sharpe | 0.2811773987070282 | 0.9838590942706257 |
| maxdd | -0.1581411679907626 | -0.09689064402380032 |
| pf | 1.2000424799114413 | 1.9063891369471433 |
| ann | 0.031187063087695366 | 0.18916157648014376 |

- **Combined OOS gain (stress):** 18.319%
- Full history @ stress: total 13.925%, CAGR 4.090%, benchmark -44.846%, sharpe 0.33, maxdd -0.190, trades 34

## 4083

### PSAR Trader v2 (1772) — Daily
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.09153237681321325 | -0.016044217465326138 |
| alpha | 0.18885230688314336 | 0.44769624054994095 |
| trades | 17 | 8 |
| winrate | 0.29411764705882354 | 0.125 |
| sharpe | 0.539544593658786 | -0.17169086284134114 |
| maxdd | -0.1396927940984578 | -0.08759776903944438 |
| pf | 1.48175081065165 | 0.8118726100103204 |
| ann | 0.06382967620557967 | -0.022212217858871064 |

- **Combined OOS gain (stress):** 7.402%
- Full history @ stress: total 7.402%, CAGR 4.050%, benchmark -50.874%, sharpe 0.33, maxdd -0.161, trades 25

### Polarized Fractal Efficiency (2316) — Daily
> family: momentum | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | 0.14150459645702917 | -0.1442350529700379 |
| alpha | 0.2388245265269593 | 0.3195054050452292 |
| trades | 9 | 9 |
| winrate | 0.7777777777777778 | 0.3333333333333333 |
| sharpe | 1.2375869962938764 | -1.3799390313466224 |
| maxdd | -0.05069890049469017 | -0.1442350529700379 |
| pf | 3.1954760020144963 | 0.26649169096967235 |
| ann | 0.09801128251469415 | -0.19451946078487936 |

- **Combined OOS gain (stress):** -2.314%
- Full history @ stress: total -1.354%, CAGR -0.755%, benchmark -50.874%, sharpe 0.00, maxdd -0.144, trades 18

### KDJ Expert Advisor (2716) — 1h **(pick)**
> family: momentum | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.32273104593229296 | 1.25194367493329 |
| alpha | 0.4369495774008245 | 1.7105178560508236 |
| trades | 6 | 8 |
| winrate | 0.5 | 0.125 |
| sharpe | 1.2536149395293563 | 1.0151387418229973 |
| maxdd | -0.16910440427220874 | -0.21853219888739106 |
| pf | 5.821458717307386 | 3.4480748778828767 |
| ann | 0.21847656542292349 | 2.0876352528969866 |

- **Combined OOS gain (stress):** 197.872%
- Full history @ stress: total 197.872%, CAGR 83.455%, benchmark -50.874%, sharpe 0.75, maxdd -0.219, trades 14

### Gold Scalping BOS & CHoCH (849) — 30min
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.084918430723111 | 0.012019380341533159 |
| alpha | 0.19913696219164256 | 0.47059356145906683 |
| trades | 23 | 9 |
| winrate | 0.391304347826087 | 0.2222222222222222 |
| sharpe | 0.7554451588050707 | 0.23788749064629525 |
| maxdd | -0.09278558070104403 | -0.06817831154850007 |
| pf | 1.425108250606178 | 1.1495485138531576 |
| ann | 0.059271586638800944 | 0.016731220328314533 |

- **Combined OOS gain (stress):** 9.796%
- Full history @ stress: total 9.796%, CAGR 5.333%, benchmark -50.874%, sharpe 0.57, maxdd -0.117, trades 32

## 4090

### Timer (1788) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.3429340075593188 | 1.4925226547000916 |
| alpha | 0.6391412352487728 | 0.44171047425576804 |
| trades | 17 | 12 |
| winrate | 0.5294117647058824 | 0.4166666666666667 |
| sharpe | 1.3249132109663055 | 1.4606555487258726 |
| maxdd | -0.16774395820886656 | -0.08653641932503475 |
| pf | 2.4033310504607615 | 4.730366979269428 |
| ann | 0.23159530561936936 | 2.555050433470428 |

- **Combined OOS gain (stress):** 234.729%
- Full history @ stress: total 234.729%, CAGR 77.374%, benchmark 48.805%, sharpe 1.05, maxdd -0.168, trades 29

### Last Price (2126) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.06672336833917525 | 1.3319453443921976 |
| alpha | 0.3629305960286292 | 0.281133163947874 |
| trades | 36 | 24 |
| winrate | 0.3888888888888889 | 0.4166666666666667 |
| sharpe | 0.34885926099809883 | 1.3807538694040757 |
| maxdd | -0.17601934717661094 | -0.10958786622890793 |
| pf | 1.1724055947408583 | 4.864104459419345 |
| ann | 0.0466898998982328 | 2.241015563797487 |

- **Combined OOS gain (stress):** 148.754%
- Full history @ stress: total 156.490%, CAGR 56.330%, benchmark 48.805%, sharpe 0.87, maxdd -0.176, trades 60

### Bollinger K-Means Cluster (319) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.20483022275612628 | 1.4620204481860148 |
| alpha | 0.5010374504455802 | 0.4112082677416913 |
| trades | 19 | 9 |
| winrate | 0.3157894736842105 | 0.5555555555555556 |
| sharpe | 0.9549840263188039 | 1.4466988818717572 |
| maxdd | -0.19543126932795896 | -0.08562659391796723 |
| pf | 1.8089280027407821 | 10.746163343001681 |
| ann | 0.1407027056792347 | 2.4947756815244917 |

- **Combined OOS gain (stress):** 196.632%
- Full history @ stress: total 196.632%, CAGR 67.493%, benchmark 48.805%, sharpe 0.97, maxdd -0.195, trades 28

### Anands (521) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.10089799703830771 | 1.3319564223495561 |
| alpha | 0.39710522472776166 | 0.2811442419052326 |
| trades | 36 | 24 |
| winrate | 0.3888888888888889 | 0.4166666666666667 |
| sharpe | 0.4781977304315509 | 1.3807498675484216 |
| maxdd | -0.17601934717661094 | -0.10958828991578373 |
| pf | 1.2619047170332531 | 4.864110549399983 |
| ann | 0.07027027867791613 | 2.241036946240121 |

- **Combined OOS gain (stress):** 156.725%
- Full history @ stress: total 164.708%, CAGR 58.687%, benchmark 48.805%, sharpe 0.89, maxdd -0.176, trades 60

### Long Explosive V1 (992) — 4h **(pick)**
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.2917260811417617 | 1.6450544622250556 |
| alpha | 0.5879333088312156 | 0.594242281780732 |
| trades | 37 | 21 |
| winrate | 0.4594594594594595 | 0.47619047619047616 |
| sharpe | 1.1290634368956172 | 1.531069657465951 |
| maxdd | -0.12105460068945972 | -0.0931899133332511 |
| pf | 1.520290984197513 | 4.225679531619861 |
| ann | 0.19822851319385548 | 2.8607362294653456 |

- **Combined OOS gain (stress):** 241.669%
- Full history @ stress: total 241.669%, CAGR 79.108%, benchmark 48.805%, sharpe 1.06, maxdd -0.126, trades 58

## 4100

### ZeroLag MACD Cross (1627) — 4h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.2154746856159493 | 0.0966744063321614 |
| alpha | 0.2420742651069676 | 0.13292440633216152 |
| trades | 77 | 40 |
| winrate | 0.38961038961038963 | 0.45 |
| sharpe | 0.6269099532342717 | 0.6890141580107111 |
| maxdd | -0.19887269966262078 | -0.1466215070859619 |
| pf | 1.2612033370486264 | 1.326418703964205 |
| ann | 0.14781334608584573 | 0.13673504864899555 |

- **Combined OOS gain (stress):** 33.298%
- Full history @ stress: total 36.132%, CAGR 15.756%, benchmark -3.162%, sharpe 0.68, maxdd -0.199, trades 117

### Charles 1.3.7 (1747) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.3443514819460789 | 0.06768094582905282 |
| alpha | 0.3709510614370972 | 0.10393094582905293 |
| trades | 107 | 56 |
| winrate | 0.35514018691588783 | 0.375 |
| sharpe | 0.8513270211129805 | 0.491226932095999 |
| maxdd | -0.16199207188370646 | -0.20212221252540463 |
| pf | 1.2962503659022224 | 1.152824306692318 |
| ann | 0.232513555763582 | 0.09521420651371604 |

- **Combined OOS gain (stress):** 43.534%
- Full history @ stress: total 48.181%, CAGR 20.508%, benchmark -3.162%, sharpe 0.79, maxdd -0.202, trades 163

### I Trend (2061) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.04606435210952342 | 0.1463590548277136 |
| alpha | 0.07266393160054174 | 0.18260905482771372 |
| trades | 61 | 30 |
| winrate | 0.3770491803278688 | 0.43333333333333335 |
| sharpe | 0.2488622708250739 | 1.0366388581371704 |
| maxdd | -0.23413860434943112 | -0.11204796470537226 |
| pf | 1.0790926004245622 | 1.5735178876708105 |
| ann | 0.03232777928190678 | 0.20888098967141633 |

- **Combined OOS gain (stress):** 19.917%
- Full history @ stress: total 23.800%, CAGR 10.658%, benchmark -3.162%, sharpe 0.52, maxdd -0.234, trades 91

### Long Explosive V1 (992) — 4h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.07353542151855885 | 0.08480620708037812 |
| alpha | 0.10013500100957717 | 0.12105620708037823 |
| trades | 56 | 30 |
| winrate | 0.35714285714285715 | 0.5 |
| sharpe | 0.35150668358044623 | 0.6644687890939389 |
| maxdd | -0.23106034806567588 | -0.1214375893776366 |
| pf | 1.1204235771612592 | 1.2820932682500399 |
| ann | 0.05140768157788633 | 0.11968662493955762 |

- **Combined OOS gain (stress):** 16.458%
- Full history @ stress: total 17.199%, CAGR 7.819%, benchmark -3.162%, sharpe 0.47, maxdd -0.231, trades 86

## 4110

### Fractured Fractals (2785) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.044961814690003266 | 0.09577548423364313 |
| alpha | 0.4248319445601332 | 0.16143204989020876 |
| trades | 32 | 16 |
| winrate | 0.3125 | 0.3125 |
| sharpe | 0.2565329707606256 | 0.7767285271840454 |
| maxdd | -0.1627092515573053 | -0.131125371743123 |
| pf | 1.10011580897125 | 1.5443468842561339 |
| ann | 0.03155896855419971 | 0.13544124354985 |

- **Combined OOS gain (stress):** 14.504%
- Full history @ stress: total 14.504%, CAGR 6.636%, benchmark -39.935%, sharpe 0.42, maxdd -0.163, trades 48

### The 20s Breakout (2986) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.23510170549160758 | 0.08882403019421625 |
| alpha | 0.6149718353617375 | 0.1544805958507819 |
| trades | 50 | 22 |
| winrate | 0.38 | 0.3181818181818182 |
| sharpe | 0.8654852622392705 | 0.756485646099296 |
| maxdd | -0.1239071837301926 | -0.128176512273929 |
| pf | 1.4607394731608068 | 1.486732889174558 |
| ann | 0.1608767419727386 | 0.12545006724838226 |

- **Combined OOS gain (stress):** 34.481%
- Full history @ stress: total 36.579%, CAGR 15.936%, benchmark -39.935%, sharpe 0.87, maxdd -0.128, trades 72

### Daily Range (3167) — 1h **(pick)**
> family: breakout | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.16646712884040138 | 0.17446616072028642 |
| alpha | 0.5483441514941231 | 0.24012272637685206 |
| trades | 11 | 6 |
| winrate | 0.45454545454545453 | 0.6666666666666666 |
| sharpe | 0.5406294106461801 | 1.230118144497891 |
| maxdd | -0.21415923712202067 | -0.07324113808831467 |
| pf | 1.4235976578838714 | 3.181046255073937 |
| ann | 0.1149209252189336 | 0.2502398266992305 |

- **Combined OOS gain (stress):** 36.998%
- Full history @ stress: total 36.998%, CAGR 16.105%, benchmark -40.129%, sharpe 0.72, maxdd -0.223, trades 17

### Lbs V12 (3880) — 1h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.1433776863372036 | 0.17435446961717393 |
| alpha | 0.5252547089909253 | 0.24001103527373957 |
| trades | 24 | 10 |
| winrate | 0.4583333333333333 | 0.6 |
| sharpe | 0.4927184056783608 | 1.1517670014831205 |
| maxdd | -0.27302389439009433 | -0.09532062552128828 |
| pf | 1.2224390483683505 | 2.3038052370276905 |
| ann | 0.09928385612372637 | 0.25007470739547966 |

- **Combined OOS gain (stress):** 34.273%
- Full history @ stress: total 36.368%, CAGR 15.851%, benchmark -40.129%, sharpe 0.71, maxdd -0.277, trades 34

### Demo GPT - Day Trading Scalping (675) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.025215565256393013 | 0.14239061497356564 |
| alpha | 0.3546545646137369 | 0.20804718063013128 |
| trades | 56 | 25 |
| winrate | 0.4107142857142857 | 0.48 |
| sharpe | 0.03458020076394892 | 1.135351301653946 |
| maxdd | -0.23911496997872628 | -0.10368315210000201 |
| pf | 0.9628982754885173 | 1.745689420936514 |
| ann | -0.017880936283191207 | 0.20307301649820464 |

- **Combined OOS gain (stress):** 11.358%
- Full history @ stress: total 13.096%, CAGR 6.011%, benchmark -39.935%, sharpe 0.38, maxdd -0.239, trades 81

## 4141

### Color XMUV Time (2621) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.0017075681275919852 | 0.11295802695667168 |
| alpha | 0.32176327113272085 | 0.38173273051398393 |
| trades | 61 | 26 |
| winrate | 0.3442622950819672 | 0.5384615384615384 |
| sharpe | 0.07512755486745294 | 1.1711048692168078 |
| maxdd | -0.1564911536019955 | -0.05332671634096753 |
| pf | 0.9969135841377343 | 1.8115661417158793 |
| ann | -0.001206664743070962 | 0.16024300962186322 |

- **Combined OOS gain (stress):** 11.106%
- Full history @ stress: total 13.200%, CAGR 6.058%, benchmark -47.368%, sharpe 0.45, maxdd -0.156, trades 87

### The 20s Breakout (2986) — 4h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.07400500648240671 | 0.10125751717748077 |
| alpha | 0.39747584574271955 | 0.370032220734793 |
| trades | 56 | 25 |
| winrate | 0.3392857142857143 | 0.52 |
| sharpe | 0.4116012882860281 | 1.1155334209943057 |
| maxdd | -0.15225629696950538 | -0.07274891413213314 |
| pf | 1.1289670529974785 | 1.6800074563798604 |
| ann | 0.05173257487788918 | 0.14333785787887932 |

- **Combined OOS gain (stress):** 18.276%
- Full history @ stress: total 20.506%, CAGR 9.251%, benchmark -47.368%, sharpe 0.68, maxdd -0.152, trades 81

### Rubberbands 3 (4116) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.029832299582392974 | 0.1506517233190503 |
| alpha | 0.29363853967791986 | 0.41942642687636256 |
| trades | 68 | 26 |
| winrate | 0.3235294117647059 | 0.5 |
| sharpe | -0.059031776584733055 | 1.4962210936962594 |
| maxdd | -0.18831594817594532 | -0.07657193774135729 |
| pf | 0.9545144793609621 | 1.86072214017569 |
| ann | -0.021169395818956382 | 0.21517229098407853 |

- **Combined OOS gain (stress):** 11.633%
- Full history @ stress: total 13.737%, CAGR 6.296%, benchmark -47.368%, sharpe 0.48, maxdd -0.188, trades 94

### 5 EMA No-Touch Breakout (483) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.0009021521595923288 | 0.15540888116034357 |
| alpha | 0.3225686871007205 | 0.4241835847176558 |
| trades | 65 | 26 |
| winrate | 0.3230769230769231 | 0.5 |
| sharpe | 0.07228218292578437 | 1.5975681126526455 |
| maxdd | -0.1938729473597658 | -0.07274465970995836 |
| pf | 0.9985040472888161 | 1.9026445912328565 |
| ann | -0.0006374365967767304 | 0.22215501057310316 |

- **Combined OOS gain (stress):** 15.437%
- Full history @ stress: total 17.613%, CAGR 7.999%, benchmark -47.368%, sharpe 0.60, maxdd -0.194, trades 91

### CP Strat ORB (639) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.03072142914039333 | 0.1578454071376969 |
| alpha | 0.2927494101199195 | 0.42662011069500916 |
| trades | 65 | 25 |
| winrate | 0.3076923076923077 | 0.52 |
| sharpe | -0.06882148971954308 | 1.5748444270010273 |
| maxdd | -0.1938729473597658 | -0.06639252514471083 |
| pf | 0.951278840576534 | 1.9511800024413417 |
| ann | -0.021803242017202407 | 0.22573576083274793 |

- **Combined OOS gain (stress):** 12.227%
- Full history @ stress: total 14.343%, CAGR 6.564%, benchmark -47.368%, sharpe 0.50, maxdd -0.194, trades 90

## 4142

### Fisher Cyber Cycle (1946) — Daily
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.9883870958173808 | -0.02098147814654594 |
| alpha | 0.6416378698111889 | 0.1545381523384426 |
| trades | 44 | 18 |
| winrate | 0.5909090909090909 | 0.7222222222222222 |
| sharpe | 1.5053135201742056 | 0.024727891680470876 |
| maxdd | -0.24795024104136965 | -0.18616429849759342 |
| pf | 2.163415932519023 | 0.962265555597565 |
| ann | 0.6251178063803138 | -0.029019367550105035 |

- **Combined OOS gain (stress):** 94.667%
- Full history @ stress: total 725.384%, CAGR 75.400%, benchmark 183.333%, sharpe 1.86, maxdd -0.248, trades 115

### Spasm (2849) — 30min **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.5183701314640035 | 0.09612486616769456 |
| alpha | 0.38046977559211737 | 0.28476122980405827 |
| trades | 25 | 13 |
| winrate | 0.44 | 0.6153846153846154 |
| sharpe | 1.376694905677504 | 0.8390761119037266 |
| maxdd | -0.14374944049683724 | -0.08742087301553947 |
| pf | 2.3409446363986417 | 1.9602114566413666 |
| ann | 0.34319673489835045 | 0.13594405472523063 |

- **Combined OOS gain (stress):** 66.432%
- Full history @ stress: total 66.432%, CAGR 28.200%, benchmark -4.715%, sharpe 1.21, maxdd -0.144, trades 38

### EXP FIBO ZZ (4131) — 1h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.3994978643680027 | 0.08146461736509258 |
| alpha | 0.2615975084961166 | 0.2701009810014563 |
| trades | 33 | 17 |
| winrate | 0.42424242424242425 | 0.5882352941176471 |
| sharpe | 1.0030700176021254 | 0.6569415884420132 |
| maxdd | -0.17297691577505414 | -0.10699008346644512 |
| pf | 1.5582316834986094 | 1.547968461860144 |
| ann | 0.26802093263900795 | 0.11489953446417744 |

- **Combined OOS gain (stress):** 51.351%
- Full history @ stress: total 51.351%, CAGR 22.397%, benchmark -4.715%, sharpe 0.90, maxdd -0.173, trades 50

### Logistic RSI STOCH ROC AO (988) — Daily
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.5987032268015735 | 0.08421008415638953 |
| alpha | 0.25195400079538155 | 0.25972971464137806 |
| trades | 20 | 12 |
| winrate | 0.6 | 0.5 |
| sharpe | 1.192459309149952 | 0.8453058089787461 |
| maxdd | -0.22222144449161763 | -0.08946217337148432 |
| pf | 2.0831074331034554 | 1.949576169877427 |
| ann | 0.3930215939219637 | 0.1188322111908775 |

- **Combined OOS gain (stress):** 73.333%
- Full history @ stress: total 222.708%, CAGR 36.601%, benchmark 183.333%, sharpe 1.27, maxdd -0.229, trades 58

## 4143

### Kalman Filter Candles (2152) — Daily
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.05421672347618456 | 0.14053599299469122 |
| alpha | 0.4704603782985196 | 0.21408217315432632 |
| trades | 21 | 10 |
| winrate | 0.47619047619047616 | 0.7 |
| sharpe | 0.2745133768059072 | 1.1663573056700764 |
| maxdd | -0.1854838511091914 | -0.11056239294907277 |
| pf | 0.7010767695384625 | 1.8516495206311991 |
| ann | 0.03800515322495346 | 0.20036138847485807 |

- **Combined OOS gain (stress):** 20.237%
- Full history @ stress: total 17.731%, CAGR 7.447%, benchmark -33.943%, sharpe 0.41, maxdd -0.286, trades 32

### Hercules A.T.C. 2006 (2485) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.0776442870243953 | 0.13168688473770374 |
| alpha | 0.3660643222471278 | 0.20996255121529872 |
| trades | 38 | 19 |
| winrate | 0.4473684210526316 | 0.42105263157894735 |
| sharpe | -0.27455441867689073 | 1.1617147622958566 |
| maxdd | -0.15229266066257885 | -0.08679179264388259 |
| pf | 0.7900926858806503 | 2.091344168745229 |
| ann | -0.05550108746360005 | 0.1874468034826957 |

- **Combined OOS gain (stress):** 4.382%
- Full history @ stress: total 6.157%, CAGR 2.956%, benchmark -46.192%, sharpe 0.26, maxdd -0.213, trades 57

### Fast Slow RVI Crossover (3520) — Daily **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.0888450332543983 | 0.14856962658405504 |
| alpha | 0.32739862156793675 | 0.22211580674369014 |
| trades | 20 | 11 |
| winrate | 0.4 | 0.45454545454545453 |
| sharpe | -0.28161510102613985 | 1.234237113720361 |
| maxdd | -0.19840987373631547 | -0.10139993631906041 |
| pf | 0.717136841568108 | 1.6844553331191956 |
| ann | -0.06361867619307171 | 0.21211964460327115 |

- **Combined OOS gain (stress):** 4.652%
- Full history @ stress: total 4.652%, CAGR 2.021%, benchmark -33.943%, sharpe 0.20, maxdd -0.240, trades 31

### BONK Long Volatility (598) — Daily
> family: trend | params: `{}` | flags: thin_trades;win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.26549255034961095 | 0.09650879675376678 |
| alpha | 0.1507511044727241 | 0.17005497691340188 |
| trades | 13 | 7 |
| winrate | 0.46153846153846156 | 0.42857142857142855 |
| sharpe | -0.6962195547728587 | 0.8904652615190022 |
| maxdd | -0.37785695828591803 | -0.09951375381947947 |
| pf | 0.23497918428673914 | 1.5560883197362527 |
| ann | -0.19586486090909416 | 0.13649665827183544 |

- **Combined OOS gain (stress):** -19.461%
- Full history @ stress: total -26.563%, CAGR -12.704%, benchmark -33.943%, sharpe -0.44, maxdd -0.471, trades 21

### Hull MA Reversal (89) — Daily
> family: trend | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.23474603305948993 | -0.013143208841792542 |
| alpha | 0.18149762176284512 | 0.06040297131784256 |
| trades | 33 | 12 |
| winrate | 0.3333333333333333 | 0.4166666666666667 |
| sharpe | -0.5075750715245205 | 0.02414102102079631 |
| maxdd | -0.32327613475998085 | -0.16983160269723718 |
| pf | 0.638313236372056 | 0.8650078464526497 |
| ann | -0.1722274722140853 | -0.018206307698350077 |

- **Combined OOS gain (stress):** -24.480%
- Full history @ stress: total -13.577%, CAGR -6.219%, benchmark -33.943%, sharpe -0.09, maxdd -0.375, trades 47

## 4144

### ZeroLag MACD Cross (1627) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 1.2972780271660125 | 0.44420105711230673 |
| alpha | 0.4471339349469923 | 0.3369503018252977 |
| trades | 83 | 38 |
| winrate | 0.37349397590361444 | 0.47368421052631576 |
| sharpe | 0.9463454961662626 | 1.7331450867786626 |
| maxdd | -0.24114707126581592 | -0.17252686274239792 |
| pf | 1.9088917350071561 | 2.062383513861985 |
| ann | 0.7996582562849914 | 0.6660507315424826 |

- **Combined OOS gain (stress):** 231.773%
- Full history @ stress: total 231.773%, CAGR 76.629%, benchmark 111.239%, sharpe 0.99, maxdd -0.241, trades 121

### Charles 1.3.7 (1747) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 1.2518817246280252 | 0.7102730211724746 |
| alpha | 0.40173763240900495 | 0.6030222658854656 |
| trades | 112 | 51 |
| winrate | 0.35714285714285715 | 0.43137254901960786 |
| sharpe | 0.9308651057909421 | 2.413229619119724 |
| maxdd | -0.2293759838395948 | -0.08947177625387992 |
| pf | 1.780037997952091 | 2.019573033682802 |
| ann | 0.7744603096712266 | 1.1070623683776075 |

- **Combined OOS gain (stress):** 285.133%
- Full history @ stress: total 297.180%, CAGR 92.367%, benchmark 111.239%, sharpe 1.09, maxdd -0.229, trades 163

### Bull vs Medved (2510) — 4h **(pick)**
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 1.372589115062004 | 0.6286294813381641 |
| alpha | 0.5224450228429838 | 0.5213787260511551 |
| trades | 22 | 7 |
| winrate | 0.45454545454545453 | 0.7142857142857143 |
| sharpe | 0.9718220826255548 | 2.324954936559038 |
| maxdd | -0.3139238712990787 | -0.14131688876448179 |
| pf | 3.2240706545440903 | 15.805070006182525 |
| ann | 0.8411412123932633 | 0.9686805720316283 |

- **Combined OOS gain (stress):** 286.407%
- Full history @ stress: total 286.407%, CAGR 89.874%, benchmark 111.239%, sharpe 1.09, maxdd -0.314, trades 29

### Explosion Range Expansion (3263) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 1.5789984372100139 | 0.5237690005064357 |
| alpha | 0.7288543449909937 | 0.4165182452194267 |
| trades | 59 | 27 |
| winrate | 0.4576271186440678 | 0.4444444444444444 |
| sharpe | 1.0341737702672162 | 2.1437956907667988 |
| maxdd | -0.18365891402942924 | -0.10698862194524617 |
| pf | 2.899265010964425 | 2.7479840589021256 |
| ann | 0.9529082088558294 | 0.7948784080466691 |

- **Combined OOS gain (stress):** 292.980%
- Full history @ stress: total 305.274%, CAGR 94.216%, benchmark 111.239%, sharpe 1.11, maxdd -0.184, trades 86

### Aftershock Playbook (509) — 4h
> family: volatility | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 1.2986786311940017 | 0.5439925732169326 |
| alpha | 0.4485345389749815 | 0.4367418179299236 |
| trades | 13 | 7 |
| winrate | 0.46153846153846156 | 0.5714285714285714 |
| sharpe | 0.9463884282771778 | 2.1721456172949543 |
| maxdd | -0.2665143227230574 | -0.08674869404446572 |
| pf | 2.832496050135475 | 4.8394221776919215 |
| ann | 0.8004333472709293 | 0.8280467894047359 |

- **Combined OOS gain (stress):** 254.914%
- Full history @ stress: total 254.914%, CAGR 82.369%, benchmark 111.239%, sharpe 1.03, maxdd -0.267, trades 20

## 4145

### Fisher Cyber Cycle (1946) — 4h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.17788544185120814 | 0.45625091842389587 |
| alpha | 0.6697553605503952 | 0.4876234674435037 |
| trades | 65 | 33 |
| winrate | 0.38461538461538464 | 0.5151515151515151 |
| sharpe | 0.517900619471632 | 2.3747888393232834 |
| maxdd | -0.29029370258734377 | -0.10171425833208547 |
| pf | 1.1725762829099255 | 2.4318338452319064 |
| ann | 0.12262022892702484 | 0.685387314047641 |

- **Combined OOS gain (stress):** 71.530%
- Full history @ stress: total 71.754%, CAGR 29.249%, benchmark -49.797%, sharpe 1.00, maxdd -0.290, trades 98

### EMA Prediction (2034) — Daily
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.019857539583431283 | 0.35470058109879465 |
| alpha | 0.5903660141597025 | 0.38455132736745146 |
| trades | 34 | 24 |
| winrate | 0.4411764705882353 | 0.5 |
| sharpe | 0.211938161344539 | 1.8851771066084488 |
| maxdd | -0.31199598436380505 | -0.10883577101996644 |
| pf | 1.1226452399909121 | 1.8221851623709213 |
| ann | 0.013988410037636179 | 0.5244100140191188 |

- **Combined OOS gain (stress):** 38.160%
- Full history @ stress: total -8.274%, CAGR -1.852%, benchmark -50.327%, sharpe 0.10, maxdd -0.556, trades 109

### Hull MA Reversal (89) — Daily
> family: trend | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.37411673428080083 | 0.003235404753811899 |
| alpha | 0.19639174029547035 | 0.0330861510224687 |
| trades | 34 | 18 |
| winrate | 0.4117647058823529 | 0.3888888888888889 |
| sharpe | -0.5737449361681907 | 0.15733223911823904 |
| maxdd | -0.5604009792595914 | -0.17508381096706216 |
| pf | 0.8126608810121325 | 0.8420447530468497 |
| ann | -0.28183096187192214 | 0.004496100114571355 |

- **Combined OOS gain (stress):** -37.209%
- Full history @ stress: total -50.673%, CAGR -14.187%, benchmark -50.327%, sharpe -0.21, maxdd -0.685, trades 110

## 4146

### US Index First 30m Candle (1515) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.28489192250240936 | 0.694193154652299 |
| alpha | 0.32495126968341836 | 0.39764143051436784 |
| trades | 56 | 27 |
| winrate | 0.35714285714285715 | 0.5185185185185185 |
| sharpe | 0.8878066957797703 | 2.7754790208108875 |
| maxdd | -0.17350562433975814 | -0.060642834906552534 |
| pf | 1.4414128340261436 | 3.672081300036718 |
| ann | 0.19374630717967145 | 1.0796003239831617 |

- **Combined OOS gain (stress):** 117.686%
- Full history @ stress: total 117.686%, CAGR 44.627%, benchmark 25.519%, sharpe 1.60, maxdd -0.221, trades 83

### Explosion Range Expansion (3263) — 4h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.327892280843207 | 0.6558667356262107 |
| alpha | 0.367951628024216 | 0.3593150114882795 |
| trades | 54 | 38 |
| winrate | 0.5185185185185185 | 0.4473684210526316 |
| sharpe | 0.9659673500085967 | 2.5593577271118373 |
| maxdd | -0.15923641922484932 | -0.05937104381200342 |
| pf | 1.5046789743943048 | 2.622730914275172 |
| ann | 0.22183355960693873 | 1.0145534099230709 |

- **Combined OOS gain (stress):** 119.881%
- Full history @ stress: total 119.967%, CAGR 45.344%, benchmark 25.519%, sharpe 1.57, maxdd -0.160, trades 92

### Rubberbands 3 (4116) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.15377653930001034 | 0.5127328465726255 |
| alpha | 0.19383588648101935 | 0.21618112243469434 |
| trades | 67 | 31 |
| winrate | 0.34328358208955223 | 0.4838709677419355 |
| sharpe | 0.5444028814561138 | 2.0806168046217635 |
| maxdd | -0.1857962741068916 | -0.11331290912357117 |
| pf | 1.1969600669995366 | 2.400014082070366 |
| ann | 0.1063377261623244 | 0.7768500847204629 |

- **Combined OOS gain (stress):** 74.536%
- Full history @ stress: total 74.536%, CAGR 30.238%, benchmark 25.519%, sharpe 1.13, maxdd -0.232, trades 98

### Futures Engulfing Candle Size (823) — 4h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.3260211918084097 | 0.4910059099086226 |
| alpha | 0.3660805389894187 | 0.1944541857706914 |
| trades | 60 | 36 |
| winrate | 0.45 | 0.4722222222222222 |
| sharpe | 0.8880784838125166 | 1.9763898135540345 |
| maxdd | -0.2085548984056148 | -0.086884898494478 |
| pf | 1.3087545847694715 | 2.01470505601854 |
| ann | 0.22061700055749967 | 0.7415070608319061 |

- **Combined OOS gain (stress):** 97.711%
- Full history @ stress: total 97.711%, CAGR 38.173%, benchmark 25.519%, sharpe 1.29, maxdd -0.233, trades 96

### LSMA Fast And Simple Alternative Calculation (998) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.1953045528504045 | 0.5359082442188783 |
| alpha | 0.2353639000314135 | 0.2393565200809471 |
| trades | 33 | 18 |
| winrate | 0.3333333333333333 | 0.6666666666666666 |
| sharpe | 0.5663641716416353 | 2.0874620739015786 |
| maxdd | -0.24650544963680332 | -0.1346045260390828 |
| pf | 1.3496221424591195 | 2.7459068079554583 |
| ann | 0.13432378532012734 | 0.81476740880145 |

- **Combined OOS gain (stress):** 83.588%
- Full history @ stress: total 85.155%, CAGR 33.939%, benchmark 25.519%, sharpe 1.09, maxdd -0.261, trades 51

## 4147

### Martingale Breakout (3635) — 15min **(pick)**
> family: breakout | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | -0.0009614586823998295 | -0.07239426998715659 |
| alpha | 0.10668441656910921 | 0.2521958939472697 |
| trades | 5 | 38 |
| winrate | 0.4 | 0.2894736842105263 |
| sharpe | -0.0777694021296192 | -1.0227262826357482 |
| maxdd | -0.02056657105934645 | -0.13371695450273557 |
| pf | 0.9641187299260907 | 0.7239059182595041 |
| ann | -0.0006793469170655042 | -0.09910356683879717 |

- **Combined OOS gain (stress):** -7.329%
- Full history @ stress: total -8.455%, CAGR -10.669%, benchmark -37.827%, sharpe -1.08, maxdd -0.134, trades 44

## 4148

### Rally Base Drop SND Pivots (1215) — 4h
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.9731196689144039 | 0.5716427901179328 |
| alpha | 0.573119668914404 | 0.7157604371767563 |
| trades | 24 | 6 |
| winrate | 0.5416666666666666 | 0.6666666666666666 |
| sharpe | 1.763918599751336 | 3.538161295189526 |
| maxdd | -0.14739768941085996 | -0.07157320130038802 |
| pf | 3.3449579211830063 | 10.252678555287568 |
| ann | 0.6162922887597346 | 0.8736692713899412 |

- **Combined OOS gain (stress):** 210.104%
- Full history @ stress: total 210.104%, CAGR 71.059%, benchmark 21.250%, sharpe 2.13, maxdd -0.147, trades 30

### HSI1 First 30m Candle (1413) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 1.2059431528588043 | 0.5120481063059841 |
| alpha | 0.8059431528588044 | 0.6561657533648075 |
| trades | 29 | 9 |
| winrate | 0.4827586206896552 | 0.5555555555555556 |
| sharpe | 1.9974594795699736 | 2.9461800851628004 |
| maxdd | -0.12321080071282853 | -0.0851471059622203 |
| pf | 3.1587434028672585 | 5.433662340989261 |
| ann | 0.7488091076224301 | 0.7757331940208168 |

- **Combined OOS gain (stress):** 233.549%
- Full history @ stress: total 233.549%, CAGR 77.077%, benchmark 21.250%, sharpe 2.20, maxdd -0.123, trades 38

### Anands (521) — 4h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 1.1109177789412041 | 0.55437168804811 |
| alpha | 0.7109177789412042 | 0.6984893351069335 |
| trades | 28 | 8 |
| winrate | 0.5 | 0.625 |
| sharpe | 1.8681410356622756 | 3.2001609480801934 |
| maxdd | -0.12907989644778384 | -0.07251058936700039 |
| pf | 2.9063514074315044 | 7.123414463550322 |
| ann | 0.6952447032627875 | 0.8451352626715671 |

- **Combined OOS gain (stress):** 228.115%
- Full history @ stress: total 228.115%, CAGR 75.702%, benchmark 21.250%, sharpe 2.15, maxdd -0.129, trades 36

### Gann Swing Multi Layer (830) — 4h
> family: other | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.9731196689144039 | 0.5716427901179328 |
| alpha | 0.573119668914404 | 0.7157604371767563 |
| trades | 24 | 6 |
| winrate | 0.5416666666666666 | 0.6666666666666666 |
| sharpe | 1.763918599751336 | 3.538161295189526 |
| maxdd | -0.14739768941085996 | -0.07157320130038802 |
| pf | 3.3449579211830063 | 10.252678555287568 |
| ann | 0.6162922887597346 | 0.8736692713899412 |

- **Combined OOS gain (stress):** 210.104%
- Full history @ stress: total 210.104%, CAGR 71.059%, benchmark 21.250%, sharpe 2.13, maxdd -0.147, trades 30

### IU Open Equal to High Low (942) — 4h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 1.3907032832852106 | 0.4773577515440388 |
| alpha | 0.9907032832852107 | 0.6214753986028623 |
| trades | 60 | 22 |
| winrate | 0.43333333333333335 | 0.45454545454545453 |
| sharpe | 2.033513877474196 | 2.520164264822927 |
| maxdd | -0.13464115348576555 | -0.18656274601651823 |
| pf | 2.106431829400945 | 2.6856335676495227 |
| ann | 0.8510608852494612 | 0.7194077115881363 |

- **Combined OOS gain (stress):** 253.192%
- Full history @ stress: total 257.415%, CAGR 82.977%, benchmark 21.250%, sharpe 2.14, maxdd -0.205, trades 82

## 4160

### Kalman Filter Candles (2152) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.39694995326000626 | 0.3998502673276807 |
| alpha | 0.48895963849003043 | 0.5587044339943474 |
| trades | 41 | 20 |
| winrate | 0.5121951219512195 | 0.55 |
| sharpe | 0.9658675387572558 | 1.8947103639239131 |
| maxdd | -0.18238462245097675 | -0.097709898045099 |
| pf | 1.712394626698954 | 2.6415107169565837 |
| ann | 0.26638955595338665 | 0.5954223095374882 |

- **Combined OOS gain (stress):** 95.552%
- Full history @ stress: total 95.552%, CAGR 37.455%, benchmark -21.792%, sharpe 1.26, maxdd -0.182, trades 61

### Explosion Range Expansion (3263) — 4h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 1.0982101579472094 | 0.44714947336676025 |
| alpha | 1.1902198431772337 | 0.606003640033427 |
| trades | 67 | 36 |
| winrate | 0.43283582089552236 | 0.4722222222222222 |
| sharpe | 1.922488326396302 | 2.0745874088099603 |
| maxdd | -0.16491257156470374 | -0.07931905918287774 |
| pf | 2.417018421915884 | 2.2664498456111715 |
| ann | 0.6880284870538693 | 0.6707763220429943 |

- **Combined OOS gain (stress):** 203.642%
- Full history @ stress: total 204.748%, CAGR 69.651%, benchmark -21.792%, sharpe 1.97, maxdd -0.228, trades 103

### Fast Slow RVI Crossover (3520) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.4376035706852106 | 0.5065184456439427 |
| alpha | 0.5296132559152348 | 0.6653726123106094 |
| trades | 60 | 30 |
| winrate | 0.4166666666666667 | 0.4 |
| sharpe | 0.9577146749053623 | 2.009943941563709 |
| maxdd | -0.15977269902334035 | -0.14303303578248316 |
| pf | 1.6274732865179815 | 2.3258328723121253 |
| ann | 0.2923163913332445 | 0.7667208869702773 |

- **Combined OOS gain (stress):** 116.578%
- Full history @ stress: total 121.796%, CAGR 45.916%, benchmark -21.792%, sharpe 1.33, maxdd -0.160, trades 90

### 5 EMA No-Touch Breakout (483) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.619540627510011 | 0.4122003163863619 |
| alpha | 0.7115503127400352 | 0.5710544830530286 |
| trades | 66 | 33 |
| winrate | 0.4090909090909091 | 0.42424242424242425 |
| sharpe | 1.4195978301635175 | 2.0791358133965545 |
| maxdd | -0.10613553234017892 | -0.09465808421125088 |
| pf | 1.8090327042685033 | 2.3594756469519016 |
| ann | 0.40582443408693103 | 0.6150035446156166 |

- **Combined OOS gain (stress):** 128.712%
- Full history @ stress: total 130.460%, CAGR 48.593%, benchmark -21.792%, sharpe 1.64, maxdd -0.114, trades 99

### Futures Engulfing Candle Size (823) — 4h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.7692859483180108 | 0.4042075703944472 |
| alpha | 0.861295633548035 | 0.563061737061114 |
| trades | 64 | 35 |
| winrate | 0.484375 | 0.4857142857142857 |
| sharpe | 1.4907847835253432 | 1.8117684462170731 |
| maxdd | -0.13532666578303298 | -0.1265787485138984 |
| pf | 1.9527968289840518 | 1.8425254742970043 |
| ann | 0.49645711122482883 | 0.602323259170839 |

- **Combined OOS gain (stress):** 148.444%
- Full history @ stress: total 149.349%, CAGR 54.250%, benchmark -21.792%, sharpe 1.60, maxdd -0.173, trades 99

## 4161

### Hercules A.T.C. 2006 (2485) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.005300020767994407 | 0.12542492112880965 |
| alpha | 0.34628499364122756 | 0.1663731969908785 |
| trades | 46 | 23 |
| winrate | 0.2391304347826087 | 0.5217391304347826 |
| sharpe | 0.03875208844099168 | 1.1244217695474226 |
| maxdd | -0.20643548256560884 | -0.06485488849079801 |
| pf | 0.9868016871174757 | 1.6907015942637245 |
| ann | -0.003747276188137749 | 0.17833162920354773 |

- **Combined OOS gain (stress):** 11.946%
- Full history @ stress: total 11.946%, CAGR 5.499%, benchmark -35.879%, sharpe 0.44, maxdd -0.206, trades 69

### The 20s Breakout (2986) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.019502500375995102 | 0.10677746838258062 |
| alpha | 0.33208251403322686 | 0.14772574424464946 |
| trades | 48 | 28 |
| winrate | 0.22916666666666666 | 0.5 |
| sharpe | -0.017615970511715286 | 0.9080851907124766 |
| maxdd | -0.22903478592733806 | -0.1106794615386203 |
| pf | 0.9579223720066732 | 1.4210096717806897 |
| ann | -0.013817891397071569 | 0.15130454826952855 |

- **Combined OOS gain (stress):** 8.519%
- Full history @ stress: total 8.919%, CAGR 4.136%, benchmark -35.879%, sharpe 0.33, maxdd -0.229, trades 76

### Rubberbands 3 (4116) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.08988185425199469 | 0.1376351378596563 |
| alpha | 0.2617031601572273 | 0.17858341372172515 |
| trades | 56 | 31 |
| winrate | 0.23214285714285715 | 0.45161290322580644 |
| sharpe | -0.34197730794200987 | 1.0263742465481394 |
| maxdd | -0.27371742631383345 | -0.11372994609568277 |
| pf | 0.834530655311104 | 1.5117571829343674 |
| ann | -0.06437157484387501 | 0.19612350850881355 |

- **Combined OOS gain (stress):** 3.538%
- Full history @ stress: total 3.920%, CAGR 1.841%, benchmark -35.879%, sharpe 0.19, maxdd -0.274, trades 87

### 5 EMA No-Touch Breakout (483) — 4h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.00196744195399412 | 0.17972426894167248 |
| alpha | 0.34961757245522784 | 0.22067254480374132 |
| trades | 54 | 29 |
| winrate | 0.2222222222222222 | 0.4827586206896552 |
| sharpe | 0.06539482510899292 | 1.36583926264282 |
| maxdd | -0.22084355773532638 | -0.07736864757104323 |
| pf | 0.995896959768554 | 1.7726145206987711 |
| ann | -0.0013903594629315341 | 0.258020089627198 |

- **Combined OOS gain (stress):** 17.740%
- Full history @ stress: total 18.175%, CAGR 8.243%, benchmark -35.879%, sharpe 0.57, maxdd -0.221, trades 83

### CP Strat ORB (639) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.07816152401079457 | 0.12039835176274472 |
| alpha | 0.2734234903984274 | 0.16134662762481355 |
| trades | 52 | 30 |
| winrate | 0.19230769230769232 | 0.4666666666666667 |
| sharpe | -0.2955277766651576 | 0.9216641990736483 |
| maxdd | -0.26436360138400217 | -0.11372868391369362 |
| pf | 0.8494752841572945 | 1.4485192191381429 |
| ann | -0.055875308350676556 | 0.17102899427194806 |

- **Combined OOS gain (stress):** 3.283%
- Full history @ stress: total 3.664%, CAGR 1.721%, benchmark -35.879%, sharpe 0.18, maxdd -0.264, trades 82

## 4162

### Nadaraya-Watson Envelope (1109) — 4h
> family: other | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.06738073966199609 | 0.22292670733747033 |
| alpha | 0.41139433953546956 | 0.0926622607165104 |
| trades | 37 | 25 |
| winrate | 0.5135135135135135 | 0.48 |
| sharpe | -0.20553237418705236 | 1.5076632308086777 |
| maxdd | -0.21392089250856394 | -0.1262234204773991 |
| pf | 0.8995117515439536 | 1.7619897732131073 |
| ann | -0.048088091523783905 | 0.3224530251801052 |

- **Combined OOS gain (stress):** 14.053%
- Full history @ stress: total 17.973%, CAGR 8.156%, benchmark -39.071%, sharpe 0.52, maxdd -0.214, trades 62

### Bull vs Medved (2510) — 4h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.31331814417000103 | 0.40412188252757564 |
| alpha | 0.7920932233674667 | 0.2738574359066157 |
| trades | 16 | 12 |
| winrate | 0.625 | 0.5833333333333334 |
| sharpe | 1.0957609662572845 | 2.333568847363595 |
| maxdd | -0.19330375080779327 | -0.08976155307505052 |
| pf | 2.507510707825312 | 3.4944830336843142 |
| ann | 0.21234426290823172 | 0.6021874692663891 |

- **Combined OOS gain (stress):** 84.406%
- Full history @ stress: total 84.406%, CAGR 33.681%, benchmark -39.071%, sharpe 1.53, maxdd -0.193, trades 28

### 80-20 (488) — Daily
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.04577275344848308 | 0.3773080129910107 |
| alpha | 0.5421437211904185 | 0.24925327203304382 |
| trades | 20 | 15 |
| winrate | 0.25 | 0.6666666666666666 |
| sharpe | 0.26059736285118246 | 2.0326225846224832 |
| maxdd | -0.2865872129231891 | -0.08292375485578907 |
| pf | 1.0228245815091899 | 3.969061461975157 |
| ann | 0.03212446766809496 | 0.5598542832204778 |

- **Combined OOS gain (stress):** 44.035%
- Full history @ stress: total 243.457%, CAGR 29.642%, benchmark -8.991%, sharpe 1.24, maxdd -0.287, trades 73

### Long Explosive V1 (992) — 4h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.39059326135800543 | 0.26587412909037034 |
| alpha | 0.8693683405554711 | 0.1356096824694104 |
| trades | 44 | 24 |
| winrate | 0.5227272727272727 | 0.5416666666666666 |
| sharpe | 1.5494854305907775 | 1.8846318756532325 |
| maxdd | -0.09592479006495325 | -0.07041494425537764 |
| pf | 1.8874511870589448 | 2.0900476939589767 |
| ann | 0.26231567982167636 | 0.3873890005145799 |

- **Combined OOS gain (stress):** 76.032%
- Full history @ stress: total 79.059%, CAGR 31.829%, benchmark -39.071%, sharpe 1.71, maxdd -0.096, trades 68

## 4163

### Up Gap Strategy With Delay (1511) — 1h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.03218984395199487 | -0.025202517722386464 |
| alpha | 0.44425555219361546 | 0.24568857138652445 |
| trades | 37 | 17 |
| winrate | 0.3783783783783784 | 0.29411764705882354 |
| sharpe | -0.1602523860489013 | -0.33117475106558336 |
| maxdd | -0.13215827869706798 | -0.10699822010465643 |
| pf | 0.8602323157813379 | 0.8698052334754369 |
| ann | -0.022850425195409363 | -0.03482847079683682 |

- **Combined OOS gain (stress):** -5.658%
- Full history @ stress: total -5.954%, CAGR -2.949%, benchmark -60.578%, sharpe -0.23, maxdd -0.192, trades 55

### Consecutive Close High1 Mean Reversion (1601) — 1h
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | -0.007293514049998673 | 0.010318127526887544 |
| alpha | 0.46915188209561165 | 0.28120921663579845 |
| trades | 13 | 6 |
| winrate | 0.3076923076923077 | 0.3333333333333333 |
| sharpe | -0.06705597990793775 | 0.2753624018688774 |
| maxdd | -0.06109651365410995 | -0.04415212485044373 |
| pf | 0.8944390093739918 | 1.2046953431643261 |
| ann | -0.0051582524234269345 | 0.014358324506611897 |

- **Combined OOS gain (stress):** 0.295%
- Full history @ stress: total 0.295%, CAGR 0.144%, benchmark -60.578%, sharpe 0.05, maxdd -0.063, trades 19

### ZeroLag MACD Cross (1627) — Daily
> family: trend | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.26002977068549527 | 0.03145596547127716 |
| alpha | 0.1722796718628552 | 0.3052232238539202 |
| trades | 44 | 18 |
| winrate | 0.25 | 0.5 |
| sharpe | -0.8167799834714634 | 0.4206774083750748 |
| maxdd | -0.3256954017031931 | -0.056882481061315215 |
| pf | 0.590415029679013 | 1.282168321212992 |
| ann | -0.19164426840902615 | 0.043950955148073456 |

- **Combined OOS gain (stress):** -23.675%
- Full history @ stress: total -3.947%, CAGR -0.886%, benchmark -53.155%, sharpe 0.07, maxdd -0.447, trades 135

### Daily BreakPoint (2717) — 30min
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.005826258936000972 | 0.012120283293952872 |
| alpha | 0.48394792382394125 | 0.2830113724028638 |
| trades | 5 | 7 |
| winrate | 0.2 | 0.42857142857142855 |
| sharpe | 0.11821197520294932 | 0.28018982741732035 |
| maxdd | -0.05313114010942166 | -0.03648320828943741 |
| pf | 1.1863131437402656 | 1.2582105969087647 |
| ann | 0.004112622869984595 | 0.016872007828333535 |

- **Combined OOS gain (stress):** 1.802%
- Full history @ stress: total 1.802%, CAGR 0.875%, benchmark -60.704%, sharpe 0.19, maxdd -0.067, trades 12

### Rectangle Test (3627) — 30min **(pick)**
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | -0.031316574451997536 | 0.020530380239292434 |
| alpha | 0.44680509043594274 | 0.29142146934820334 |
| trades | 19 | 7 |
| winrate | 0.3157894736842105 | 0.2857142857142857 |
| sharpe | -0.19546538873522573 | 0.4245030113563378 |
| maxdd | -0.11354986037323667 | -0.040789965571783604 |
| pf | 0.7630068675977172 | 1.6807009933109847 |
| ann | -0.022227606911655484 | 0.02862556703707586 |

- **Combined OOS gain (stress):** -1.143%
- Full history @ stress: total -1.143%, CAGR -0.559%, benchmark -60.704%, sharpe -0.02, maxdd -0.123, trades 26

## 4164

### Smoothing Average (1968) — 30min
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.04135763767999756 | 0.028931922124616705 |
| alpha | 0.2643652538862675 | 0.05926665015808941 |
| trades | 18 | 10 |
| winrate | 0.2777777777777778 | 0.4 |
| sharpe | -0.30930861334537335 | 0.39671176326878305 |
| maxdd | -0.09673043202935838 | -0.0721373316343592 |
| pf | 0.7007701348490186 | 1.2863760714346362 |
| ann | -0.029398915782232304 | 0.040404830906400235 |

- **Combined OOS gain (stress):** -1.362%
- Full history @ stress: total -1.362%, CAGR -0.667%, benchmark -30.196%, sharpe -0.02, maxdd -0.097, trades 28

### ADX System (2449) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.032704785840001804 | -0.0006238710818745608 |
| alpha | 0.3342199373551533 | 0.037757871656714626 |
| trades | 14 | 8 |
| winrate | 0.2857142857142857 | 0.375 |
| sharpe | 0.2871381052865638 | 0.028637327647309627 |
| maxdd | -0.08011135379720513 | -0.07027098105247609 |
| pf | 1.2459836180182766 | 0.9899040059201493 |
| ann | 0.022995902392663803 | -0.0008663166321901672 |

- **Combined OOS gain (stress):** 3.206%
- Full history @ stress: total 3.206%, CAGR 1.551%, benchmark -29.773%, sharpe 0.21, maxdd -0.080, trades 22

### Supertrend Distance Breakout (260) — 4h **(pick)**
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | -0.01871673483199865 | 0.07733914662756258 |
| alpha | 0.28279841668315286 | 0.11572088936615177 |
| trades | 11 | 6 |
| winrate | 0.2727272727272727 | 0.5 |
| sharpe | -0.09141407015000588 | 0.8886486409227843 |
| maxdd | -0.08820813582545639 | -0.08203498999082115 |
| pf | 0.8666025165384849 | 2.2065984701354218 |
| ann | -0.013259611194657461 | 0.10899740154294046 |

- **Combined OOS gain (stress):** 5.717%
- Full history @ stress: total 5.717%, CAGR 2.748%, benchmark -29.773%, sharpe 0.30, maxdd -0.088, trades 17

## 4165

### Gap Momentum System (1401) — 4h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.24048739473200298 | 0.12330055189395517 |
| alpha | 0.193842550214818 | 0.23799320556711867 |
| trades | 16 | 11 |
| winrate | 0.5 | 0.45454545454545453 |
| sharpe | 0.8539585299615333 | 0.9910633335769526 |
| maxdd | -0.1954160174143743 | -0.06350063518782001 |
| pf | 2.3605580351403006 | 2.8071026102624868 |
| ann | 0.16445067875608177 | 0.17524378032296783 |

- **Combined OOS gain (stress):** 39.344%
- Full history @ stress: total 38.579%, CAGR 18.164%, benchmark -3.355%, sharpe 0.87, maxdd -0.195, trades 27

### Stoch TP TS V3103 (1791) — Daily
> family: other | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.25499619469600576 | 0.0831209482923232 |
| alpha | 0.1723448035339763 | 0.197149455419105 |
| trades | 38 | 24 |
| winrate | 0.47368421052631576 | 0.4583333333333333 |
| sharpe | 0.9749345995847905 | 0.6652366383003778 |
| maxdd | -0.14584885758227895 | -0.15820500435344642 |
| pf | 1.5313506611457324 | 1.3333265628439355 |
| ann | 0.17405612498552903 | 0.11727164130639278 |

- **Combined OOS gain (stress):** 35.931%
- Full history @ stress: total 36.278%, CAGR 17.156%, benchmark -3.355%, sharpe 0.87, maxdd -0.158, trades 62

### Bezier ReOpen (2414) — Daily **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.4288276372320037 | 0.09633544526403615 |
| alpha | 0.3461762460699742 | 0.21036395239081795 |
| trades | 20 | 14 |
| winrate | 0.5 | 0.42857142857142855 |
| sharpe | 1.3247943158147004 | 0.6998553289492441 |
| maxdd | -0.18225572264595125 | -0.1696952724247346 |
| pf | 2.902311121276564 | 1.4679210560935814 |
| ann | 0.28673795279544767 | 0.1362471386234283 |

- **Combined OOS gain (stress):** 56.647%
- Full history @ stress: total 57.047%, CAGR 25.974%, benchmark -3.355%, sharpe 1.11, maxdd -0.182, trades 34

### Hamster Bot MRS 2 (869) — Daily
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.15806330132000324 | 0.05623052925102412 |
| alpha | 0.07541191015797377 | 0.17025903637780593 |
| trades | 27 | 15 |
| winrate | 0.4074074074074074 | 0.5333333333333333 |
| sharpe | 0.6668712393866286 | 0.48862060634730314 |
| maxdd | -0.1755475789883041 | -0.14433519406953677 |
| pf | 1.419299902602413 | 1.310403230865684 |
| ann | 0.10924013493580387 | 0.07893605820856875 |

- **Combined OOS gain (stress):** 22.318%
- Full history @ stress: total 22.630%, CAGR 11.000%, benchmark -3.355%, sharpe 0.61, maxdd -0.176, trades 42

## 4180

### Polarized Fractal Efficiency (2316) — 4h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.006432828827604542 | 0.09036931476854027 |
| alpha | 0.3027291251239007 | 0.30033372757992816 |
| trades | 39 | 27 |
| winrate | 0.358974358974359 | 0.4444444444444444 |
| sharpe | 0.10204749331568783 | 0.8873133116724153 |
| maxdd | -0.14314533691164832 | -0.07903720465811592 |
| pf | 1.0139467582426533 | 1.4577454446719347 |
| ann | 0.004540384237321726 | 0.12766893410965197 |

- **Combined OOS gain (stress):** 9.738%
- Full history @ stress: total 12.817%, CAGR 5.887%, benchmark -41.270%, sharpe 0.47, maxdd -0.143, trades 66

### Explosion Range Expansion (3263) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.08667151322520783 | 0.09206874004625587 |
| alpha | 0.382967809521504 | 0.30203315285764376 |
| trades | 58 | 31 |
| winrate | 0.3793103448275862 | 0.3870967741935484 |
| sharpe | 0.41218400581420694 | 0.7806712155552051 |
| maxdd | -0.174069163836436 | -0.12354982975475837 |
| pf | 1.1518539515035493 | 1.3754920754941662 |
| ann | 0.06048053942749876 | 0.1301105428088405 |

- **Combined OOS gain (stress):** 18.672%
- Full history @ stress: total 18.672%, CAGR 8.459%, benchmark -41.270%, sharpe 0.53, maxdd -0.174, trades 89

### SVOS EURJPY D1 (4071) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.021934227954397034 | 0.0932834517720389 |
| alpha | 0.27436206834189913 | 0.3032478645834268 |
| trades | 33 | 17 |
| winrate | 0.3333333333333333 | 0.5294117647058824 |
| sharpe | -0.1181183905770625 | 1.3291746949324923 |
| maxdd | -0.10224141760474725 | -0.04122251610041805 |
| pf | 0.9285337481920058 | 2.190116172156905 |
| ann | -0.015546447361769467 | 0.13185665652324996 |

- **Combined OOS gain (stress):** 6.930%
- Full history @ stress: total 9.125%, CAGR 4.229%, benchmark -41.270%, sharpe 0.47, maxdd -0.102, trades 50

### Futures Engulfing Candle Size (823) — 4h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.07734226146039391 | 0.050776702488092074 |
| alpha | 0.21895403483590226 | 0.26074111529947996 |
| trades | 59 | 34 |
| winrate | 0.3220338983050847 | 0.4411764705882353 |
| sharpe | -0.18578776777479886 | 0.4627637614258905 |
| maxdd | -0.17346923266183356 | -0.11725476589473693 |
| pf | 0.8824529323489708 | 1.2230823555031245 |
| ann | -0.05528260049586875 | 0.07120682858686167 |

- **Combined OOS gain (stress):** -3.049%
- Full history @ stress: total -0.329%, CAGR -0.156%, benchmark -41.270%, sharpe 0.09, maxdd -0.173, trades 93

### Long Explosive V1 (992) — 4h **(pick)**
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.2041580045612057 | 0.11438274512696633 |
| alpha | 0.5004543008575019 | 0.3243471579383542 |
| trades | 46 | 22 |
| winrate | 0.41304347826086957 | 0.5454545454545454 |
| sharpe | 0.7414784603380995 | 0.9645404946632875 |
| maxdd | -0.1746252216962848 | -0.10004213979386978 |
| pf | 1.3572393916932681 | 1.6808355116059097 |
| ann | 0.14025303752492757 | 0.16230621111685228 |

- **Combined OOS gain (stress):** 34.189%
- Full history @ stress: total 37.954%, CAGR 16.489%, benchmark -41.270%, sharpe 0.87, maxdd -0.175, trades 68

## 4190

### Step Stochastic Cross (2117) — 1h **(pick)**
> family: volatility | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.01701338953680054 | 0.2875146761644103 |
| alpha | 0.013076381662784797 | 0.03654342519315912 |
| trades | 6 | 6 |
| winrate | 0.16666666666666666 | 0.6666666666666666 |
| sharpe | 0.15653501169957712 | 1.9090758543011972 |
| maxdd | -0.11826404537127799 | -0.08633317302443033 |
| pf | 0.9259618790968374 | 6.568731579544764 |
| ann | 0.011989820581185251 | 0.42043708628989607 |

- **Combined OOS gain (stress):** 30.942%
- Full history @ stress: total 32.179%, CAGR 14.149%, benchmark 26.772%, sharpe 0.90, maxdd -0.118, trades 12

## 4191

### Kalman Filter Candles (2152) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.9208120247996063 | 0.11990872050464296 |
| alpha | 0.2941453581329396 | 0.3481295794003484 |
| trades | 40 | 27 |
| winrate | 0.5 | 0.4074074074074074 |
| sharpe | 1.8468477789636577 | 0.7109340070316447 |
| maxdd | -0.13346788379324293 | -0.16872232181875324 |
| pf | 2.5309078707209998 | 1.4480432240304115 |
| ann | 0.5859018301705199 | 0.17031833422642828 |

- **Combined OOS gain (stress):** 115.113%
- Full history @ stress: total 125.615%, CAGR 47.103%, benchmark 43.771%, sharpe 1.52, maxdd -0.169, trades 67

### Explosion Range Expansion (3263) — 4h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 1.2247916668564094 | 0.15268114313541514 |
| alpha | 0.5981250001897427 | 0.38090200203112057 |
| trades | 61 | 35 |
| winrate | 0.5573770491803278 | 0.37142857142857144 |
| sharpe | 2.492178641770567 | 1.0353624030210609 |
| maxdd | -0.10930226114328812 | -0.10383707201816483 |
| pf | 3.345908390235519 | 1.6277182274043245 |
| ann | 0.7593525383302375 | 0.21814977307504657 |

- **Combined OOS gain (stress):** 156.448%
- Full history @ stress: total 168.969%, CAGR 59.893%, benchmark 43.771%, sharpe 2.09, maxdd -0.109, trades 96

### Fast Slow RVI Crossover (3520) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.7904018792060081 | 0.13523251819327653 |
| alpha | 0.16373521253934142 | 0.36345337708898195 |
| trades | 57 | 26 |
| winrate | 0.45614035087719296 | 0.3076923076923077 |
| sharpe | 1.6527193923268892 | 0.8033406596533988 |
| maxdd | -0.19967476399419903 | -0.22078903720256782 |
| pf | 1.8117417570888885 | 1.4541196276130768 |
| ann | 0.5090527066482406 | 0.19261668328339598 |

- **Combined OOS gain (stress):** 103.252%
- Full history @ stress: total 113.174%, CAGR 43.198%, benchmark 43.771%, sharpe 1.44, maxdd -0.251, trades 83

### Balance of Power (546) — 1h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.9383577713048066 | 0.17114683164844813 |
| alpha | 0.30858677893839426 | 0.4074883937690471 |
| trades | 61 | 27 |
| winrate | 0.4262295081967213 | 0.4074074074074074 |
| sharpe | 1.832941836222884 | 0.9238811408405704 |
| maxdd | -0.18936370256757085 | -0.15502714979922405 |
| pf | 1.9964010270666042 | 1.7754970931286922 |
| ann | 0.5961225774593368 | 0.2453352808021354 |

- **Combined OOS gain (stress):** 127.010%
- Full history @ stress: total 140.635%, CAGR 51.669%, benchmark 44.046%, sharpe 1.60, maxdd -0.189, trades 88

### Long Explosive V1 (992) — 4h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 1.039676541488007 | 0.10392934659790254 |
| alpha | 0.4130098748213402 | 0.33215020549360796 |
| trades | 66 | 37 |
| winrate | 0.45454545454545453 | 0.32432432432432434 |
| sharpe | 2.04269564716956 | 0.689935307190562 |
| maxdd | -0.18621593195440067 | -0.1429399122923355 |
| pf | 1.9300319938168373 | 1.3293543226671822 |
| ann | 0.6546219151289705 | 0.1471920519313441 |

- **Combined OOS gain (stress):** 125.166%
- Full history @ stress: total 136.159%, CAGR 50.324%, benchmark 43.771%, sharpe 1.68, maxdd -0.186, trades 103

## 4193

### SMB Magic (1320) — 30min **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.09811085288600219 | 0.29659239157434314 |
| alpha | 0.7128361276112769 | 0.6938299606351167 |
| trades | 18 | 9 |
| winrate | 0.3333333333333333 | 0.5555555555555556 |
| sharpe | 0.5711487119203691 | 1.741281229219178 |
| maxdd | -0.12522528931028842 | -0.09401906767112844 |
| pf | 1.4942643824290711 | 6.6826401754545826 |
| ann | 0.06835528649240175 | 0.43436463952201043 |

- **Combined OOS gain (stress):** 42.380%
- Full history @ stress: total 42.380%, CAGR 23.099%, benchmark -76.022%, sharpe 1.09, maxdd -0.125, trades 27

### Ingrit (3195) — 30min
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.022025706039606963 | 0.3197285028477934 |
| alpha | 0.6367509807648817 | 0.716966071908567 |
| trades | 48 | 21 |
| winrate | 0.2708333333333333 | 0.47619047619047616 |
| sharpe | 0.21122599066612457 | 1.9515766388138014 |
| maxdd | -0.18819292882474747 | -0.05492014790329691 |
| pf | 1.0434523568268832 | 2.878464814703473 |
| ann | 0.01551088578712001 | 0.4700326878068062 |

- **Combined OOS gain (stress):** 34.880%
- Full history @ stress: total 34.880%, CAGR 19.242%, benchmark -76.022%, sharpe 0.98, maxdd -0.206, trades 69

### Consolidation Breakout (3284) — 30min
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.20526542912760304 | 0.25784715003046843 |
| alpha | 0.8199907038528778 | 0.655084719091242 |
| trades | 20 | 10 |
| winrate | 0.45 | 0.6 |
| sharpe | 1.342463196200551 | 2.03977534312539 |
| maxdd | -0.06064471625422918 | -0.03926824495651715 |
| pf | 2.194422060622347 | 7.229460841603012 |
| ann | 0.14099378980701616 | 0.37518624325781436 |

- **Combined OOS gain (stress):** 51.604%
- Full history @ stress: total 51.604%, CAGR 27.728%, benchmark -76.022%, sharpe 1.65, maxdd -0.072, trades 30

### Function Logistic Equation (816) — 4h
> family: other | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.06715540956240007 | 0.259886357040094 |
| alpha | 0.6818806842876748 | 0.6646872299260732 |
| trades | 6 | 7 |
| winrate | 0.5 | 0.7142857142857143 |
| sharpe | 0.6882237715263909 | 1.4613154573279565 |
| maxdd | -0.08724288358166654 | -0.06646826015794183 |
| pf | 2.2639377736677444 | 9.337687834463457 |
| ann | 0.046989378144973726 | 0.3782834217858726 |

- **Combined OOS gain (stress):** 34.449%
- Full history @ stress: total 34.449%, CAGR 19.018%, benchmark -76.022%, sharpe 1.08, maxdd -0.104, trades 13

### Keltner Channel Golden Cross (954) — 15min
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.06374023923600558 | 0.22400987280235407 |
| alpha | 0.6784655139612803 | 0.6185714710265494 |
| trades | 42 | 22 |
| winrate | 0.35714285714285715 | 0.5 |
| sharpe | 0.4406501660476451 | 1.4468191215086679 |
| maxdd | -0.1584593975606743 | -0.09344885327175478 |
| pf | 1.1463253322959344 | 2.18396851227733 |
| ann | 0.04462111004917535 | 0.32408001134795983 |

- **Combined OOS gain (stress):** 30.203%
- Full history @ stress: total 30.203%, CAGR 16.793%, benchmark -76.022%, sharpe 0.90, maxdd -0.229, trades 64

## 4194

### MACD Sample Hedging Grid (3360) — 30min **(pick)**
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.020107599042000324 | 0.046595033977042455 |
| alpha | 0.40440992462339564 | 0.37006535361174564 |
| trades | 5 | 10 |
| winrate | 0.4 | 0.3 |
| sharpe | 0.5006385071919721 | 0.5553131526268655 |
| maxdd | -0.05431858221409469 | -0.08874058730459666 |
| pf | 1.6426608806083833 | 1.4786193860879306 |
| ann | 0.014164048983436262 | 0.06529106782551786 |

- **Combined OOS gain (stress):** 6.764%
- Full history @ stress: total 6.764%, CAGR 6.423%, benchmark -56.930%, sharpe 0.54, maxdd -0.089, trades 15

### Farhad Hill Version 2 Strategy (C#) (3837) — 30min
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.004130469236000689 | 0.04560229942035465 |
| alpha | 0.388432794817396 | 0.36907261905505784 |
| trades | 6 | 10 |
| winrate | 0.3333333333333333 | 0.3 |
| sharpe | 0.15814259954668541 | 0.543558689799295 |
| maxdd | -0.05432626751398828 | -0.08961360700656906 |
| pf | 1.0888893174775562 | 1.4636923431468558 |
| ann | 0.0029163268568435097 | 0.0638880049603654 |

- **Combined OOS gain (stress):** 4.992%
- Full history @ stress: total 4.992%, CAGR 4.743%, benchmark -56.930%, sharpe 0.41, maxdd -0.090, trades 16

### Long Explosive V1 (992) — 4h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.016441775808000436 | -0.04172050116421844 |
| alpha | 0.3730638900242823 | 0.27989122044750325 |
| trades | 8 | 22 |
| winrate | 0.25 | 0.45454545454545453 |
| sharpe | 0.4061029543362573 | -0.0957254890917548 |
| maxdd | -0.04310473887375321 | -0.1394359176449741 |
| pf | 1.2921280956372474 | 0.8664108355282387 |
| ann | 0.01158794868452162 | -0.05746676506387283 |

- **Combined OOS gain (stress):** -2.596%
- Full history @ stress: total -2.546%, CAGR -2.423%, benchmark -54.994%, sharpe 0.01, maxdd -0.139, trades 30

## 4200

### Sunil 2 Bar Breakout (1360) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.4746334901440059 | 0.18127270942359663 |
| alpha | 0.3408179386069352 | 0.25351605543120115 |
| trades | 34 | 17 |
| winrate | 0.5 | 0.47058823529411764 |
| sharpe | 1.2587870385410973 | 1.687391923802523 |
| maxdd | -0.26948772077169203 | -0.08770488467651982 |
| pf | 1.737725584544466 | 2.5070352655851917 |
| ann | 0.3157454768792636 | 0.26031384353383324 |

- **Combined OOS gain (stress):** 74.194%
- Full history @ stress: total 78.923%, CAGR 31.781%, benchmark 10.307%, sharpe 1.37, maxdd -0.269, trades 51

### Hull Ma Volume (144) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.37905970304000425 | 0.2119643911569815 |
| alpha | 0.24524415150293355 | 0.284207737164586 |
| trades | 32 | 15 |
| winrate | 0.375 | 0.5333333333333333 |
| sharpe | 1.5231677644098822 | 2.3437225296438053 |
| maxdd | -0.10918616534907533 | -0.03515981457011175 |
| pf | 2.2641991355242483 | 5.922330844320914 |
| ann | 0.25491006595071064 | 0.3060184756136779 |

- **Combined OOS gain (stress):** 67.137%
- Full history @ stress: total 67.137%, CAGR 27.589%, benchmark 10.307%, sharpe 1.73, maxdd -0.109, trades 47

### Parabolic SAR Bug5 (1626) — 4h **(pick)**
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.46120904891600367 | 0.2095066621317474 |
| alpha | 0.327393497378933 | 0.2817500081393519 |
| trades | 19 | 8 |
| winrate | 0.5263157894736842 | 0.625 |
| sharpe | 1.3059563906124456 | 1.7277386576367875 |
| maxdd | -0.26093131767426647 | -0.0733362149879403 |
| pf | 2.106494421557107 | 12.938608080710457 |
| ann | 0.307271918471689 | 0.30234178886487784 |

- **Combined OOS gain (stress):** 76.734%
- Full history @ stress: total 81.529%, CAGR 32.688%, benchmark 10.307%, sharpe 1.45, maxdd -0.261, trades 27

### Hercules A.T.C. 2006 (2485) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.585676515712007 | 0.14772433415667052 |
| alpha | 0.45186096417493626 | 0.21996768016427504 |
| trades | 48 | 25 |
| winrate | 0.4166666666666667 | 0.52 |
| sharpe | 2.0419582490218797 | 1.660435167187875 |
| maxdd | -0.0930583307826659 | -0.08639182100285991 |
| pf | 2.2043944747045634 | 2.150561220957654 |
| ann | 0.3849928920830734 | 0.2108809407981811 |

- **Combined OOS gain (stress):** 81.992%
- Full history @ stress: total 86.932%, CAGR 34.547%, benchmark 10.307%, sharpe 1.98, maxdd -0.093, trades 73

### Explosion (3261) — 4h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.6838972379320105 | 0.16448345503751294 |
| alpha | 0.5500816863949398 | 0.23672680104511745 |
| trades | 56 | 26 |
| winrate | 0.48214285714285715 | 0.38461538461538464 |
| sharpe | 1.788290192361844 | 1.6766177155275004 |
| maxdd | -0.14054292604263996 | -0.08263347555410272 |
| pf | 2.454338976185024 | 2.0272895157186777 |
| ann | 0.44506493930554925 | 0.23550598012912904 |

- **Combined OOS gain (stress):** 96.087%
- Full history @ stress: total 105.662%, CAGR 40.781%, benchmark 10.307%, sharpe 1.82, maxdd -0.141, trades 82

## 4240

### Nova (2691) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 1.9418362093528074 | 0.6336313207104145 |
| alpha | 0.9056519988264915 | 0.8193381543045721 |
| trades | 56 | 31 |
| winrate | 0.5178571428571429 | 0.5483870967741935 |
| sharpe | 2.758715037591503 | 2.7769663820416643 |
| maxdd | -0.1432878665432915 | -0.043785744608824784 |
| pf | 2.8152607217068644 | 5.758353168958412 |
| ann | 1.1432332840952903 | 0.9770824471320967 |

- **Combined OOS gain (stress):** 380.588%
- Full history @ stress: total 382.991%, CAGR 111.070%, benchmark 71.162%, sharpe 2.76, maxdd -0.143, trades 87

### Explosion Range Expansion (3263) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 7.734608262245619 | 0.5965545188089847 |
| alpha | 6.698424051719303 | 0.7822613524031423 |
| trades | 56 | 39 |
| winrate | 0.44642857142857145 | 0.358974358974359 |
| sharpe | 3.9539147614375607 | 2.250976641827913 |
| maxdd | -0.12385620860738289 | -0.15106762576749144 |
| pf | 4.417417679801158 | 2.8340155324820793 |
| ann | 3.623484101960768 | 0.915041533249519 |

- **Combined OOS gain (stress):** 1294.528%
- Full history @ stress: total 1301.503%, CAGR 249.855%, benchmark 71.162%, sharpe 3.45, maxdd -0.151, trades 95

### Breakthrough Volatility (3271) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 6.053316131688432 | 0.6383919305490322 |
| alpha | 5.017131921162116 | 0.8240987641431898 |
| trades | 99 | 50 |
| winrate | 0.40404040404040403 | 0.38 |
| sharpe | 3.495706929385714 | 2.436739232774584 |
| maxdd | -0.19016248694366933 | -0.08214688429182249 |
| pf | 3.4889981187446057 | 2.628366915232908 |
| ann | 2.9753252845957716 | 0.9850884105171003 |

- **Combined OOS gain (stress):** 1055.610%
- Full history @ stress: total 1061.389%, CAGR 220.017%, benchmark 71.162%, sharpe 3.17, maxdd -0.190, trades 149

### 5 EMA No-Touch Breakout (483) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 3.486763593111216 | 0.6292124234117409 |
| alpha | 2.4505793825849 | 0.8149192570058985 |
| trades | 58 | 32 |
| winrate | 0.39655172413793105 | 0.4375 |
| sharpe | 2.9599594518111165 | 2.482175219183013 |
| maxdd | -0.12673446870324245 | -0.09300972737102331 |
| pf | 3.185691571460803 | 4.22896352875985 |
| ann | 1.8878694491620611 | 0.9696592573100851 |

- **Combined OOS gain (stress):** 630.989%
- Full history @ stress: total 634.645%, CAGR 157.528%, benchmark 71.162%, sharpe 2.80, maxdd -0.153, trades 90

### Hamster Bot MRS 2 (869) — 4h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 2.321315950462819 | 0.7154014296695697 |
| alpha | 1.285131739936503 | 0.9011082632637273 |
| trades | 84 | 40 |
| winrate | 0.44047619047619047 | 0.45 |
| sharpe | 2.077536652022143 | 2.204819218740781 |
| maxdd | -0.3055411119912985 | -0.13536996794103884 |
| pf | 1.74722382916011 | 2.553574622119408 |
| ann | 1.3350439676960595 | 1.115842114451929 |

- **Combined OOS gain (stress):** 469.739%
- Full history @ stress: total 472.588%, CAGR 128.814%, benchmark 71.162%, sharpe 2.10, maxdd -0.306, trades 124

## 4260

### Timer (1788) — 1h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.05347512732263571 | 0.31584669146247824 |
| alpha | 0.33733794016497165 | 0.46790469956655156 |
| trades | 66 | 35 |
| winrate | 0.36363636363636365 | 0.4 |
| sharpe | 0.29081073201090296 | 1.0716706696338567 |
| maxdd | -0.18071071968381758 | -0.13726525995171523 |
| pf | 1.0792524420051781 | 1.8202234588701705 |
| ann | 0.037489234125364534 | 0.46403114703440096 |

- **Combined OOS gain (stress):** 38.621%
- Full history @ stress: total 39.260%, CAGR 17.010%, benchmark -37.179%, sharpe 0.66, maxdd -0.181, trades 101

### Explosion Range Expansion (3263) — 4h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.428273018026033 | 0.44416016911221523 |
| alpha | 0.712135830868369 | 0.5975686793156015 |
| trades | 68 | 30 |
| winrate | 0.29411764705882354 | 0.43333333333333335 |
| sharpe | 1.6387361257460495 | 1.3382860743891023 |
| maxdd | -0.11237229224590839 | -0.1082267876132561 |
| pf | 1.9696353890531288 | 2.491659335241502 |
| ann | 0.286385070720085 | 0.6659852244207218 |

- **Combined OOS gain (stress):** 106.266%
- Full history @ stress: total 109.657%, CAGR 42.072%, benchmark -37.179%, sharpe 1.33, maxdd -0.112, trades 98

### 5 EMA No-Touch Breakout (483) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.04694780531339937 | 0.26146376149303574 |
| alpha | 0.3308106181557353 | 0.41487227169642205 |
| trades | 67 | 37 |
| winrate | 0.29850746268656714 | 0.32432432432432434 |
| sharpe | 0.27270691290210564 | 0.9630296482824403 |
| maxdd | -0.1281501102406699 | -0.12672072194889228 |
| pf | 1.06733780714348 | 1.55742981106264 |
| ann | 0.03294364868759758 | 0.3806805450003605 |

- **Combined OOS gain (stress):** 32.069%
- Full history @ stress: total 33.427%, CAGR 14.659%, benchmark -37.179%, sharpe 0.61, maxdd -0.158, trades 104

### Futures Engulfing Candle Size (823) — 4h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.03726323167428336 | 0.2560196662305101 |
| alpha | 0.3211260445166193 | 0.4094281764338964 |
| trades | 70 | 36 |
| winrate | 0.32857142857142857 | 0.4166666666666667 |
| sharpe | 0.2381595896400416 | 0.903972554319423 |
| maxdd | -0.138392552661338 | -0.1592500140388604 |
| pf | 1.0687504764047386 | 1.6014649727224972 |
| ann | 0.026184012314685257 | 0.37241229119490393 |

- **Combined OOS gain (stress):** 30.282%
- Full history @ stress: total 32.424%, CAGR 14.250%, benchmark -37.179%, sharpe 0.58, maxdd -0.159, trades 106

### Long Explosive V1 (992) — 1h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.16762174656675133 | 0.34973983700872857 |
| alpha | 0.45148455940908727 | 0.5017978451128019 |
| trades | 59 | 32 |
| winrate | 0.3898305084745763 | 0.40625 |
| sharpe | 0.6948986718269112 | 1.167034978999535 |
| maxdd | -0.15280557031708464 | -0.14974530414270282 |
| pf | 1.2658410382548217 | 1.8883476527752545 |
| ann | 0.11570047956412566 | 0.5166630723269283 |

- **Combined OOS gain (stress):** 57.599%
- Full history @ stress: total 58.324%, CAGR 24.353%, benchmark -37.179%, sharpe 0.88, maxdd -0.153, trades 91

## 4261

### Keltner RSI Divergence (311) — 4h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.4252409719902688 | 0.08050688535860129 |
| alpha | 0.18502386585289776 | 0.5736863187269119 |
| trades | 9 | 10 |
| winrate | 0.7777777777777778 | 0.6 |
| sharpe | 0.7129499188105225 | 1.034241685106058 |
| maxdd | -0.15981251791880802 | -0.06697081709388031 |
| pf | 4.533263384339926 | 5.544770439785945 |
| ann | 0.2844551892303997 | 0.11352856711297554 |

- **Combined OOS gain (stress):** 53.998%
- Full history @ stress: total 53.998%, CAGR 22.729%, benchmark -34.173%, sharpe 0.67, maxdd -0.160, trades 19

### CorrTime (3319) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.35641738605566187 | 0.00970188858971599 |
| alpha | 0.11620027991829085 | 0.5028813219580266 |
| trades | 11 | 10 |
| winrate | 0.36363636363636365 | 0.3 |
| sharpe | 0.6428510944431426 | 0.21597402315982067 |
| maxdd | -0.1773735884006029 | -0.049968726307770384 |
| pf | 3.0253128898710067 | 1.2437695301026588 |
| ann | 0.24031847109900029 | 0.01349918169396691 |

- **Combined OOS gain (stress):** 36.958%
- Full history @ stress: total 37.724%, CAGR 16.396%, benchmark -34.173%, sharpe 0.54, maxdd -0.177, trades 21

### Donchian Zig-Zag LuxAlgo (688) — Daily
> family: breakout | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.5045845622270233 | -0.08280808146399876 |
| alpha | 0.1489407936815641 | 0.4111678221504591 |
| trades | 5 | 7 |
| winrate | 0.6 | 0.14285714285714285 |
| sharpe | 0.826691637175346 | -1.75349404180843 |
| maxdd | -0.09905831028114642 | -0.12777111891700543 |
| pf | 7.3391896413969135 | 0.28627377108466573 |
| ann | 0.3345695932016042 | -0.11311893894197833 |

- **Combined OOS gain (stress):** 37.999%
- Full history @ stress: total 37.925%, CAGR 6.042%, benchmark -12.527%, sharpe 0.35, maxdd -0.174, trades 18

## 4262

### Up Gap Strategy With Delay (1511) — 1h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.03611244647120526 | -0.0223290352760398 |
| alpha | 0.4503811741763182 | 0.476089937055976 |
| trades | 40 | 19 |
| winrate | 0.425 | 0.3684210526315789 |
| sharpe | 0.2960150209706537 | -0.15556086517271397 |
| maxdd | -0.0825648429024467 | -0.08565749482360008 |
| pf | 1.1699441285339933 | 0.8851287528151288 |
| ann | 0.025379558802657742 | -0.03087497056734323 |

- **Combined OOS gain (stress):** 1.298%
- Full history @ stress: total 1.298%, CAGR 0.631%, benchmark -69.822%, sharpe 0.11, maxdd -0.116, trades 59

### VininI Trend LRMA (2050) — 4h **(pick)**
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.03786509581800179 | 0.07867677131163475 |
| alpha | 0.4528294663643201 | 0.5839399292063716 |
| trades | 12 | 6 |
| winrate | 0.25 | 0.5 |
| sharpe | 0.33764624644522345 | 0.9020716654326367 |
| maxdd | -0.07999977616911613 | -0.08149279936305487 |
| pf | 1.2572532437034873 | 2.5789691457643524 |
| ann | 0.02660463959664039 | 0.11091012251224597 |

- **Combined OOS gain (stress):** 11.952%
- Full history @ stress: total 11.952%, CAGR 5.660%, benchmark -69.857%, sharpe 0.57, maxdd -0.081, trades 18

### Polarized Fractal Efficiency (2316) — Daily
> family: momentum | params: `{}` | flags: thin_trades;win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.20382644572746056 | 0.06193306728279291 |
| alpha | 0.2535648586203655 | 0.566713555087671 |
| trades | 20 | 7 |
| winrate | 0.35 | 0.42857142857142855 |
| sharpe | -1.3468662568688592 | 0.809559278424839 |
| maxdd | -0.24992437413446722 | -0.07865095686470314 |
| pf | 0.39168050925778 | 1.638124318574635 |
| ann | -0.14873655478477588 | 0.0870343741498747 |

- **Combined OOS gain (stress):** -15.452%
- Full history @ stress: total 5.395%, CAGR 1.773%, benchmark -70.420%, sharpe 0.21, maxdd -0.270, trades 36

### Nova (2691) — Daily
> family: breakout | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | -0.025571463137810224 | 0.0753082743319331 |
| alpha | 0.4318198412100158 | 0.5800887621368112 |
| trades | 17 | 7 |
| winrate | 0.4117647058823529 | 0.42857142857142855 |
| sharpe | -0.12004678405499851 | 1.1541059692809916 |
| maxdd | -0.08979995381168981 | -0.03343642682902337 |
| pf | 0.9969956697178435 | 2.28958674327071 |
| ann | -0.018134276369006552 | 0.10609514403070763 |

- **Combined OOS gain (stress):** 4.781%
- Full history @ stress: total 15.289%, CAGR 4.874%, benchmark -70.420%, sharpe 0.48, maxdd -0.090, trades 42

### 80-20 (488) — Daily
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.09078026657917071 | 0.07059521570067506 |
| alpha | 0.36661103776865533 | 0.5753757035055531 |
| trades | 25 | 8 |
| winrate | 0.4 | 0.5 |
| sharpe | -0.4221078161277149 | 0.8169077976300394 |
| maxdd | -0.20934483278248628 | -0.04325496541334306 |
| pf | 0.7555146358595574 | 2.224534716537321 |
| ann | -0.06502417016781792 | 0.09936806852856317 |

- **Combined OOS gain (stress):** -2.659%
- Full history @ stress: total 23.903%, CAGR 7.432%, benchmark -70.420%, sharpe 0.51, maxdd -0.234, trades 48

## 4263

### Fisher Cyber Cycle (1946) — Daily
> family: trend | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.38159826825494425 | 0.08513917050191666 |
| alpha | 0.10757370626734875 | 0.021519652280792556 |
| trades | 45 | 22 |
| winrate | 0.4222222222222222 | 0.45454545454545453 |
| sharpe | -1.070188100662838 | 0.6118505186696256 |
| maxdd | -0.4407022175687678 | -0.17696415255183595 |
| pf | 0.48016217530243516 | 1.1181391347205034 |
| ann | -0.28790655716396374 | 0.12016393571706763 |

- **Combined OOS gain (stress):** -32.895%
- Full history @ stress: total 36.574%, CAGR 11.395%, benchmark 29.864%, sharpe 0.51, maxdd -0.462, trades 81

### ADX Slope Mean Reversion (291) — Daily **(pick)**
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.04169290375894885 | 0.11681686776907818 |
| alpha | 0.5308648782812418 | 0.053197349547954076 |
| trades | 10 | 5 |
| winrate | 0.6 | 0.6 |
| sharpe | 0.31842452339074284 | 1.2724279548869248 |
| maxdd | -0.09579765762601389 | -0.04866604628378479 |
| pf | 1.2961810286867435 | 4.145550314895686 |
| ann | 0.029278122270195883 | 0.1658335516966032 |

- **Combined OOS gain (stress):** 16.338%
- Full history @ stress: total 27.031%, CAGR 8.636%, benchmark 29.864%, sharpe 0.82, maxdd -0.096, trades 18

### Consolidation Breakout (3284) — 1h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.023345428191998918 | 0.0825352080570072 |
| alpha | 0.44710453822841756 | 0.02544496864632584 |
| trades | 18 | 8 |
| winrate | 0.3888888888888889 | 0.625 |
| sharpe | -0.18919116148599133 | 1.3662644698959796 |
| maxdd | -0.10395179762583351 | -0.035312564577267946 |
| pf | 0.8455762627866852 | 3.355528443318487 |
| ann | -0.016550155632191532 | 0.11643261478108569 |

- **Combined OOS gain (stress):** 5.726%
- Full history @ stress: total 5.726%, CAGR 2.753%, benchmark -42.176%, sharpe 0.38, maxdd -0.104, trades 26

### Adaptive KDJ (MTF) (492) — Daily
> family: trend | params: `{}` | flags: thin_trades;win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.35617380373888896 | 0.09352572477243859 |
| alpha | 0.13299817078340403 | 0.029906206551314485 |
| trades | 11 | 7 |
| winrate | 0.18181818181818182 | 0.42857142857142855 |
| sharpe | -1.803509765188218 | 1.3703657845119595 |
| maxdd | -0.36789763651087226 | -0.023240175824644882 |
| pf | 0.05017770157535651 | 4.2194341881176305 |
| ann | -0.2673459909144047 | 0.13220500735811824 |

- **Combined OOS gain (stress):** -29.596%
- Full history @ stress: total 6.805%, CAGR 2.305%, benchmark 29.864%, sharpe 0.22, maxdd -0.375, trades 23

## 4264

### Supertrend AT v1.0 (1373) — 30min
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.04802750432000069 | -0.007062479057361237 |
| alpha | 0.25683253576654164 | 0.34244171621342434 |
| trades | 5 | 6 |
| winrate | 0.8 | 0.3333333333333333 |
| sharpe | 0.9459961783597363 | -0.063837818830517 |
| maxdd | -0.042224243933943084 | -0.06616724887583214 |
| pf | 3.8425020520463478 | 0.9149393164546681 |
| ann | 0.03369611710308784 | -0.009794767707045238 |

- **Combined OOS gain (stress):** 4.063%
- Full history @ stress: total 4.063%, CAGR 3.212%, benchmark -46.365%, sharpe 0.38, maxdd -0.066, trades 11

### Stoch TP TS V3103 (1791) — Daily
> family: other | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.07616021152000196 | 0.021441939125575127 |
| alpha | 0.23463369146825552 | 0.37044957271336143 |
| trades | 19 | 27 |
| winrate | 0.42105263157894735 | 0.4074074074074074 |
| sharpe | 0.8924247405555964 | 0.2424615833885111 |
| maxdd | -0.08879547490199946 | -0.09949476403800972 |
| pf | 1.4014175285196357 | 1.1301348748672395 |
| ann | 0.05322316927693649 | 0.02990178828364165 |

- **Combined OOS gain (stress):** 9.924%
- Full history @ stress: total 10.134%, CAGR 7.966%, benchmark -44.838%, sharpe 0.49, maxdd -0.102, trades 46

### RSI MA on RSI Dual (3531) — 1h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.07539439923000102 | -0.011345519393010872 |
| alpha | 0.291105122422021 | 0.3381586758777747 |
| trades | 8 | 8 |
| winrate | 0.625 | 0.25 |
| sharpe | 1.3075520786647201 | -0.14131602497549037 |
| maxdd | -0.06413816829165642 | -0.07682876882445833 |
| pf | 2.499380324372385 | 0.83897864006557 |
| ann | 0.05269361454330057 | -0.015721636345729095 |

- **Combined OOS gain (stress):** 6.319%
- Full history @ stress: total 6.319%, CAGR 4.986%, benchmark -46.833%, sharpe 0.55, maxdd -0.077, trades 16

### Hamster Bot MRS 2 (869) — Daily
> family: trend | params: `{}` | flags: thin_trades;win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.020518672353998735 | -0.2151983331913434 |
| alpha | 0.13795480759425482 | 0.1338093003964429 |
| trades | 7 | 17 |
| winrate | 0.2857142857142857 | 0.29411764705882354 |
| sharpe | -0.058864022884993226 | -1.461968535385739 |
| maxdd | -0.2449815548684875 | -0.27230381863449804 |
| pf | 0.990419908829914 | 0.3132488700284779 |
| ann | -0.014540068318412702 | -0.28575972950904693 |

- **Combined OOS gain (stress):** -23.130%
- Full history @ stress: total -22.597%, CAGR -18.403%, benchmark -44.838%, sharpe -0.82, maxdd -0.359, trades 24

## 4265

### IMACD Sniper (917) — 15min **(pick)**
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | -0.0012958040055994768 | -0.07841831843255842 |
| alpha | 0.15216600898512145 | 0.01579655760049936 |
| trades | 5 | 38 |
| winrate | 0.4 | 0.42105263157894735 |
| sharpe | 0.0280545980667273 | -0.6230488232707195 |
| maxdd | -0.054679602589149945 | -0.17680818877716153 |
| pf | 0.982024866311213 | 0.7231616164926565 |
| ann | -0.0009156334052677906 | -0.10721850176633108 |

- **Combined OOS gain (stress):** -7.961%
- Full history @ stress: total -9.333%, CAGR -11.461%, benchmark -21.770%, sharpe -0.64, maxdd -0.188, trades 44

## 4290

### Timer (1788) — 1h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.10714946941200809 | 0.02939581332329455 |
| alpha | 0.4128965958487897 | 0.40346436771971783 |
| trades | 68 | 37 |
| winrate | 0.4264705882352941 | 0.4864864864864865 |
| sharpe | 0.4210904164398975 | 0.2950042674896069 |
| maxdd | -0.3163105254783598 | -0.16745605482891057 |
| pf | 1.104242977710945 | 1.185064801585096 |
| ann | 0.07456037637184387 | 0.04105631585207781 |

- **Combined OOS gain (stress):** 13.970%
- Full history @ stress: total 21.130%, CAGR 9.519%, benchmark -51.724%, sharpe 0.50, maxdd -0.316, trades 105

### Genie (1875) — 1h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.029438607380807724 | 0.0035790015257777252 |
| alpha | 0.3351857338175893 | 0.377647555922201 |
| trades | 70 | 40 |
| winrate | 0.4 | 0.525 |
| sharpe | 0.20478454990765754 | 0.12938178606688167 |
| maxdd | -0.1916102742122221 | -0.14297238732507977 |
| pf | 1.0381445849575968 | 1.173028254055603 |
| ann | 0.020709044864324344 | 0.004973913010430708 |

- **Combined OOS gain (stress):** 3.312%
- Full history @ stress: total 9.803%, CAGR 4.536%, benchmark -51.724%, sharpe 0.31, maxdd -0.192, trades 110

### Explosion Range Expansion (3263) — 4h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.21905729836120913 | 0.10529641624504693 |
| alpha | 0.5248044247979907 | 0.47843074460325596 |
| trades | 72 | 32 |
| winrate | 0.4027777777777778 | 0.5 |
| sharpe | 0.8128471921911314 | 0.8158383401460227 |
| maxdd | -0.13651422692338133 | -0.09313095983107522 |
| pf | 1.3683971896051372 | 1.4057903768646072 |
| ann | 0.15020246206223242 | 0.14916549442565574 |

- **Combined OOS gain (stress):** 34.742%
- Full history @ stress: total 34.742%, CAGR 15.194%, benchmark -51.724%, sharpe 0.81, maxdd -0.137, trades 104

### 5 EMA No-Touch Breakout (483) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.20306737355280968 | 0.07778173794689969 |
| alpha | 0.5088144999895913 | 0.4509160663051087 |
| trades | 71 | 29 |
| winrate | 0.3380281690140845 | 0.4482758620689655 |
| sharpe | 0.7591531098233689 | 0.6401120166807279 |
| maxdd | -0.1663059603332231 | -0.09124180053464581 |
| pf | 1.2786477344373992 | 1.462465701881489 |
| ann | 0.1395233229337718 | 0.1096301777398283 |

- **Combined OOS gain (stress):** 29.664%
- Full history @ stress: total 36.804%, CAGR 16.027%, benchmark -51.724%, sharpe 0.83, maxdd -0.166, trades 100

### Futures Engulfing Candle Size (823) — 4h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.11410439056080746 | 0.0753902997460354 |
| alpha | 0.41985151699758905 | 0.4485246281042444 |
| trades | 66 | 30 |
| winrate | 0.45454545454545453 | 0.5333333333333333 |
| sharpe | 0.4589130147764649 | 0.5758837667619224 |
| maxdd | -0.16953480629011586 | -0.08351003848127114 |
| pf | 1.139005793651828 | 1.427060248694822 |
| ann | 0.07932487240141417 | 0.1062123227765519 |

- **Combined OOS gain (stress):** 19.810%
- Full history @ stress: total 26.407%, CAGR 11.757%, benchmark -51.724%, sharpe 0.61, maxdd -0.170, trades 96

## 4291

### MomentumSync PSAR RSI ADX Filtered 3-Tier Exit (1066) — 1h **(pick)**
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.15197817293600258 | 0.20313490435638704 |
| alpha | 0.34913726384509347 | 0.2583796596011423 |
| trades | 18 | 7 |
| winrate | 0.4444444444444444 | 0.42857142857142855 |
| sharpe | 0.6829297561461285 | 1.531291806617374 |
| maxdd | -0.1264147872786805 | -0.06481207100966946 |
| pf | 1.749433441887303 | 5.55333745897935 |
| ann | 0.10511917639253276 | 0.2928233660740287 |

- **Combined OOS gain (stress):** 38.599%
- Full history @ stress: total 38.599%, CAGR 16.746%, benchmark -23.239%, sharpe 0.98, maxdd -0.126, trades 25

### Z-Score RSI (1571) — Daily
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.29155025243203125 | 0.1675984052124324 |
| alpha | 0.5122660875730292 | 0.2248210151217137 |
| trades | 27 | 11 |
| winrate | 0.4074074074074074 | 0.45454545454545453 |
| sharpe | 0.8786976618082105 | 1.2343899978537554 |
| maxdd | -0.25785097275919 | -0.07704744826497878 |
| pf | 1.5679822467985975 | 2.4326746999166855 |
| ann | 0.19811328271454376 | 0.24009820088523393 |

- **Combined OOS gain (stress):** 50.801%
- Full history @ stress: total 643.999%, CAGR 29.167%, benchmark 575.500%, sharpe 1.18, maxdd -0.274, trades 146

### Lbs V12 (3880) — 1h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.4500351465600039 | 0.1805721456760334 |
| alpha | 0.6471942374690948 | 0.23581690092078866 |
| trades | 35 | 20 |
| winrate | 0.5142857142857142 | 0.35 |
| sharpe | 1.4284900356387153 | 1.1187149353609456 |
| maxdd | -0.16262021757541611 | -0.11939971203279476 |
| pf | 2.1327768168343715 | 1.9017776297337916 |
| ann | 0.30020147147369625 | 0.25927593138571225 |

- **Combined OOS gain (stress):** 71.187%
- Full history @ stress: total 71.187%, CAGR 29.047%, benchmark -23.239%, sharpe 1.31, maxdd -0.163, trades 55

## 4292

### I Gap (2145) — 1h
> family: volatility | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.14679097042598022 | 0.057770650692674286 |
| alpha | 0.07170768909144598 | 0.36226598572236046 |
| trades | 186 | 91 |
| winrate | 0.3548387096774194 | 0.3516483516483517 |
| sharpe | -0.35589852559894075 | 0.4456318141526502 |
| maxdd | -0.21248048459714108 | -0.1454377251415495 |
| pf | 0.8968332457809516 | 1.1016926712803292 |
| ann | -0.10609355053875413 | 0.08112155151495437 |

- **Combined OOS gain (stress):** -9.750%
- Full history @ stress: total -9.496%, CAGR -4.623%, benchmark -45.040%, sharpe -0.08, maxdd -0.215, trades 278

### JK BullP AutoTrader (2482) — 1h
> family: volatility | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.22320633064800277 | 0.09705494662663305 |
| alpha | 0.44170499016542897 | 0.40155028165631923 |
| trades | 22 | 13 |
| winrate | 0.5909090909090909 | 0.46153846153846156 |
| sharpe | 0.90575500435162 | 0.7334831769828175 |
| maxdd | -0.19147476745046732 | -0.12928557756808612 |
| pf | 2.4155032848778344 | 2.085092226363118 |
| ann | 0.15296672916847553 | 0.13728287883650592 |

- **Combined OOS gain (stress):** 34.192%
- Full history @ stress: total 34.192%, CAGR 14.971%, benchmark -45.040%, sharpe 0.84, maxdd -0.191, trades 35

### Bull vs Medved (2510) — 1h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.2676791443020061 | 0.15432141915450348 |
| alpha | 0.4861778038194323 | 0.45881675418418966 |
| trades | 62 | 34 |
| winrate | 0.45161290322580644 | 0.5 |
| sharpe | 0.8711984027927635 | 1.0169335905860237 |
| maxdd | -0.1749016852637867 | -0.1069433112391247 |
| pf | 1.387126386746951 | 1.493795602247533 |
| ann | 0.18242610824260708 | 0.22055780918624524 |

- **Combined OOS gain (stress):** 46.331%
- Full history @ stress: total 46.976%, CAGR 20.042%, benchmark -45.040%, sharpe 0.93, maxdd -0.175, trades 96

### Fast Slow RVI Crossover (3520) — 1h
> family: trend | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.11719961278598556 | 0.06044487714121538 |
| alpha | 0.10129904673144063 | 0.36494021217090156 |
| trades | 150 | 79 |
| winrate | 0.34 | 0.34177215189873417 |
| sharpe | -0.2527221726074537 | 0.45670158297983343 |
| maxdd | -0.30103628426081486 | -0.2078453690636649 |
| pf | 0.899443209318605 | 1.0869679506273493 |
| ann | -0.08430052258464016 | 0.08491932398663393 |

- **Combined OOS gain (stress):** -6.384%
- Full history @ stress: total -6.830%, CAGR -3.300%, benchmark -45.040%, sharpe -0.02, maxdd -0.301, trades 230

### Long Explosive V1 (992) — 1h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.07310766681601022 | 0.07104268473580988 |
| alpha | 0.2916063263334364 | 0.37553801976549606 |
| trades | 87 | 39 |
| winrate | 0.39080459770114945 | 0.38461538461538464 |
| sharpe | 0.33330861840677767 | 0.5108008096736353 |
| maxdd | -0.19834886188476408 | -0.13355465480192363 |
| pf | 1.0750029532370569 | 1.1575290006370085 |
| ann | 0.051111693211915776 | 0.10000625936686625 |

- **Combined OOS gain (stress):** 14.934%
- Full history @ stress: total 15.441%, CAGR 7.048%, benchmark -45.040%, sharpe 0.40, maxdd -0.198, trades 126

## 4300

### RSI Adaptive T3 (1281) — 4h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.58064520437601 | 0.35209139463645367 |
| alpha | 0.40315275724610067 | 0.1810055360505951 |
| trades | 67 | 41 |
| winrate | 0.47761194029850745 | 0.43902439024390244 |
| sharpe | 1.5356070177927252 | 1.8828445580853734 |
| maxdd | -0.156618686425957 | -0.1287942513490028 |
| pf | 1.7827995232196918 | 2.1158977874932563 |
| ann | 0.3818867859560444 | 0.5203340027777255 |

- **Combined OOS gain (stress):** 113.718%
- Full history @ stress: total 111.310%, CAGR 42.602%, benchmark 40.106%, sharpe 1.63, maxdd -0.157, trades 108

### Breakthrough Volatility (3271) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 1.01135116927562 | 0.2606345408239299 |
| alpha | 0.8338587221457108 | 0.08954868223807133 |
| trades | 95 | 51 |
| winrate | 0.43157894736842106 | 0.43137254901960786 |
| sharpe | 2.023456071732952 | 1.437599821919603 |
| maxdd | -0.1361179602023045 | -0.1182980900105266 |
| pf | 1.7734501252211854 | 1.5731617184878364 |
| ann | 0.6383551072113598 | 0.37942026363478565 |

- **Combined OOS gain (stress):** 153.558%
- Full history @ stress: total 151.025%, CAGR 54.741%, benchmark 40.106%, sharpe 1.81, maxdd -0.136, trades 146

### Adaptive Trend Flow (496) — Daily
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.5264689334095916 | 0.31279512610640725 |
| alpha | 0.34397635180721764 | 0.1387444931950148 |
| trades | 34 | 21 |
| winrate | 0.5588235294117647 | 0.6666666666666666 |
| sharpe | 1.5717875104271226 | 1.8070231942371084 |
| maxdd | -0.11204369850302964 | -0.09529283843054737 |
| pf | 2.3994274451349296 | 2.4488884601391505 |
| ann | 0.3482543190356002 | 0.4593180513835662 |

- **Combined OOS gain (stress):** 100.394%
- Full history @ stress: total 802.972%, CAGR 12.467%, benchmark -1.969%, sharpe 0.57, maxdd -0.548, trades 468

## 4310

### Kalman Filter Candles (2152) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.008128419508004248 | 0.790489590131108 |
| alpha | 0.17868235536806254 | 0.06501626827224372 |
| trades | 46 | 26 |
| winrate | 0.30434782608695654 | 0.4230769230769231 |
| sharpe | 0.1312313573489513 | 3.197001213660776 |
| maxdd | -0.2120339875543663 | -0.09018930950690274 |
| pf | 1.012345328432046 | 5.741360647380797 |
| ann | 0.00573573673122052 | 1.2455514193968478 |

- **Combined OOS gain (stress):** 80.504%
- Full history @ stress: total 80.504%, CAGR 32.332%, benchmark 46.137%, sharpe 1.33, maxdd -0.233, trades 72

### CP Strat ORB (639) — 4h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.020706224747608193 | 0.8005983944616635 |
| alpha | 0.19126016060766649 | 0.07512507260279921 |
| trades | 57 | 33 |
| winrate | 0.3684210526315789 | 0.5151515151515151 |
| sharpe | 0.1711592504522346 | 3.3571982456204448 |
| maxdd | -0.27026783028883095 | -0.07428372801038619 |
| pf | 1.0311433800081065 | 5.376576292266331 |
| ann | 0.014584465604275954 | 1.2631777252468401 |

- **Combined OOS gain (stress):** 83.788%
- Full history @ stress: total 84.785%, CAGR 33.812%, benchmark 46.137%, sharpe 1.49, maxdd -0.282, trades 90

## 4320

### I Gap (2145) — 4h
> family: volatility | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.13146290974838948 | -0.028568206394172346 |
| alpha | 0.07123979295431326 | 0.19408587467190208 |
| trades | 113 | 39 |
| winrate | 0.35398230088495575 | 0.41025641025641024 |
| sharpe | -0.290397582248245 | -0.11274253034585115 |
| maxdd | -0.28805051385896907 | -0.15038421060692742 |
| pf | 0.8770459609941343 | 0.9309451927295201 |
| ann | -0.09477773756043639 | -0.03945341746386588 |

- **Combined OOS gain (stress):** -15.628%
- Full history @ stress: total -15.002%, CAGR -7.420%, benchmark -36.937%, sharpe -0.22, maxdd -0.290, trades 152

### IMA Expert (2197) — Daily
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.0791544440201375 | 0.03484435274275022 |
| alpha | 0.16415659276916017 | 0.26856082783853563 |
| trades | 74 | 34 |
| winrate | 0.3918918918918919 | 0.5294117647058824 |
| sharpe | -0.09328360970000091 | 0.3333111649689417 |
| maxdd | -0.25789795313275765 | -0.08644269874424093 |
| pf | 0.9237554123035244 | 1.087080008646717 |
| ann | -0.0565938586050273 | 0.04871673506384555 |

- **Combined OOS gain (stress):** -4.707%
- Full history @ stress: total -57.630%, CAGR -7.718%, benchmark 25.718%, sharpe -0.23, maxdd -0.670, trades 504

### 80-20 (488) — 4h **(pick)**
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.08353218488120229 | 0.10951174190069013 |
| alpha | 0.28623488758390503 | 0.33216582296676456 |
| trades | 34 | 16 |
| winrate | 0.5294117647058824 | 0.3125 |
| sharpe | 0.38047917135840614 | 0.9080185251924594 |
| maxdd | -0.21174395937657298 | -0.08316813686697144 |
| pf | 1.2527033159069354 | 1.6257930883097524 |
| ann | 0.05831520407242308 | 0.15525652842012394 |

- **Combined OOS gain (stress):** 20.219%
- Full history @ stress: total 21.111%, CAGR 9.511%, benchmark -36.937%, sharpe 0.55, maxdd -0.212, trades 50

### Futures Engulfing Candle Size (823) — 4h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.03818457792079355 | 0.01417548809067748 |
| alpha | 0.1645181247819092 | 0.2368295691567519 |
| trades | 67 | 35 |
| winrate | 0.3880597014925373 | 0.34285714285714286 |
| sharpe | -0.030183086829357716 | 0.1957803889103077 |
| maxdd | -0.19653198083677326 | -0.11023825463057868 |
| pf | 0.9466000000492246 | 1.0810231511255064 |
| ann | -0.0271303500315897 | 0.019740773461414785 |

- **Combined OOS gain (stress):** -2.455%
- Full history @ stress: total -1.208%, CAGR -0.575%, benchmark -36.937%, sharpe 0.07, maxdd -0.197, trades 102

## 4321

### RSI Failure Swing (110) — 4h **(pick)**
> family: other | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.09079059927985966 | -0.008387007722465256 |
| alpha | 0.169192966143765 | 0.16876183923770238 |
| trades | 9 | 8 |
| winrate | 0.5555555555555556 | 0.625 |
| sharpe | 0.6582866213671238 | -0.022278735261718995 |
| maxdd | -0.09572331785685106 | -0.07200088657197867 |
| pf | 1.7319684391630443 | 0.9096390148593565 |
| ann | 0.06331887470958919 | -0.011628713399311374 |

- **Combined OOS gain (stress):** 8.164%
- Full history @ stress: total 8.164%, CAGR 3.793%, benchmark -22.584%, sharpe 0.38, maxdd -0.135, trades 17

### Stochastic Failure Swing (111) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.09079059927985966 | -0.008387007722465256 |
| alpha | 0.169192966143765 | 0.16876183923770238 |
| trades | 9 | 8 |
| winrate | 0.5555555555555556 | 0.625 |
| sharpe | 0.6582866213671238 | -0.022278735261718995 |
| maxdd | -0.09572331785685106 | -0.07200088657197867 |
| pf | 1.7319684391630443 | 0.9096390148593565 |
| ann | 0.06331887470958919 | -0.011628713399311374 |

- **Combined OOS gain (stress):** 8.164%
- Full history @ stress: total 8.164%, CAGR 3.793%, benchmark -22.584%, sharpe 0.38, maxdd -0.135, trades 17

### MACD Parabolic SAR Wizard (2513) — Daily
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.059750952008728486 | -0.0017662579718149551 |
| alpha | 0.1166940089517855 | 0.1779620596875372 |
| trades | 14 | 5 |
| winrate | 0.35714285714285715 | 0.2 |
| sharpe | 0.33534260606856875 | 0.047357719664624945 |
| maxdd | -0.12112407831696503 | -0.05403641966098938 |
| pf | 1.2252956529930874 | 0.629025324758928 |
| ann | 0.041851889477829696 | -0.0024521070085494756 |

- **Combined OOS gain (stress):** 5.788%
- Full history @ stress: total 47.565%, CAGR 5.448%, benchmark -37.200%, sharpe 0.39, maxdd -0.170, trades 60

### Keltner RSI Divergence (311) — 4h
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.1942313083208016 | -0.03737715066561531 |
| alpha | 0.27263367518470694 | 0.13977169629455233 |
| trades | 11 | 7 |
| winrate | 0.5454545454545454 | 0.7142857142857143 |
| sharpe | 1.1638729998186994 | -0.3256764816662395 |
| maxdd | -0.05919880932162691 | -0.08083971113185862 |
| pf | 4.164863891373897 | 0.5776371704256084 |
| ann | 0.13360414733814796 | -0.051528686323172423 |

- **Combined OOS gain (stress):** 14.959%
- Full history @ stress: total 15.234%, CAGR 6.957%, benchmark -22.584%, sharpe 0.61, maxdd -0.087, trades 18

## 4322

### Stochastic Breakout (248) — 1h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.17950908257520481 | 0.10208416954985622 |
| alpha | 0.3276293833270846 | 0.32298476428222667 |
| trades | 34 | 17 |
| winrate | 0.4411764705882353 | 0.29411764705882354 |
| sharpe | 0.8432001492138638 | 0.7415103512943579 |
| maxdd | -0.15268011457002917 | -0.21986545288252302 |
| pf | 1.5339673875947302 | 1.363374749475503 |
| ann | 0.12371325774521913 | 0.14452994075103032 |

- **Combined OOS gain (stress):** 29.992%
- Full history @ stress: total 29.992%, CAGR 13.645%, benchmark -31.053%, sharpe 0.79, maxdd -0.220, trades 51

### RSI Expert Breakout (2972) — 30min
> family: breakout | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.475052687710402 | 0.09714498986095488 |
| alpha | 0.6180178919464081 | 0.3180455845933253 |
| trades | 11 | 7 |
| winrate | 0.9090909090909091 | 0.7142857142857143 |
| sharpe | 1.8894385453650921 | 0.8782991784512341 |
| maxdd | -0.08737630497548465 | -0.20115616715921036 |
| pf | 33.86398564188742 | 1.5163102489730342 |
| ann | 0.3160097105209265 | 0.13741251692316392 |

- **Combined OOS gain (stress):** 61.835%
- Full history @ stress: total 61.835%, CAGR 26.460%, benchmark -30.635%, sharpe 1.53, maxdd -0.201, trades 18

### Bullish & Bearish Harami Stochastic (3422) — 30min **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.2300270648568019 | 0.26103548691766454 |
| alpha | 0.372992269092808 | 0.481936081650035 |
| trades | 12 | 13 |
| winrate | 0.5833333333333334 | 0.3076923076923077 |
| sharpe | 0.7013903821390037 | 1.4567683637476476 |
| maxdd | -0.26720341854800533 | -0.15041063098030594 |
| pf | 1.452221006090243 | 2.125880094059509 |
| ann | 0.15750502878575134 | 0.380029596650284 |

- **Combined OOS gain (stress):** 55.111%
- Full history @ stress: total 55.111%, CAGR 23.870%, benchmark -30.635%, sharpe 0.94, maxdd -0.267, trades 25

### Neuro Nirvaman MQ4 (4093) — 30min
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.1058286157004047 | 0.10936234282482937 |
| alpha | 0.2487938199364108 | 0.3302629375571998 |
| trades | 47 | 29 |
| winrate | 0.40425531914893614 | 0.3793103448275862 |
| sharpe | 0.4837339808521972 | 0.8024596534004237 |
| maxdd | -0.2435557335415982 | -0.17267700990485146 |
| pf | 1.2133579479684897 | 1.3443263798079528 |
| ann | 0.07365452897490465 | 0.15504049668809494 |

- **Combined OOS gain (stress):** 22.676%
- Full history @ stress: total 23.752%, CAGR 10.952%, benchmark -30.635%, sharpe 0.62, maxdd -0.244, trades 76

### MACD Long (433) — 30min
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.2058337723256014 | 0.09486862327984813 |
| alpha | 0.3487989765616075 | 0.3157692180122186 |
| trades | 17 | 18 |
| winrate | 0.5882352941176471 | 0.3888888888888889 |
| sharpe | 1.0540534142486078 | 0.8695313791216024 |
| maxdd | -0.07711376165610162 | -0.1039788003683706 |
| pf | 2.3204949342552146 | 1.4141348081993308 |
| ann | 0.14137387493679787 | 0.13413643023713862 |

- **Combined OOS gain (stress):** 32.023%
- Full history @ stress: total 32.607%, CAGR 14.755%, benchmark -30.635%, sharpe 1.00, maxdd -0.104, trades 35

## 4323

### I Gap (2145) — 1h
> family: volatility | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.20130085146558385 | -0.010921322313339976 |
| alpha | 0.028972101388014093 | 0.22912766727637213 |
| trades | 163 | 77 |
| winrate | 0.31901840490797545 | 0.33766233766233766 |
| sharpe | -0.5613248438397564 | 0.030245067977980114 |
| maxdd | -0.27693355658323393 | -0.1657129403115145 |
| pf | 0.8406708962880481 | 1.007825826407224 |
| ann | -0.14682970033537512 | -0.015135077257118157 |

- **Combined OOS gain (stress):** -21.002%
- Full history @ stress: total -19.770%, CAGR -9.921%, benchmark -38.412%, sharpe -0.34, maxdd -0.277, trades 240

### Polarized Fractal Efficiency (2316) — 4h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.029040333681607633 | 0.12292786848191795 |
| alpha | 0.26405882936594793 | 0.370350548894289 |
| trades | 60 | 28 |
| winrate | 0.43333333333333335 | 0.5357142857142857 |
| sharpe | 0.20201175925960085 | 0.9700699806590506 |
| maxdd | -0.17031048467092158 | -0.08927032412009983 |
| pf | 1.0448260232067812 | 1.832084252730368 |
| ann | 0.020430042757228595 | 0.17470230519084806 |

- **Combined OOS gain (stress):** 15.554%
- Full history @ stress: total 18.660%, CAGR 8.454%, benchmark -38.792%, sharpe 0.52, maxdd -0.170, trades 88

### Adaptive Trend Flow (496) — Daily
> family: trend | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | 0.42002953239737395 | -0.2055011837156846 |
| alpha | 0.706540123255791 | 0.04237760416310332 |
| trades | 42 | 20 |
| winrate | 0.5714285714285714 | 0.4 |
| sharpe | 1.2238910977470896 | -1.6854338218571767 |
| maxdd | -0.17176715714958124 | -0.2501831114509432 |
| pf | 1.8010850301020624 | 0.4929600359012172 |
| ann | 0.2811353166843944 | -0.27347396255095147 |

- **Combined OOS gain (stress):** 12.821%
- Full history @ stress: total 525.116%, CAGR 33.382%, benchmark 244.650%, sharpe 1.06, maxdd -0.272, trades 174

### Demo GPT - Day Trading Scalping (675) — 4h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.23489205471560792 | 0.1001451417121122 |
| alpha | 0.4699105503999482 | 0.34756782212448323 |
| trades | 52 | 31 |
| winrate | 0.36538461538461536 | 0.5161290322580645 |
| sharpe | 0.824314156280611 | 0.7653029622168648 |
| maxdd | -0.11722144114957966 | -0.09238333589112269 |
| pf | 1.3958705877151947 | 1.4263414741405027 |
| ann | 0.16073752558393406 | 0.14173429396605242 |

- **Combined OOS gain (stress):** 35.856%
- Full history @ stress: total 39.508%, CAGR 17.109%, benchmark -38.792%, sharpe 0.86, maxdd -0.117, trades 83

### Futures Engulfing Candle Size (823) — 4h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.385787497484009 | 0.0653661434264774 |
| alpha | 0.6208059931683493 | 0.31278882383884843 |
| trades | 63 | 33 |
| winrate | 0.49206349206349204 | 0.5151515151515151 |
| sharpe | 1.1677275467755557 | 0.6681621743628883 |
| maxdd | -0.10078146445078617 | -0.08542213982362945 |
| pf | 1.6851365032062198 | 1.4620332984678805 |
| ann | 0.25923213327330763 | 0.09191793617641797 |

- **Combined OOS gain (stress):** 47.637%
- Full history @ stress: total 57.002%, CAGR 23.859%, benchmark -38.792%, sharpe 1.16, maxdd -0.101, trades 96

## 4324

### Order Block Finder (1145) — 4h **(pick)**
> family: other | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.34052535025960706 | 0.21434852832557572 |
| alpha | 0.6807122661474575 | 0.35407455572283597 |
| trades | 54 | 22 |
| winrate | 0.4074074074074074 | 0.45454545454545453 |
| sharpe | 0.8090759082385106 | 1.8234834383713876 |
| maxdd | -0.16309910262147131 | -0.07780135105271069 |
| pf | 1.4518875913037623 | 3.008941328356454 |
| ann | 0.23003430728668706 | 0.30958784218274293 |

- **Combined OOS gain (stress):** 62.786%
- Full history @ stress: total 64.231%, CAGR 26.532%, benchmark -41.308%, sharpe 0.98, maxdd -0.163, trades 76

### Renko Live Chart (1744) — 4h
> family: volatility | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.05931213836720861 | 0.08553921072061255 |
| alpha | 0.39949905425505905 | 0.2252652381178728 |
| trades | 83 | 30 |
| winrate | 0.42168674698795183 | 0.36666666666666664 |
| sharpe | 0.2925058074790521 | 0.7967668678924564 |
| maxdd | -0.26078237589332876 | -0.08187856565029117 |
| pf | 1.051994813044471 | 1.4473221533567795 |
| ann | 0.04154709410775714 | 0.12073747794262912 |

- **Combined OOS gain (stress):** 14.992%
- Full history @ stress: total 16.013%, CAGR 7.300%, benchmark -41.308%, sharpe 0.38, maxdd -0.261, trades 113

### Fibo Candles Trend (2219) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.10812053510480224 | 0.12631558469465243 |
| alpha | 0.4483074509926527 | 0.2660416120919127 |
| trades | 20 | 14 |
| winrate | 0.4 | 0.5 |
| sharpe | 0.38823504429182054 | 1.0084978824015671 |
| maxdd | -0.347144202732245 | -0.12005386520611339 |
| pf | 1.269721965519259 | 2.1149259463061973 |
| ann | 0.07522613525987887 | 0.17962691608635661 |

- **Combined OOS gain (stress):** 24.809%
- Full history @ stress: total 29.069%, CAGR 12.867%, benchmark -41.308%, sharpe 0.57, maxdd -0.347, trades 34

### ColorMaRsi Trigger MMRec Duplex (3161) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.10654611018360272 | 0.12561493663862366 |
| alpha | 0.44673302607145315 | 0.2653409640358839 |
| trades | 25 | 16 |
| winrate | 0.44 | 0.375 |
| sharpe | 0.5897426363231977 | 1.1713953613684307 |
| maxdd | -0.10638273910072726 | -0.1252700995220406 |
| pf | 1.344022822299605 | 1.9111821418893387 |
| ann | 0.07414662928541227 | 0.17860793423159094 |

- **Combined OOS gain (stress):** 24.554%
- Full history @ stress: total 25.660%, CAGR 11.443%, benchmark -41.308%, sharpe 0.82, maxdd -0.125, trades 41

### Futures Engulfing Candle Size (823) — 4h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.4322428324952079 | 0.0902763305509866 |
| alpha | 0.7724297483830583 | 0.23000235794824686 |
| trades | 50 | 30 |
| winrate | 0.44 | 0.43333333333333335 |
| sharpe | 0.8986372452541872 | 0.733380292138879 |
| maxdd | -0.19619471040501535 | -0.12220652242299912 |
| pf | 1.5253247841311819 | 1.424234957562715 |
| ann | 0.2889100200827275 | 0.12753538391889596 |

- **Combined OOS gain (stress):** 56.154%
- Full history @ stress: total 61.484%, CAGR 25.524%, benchmark -41.308%, sharpe 0.88, maxdd -0.196, trades 80

## 4325

### Stochastic (1341) — Daily
> family: mean_reversion | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.14255234205840117 | 0.2379364975978535 |
| alpha | 0.26101388051993957 | 0.26532577498713084 |
| trades | 8 | 7 |
| winrate | 0.375 | 0.5714285714285714 |
| sharpe | 0.8913374766860143 | 1.4909421891533559 |
| maxdd | -0.10986247545898442 | -0.0753034920123522 |
| pf | 3.1309991642201735 | 3.733363990888371 |
| ann | 0.0987231943009601 | 0.3450484910660343 |

- **Combined OOS gain (stress):** 41.441%
- Full history @ stress: total 41.441%, CAGR 26.104%, benchmark -14.410%, sharpe 1.17, maxdd -0.134, trades 15

### Color Schaff Trend Cycle (2129) — 4h
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.10616030254160091 | 0.2693315515813284 |
| alpha | 0.2328269692082675 | 0.2967208289706057 |
| trades | 8 | 6 |
| winrate | 0.5 | 0.6666666666666666 |
| sharpe | 0.596027145560259 | 1.5510813881489918 |
| maxdd | -0.18710349416237093 | -0.0750514709123824 |
| pf | 1.5424373890784253 | 5.946568808818837 |
| ann | 0.07388203114555547 | 0.3926543238245792 |

- **Combined OOS gain (stress):** 40.408%
- Full history @ stress: total 40.408%, CAGR 25.487%, benchmark -14.410%, sharpe 1.00, maxdd -0.187, trades 14

### 1H Bollinger Bands (3200) — Daily **(pick)**
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.17280947870120067 | 0.2624227850208327 |
| alpha | 0.29127101716273907 | 0.28981206241011004 |
| trades | 7 | 6 |
| winrate | 0.5714285714285714 | 0.6666666666666666 |
| sharpe | 0.8167067510581314 | 1.5275801521629553 |
| maxdd | -0.1350205521195198 | -0.07292453747557337 |
| pf | 2.4482075570191317 | 6.23065918237849 |
| ann | 0.1192002530400913 | 0.38213850742806943 |

- **Combined OOS gain (stress):** 48.058%
- Full history @ stress: total 48.058%, CAGR 30.020%, benchmark -14.410%, sharpe 1.09, maxdd -0.135, trades 13

### Macd Pattern Trader v03 (StockSharp port) (3954) — Daily
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.14822761203600088 | 0.20949061035997674 |
| alpha | 0.2666891504975393 | 0.23687988774925406 |
| trades | 8 | 7 |
| winrate | 0.5 | 0.5714285714285714 |
| sharpe | 0.7381076674833158 | 1.2088721137352383 |
| maxdd | -0.12893012164985485 | -0.16722793078173803 |
| pf | 2.068284237245601 | 6.011949449739819 |
| ann | 0.10257604661770281 | 0.30231778544935817 |

- **Combined OOS gain (stress):** 38.877%
- Full history @ stress: total 38.877%, CAGR 24.570%, benchmark -14.410%, sharpe 0.93, maxdd -0.167, trades 15

### OsMaMaster (4197) — Daily
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.14822761203600088 | 0.20949061035997674 |
| alpha | 0.2666891504975393 | 0.23687988774925406 |
| trades | 8 | 7 |
| winrate | 0.5 | 0.5714285714285714 |
| sharpe | 0.7381076674833158 | 1.2088721137352383 |
| maxdd | -0.12893012164985485 | -0.16722793078173803 |
| pf | 2.068284237245601 | 6.011949449739819 |
| ann | 0.10257604661770281 | 0.30231778544935817 |

- **Combined OOS gain (stress):** 38.877%
- Full history @ stress: total 38.877%, CAGR 24.570%, benchmark -14.410%, sharpe 0.93, maxdd -0.167, trades 15

## 4326

### Smoothing Average (1968) — 15min
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.0014107919240009537 | 0.008112174823274199 |
| alpha | 0.31469750521071427 | 0.40711714994765236 |
| trades | 7 | 10 |
| winrate | 0.42857142857142855 | 0.3 |
| sharpe | 0.09639515850445206 | 0.17530971070980633 |
| maxdd | -0.05570668011456614 | -0.05312387713697975 |
| pf | 1.044207195579614 | 1.1580380516823277 |
| ann | 0.0009964896033667348 | 0.011283789287303225 |

- **Combined OOS gain (stress):** 0.953%
- Full history @ stress: total 0.953%, CAGR 0.926%, benchmark -57.762%, sharpe 0.15, maxdd -0.066, trades 17

### Ingrit (3195) — 1h
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.005026225530000206 | 0.011042919113228633 |
| alpha | 0.3045982654729388 | 0.4124304315017321 |
| trades | 5 | 10 |
| winrate | 0.2 | 0.3 |
| sharpe | 0.23439336151367063 | 0.22347006006011824 |
| maxdd | -0.04600002359274169 | -0.0908363478614419 |
| pf | 1.1416014018356948 | 1.113593890521972 |
| ann | 0.00354831257772803 | 0.015369069090748644 |

- **Combined OOS gain (stress):** 1.612%
- Full history @ stress: total 1.612%, CAGR 1.566%, benchmark -56.919%, sharpe 0.23, maxdd -0.091, trades 15

### CorrTime (3319) — 30min
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | -0.00834626303079955 | -0.005629132058797559 |
| alpha | 0.2748654158013172 | 0.3957583803297059 |
| trades | 5 | 8 |
| winrate | 0.4 | 0.25 |
| sharpe | -0.10791407764330618 | -0.09542237041988993 |
| maxdd | -0.0632798590431004 | -0.04542057767065 |
| pf | 0.8814785581707408 | 0.8921355920575403 |
| ann | -0.005903714013487549 | -0.0078090800886569944 |

- **Combined OOS gain (stress):** -1.393%
- Full history @ stress: total -1.393%, CAGR -1.353%, benchmark -55.912%, sharpe -0.09, maxdd -0.098, trades 13

### Chart Oscillator (616) — 1h **(pick)**
> family: mean_reversion | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.04333332449000071 | 0.017993765667532413 |
| alpha | 0.3429053644329393 | 0.41938127805603587 |
| trades | 5 | 6 |
| winrate | 0.4 | 0.3333333333333333 |
| sharpe | 1.0519783509146226 | 0.5363504626875357 |
| maxdd | -0.024414865237557315 | -0.03536182995212411 |
| pf | 2.4138652936567557 | 1.589658185629659 |
| ann | 0.030422969802293975 | 0.02507653158316603 |

- **Combined OOS gain (stress):** 6.211%
- Full history @ stress: total 6.211%, CAGR 6.028%, benchmark -56.919%, sharpe 0.71, maxdd -0.054, trades 11

## 5110

### Rampok Scalp (1725) — 4h **(pick)**
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | -0.006865349593597969 | 0.2743998317288443 |
| alpha | 0.1661204323969233 | 0.1465010263880151 |
| trades | 14 | 6 |
| winrate | 0.5 | 0.6666666666666666 |
| sharpe | 0.008649219772985177 | 1.8884304288567668 |
| maxdd | -0.11084506867844823 | -0.08248713295390231 |
| pf | 0.9552999806846143 | 4.530734395704619 |
| ann | -0.00485513147606742 | 0.4003829096098901 |

- **Combined OOS gain (stress):** 26.565%
- Full history @ stress: total 26.565%, CAGR 11.823%, benchmark -4.917%, sharpe 0.86, maxdd -0.170, trades 20

### Follow Your Heart (1769) — 4h
> family: volatility | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | -0.0013352243591999713 | 0.2374427427147885 |
| alpha | 0.1716505576313213 | 0.10954393737395929 |
| trades | 5 | 6 |
| winrate | 0.4 | 0.3333333333333333 |
| sharpe | 0.011020828708086954 | 2.3509749691528663 |
| maxdd | -0.05914570562389021 | -0.05729159537142303 |
| pf | 0.9638320078248915 | 7.5561019917610235 |
| ann | -0.0009434938472392407 | 0.3443034987770366 |

- **Combined OOS gain (stress):** 23.579%
- Full history @ stress: total 23.579%, CAGR 10.564%, benchmark -4.917%, sharpe 1.18, maxdd -0.059, trades 11

### Raymond Cloudy Day (3674) — 4h
> family: breakout | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | -0.014174450048000109 | 0.20513303041399888 |
| alpha | 0.15881133194252117 | 0.07723422507316968 |
| trades | 8 | 5 |
| winrate | 0.25 | 0.4 |
| sharpe | -0.13415496867319138 | 2.1607185434202245 |
| maxdd | -0.08830640830809822 | -0.04435494457722722 |
| pf | 0.8044690655042909 | 5.9705394430607335 |
| ann | -0.010034920929698044 | 0.295806153909435 |

- **Combined OOS gain (stress):** 18.805%
- Full history @ stress: total 18.805%, CAGR 8.517%, benchmark -4.917%, sharpe 0.97, maxdd -0.088, trades 13

## 6001

### Parabolic SAR Bug5 (1626) — 4h **(pick)**
> family: momentum | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | -0.006836204478397945 | 0.2685964993700205 |
| alpha | 0.40119438825582765 | 0.37350447483014326 |
| trades | 18 | 7 |
| winrate | 0.5 | 0.7142857142857143 |
| sharpe | 0.0738002356501905 | 2.113747109858072 |
| maxdd | -0.24134271258326923 | -0.06586351751558328 |
| pf | 0.9842786687887433 | 6.676592993884329 |
| ann | -0.0048344994555710175 | 0.3915344424434821 |

- **Combined OOS gain (stress):** 25.992%
- Full history @ stress: total 28.854%, CAGR 12.778%, benchmark -44.207%, sharpe 0.74, maxdd -0.241, trades 25

### EMA Sticker (1656) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.03169366848400701 | 0.10501117745463406 |
| alpha | 0.4397242612182326 | 0.20991915291475682 |
| trades | 59 | 29 |
| winrate | 0.423728813559322 | 0.4827586206896552 |
| sharpe | 0.2125756362973944 | 0.9116274326302435 |
| maxdd | -0.2561239561198635 | -0.07824939373129769 |
| pf | 1.0697405672087708 | 1.7522217171563532 |
| ann | 0.022288182540959323 | 0.14875365768416593 |

- **Combined OOS gain (stress):** 14.003%
- Full history @ stress: total 20.065%, CAGR 9.062%, benchmark -44.207%, sharpe 0.51, maxdd -0.256, trades 88

### Kalman Filter Candles (2152) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.030787569809193838 | 0.09368634796844066 |
| alpha | 0.37724302292503176 | 0.19859432342856342 |
| trades | 44 | 34 |
| winrate | 0.4318181818181818 | 0.35294117647058826 |
| sharpe | 0.03342632653541157 | 0.8256791285472538 |
| maxdd | -0.2354161039942848 | -0.09102066448640123 |
| pf | 1.1092405998754489 | 1.1521217432905477 |
| ann | -0.021850399457191028 | 0.1324359750351034 |

- **Combined OOS gain (stress):** 6.001%
- Full history @ stress: total 11.641%, CAGR 5.362%, benchmark -44.207%, sharpe 0.34, maxdd -0.235, trades 78

### The 20s Breakout (2986) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.37596505960400806 | 0.11776047994438543 |
| alpha | 0.7839956523382337 | 0.2226684554045082 |
| trades | 56 | 25 |
| winrate | 0.35714285714285715 | 0.44 |
| sharpe | 1.2978058579320804 | 1.0754667207524045 |
| maxdd | -0.1497700699644009 | -0.07051878667177125 |
| pf | 1.637095484588734 | 1.8800295636897841 |
| ann | 0.2529199289432331 | 0.16720176531621012 |

- **Combined OOS gain (stress):** 53.800%
- Full history @ stress: total 57.293%, CAGR 23.968%, benchmark -44.207%, sharpe 1.28, maxdd -0.150, trades 81

### Fast Slow RVI Crossover (3520) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.020614878534407133 | 0.06710911066607439 |
| alpha | 0.4286454712686327 | 0.17201708612619715 |
| trades | 63 | 34 |
| winrate | 0.4603174603174603 | 0.29411764705882354 |
| sharpe | 0.17866395635928298 | 0.6333413479119362 |
| maxdd | -0.21700381285596393 | -0.1419417978123655 |
| pf | 1.0615610082410505 | 1.3147639160481053 |
| ann | 0.01452031756608152 | 0.09439965662905792 |

- **Combined OOS gain (stress):** 8.911%
- Full history @ stress: total 14.703%, CAGR 6.724%, benchmark -44.207%, sharpe 0.42, maxdd -0.217, trades 97

## 6002

### RSI Buy Sell Force (1264) — Daily
> family: trend | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.21405581392576234 | 0.09411929047240819 |
| alpha | 0.23304698981255545 | 0.15889126667862108 |
| trades | 22 | 12 |
| winrate | 0.36363636363636365 | 0.3333333333333333 |
| sharpe | -0.5078607080604131 | 0.6036606662087179 |
| maxdd | -0.4070547071231858 | -0.1748822755261611 |
| pf | 0.7361862197335628 | 1.6788408432791517 |
| ann | -0.15647809589758255 | 0.1330585891795164 |

- **Combined OOS gain (stress):** -14.008%
- Full history @ stress: total 313.518%, CAGR 8.911%, benchmark 38.599%, sharpe 0.46, maxdd -0.407, trades 334

### NRTR Trailing Stop (2237) — Daily
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | -0.038887537545389095 | 0.06108808110839026 |
| alpha | 0.4082152661929287 | 0.12586005731460315 |
| trades | 14 | 6 |
| winrate | 0.42857142857142855 | 0.3333333333333333 |
| sharpe | 0.049687514495508615 | 0.42981564033808506 |
| maxdd | -0.33724672067732053 | -0.17432221486945854 |
| pf | 1.5982784102275598 | 0.4596035573927437 |
| ann | -0.027632738401746626 | 0.08583331880498402 |

- **Combined OOS gain (stress):** 1.982%
- Full history @ stress: total 351.281%, CAGR 9.485%, benchmark 38.599%, sharpe 0.53, maxdd -0.337, trades 144

### The 20s Breakout (2986) — 4h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.0909120425000054 | 0.34467808377076925 |
| alpha | 0.49142442507899775 | 0.40945005997698214 |
| trades | 56 | 29 |
| winrate | 0.26785714285714285 | 0.5517241379310345 |
| sharpe | 0.4032438502053479 | 1.8302964967607047 |
| maxdd | -0.19080074851562112 | -0.07879196836715008 |
| pf | 1.1330267342324432 | 2.5046102908419696 |
| ann | 0.06340250969712158 | 0.5087697918924621 |

- **Combined OOS gain (stress):** 46.693%
- Full history @ stress: total 51.801%, CAGR 21.895%, benchmark -39.582%, sharpe 1.00, maxdd -0.191, trades 85

### 5 EMA No-Touch Breakout (483) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.20694426548360756 | 0.24336491329636334 |
| alpha | 0.6074566480625999 | 0.30813688950257623 |
| trades | 64 | 36 |
| winrate | 0.296875 | 0.5277777777777778 |
| sharpe | 0.7541138916531944 | 1.4335606627643431 |
| maxdd | -0.18627811281917206 | -0.08906166036268637 |
| pf | 1.2961851428878775 | 1.8955475737488223 |
| ann | 0.1421163765042368 | 0.3532466599538111 |

- **Combined OOS gain (stress):** 50.067%
- Full history @ stress: total 55.293%, CAGR 23.218%, benchmark -39.582%, sharpe 1.07, maxdd -0.186, trades 100

### Futures Engulfing Candle Size (823) — 4h
> family: pattern | params: `{}` | flags: win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.10088203368439497 | 0.2423791236093067 |
| alpha | 0.2996303488945974 | 0.3071510998155196 |
| trades | 73 | 35 |
| winrate | 0.3287671232876712 | 0.4857142857142857 |
| sharpe | -0.2270384391574601 | 1.5135532810230687 |
| maxdd | -0.31018097504725595 | -0.05363303270456887 |
| pf | 0.8834348648246146 | 2.0404306630519318 |
| ann | -0.07237505365462693 | 0.3517568524666994 |

- **Combined OOS gain (stress):** 11.705%
- Full history @ stress: total 15.594%, CAGR 7.116%, benchmark -39.582%, sharpe 0.42, maxdd -0.310, trades 108

## 6004

### Hercules A.T.C. 2006 (2485) — Daily
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.08167090102910124 | 0.01982663461343992 |
| alpha | 0.39256283927953006 | 0.21457632936313464 |
| trades | 28 | 15 |
| winrate | 0.39285714285714285 | 0.4 |
| sharpe | 0.4258599903298307 | 0.261921439639548 |
| maxdd | -0.13849011833509695 | -0.09076498821489676 |
| pf | 1.2474615126868105 | 1.2038894866649648 |
| ann | 0.05703052377083506 | 0.02764059629048843 |

- **Combined OOS gain (stress):** 10.312%
- Full history @ stress: total 193.229%, CAGR 7.870%, benchmark 6.371%, sharpe 0.54, maxdd -0.404, trades 303

### RSI Expert Breakout (2972) — 15min **(pick)**
> family: breakout | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.021015435160002482 | 0.03201868980842404 |
| alpha | 0.31846069063445503 | 0.23503983784467775 |
| trades | 15 | 6 |
| winrate | 0.4666666666666667 | 0.5 |
| sharpe | 0.1971943299929165 | 0.5801418893189799 |
| maxdd | -0.0747344069313125 | -0.058829727758727746 |
| pf | 1.1998863428832696 | 1.717956547021616 |
| ann | 0.014801596653217564 | 0.04474200823391361 |

- **Combined OOS gain (stress):** 5.371%
- Full history @ stress: total 5.371%, CAGR 2.513%, benchmark -39.827%, sharpe 0.31, maxdd -0.075, trades 21

### Explosion Range Expansion (3263) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.19051997056200687 | -0.017470573748112672 |
| alpha | 0.4853917654338018 | 0.17332697226415728 |
| trades | 62 | 36 |
| winrate | 0.41935483870967744 | 0.3333333333333333 |
| sharpe | 0.7730065324651456 | -0.09865553939994663 |
| maxdd | -0.137139052264731 | -0.07721171904405466 |
| pf | 1.3652384501139785 | 1.0357222239879111 |
| ann | 0.13111413537882566 | -0.0241801453150422 |

- **Combined OOS gain (stress):** 16.972%
- Full history @ stress: total 20.008%, CAGR 9.037%, benchmark -39.606%, sharpe 0.59, maxdd -0.137, trades 98

### CorrTime (3319) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.013283483420000186 | 0.04392222048640049 |
| alpha | 0.3081552782917951 | 0.23471976649867043 |
| trades | 9 | 8 |
| winrate | 0.4444444444444444 | 0.5 |
| sharpe | 0.1497477673643262 | 0.5809669942220694 |
| maxdd | -0.08210738462849765 | -0.06159827256369943 |
| pf | 1.1953337889588953 | 1.9333068670126587 |
| ann | 0.009366320274561524 | 0.06151467660546728 |

- **Combined OOS gain (stress):** 5.779%
- Full history @ stress: total 5.779%, CAGR 2.701%, benchmark -39.606%, sharpe 0.32, maxdd -0.099, trades 17

### FVG Breakout Lite (825) — Daily
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.03828051385488973 | 0.037580371092644116 |
| alpha | 0.2726114243955391 | 0.23233006584233884 |
| trades | 24 | 8 |
| winrate | 0.4166666666666667 | 0.5 |
| sharpe | -0.08445423532617442 | 0.52374752300581 |
| maxdd | -0.21763994938679931 | -0.04747522987083519 |
| pf | 0.8975005913894379 | 1.742378203516447 |
| ann | -0.02719890678872139 | 0.05256938611266104 |

- **Combined OOS gain (stress):** -0.214%
- Full history @ stress: total 360.460%, CAGR 11.352%, benchmark 6.371%, sharpe 0.76, maxdd -0.284, trades 225

## 6010

### Up3x1 Investor (2662) — 4h
> family: volatility | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.05831984078080388 | 0.05233412305559604 |
| alpha | 0.3879494704104335 | 0.30839881308255024 |
| trades | 27 | 13 |
| winrate | 0.4074074074074074 | 0.46153846153846156 |
| sharpe | 0.4995663659835256 | 0.7838676574427853 |
| maxdd | -0.10109651235064598 | -0.06979597468576282 |
| pf | 1.2843377330278039 | 1.5140358447971747 |
| ann | 0.04085771787830006 | 0.07341243670823316 |

- **Combined OOS gain (stress):** 11.371%
- Full history @ stress: total 11.371%, CAGR 5.241%, benchmark -48.889%, sharpe 0.60, maxdd -0.106, trades 40

### Alexav SpeedUp M1 (2790) — 4h
> family: volatility | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.07430335343320427 | 0.07118880420767204 |
| alpha | 0.4039329830628339 | 0.32725349423462624 |
| trades | 27 | 13 |
| winrate | 0.4444444444444444 | 0.5384615384615384 |
| sharpe | 0.6008174673034662 | 1.0144091274254148 |
| maxdd | -0.1087528977236153 | -0.06047808588198289 |
| pf | 1.3420847017699233 | 1.8279856896859108 |
| ann | 0.05193897150738147 | 0.10021468084145502 |

- **Combined OOS gain (stress):** 15.078%
- Full history @ stress: total 15.078%, CAGR 6.889%, benchmark -48.889%, sharpe 0.75, maxdd -0.113, trades 40

### Explosion (3261) — 4h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.17671370908480566 | 0.039978163434323255 |
| alpha | 0.5063433387144353 | 0.29604285346127746 |
| trades | 46 | 18 |
| winrate | 0.32608695652173914 | 0.3888888888888889 |
| sharpe | 0.981729812897744 | 0.39669157387747855 |
| maxdd | -0.08493454209715601 | -0.1303679092589387 |
| pf | 1.558900664654164 | 1.2491479567798933 |
| ann | 0.12183114809731332 | 0.05594902263033541 |

- **Combined OOS gain (stress):** 22.376%
- Full history @ stress: total 22.376%, CAGR 10.052%, benchmark -48.889%, sharpe 0.73, maxdd -0.130, trades 64

### Raymond Cloudy Day (3674) — 30min
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.03487035970559349 | 0.03511543242839821 |
| alpha | 0.2996884638238182 | 0.2879578796400928 |
| trades | 44 | 21 |
| winrate | 0.29545454545454547 | 0.2857142857142857 |
| sharpe | -0.16142332633016906 | 0.3813914424334172 |
| maxdd | -0.17775516059989172 | -0.0949593739254252 |
| pf | 0.9246608481065065 | 1.2186404104461974 |
| ann | -0.024763207844811674 | 0.049098272122158226 |

- **Combined OOS gain (stress):** -0.098%
- Full history @ stress: total -0.098%, CAGR -0.046%, benchmark -49.265%, sharpe 0.06, maxdd -0.190, trades 65

### Hammer & Shooting Star (867) — 4h **(pick)**
> family: pattern | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.11770118628160398 | 0.10047334876363578 |
| alpha | 0.4473308159112336 | 0.35653803879059 |
| trades | 22 | 6 |
| winrate | 0.5 | 0.5 |
| sharpe | 0.8548420543385001 | 1.8619275920136955 |
| maxdd | -0.08027239422225396 | -0.020769284224430806 |
| pf | 1.511730279708652 | 6.3669080770603745 |
| ann | 0.0817854452135578 | 0.14220736093831654 |

- **Combined OOS gain (stress):** 23.000%
- Full history @ stress: total 23.000%, CAGR 10.318%, benchmark -48.889%, sharpe 1.12, maxdd -0.080, trades 28

## 6013

### Bull vs Medved (2510) — 4h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.5179793485200026 | 0.07285091036945102 |
| alpha | 0.5589629550773797 | 0.3477176954493799 |
| trades | 18 | 10 |
| winrate | 0.5555555555555556 | 0.6 |
| sharpe | 1.334107084064526 | 0.4995324777984192 |
| maxdd | -0.15315717311784827 | -0.13043972730457087 |
| pf | 2.741988992064194 | 1.7375309370481309 |
| ann | 0.34295249665771044 | 0.10258624883382961 |

- **Combined OOS gain (stress):** 62.857%
- Full history @ stress: total 67.568%, CAGR 27.786%, benchmark -25.638%, sharpe 1.09, maxdd -0.153, trades 28

### CCI MA v1.5 (3993) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.1923463629240041 | 0.12156272663804901 |
| alpha | 0.23332996948138118 | 0.3964295117179779 |
| trades | 29 | 16 |
| winrate | 0.4482758620689655 | 0.375 |
| sharpe | 0.7461812798511334 | 0.8105429911786177 |
| maxdd | -0.18549356134570394 | -0.12119490210069384 |
| pf | 1.422215468247557 | 1.5288158793890039 |
| ann | 0.13233978343909225 | 0.17271947489954576 |

- **Combined OOS gain (stress):** 33.729%
- Full history @ stress: total 33.729%, CAGR 14.803%, benchmark -25.638%, sharpe 0.77, maxdd -0.185, trades 45

### Moving Average with Frames (4112) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.2891543407160033 | 0.040416972328591205 |
| alpha | 0.3301379472733804 | 0.3152837574085201 |
| trades | 23 | 14 |
| winrate | 0.4782608695652174 | 0.35714285714285715 |
| sharpe | 0.9015451050535565 | 0.335263952253548 |
| maxdd | -0.21454785294407352 | -0.10664346704820271 |
| pf | 2.1611899269163795 | 1.21145115111339 |
| ann | 0.19654264731244941 | 0.05656784249575786 |

- **Combined OOS gain (stress):** 34.126%
- Full history @ stress: total 34.126%, CAGR 14.965%, benchmark -25.638%, sharpe 0.69, maxdd -0.215, trades 37

### Long Explosive V1 (992) — 4h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.1770935942680052 | -0.036730978197752506 |
| alpha | 0.2180772008253823 | 0.2381358068821764 |
| trades | 56 | 32 |
| winrate | 0.39285714285714285 | 0.40625 |
| sharpe | 0.5909012690898562 | -0.0708894688084824 |
| maxdd | -0.2442662200921064 | -0.1584872013951122 |
| pf | 1.2047063278401564 | 0.9802415513097316 |
| ann | 0.12208699970086578 | -0.05064437004667166 |

- **Combined OOS gain (stress):** 13.386%
- Full history @ stress: total 16.665%, CAGR 7.596%, benchmark -25.638%, sharpe 0.41, maxdd -0.244, trades 88

## 6014

### Volume Climax Reversal (115) — 30min
> family: volume | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.021786904569494947 | 0.08396113788599657 |
| alpha | 0.5243057962571525 | 0.12151530254656473 |
| trades | 9 | 6 |
| winrate | 0.4444444444444444 | 0.6666666666666666 |
| sharpe | 0.27590287217393406 | 1.2346713384262684 |
| maxdd | -0.07084569394472096 | -0.05391750968148623 |
| pf | 1.290060946982307 | 3.388045977807447 |
| ann | 0.015343247067482357 | 0.11847545441249507 |

- **Combined OOS gain (stress):** 10.758%
- Full history @ stress: total 10.758%, CAGR 5.109%, benchmark -49.647%, sharpe 0.68, maxdd -0.081, trades 15

### TSI DeMarker (1845) — Daily
> family: trend | params: `{}` | flags: thin_trades;win_below_-10%

| metric | validation | test |
|---|---|---|
| eng | -0.13963894462836002 | 0.04350457644647365 |
| alpha | 0.34272913773972236 | 0.08105874110704181 |
| trades | 18 | 5 |
| winrate | 0.4444444444444444 | 0.4 |
| sharpe | -0.6219640524418423 | 0.42456198288844765 |
| maxdd | -0.22712158313130149 | -0.0880764278794437 |
| pf | 0.6312061853723497 | 1.6017282815394516 |
| ann | -0.10080626578836682 | 0.06092493081988004 |

- **Combined OOS gain (stress):** -10.221%
- Full history @ stress: total 1.190%, CAGR 0.288%, benchmark -67.230%, sharpe 0.09, maxdd -0.298, trades 38

### Rollback Rebound (2856) — Daily **(pick)**
> family: volatility | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.0647496173921529 | 0.12817885997454792 |
| alpha | 0.5471176997602353 | 0.16573302463511608 |
| trades | 26 | 16 |
| winrate | 0.38461538461538464 | 0.4375 |
| sharpe | 0.4350687085586235 | 1.2424887425380438 |
| maxdd | -0.07957509207376123 | -0.08749481934643377 |
| pf | 1.2932857538301223 | 2.029175044796873 |
| ann | 0.04532130074257701 | 0.18233795449867518 |

- **Combined OOS gain (stress):** 20.123%
- Full history @ stress: total 41.282%, CAGR 8.755%, benchmark -67.230%, sharpe 0.73, maxdd -0.105, trades 78

## 6015

### Gold Scalping BOS & CHoCH (849) — 30min **(pick)**
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.0405175058075975 | 0.45441537809817834 |
| alpha | 0.3954686533619527 | 0.030885966333472403 |
| trades | 20 | 8 |
| winrate | 0.3 | 0.75 |
| sharpe | -0.1083247707307399 | 2.2045937853556192 |
| maxdd | -0.16849757248348263 | -0.05091613394756955 |
| pf | 0.8447230174425548 | 22.036473671205833 |
| ann | -0.028798052787644246 | 0.6824377660859442 |

- **Combined OOS gain (stress):** 39.549%
- Full history @ stress: total 42.210%, CAGR 18.734%, benchmark -16.263%, sharpe 0.96, maxdd -0.173, trades 28

## 6016

### US Index First 30m Candle (1515) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.4388962670785428 | 0.0962775416921986 |
| alpha | 0.23748567496772255 | 0.39300928584061856 |
| trades | 69 | 26 |
| winrate | 0.37681159420289856 | 0.38461538461538464 |
| sharpe | 0.7771880141692069 | 0.9243518600834547 |
| maxdd | -0.21496082456215315 | -0.09281236105998592 |
| pf | 1.3843808298474292 | 1.4303453305851404 |
| ann | 0.29313725046612293 | 0.13616379646979615 |

- **Combined OOS gain (stress):** 57.743%
- Full history @ stress: total 57.743%, CAGR 24.136%, benchmark 37.681%, sharpe 0.74, maxdd -0.215, trades 95

### Adaptive Renko (1899) — 4h
> family: volatility | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.5640169572999969 | 0.1800203128662099 |
| alpha | 0.36260636518917666 | 0.47675205701462986 |
| trades | 46 | 15 |
| winrate | 0.391304347826087 | 0.4666666666666667 |
| sharpe | 0.9693965921915234 | 1.7865974060877468 |
| maxdd | -0.15594052769441524 | -0.049632887511792845 |
| pf | 1.8749419498513102 | 3.584630171151859 |
| ann | 0.37160053150197503 | 0.25845853841695177 |

- **Combined OOS gain (stress):** 84.557%
- Full history @ stress: total 84.557%, CAGR 33.733%, benchmark 37.681%, sharpe 1.00, maxdd -0.156, trades 61

### Hercules A.T.C. 2006 (2485) — 4h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.6709599704691569 | 0.13982140553145928 |
| alpha | 0.46954937835833666 | 0.43655314967987924 |
| trades | 54 | 21 |
| winrate | 0.37037037037037035 | 0.47619047619047616 |
| sharpe | 1.0395174744216213 | 1.2069807420192467 |
| maxdd | -0.15879221190261406 | -0.055145978998213496 |
| pf | 1.6500919928072084 | 1.8038599604719858 |
| ann | 0.4372124915157427 | 0.19931705310639858 |

- **Combined OOS gain (stress):** 90.460%
- Full history @ stress: total 90.460%, CAGR 35.745%, benchmark 37.681%, sharpe 0.99, maxdd -0.170, trades 75

### Bullish & Bearish Engulfing (2626) — 15min
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.6553672733548648 | 0.09941005560132088 |
| alpha | 0.4440576861803456 | 0.3999142933440524 |
| trades | 28 | 15 |
| winrate | 0.5 | 0.4666666666666667 |
| sharpe | 1.0299013117813278 | 0.600964727110516 |
| maxdd | -0.18772860216908194 | -0.16897037161233763 |
| pf | 2.103975525541523 | 3.264979605105332 |
| ann | 0.4277245363154054 | 0.14067496381545475 |

- **Combined OOS gain (stress):** 81.993%
- Full history @ stress: total 193.322%, CAGR 66.604%, benchmark 38.815%, sharpe 1.12, maxdd -0.188, trades 43

### Futures Engulfing Candle Size (823) — 4h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 1.1150430803862603 | 0.10326771480983843 |
| alpha | 0.9136324882754401 | 0.3999994589582584 |
| trades | 61 | 29 |
| winrate | 0.4918032786885246 | 0.41379310344827586 |
| sharpe | 1.3482833838910528 | 0.7712566969935555 |
| maxdd | -0.16073976139889545 | -0.11393041564876705 |
| pf | 1.7410356275701409 | 2.371984779936139 |
| ann | 0.6975845745940135 | 0.14623729002705166 |

- **Combined OOS gain (stress):** 133.346%
- Full history @ stress: total 275.334%, CAGR 87.273%, benchmark 37.681%, sharpe 1.32, maxdd -0.161, trades 90

## 6018

### Ride Alligator (1673) — 1h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.014532390540797024 | 0.07778014622450447 |
| alpha | 0.11046760945920286 | 0.12772069319239987 |
| trades | 20 | 36 |
| winrate | 0.4 | 0.3333333333333333 |
| sharpe | -0.019407613287877983 | 0.5833042493673861 |
| maxdd | -0.1809145075131834 | -0.1212100456840014 |
| pf | 0.9317923725190801 | 1.2759824000587423 |
| ann | -0.010288873997629344 | 0.10962790186109839 |

- **Combined OOS gain (stress):** 6.212%
- Full history @ stress: total 7.739%, CAGR 6.599%, benchmark -12.390%, sharpe 0.39, maxdd -0.196, trades 56

### Gazonkos Rollback (2492) — Daily
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.05294525337920164 | 0.055224131208900795 |
| alpha | 0.16584847918565337 | 0.10403365501842465 |
| trades | 14 | 18 |
| winrate | 0.2857142857142857 | 0.2777777777777778 |
| sharpe | 0.5018847332171907 | 0.4777596725464057 |
| maxdd | -0.15984177162681912 | -0.11895273182896615 |
| pf | 1.21366699910835 | 1.2337636817387185 |
| ann | 0.037120542203949336 | 0.07750860859472097 |

- **Combined OOS gain (stress):** 11.109%
- Full history @ stress: total 11.109%, CAGR 9.453%, benchmark -14.086%, sharpe 0.47, maxdd -0.208, trades 32

### Raymond Cloudy Day (3674) — 15min
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.10171309950880358 | 0.013420246583652151 |
| alpha | 0.09540792926920694 | 0.06336079355154756 |
| trades | 31 | 48 |
| winrate | 0.2903225806451613 | 0.3333333333333333 |
| sharpe | 0.9066760750719294 | 0.19183765486952142 |
| maxdd | -0.19486003841022392 | -0.12521868440151385 |
| pf | 1.2328572387272652 | 1.0338014601400005 |
| ann | 0.07083005058152558 | 0.01868630372891089 |

- **Combined OOS gain (stress):** 11.650%
- Full history @ stress: total 9.458%, CAGR 8.057%, benchmark 0.757%, sharpe 0.44, maxdd -0.267, trades 80

### FVG Breakout Lite (825) — 1h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.16596096675600314 | -0.020505167354095022 |
| alpha | 0.290960966756003 | 0.029435379613800383 |
| trades | 32 | 47 |
| winrate | 0.25 | 0.3404255319148936 |
| sharpe | 1.0647857702441785 | 0.004747318768561998 |
| maxdd | -0.17827168421150474 | -0.19433092373301675 |
| pf | 1.332981040443683 | 1.0108666300193005 |
| ann | 0.11457911226719819 | -0.028363244001921584 |

- **Combined OOS gain (stress):** 14.205%
- Full history @ stress: total 17.274%, CAGR 14.639%, benchmark -12.390%, sharpe 0.59, maxdd -0.268, trades 79

### Long Explosive V1 (992) — 15min **(pick)**
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.3089651595644063 | 0.11728082982137145 |
| alpha | 0.30265998932480964 | 0.16722137678926685 |
| trades | 39 | 28 |
| winrate | 0.38461538461538464 | 0.5 |
| sharpe | 1.7260396202047652 | 0.7263118773605202 |
| maxdd | -0.29215016782686243 | -0.20513270142401097 |
| pf | 1.3555375682554685 | 1.3727865312559742 |
| ann | 0.20950402749970953 | 0.16650622871392096 |

- **Combined OOS gain (stress):** 46.248%
- Full history @ stress: total 49.625%, CAGR 41.269%, benchmark 0.757%, sharpe 1.24, maxdd -0.364, trades 67

## 6020

### Stochastic Breakout (248) — 4h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.22724653671600126 | 0.0210576045621238 |
| alpha | 0.3412816244352995 | 0.313740531391392 |
| trades | 13 | 8 |
| winrate | 0.38461538461538464 | 0.25 |
| sharpe | 1.2767845839144105 | 0.25595173990770204 |
| maxdd | -0.13230246723135475 | -0.10151769662894017 |
| pf | 2.186773092744609 | 1.2416346608826252 |
| ann | 0.15565584791389253 | 0.02936364952046855 |

- **Combined OOS gain (stress):** 25.309%
- Full history @ stress: total 25.309%, CAGR 11.296%, benchmark -32.164%, sharpe 0.84, maxdd -0.132, trades 21

### Bull vs Medved (2510) — 1h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.19058805846880866 | 0.15175897130292837 |
| alpha | 0.31079711770225804 | 0.44872866827262536 |
| trades | 67 | 28 |
| winrate | 0.417910447761194 | 0.4642857142857143 |
| sharpe | 0.7390751368457148 | 0.9424778097297538 |
| maxdd | -0.15325187466550005 | -0.11961410938670647 |
| pf | 1.2770755322217042 | 1.5384695350857234 |
| ann | 0.13115983743756865 | 0.21679654726625874 |

- **Combined OOS gain (stress):** 37.127%
- Full history @ stress: total 36.912%, CAGR 16.070%, benchmark -32.636%, sharpe 0.81, maxdd -0.221, trades 96

### Bullish & Bearish Engulfing (2626) — 1h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.1303726419976019 | 0.004412844192504872 |
| alpha | 0.2505817012310513 | 0.30138254116220187 |
| trades | 19 | 12 |
| winrate | 0.3684210526315789 | 0.4166666666666667 |
| sharpe | 0.585467554704358 | 0.12625677079014128 |
| maxdd | -0.14435960011167626 | -0.14550007179537872 |
| pf | 1.515865711997705 | 1.5227513206038212 |
| ann | 0.09043556128363761 | 0.006133736605648865 |

- **Combined OOS gain (stress):** 13.536%
- Full history @ stress: total 21.465%, CAGR 9.663%, benchmark -32.636%, sharpe 0.58, maxdd -0.146, trades 31

### FVG Breakout Lite (825) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.12592471182120524 | 0.053430299458963715 |
| alpha | 0.2399597995405035 | 0.34611322628823193 |
| trades | 30 | 15 |
| winrate | 0.3333333333333333 | 0.4666666666666667 |
| sharpe | 0.6500305044450219 | 0.48903195937218186 |
| maxdd | -0.11327000029615841 | -0.07655104161389459 |
| pf | 1.3532523321732206 | 1.3979519113916512 |
| ann | 0.08740245823524062 | 0.07496559531548375 |

- **Combined OOS gain (stress):** 18.608%
- Full history @ stress: total 18.160%, CAGR 8.237%, benchmark -32.164%, sharpe 0.57, maxdd -0.113, trades 45

### Intraday Volume Swings (931) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.15097032793200205 | -0.013017246809423622 |
| alpha | 0.2650054156513003 | 0.2796656800198446 |
| trades | 21 | 10 |
| winrate | 0.3333333333333333 | 0.4 |
| sharpe | 0.7607484181498351 | 0.004154633895588616 |
| maxdd | -0.10703568913608863 | -0.10218931590218483 |
| pf | 1.504463419586802 | 0.879757599875797 |
| ann | 0.10443602953746844 | -0.018032266921084283 |

- **Combined OOS gain (stress):** 13.599%
- Full history @ stress: total 13.170%, CAGR 6.044%, benchmark -32.164%, sharpe 0.44, maxdd -0.141, trades 31

## 6040

### Williams %R Cross Strategy with 200 MA Filter (1557) — 1h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.0018161158375986641 | 0.4683538377262979 |
| alpha | 0.5439155914794744 | 0.39283300439296465 |
| trades | 18 | 16 |
| winrate | 0.3333333333333333 | 0.4375 |
| sharpe | 0.02330798629451771 | 1.6708359808370865 |
| maxdd | -0.08637250550389797 | -0.18307491832664757 |
| pf | 0.9887524798700286 | 2.290045973793532 |
| ann | -0.0012833911984194701 | 0.7048717579858994 |

- **Combined OOS gain (stress):** 46.569%
- Full history @ stress: total 46.569%, CAGR 19.884%, benchmark -49.634%, sharpe 0.94, maxdd -0.183, trades 34

### Nova (2691) — 4h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.02888181873080331 | 0.7976696580839624 |
| alpha | 0.5718266040068769 | 0.7179310959924592 |
| trades | 34 | 29 |
| winrate | 0.4117647058823529 | 0.5862068965517241 |
| sharpe | 0.25827386895182775 | 2.6475495333605044 |
| maxdd | -0.12915639555438285 | -0.1562702545405753 |
| pf | 1.10806170802776 | 3.478275139745037 |
| ann | 0.020318989687116318 | 1.2580670395311584 |

- **Combined OOS gain (stress):** 84.959%
- Full history @ stress: total 85.049%, CAGR 33.902%, benchmark -49.325%, sharpe 1.50, maxdd -0.222, trades 63

### Explosion Range Expansion (3263) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.08291982393359387 | 1.051142917765596 |
| alpha | 0.4600249613424797 | 0.9714043556740928 |
| trades | 60 | 34 |
| winrate | 0.4 | 0.5 |
| sharpe | -0.2860418663280403 | 2.882604461627922 |
| maxdd | -0.2602225407986324 | -0.10632899137641572 |
| pf | 0.8596689832329896 | 3.6046382387845397 |
| ann | -0.05932083508239849 | 1.7120314188363346 |

- **Combined OOS gain (stress):** 88.106%
- Full history @ stress: total 88.651%, CAGR 35.132%, benchmark -49.325%, sharpe 1.30, maxdd -0.260, trades 94

### Weekly Rebound Corridor (3885) — 4h
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.03499166448720081 | 0.4649524099586131 |
| alpha | 0.5779364497632744 | 0.3852138478671099 |
| trades | 8 | 7 |
| winrate | 0.25 | 0.7142857142857143 |
| sharpe | 0.45607726086308414 | 2.172474570016618 |
| maxdd | -0.04867396867279994 | -0.050218461309223694 |
| pf | 1.6659448823786533 | 7.697283048474866 |
| ann | 0.02459582683826622 | 0.6993894804102705 |

- **Combined OOS gain (stress):** 51.621%
- Full history @ stress: total 51.621%, CAGR 21.827%, benchmark -49.325%, sharpe 1.32, maxdd -0.050, trades 15

### Futures Engulfing Candle Size (823) — 4h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.09196462157679464 | 0.893481954281611 |
| alpha | 0.45098016369927896 | 0.8137433921901078 |
| trades | 57 | 29 |
| winrate | 0.45614035087719296 | 0.5862068965517241 |
| sharpe | -0.2983870085586506 | 2.6376231785195308 |
| maxdd | -0.22610061905443235 | -0.11703913030688518 |
| pf | 0.834010008670731 | 3.239449556818012 |
| ann | -0.06588475992476583 | 1.426921197443304 |

- **Combined OOS gain (stress):** 71.935%
- Full history @ stress: total 72.433%, CAGR 29.491%, benchmark -49.325%, sharpe 1.13, maxdd -0.226, trades 86

## 6070

### Timer (1788) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.14045594950360174 | 0.16708050152670118 |
| alpha | 0.3808814814184953 | 0.3430148679806667 |
| trades | 17 | 8 |
| winrate | 0.5294117647058824 | 0.375 |
| sharpe | 0.7263060859566496 | 1.5092651205730785 |
| maxdd | -0.12607251328650648 | -0.09558611378504567 |
| pf | 1.8095327989986545 | 3.887824362940268 |
| ann | 0.09729856621582411 | 0.23933434995802783 |

- **Combined OOS gain (stress):** 33.100%
- Full history @ stress: total 33.289%, CAGR 14.603%, benchmark -35.887%, sharpe 1.00, maxdd -0.126, trades 25

### Bull vs Medved (2510) — 4h **(pick)**
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.10675784972920188 | 0.276060667802589 |
| alpha | 0.34718338164409546 | 0.4519950342565545 |
| trades | 17 | 7 |
| winrate | 0.47058823529411764 | 0.7142857142857143 |
| sharpe | 0.598144729536 | 2.387123617742264 |
| maxdd | -0.14325882044133897 | -0.05912825597084126 |
| pf | 1.4735806206595288 | 10.604041493454272 |
| ann | 0.07429183493599179 | 0.4029181101669763 |

- **Combined OOS gain (stress):** 41.229%
- Full history @ stress: total 41.229%, CAGR 17.792%, benchmark -35.887%, sharpe 1.23, maxdd -0.143, trades 24

### Long Explosive V1 (992) — 4h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.012623134117604629 | 0.09088282123526326 |
| alpha | 0.2530486660324982 | 0.2668171876892288 |
| trades | 45 | 17 |
| winrate | 0.35555555555555557 | 0.35294117647058826 |
| sharpe | 0.13512838157636062 | 0.8446296071457828 |
| maxdd | -0.24880285322203488 | -0.10412923104344862 |
| pf | 1.028380365017792 | 1.4384366931285715 |
| ann | 0.008901555935808547 | 0.12840654639543247 |

- **Combined OOS gain (stress):** 10.465%
- Full history @ stress: total 10.622%, CAGR 4.905%, benchmark -35.887%, sharpe 0.39, maxdd -0.249, trades 62

## 6090

### Sunil 2 Bar Breakout (1360) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.1545100745420045 | 0.1254468276479399 |
| alpha | 0.5755627061209518 | 0.19574985795097022 |
| trades | 32 | 20 |
| winrate | 0.46875 | 0.45 |
| sharpe | 0.7453495990087796 | 0.7351671962839246 |
| maxdd | -0.10608490287220673 | -0.12230581340590341 |
| pf | 1.4954309036654385 | 1.8353197028320176 |
| ann | 0.10683460004665779 | 0.17836348294876792 |

- **Combined OOS gain (stress):** 29.934%
- Full history @ stress: total 35.035%, CAGR 15.313%, benchmark -42.331%, sharpe 0.80, maxdd -0.122, trades 52

### PChannel System (2299) — 1h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.0455434328395965 | 0.12869865692218796 |
| alpha | 0.3746372900519698 | 0.18643821466174582 |
| trades | 30 | 16 |
| winrate | 0.3 | 0.4375 |
| sharpe | -0.19854553340064718 | 1.1031674146843438 |
| maxdd | -0.1405050643940704 | -0.07375650303746584 |
| pf | 0.841923422940867 | 2.3216322331566803 |
| ann | -0.032394907060511624 | 0.183094562215379 |

- **Combined OOS gain (stress):** 7.729%
- Full history @ stress: total 9.349%, CAGR 4.330%, benchmark -42.244%, sharpe 0.37, maxdd -0.156, trades 46

### The 20s Breakout (2986) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.012393525852405718 | 0.12478216447183743 |
| alpha | 0.43344615743135306 | 0.19508519477486774 |
| trades | 50 | 27 |
| winrate | 0.32 | 0.5555555555555556 |
| sharpe | 0.13358334247927406 | 0.7955096561771596 |
| maxdd | -0.13751536575899803 | -0.1780017944995269 |
| pf | 1.0960503853484096 | 1.5886424911844659 |
| ann | 0.008739933145990086 | 0.17739711944134662 |

- **Combined OOS gain (stress):** 13.872%
- Full history @ stress: total 22.039%, CAGR 9.909%, benchmark -42.331%, sharpe 0.60, maxdd -0.178, trades 77

### 5 EMA No-Touch Breakout (483) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.0680660369343945 | 0.09844601055863422 |
| alpha | 0.35298659464455284 | 0.16874904086166453 |
| trades | 61 | 31 |
| winrate | 0.3114754098360656 | 0.5161290322580645 |
| sharpe | -0.28866772520167905 | 0.6558142661422344 |
| maxdd | -0.1384983138794892 | -0.1566263431631667 |
| pf | 0.9196581913269055 | 1.426024914464704 |
| ann | -0.04858230878699166 | 0.13928609905616862 |

- **Combined OOS gain (stress):** 2.368%
- Full history @ stress: total 9.709%, CAGR 4.494%, benchmark -42.331%, sharpe 0.33, maxdd -0.157, trades 92

### Long Explosive V1 (992) — 4h **(pick)**
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.04064468791239417 | 0.16220708572440046 |
| alpha | 0.38040794366655317 | 0.23251011602743077 |
| trades | 48 | 37 |
| winrate | 0.375 | 0.5405405405405406 |
| sharpe | -0.10563375464073346 | 0.880650431893011 |
| maxdd | -0.1677590240017799 | -0.12886922551493118 |
| pf | 0.9195602893836904 | 1.5576968973345469 |
| ann | -0.028889003609444575 | 0.23215305699339606 |

- **Combined OOS gain (stress):** 11.497%
- Full history @ stress: total 15.874%, CAGR 7.239%, benchmark -42.331%, sharpe 0.43, maxdd -0.168, trades 85

## 7020

### Rampok Scalp (1725) — 4h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.34720653792800005 | 0.10334254489154016 |
| alpha | 0.040433629561466455 | 0.13284330132119204 |
| trades | 13 | 10 |
| winrate | 0.6923076923076923 | 0.6 |
| sharpe | 1.2833407640685717 | 1.1334676957680847 |
| maxdd | -0.09235959542752681 | -0.05157601616980101 |
| pf | 4.435774579030593 | 3.4594619298421576 |
| ann | 0.23436221951485137 | 0.1463452617533303 |

- **Combined OOS gain (stress):** 48.643%
- Full history @ stress: total 48.643%, CAGR 20.686%, benchmark 27.789%, sharpe 1.23, maxdd -0.092, trades 23

### NRTR ATR Stop (2624) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.4077700717340016 | 0.0003618170440102819 |
| alpha | 0.100997163367468 | 0.02986257347366217 |
| trades | 22 | 9 |
| winrate | 0.5 | 0.4444444444444444 |
| sharpe | 1.468581504592401 | 0.045544620889094625 |
| maxdd | -0.08121273344213253 | -0.06260757503687442 |
| pf | 4.468298483598175 | 1.0073363221349307 |
| ann | 0.27331146446683574 | 0.0005025207968196721 |

- **Combined OOS gain (stress):** 40.828%
- Full history @ stress: total 40.828%, CAGR 17.633%, benchmark 27.789%, sharpe 1.14, maxdd -0.081, trades 31

### Dynamic Support and Resistance Pivot (717) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.35305348545000226 | -0.016539343015216534 |
| alpha | 0.046280577083468666 | 0.012961413414435352 |
| trades | 15 | 10 |
| winrate | 0.4666666666666667 | 0.2 |
| sharpe | 1.5832906632427106 | -0.26097832162878115 |
| maxdd | -0.053952961041018876 | -0.09195109284858993 |
| pf | 5.303158263202742 | 0.8725861356799204 |
| ann | 0.23814456436418574 | -0.022895462681854495 |

- **Combined OOS gain (stress):** 33.067%
- Full history @ stress: total 34.085%, CAGR 14.927%, benchmark 27.789%, sharpe 1.17, maxdd -0.103, trades 25

## 7030

### SJ NIFTY (1309) — 1h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.0053085075831968975 | 0.01643805560925582 |
| alpha | 0.015485443267464816 | 0.06037310814029695 |
| trades | 26 | 11 |
| winrate | 0.2692307692307692 | 0.5454545454545454 |
| sharpe | 0.020549114041651387 | 0.3752424381356223 |
| maxdd | -0.11375974892559892 | -0.049422552231992434 |
| pf | 0.9764891533937883 | 1.3972869384613797 |
| ann | -0.00375328131772823 | 0.022901601841297747 |

- **Combined OOS gain (stress):** 1.104%
- Full history @ stress: total 1.104%, CAGR 0.522%, benchmark -5.388%, sharpe 0.10, maxdd -0.114, trades 37

### Heiken Ashi Simplified EA (1854) — 4h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.16917590114600145 | 0.005649118067115877 |
| alpha | 0.18625370000748154 | 0.048670150571896054 |
| trades | 17 | 9 |
| winrate | 0.5882352941176471 | 0.4444444444444444 |
| sharpe | 0.9662539000495607 | 0.1659422008168652 |
| maxdd | -0.050503098632461385 | -0.046367512940940325 |
| pf | 2.9378264004293593 | 1.1347392526520672 |
| ann | 0.1167494289721529 | 0.007854006126802426 |

- **Combined OOS gain (stress):** 17.578%
- Full history @ stress: total 17.578%, CAGR 7.984%, benchmark -5.028%, sharpe 0.77, maxdd -0.051, trades 26

### Ichimoku Implied Volatility (340) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.024008173652801723 | 0.019778413256756888 |
| alpha | 0.04108597251428181 | 0.06279944576153706 |
| trades | 17 | 10 |
| winrate | 0.23529411764705882 | 0.2 |
| sharpe | 0.215093032906651 | 0.32969771383434154 |
| maxdd | -0.07192441722271825 | -0.0799125923459153 |
| pf | 1.1749571936948409 | 1.236151016395636 |
| ann | 0.016902135214424074 | 0.027573114777482033 |

- **Combined OOS gain (stress):** 4.426%
- Full history @ stress: total 4.426%, CAGR 2.076%, benchmark -5.028%, sharpe 0.25, maxdd -0.080, trades 27

### Hammer Candle Reversal (59) — 1h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.04907518401800259 | -0.014351243978466988 |
| alpha | 0.0698691348686643 | 0.029583808552574142 |
| trades | 40 | 21 |
| winrate | 0.35 | 0.2857142857142857 |
| sharpe | 0.3930112557165297 | -0.1476401809745831 |
| maxdd | -0.07382874511223758 | -0.10884428681222147 |
| pf | 1.1987390133695255 | 0.90893538840125 |
| ann | 0.034426052998475676 | -0.01987500192463676 |

- **Combined OOS gain (stress):** 3.402%
- Full history @ stress: total 3.402%, CAGR 1.600%, benchmark -5.388%, sharpe 0.21, maxdd -0.109, trades 61

## 7040

### Sunil 2 Bar Breakout (1360) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.2556380618800074 | 0.10643878224572556 |
| alpha | 0.18291078915273462 | 0.17031543422810436 |
| trades | 43 | 18 |
| winrate | 0.4186046511627907 | 0.5 |
| sharpe | 0.8548391132960872 | 1.0350623592334154 |
| maxdd | -0.13531468498803045 | -0.06051246801023802 |
| pf | 1.445318925692544 | 1.849578477415312 |
| ann | 0.17448031331065827 | 0.15081529248303638 |

- **Combined OOS gain (stress):** 38.929%
- Full history @ stress: total 42.552%, CAGR 18.315%, benchmark 3.030%, sharpe 0.94, maxdd -0.135, trades 61

### Hercules A.T.C. 2006 (2485) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.24065987829800717 | 0.15976243714079374 |
| alpha | 0.16793260557073442 | 0.22363908912317254 |
| trades | 54 | 25 |
| winrate | 0.37037037037037035 | 0.6 |
| sharpe | 0.9810133704817324 | 1.4057910880474012 |
| maxdd | -0.16978818476725466 | -0.07193750680585753 |
| pf | 1.481656934226768 | 2.313345603001239 |
| ann | 0.16456506328419596 | 0.22855511330669276 |

- **Combined OOS gain (stress):** 43.887%
- Full history @ stress: total 47.640%, CAGR 20.299%, benchmark 3.030%, sharpe 1.18, maxdd -0.170, trades 79

### Explosion Range Expansion (3263) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.43318855388001043 | 0.12020574609210688 |
| alpha | 0.3604612811527377 | 0.18408239807448568 |
| trades | 72 | 33 |
| winrate | 0.375 | 0.45454545454545453 |
| sharpe | 1.360096864077479 | 1.2566088597326424 |
| maxdd | -0.16344194736669937 | -0.08869133979642407 |
| pf | 1.7255378451741636 | 1.6825037041107977 |
| ann | 0.2895112308600978 | 0.1707494283582467 |

- **Combined OOS gain (stress):** 60.547%
- Full history @ stress: total 64.733%, CAGR 26.716%, benchmark 3.030%, sharpe 1.37, maxdd -0.163, trades 105

### Futures Engulfing Candle Size (823) — 4h **(pick)**
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.3660980843720085 | 0.16753705954489484 |
| alpha | 0.2933708116447358 | 0.23141371152727364 |
| trades | 59 | 31 |
| winrate | 0.4067796610169492 | 0.4838709677419355 |
| sharpe | 1.1718509600177645 | 1.3854568148781123 |
| maxdd | -0.1323305019411669 | -0.09089453438088668 |
| pf | 1.6391725799210748 | 1.7727001114528347 |
| ann | 0.2465657730773516 | 0.24000771589968184 |

- **Combined OOS gain (stress):** 59.497%
- Full history @ stress: total 63.657%, CAGR 26.322%, benchmark 3.030%, sharpe 1.28, maxdd -0.132, trades 90

### Hamster Bot MRS 2 (869) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.08360960325801314 | 0.013636178220471917 |
| alpha | 0.010882330530740392 | 0.07751283020285071 |
| trades | 98 | 45 |
| winrate | 0.41836734693877553 | 0.4 |
| sharpe | 0.3609883932700043 | 0.19368766670130602 |
| maxdd | -0.24474480926489983 | -0.16974298434241042 |
| pf | 1.075816039615707 | 0.9952233770741222 |
| ann | 0.058368625121015594 | 0.01898775674301456 |

- **Combined OOS gain (stress):** 9.839%
- Full history @ stress: total 8.142%, CAGR 3.783%, benchmark 3.030%, sharpe 0.27, maxdd -0.329, trades 143

## 7200

### I Gap (2145) — 4h
> family: volatility | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.05297207523600922 | 0.6740097123136317 |
| alpha | 0.0060970752360092195 | 0.008306993979334543 |
| trades | 92 | 63 |
| winrate | 0.34782608695652173 | 0.49206349206349204 |
| sharpe | 0.2782822973926308 | 2.354787798991464 |
| maxdd | -0.27253216816381143 | -0.1323827605628919 |
| pf | 1.0668379434851256 | 1.992282391177417 |
| ann | 0.03713920644534552 | 1.0452732106826037 |

- **Combined OOS gain (stress):** 76.269%
- Full history @ stress: total 75.470%, CAGR 30.568%, benchmark 80.000%, sharpe 1.15, maxdd -0.273, trades 155

### Kalman Filter Candles (2152) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.11216420814800343 | 0.8265777354763371 |
| alpha | 0.06528920814800343 | 0.1608750171420399 |
| trades | 44 | 31 |
| winrate | 0.45454545454545453 | 0.4838709677419355 |
| sharpe | 0.4873405568314801 | 2.8387154239689654 |
| maxdd | -0.2469994693905576 | -0.09559366505193723 |
| pf | 1.2820226464322744 | 2.8762154729184184 |
| ann | 0.07799662305704769 | 1.308653198336435 |

- **Combined OOS gain (stress):** 103.145%
- Full history @ stress: total 104.264%, CAGR 40.327%, benchmark 80.000%, sharpe 1.51, maxdd -0.247, trades 75

### Explosion (3261) — 4h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.38652329435200516 | 0.8549288984468306 |
| alpha | 0.33964829435200516 | 0.18922618011253345 |
| trades | 51 | 21 |
| winrate | 0.43137254901960786 | 0.5714285714285714 |
| sharpe | 1.4538560352469505 | 3.3469081297281438 |
| maxdd | -0.16282635100429288 | -0.09345659869029754 |
| pf | 2.196196769305252 | 3.862145194236651 |
| ann | 0.25970444957987193 | 1.3585680962425557 |

- **Combined OOS gain (stress):** 157.190%
- Full history @ stress: total 158.607%, CAGR 56.941%, benchmark 80.000%, sharpe 2.25, maxdd -0.163, trades 72

### Futures Engulfing Candle Size (823) — 4h **(pick)**
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.2520169422040077 | 1.2402796884488718 |
| alpha | 0.20514194220400772 | 0.5745769701145746 |
| trades | 68 | 32 |
| winrate | 0.36764705882352944 | 0.6875 |
| sharpe | 1.0075123594329964 | 4.399041443905647 |
| maxdd | -0.16097805103967855 | -0.05764185375395514 |
| pf | 1.611752916265513 | 7.147431568097168 |
| ann | 0.17208640324914204 | 2.065447567670598 |

- **Combined OOS gain (stress):** 180.487%
- Full history @ stress: total 191.787%, CAGR 66.190%, benchmark 80.000%, sharpe 2.51, maxdd -0.161, trades 100

## 7201

### XMA Candles (2374) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.0043312137284028385 | 0.22275231277861374 |
| alpha | 0.35130339048781367 | 0.3814061589324599 |
| trades | 25 | 15 |
| winrate | 0.32 | 0.6666666666666666 |
| sharpe | 0.11302539057832252 | 1.7267919405448446 |
| maxdd | -0.17572621026019786 | -0.09446221714933067 |
| pf | 1.1224928312021232 | 3.3792604631578183 |
| ann | 0.0030579731243502994 | 0.3221911253648677 |

- **Combined OOS gain (stress):** 22.805%
- Full history @ stress: total 28.059%, CAGR 12.448%, benchmark -42.717%, sharpe 0.71, maxdd -0.176, trades 40

### Bull vs Medved (2510) — 4h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.019233104676402046 | 0.19546146544149434 |
| alpha | 0.3662052814358129 | 0.3541153115953405 |
| trades | 14 | 11 |
| winrate | 0.35714285714285715 | 0.5454545454545454 |
| sharpe | 0.16492746029663966 | 1.5243956551574716 |
| maxdd | -0.202252721460062 | -0.11626755193276428 |
| pf | 1.2173201823880755 | 2.024032637098624 |
| ann | 0.01354975879110687 | 0.281386424407166 |

- **Combined OOS gain (stress):** 21.845%
- Full history @ stress: total 27.058%, CAGR 12.030%, benchmark -42.717%, sharpe 0.71, maxdd -0.202, trades 25

### E9 Shark-32 Pattern (720) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.052038555329996905 | 0.1403772184945391 |
| alpha | 0.29493362142941393 | 0.29903106464838525 |
| trades | 23 | 14 |
| winrate | 0.34782608695652173 | 0.5 |
| sharpe | -0.1042741973276936 | 1.1472203126853464 |
| maxdd | -0.2257458668622726 | -0.129594601975353 |
| pf | 0.9789671740558411 | 2.2224801372037386 |
| ann | -0.037051451977190286 | 0.20012932515593485 |

- **Combined OOS gain (stress):** 8.103%
- Full history @ stress: total 12.728%, CAGR 5.848%, benchmark -42.717%, sharpe 0.40, maxdd -0.249, trades 37

### FVG Breakout Lite (825) — 1h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.09270183221039208 | 0.10201586281088826 |
| alpha | 0.2553373834758824 | 0.26669366710683107 |
| trades | 86 | 35 |
| winrate | 0.2558139534883721 | 0.4857142857142857 |
| sharpe | -0.2688294907861871 | 0.7069211613068007 |
| maxdd | -0.31378323622821125 | -0.10879879941928261 |
| pf | 0.8949157947846234 | 1.410508238033566 |
| ann | -0.06642060682409157 | 0.14443142510951312 |

- **Combined OOS gain (stress):** -0.014%
- Full history @ stress: total 1.678%, CAGR 0.793%, benchmark -42.810%, sharpe 0.14, maxdd -0.358, trades 121

### ICT NY Kill Zone Auto Trading (915) — 4h
> family: breakout | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.0841903207684025 | 0.1756727783880352 |
| alpha | 0.4311624975278133 | 0.33432662454188133 |
| trades | 16 | 6 |
| winrate | 0.375 | 0.6666666666666666 |
| sharpe | 0.41875039772355555 | 1.6665652134259 |
| maxdd | -0.14072916612223696 | -0.06107721853453785 |
| pf | 1.3156889565766585 | 16.37143353182167 |
| ann | 0.05876930225984078 | 0.2520240273150456 |

- **Combined OOS gain (stress):** 27.465%
- Full history @ stress: total 27.465%, CAGR 12.200%, benchmark -42.717%, sharpe 0.78, maxdd -0.141, trades 22

## 7202

### RSI Buy Sell Force (1264) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.07255431496799258 | 0.24527754961112702 |
| alpha | 0.15909388447799078 | 0.2686977882324262 |
| trades | 54 | 25 |
| winrate | 0.3148148148148148 | 0.4 |
| sharpe | -0.15286510254063318 | 1.434449079229527 |
| maxdd | -0.27145137963403 | -0.11375663621211218 |
| pf | 0.8877034225882104 | 1.9511858974649832 |
| ann | -0.051821771691220486 | 0.3561385051138668 |

- **Combined OOS gain (stress):** 15.493%
- Full history @ stress: total 15.376%, CAGR 7.020%, benchmark -23.476%, sharpe 0.42, maxdd -0.299, trades 79

### Timer (1788) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.16093191122400285 | 0.23246362311304014 |
| alpha | 0.3925801106699862 | 0.2558838617343393 |
| trades | 22 | 14 |
| winrate | 0.5 | 0.5714285714285714 |
| sharpe | 0.7592082958858666 | 1.3617404352845914 |
| maxdd | -0.10450259689161134 | -0.12019138137621832 |
| pf | 1.6018455752165994 | 1.9913472121733102 |
| ann | 0.11118060393525164 | 0.336797315862275 |

- **Combined OOS gain (stress):** 43.081%
- Full history @ stress: total 42.936%, CAGR 18.466%, benchmark -23.476%, sharpe 1.00, maxdd -0.157, trades 36

### Explosion Range Expansion (3263) — 4h **(pick)**
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.09753851345200903 | 0.25866167030513876 |
| alpha | 0.3291867128979924 | 0.2820819089264379 |
| trades | 72 | 30 |
| winrate | 0.3333333333333333 | 0.6333333333333333 |
| sharpe | 0.4944573458085221 | 1.5541119292907655 |
| maxdd | -0.11395860734189778 | -0.09797550752422546 |
| pf | 1.1795566199520755 | 2.2024452593713435 |
| ann | 0.0679618667977584 | 0.3764231150407533 |

- **Combined OOS gain (stress):** 38.143%
- Full history @ stress: total 38.225%, CAGR 16.597%, benchmark -23.476%, sharpe 0.92, maxdd -0.148, trades 102

### Logistic RSI STOCH ROC AO (988) — 4h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | -0.009112969231996448 | 0.2937584869306611 |
| alpha | 0.2225352302139869 | 0.31717872555196025 |
| trades | 39 | 20 |
| winrate | 0.358974358974359 | 0.45 |
| sharpe | 0.05704987111473179 | 1.6729835430114615 |
| maxdd | -0.21398863573704496 | -0.11715027804251887 |
| pf | 1.0284884410025579 | 2.4399599754383434 |
| ann | -0.006446772179249383 | 0.4300126166525813 |

- **Combined OOS gain (stress):** 28.197%
- Full history @ stress: total 30.747%, CAGR 13.561%, benchmark -23.476%, sharpe 0.73, maxdd -0.234, trades 59

### Long Explosive V1 (992) — 4h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.17367293063600586 | 0.20505378996945245 |
| alpha | 0.4053211300819892 | 0.2284740285907516 |
| trades | 38 | 22 |
| winrate | 0.42105263157894735 | 0.45454545454545453 |
| sharpe | 0.81474648176612 | 1.2302699550624634 |
| maxdd | -0.08882898970716846 | -0.16110849838347263 |
| pf | 1.445700896022447 | 1.7024934874563893 |
| ann | 0.11978231774890813 | 0.2956878277205901 |

- **Combined OOS gain (stress):** 41.434%
- Full history @ stress: total 41.291%, CAGR 17.817%, benchmark -23.476%, sharpe 0.97, maxdd -0.200, trades 60

## 7203

### Breakout Bars Trend (2096) — 4h **(pick)**
> family: trend | params: `{}` | flags: thin_trades

| metric | validation | test |
|---|---|---|
| eng | 0.2833877995840004 | 0.30544124794318894 |
| alpha | 0.5075257306184832 | 0.5110115397203773 |
| trades | 6 | 5 |
| winrate | 0.6666666666666666 | 0.8 |
| sharpe | 1.5647422742191701 | 1.8777298276050982 |
| maxdd | -0.058577499409018685 | -0.0580357518357526 |
| pf | 67.48543501728275 | 56.99313556260038 |
| ann | 0.19275888450539092 | 0.4479776038659462 |

- **Combined OOS gain (stress):** 67.539%
- Full history @ stress: total 67.539%, CAGR 27.735%, benchmark -36.249%, sharpe 1.65, maxdd -0.059, trades 11

### Explosion Range Expansion (3263) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.23097675531201012 | 0.3397107682193612 |
| alpha | 0.4551146863464929 | 0.5452810599965495 |
| trades | 72 | 36 |
| winrate | 0.4444444444444444 | 0.3611111111111111 |
| sharpe | 0.9113459791540311 | 1.7885709797345153 |
| maxdd | -0.12135841785273938 | -0.15374228578954707 |
| pf | 1.3807043303870479 | 1.9927343053037172 |
| ann | 0.15813633603526545 | 0.5010349993815011 |

- **Combined OOS gain (stress):** 64.915%
- Full history @ stress: total 66.192%, CAGR 27.247%, benchmark -36.249%, sharpe 1.27, maxdd -0.154, trades 108

### Breakthrough Volatility (3271) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.1434648868320123 | 0.30550583345721716 |
| alpha | 0.36760281786649507 | 0.5110761252344055 |
| trades | 93 | 45 |
| winrate | 0.43010752688172044 | 0.37777777777777777 |
| sharpe | 0.5724027277654113 | 1.5367080937014233 |
| maxdd | -0.14733884657304197 | -0.16813470813607778 |
| pf | 1.192144521696407 | 1.5932945570682921 |
| ann | 0.09934308505653644 | 0.4480770936038798 |

- **Combined OOS gain (stress):** 49.280%
- Full history @ stress: total 50.433%, CAGR 21.373%, benchmark -36.249%, sharpe 0.97, maxdd -0.168, trades 138

### Futures Engulfing Candle Size (823) — 4h
> family: pattern | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.2859357968080076 | 0.2880917508363059 |
| alpha | 0.5100737278424904 | 0.4936620426134942 |
| trades | 59 | 32 |
| winrate | 0.4406779661016949 | 0.40625 |
| sharpe | 1.0429323840619282 | 1.5342597661573192 |
| maxdd | -0.10425424827186858 | -0.13692552340940745 |
| pf | 1.5194733508057345 | 1.8162780498471516 |
| ann | 0.19443138761513357 | 0.4213213343956195 |

- **Combined OOS gain (stress):** 65.640%
- Full history @ stress: total 71.340%, CAGR 29.101%, benchmark -36.249%, sharpe 1.30, maxdd -0.137, trades 91

### Long Explosive V1 (992) — 1h
> family: momentum | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.2605384833880091 | 0.3200269213621163 |
| alpha | 0.48252354208598136 | 0.5266494379184077 |
| trades | 60 | 27 |
| winrate | 0.5166666666666667 | 0.48148148148148145 |
| sharpe | 0.9898525926775606 | 1.7390586057537112 |
| maxdd | -0.18746763686997203 | -0.10110866103989258 |
| pf | 1.4050315885759024 | 1.9257691315257048 |
| ann | 0.1777167415803671 | 0.4704943472505947 |

- **Combined OOS gain (stress):** 66.394%
- Full history @ stress: total 72.332%, CAGR 29.455%, benchmark -36.073%, sharpe 1.36, maxdd -0.187, trades 87

## 7211

### Hercules A.T.C. 2006 (2485) — 4h
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.26936718318280484 | 0.46722843393076197 |
| alpha | 0.32406734525735914 | 0.34270013204396954 |
| trades | 51 | 24 |
| winrate | 0.37254901960784315 | 0.5833333333333334 |
| sharpe | 0.7651277134584725 | 2.717569664592227 |
| maxdd | -0.22308692162938892 | -0.05305853002543459 |
| pf | 1.379541101260061 | 3.968264413824008 |
| ann | 0.18353825464242113 | 0.7030573325506906 |

- **Combined OOS gain (stress):** 86.245%
- Full history @ stress: total 86.245%, CAGR 34.312%, benchmark 8.671%, sharpe 1.29, maxdd -0.223, trades 75

### The 20s Breakout (2986) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.20417514865400577 | 0.5640347126352778 |
| alpha | 0.25887531072856007 | 0.4395064107484854 |
| trades | 52 | 23 |
| winrate | 0.38461538461538464 | 0.6086956521739131 |
| sharpe | 0.5891790340645809 | 2.9836526584943672 |
| maxdd | -0.17528208264580092 | -0.05170039127844672 |
| pf | 1.287227745260743 | 6.7264962233728305 |
| ann | 0.14026450666993817 | 0.8610846771726612 |

- **Combined OOS gain (stress):** 88.337%
- Full history @ stress: total 88.337%, CAGR 35.026%, benchmark 8.671%, sharpe 1.21, maxdd -0.175, trades 75

### FT Bill Williams Trader (4004) — 1h **(pick)**
> family: trend | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.3231973482552033 | 0.4693876296532824 |
| alpha | 0.3654797784686681 | 0.3500220203043676 |
| trades | 18 | 12 |
| winrate | 0.5 | 0.6666666666666666 |
| sharpe | 0.7102382519431528 | 2.4073944825524514 |
| maxdd | -0.18281778051652497 | -0.1259111909152819 |
| pf | 2.269793802691419 | 3.3321226257863694 |
| ann | 0.2187800177190069 | 0.7065389592534441 |

- **Combined OOS gain (stress):** 94.429%
- Full history @ stress: total 99.702%, CAGR 38.831%, benchmark 10.099%, sharpe 1.12, maxdd -0.183, trades 30

### 5 EMA No-Touch Breakout (483) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.17803107001240903 | 0.5392805602573041 |
| alpha | 0.23273123208696334 | 0.41475225837051166 |
| trades | 63 | 28 |
| winrate | 0.4126984126984127 | 0.6428571428571429 |
| sharpe | 0.5533240759164813 | 2.9254979018607377 |
| maxdd | -0.21984006843519843 | -0.053058727218153856 |
| pf | 1.215369946117964 | 5.122789436561919 |
| ann | 0.12271828330231283 | 0.8203035057284083 |

- **Combined OOS gain (stress):** 81.332%
- Full history @ stress: total 81.332%, CAGR 32.620%, benchmark 8.671%, sharpe 1.19, maxdd -0.220, trades 91

### CP Strat ORB (639) — 4h
> family: breakout | params: `{}` | flags: ok

| metric | validation | test |
|---|---|---|
| eng | 0.14405327912200705 | 0.5011047522272472 |
| alpha | 0.19875344119656135 | 0.3765764503404547 |
| trades | 60 | 29 |
| winrate | 0.4166666666666667 | 0.6206896551724138 |
| sharpe | 0.4725021469673918 | 2.7425005157527127 |
| maxdd | -0.2136629456766489 | -0.05305812352072026 |
| pf | 1.16631335912617 | 3.965872094773507 |
| ann | 0.099742702355188 | 0.7579100347082315 |

- **Combined OOS gain (stress):** 71.734%
- Full history @ stress: total 71.734%, CAGR 29.242%, benchmark 8.671%, sharpe 1.07, maxdd -0.214, trades 89
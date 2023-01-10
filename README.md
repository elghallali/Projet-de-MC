# Projet-de-MC

## Analyse sectorielle des indices boursiers et les comparer avec les indices globaux (le MASI et le MADEX)

### Etapes

1. Calculer les indices de chaque secteurs pour 2022.

2. Calculer les indices globaux (MASI et MADEX) pour 2022.

3. Comparer chaque indice sectoriel à l'indice global MASI.

4. Comparer chaque indice sectoriel à l'indice global MADEX.

## Comment construit-t-on un indice? (les différentes méthodes de calcul) :

Il existe en réalité trois méthodes de calcul des indices boursiers à
savoir :
### a- Les indices équipondérés :

Appelés aussi indices arithmétique simples. Comme leur nom l’indique, ils sont calculés sur la base de la moyenne arithmétique simple. C'est-à-dire qu’on divise la somme des cours des actions qui composent l’indice à un temps « t » sur le nombre d’action, pour obtenir ce qu’on appelle la moyenne équipondérés (MEP).

$$Moyenne_{t} = \frac{\sum_{k=1}^n P_{i}(t)}{D(t)}$$

Avec :

$n$ : le nombre de titres

$P_{i}(t)$ : le prix de titre $i$ au temps $t$

$D(t)$ : le diviseur au temps $t$

### b- les indices (moyennes géométriques) :

$$ VL(t) = VL(t-1).\sqrt[n]{\Pi[\frac{P_{i}(t)}{P_{i}(t-1)}]}$$

Avec :

$VL(t)$ et $VL(t-1)$ : les valeurs prises par l'indice à ces même instants

$P_{i}(t)$ : cours du titre $i$ au instant $t$

$n$ : nombre d'actions dans l'indice

### c- Les indices pondérés par la capitalisation boursière :

Cette méthode est plus représentative, parce qu’elle tient compte du nombre d’actions émis, ainsi que leurs cours à un temps donné t=T. elle consiste à multiplier le nombre d’actions par leurs cours à la date t=T et diviser le total obtenu sur le total des actions.

$$Indice(t)  = Indice(t-1).\frac{\sum_{i=1}^n P_{i}(t).NAC_{i}(t-1)}{\sum_{i=1}^n P_{i}(t-1).NAC_{i}(t-1)}$$

Avec :

$n$ : est le nombre de titres dans l'indice.

$P_{i}(t)$ : est le prix du titre à la période $t$.

$NAC_{i}(t-1)$ : le nombre d'actions en circulation à $t-1$.

### d- Méthode de calcul de MASI et MADEX :

$$I = \frac{\sum_{i = 1}^n f_{i}(t).F_{i}(t).Q_{i}(t).C_{i}(t)}{Bo.K(t)}$$

Avec :

$t$ : instant de calcul

$n$ : nombre des valeurs de l’échantillon

$f_{i}(t)$ : facteur flottant

$F_{i}(t)$ : facteur de plafonnement

$Q_{i}(t)$ : nombre de titres total de la valeur $i$ en $t$

$C_{i}(t)$ : cours de la valeur $i$ en $t$

$Bo$ : capitalisation de base au 31/12/1991

$K(t)$ : coefficient d’ajustement en t de la capitalisation de base

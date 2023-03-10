# Comment construit-t-on un indice? (les différentes méthodes de calcul)

Il existe en réalité trois méthodes de calcul des indices boursiers à
savoir :

## a- Les indices équipondérés

Appelés aussi indices arithmétique simples. Comme leur nom l’indique, ils sont calculés sur la base de la moyenne arithmétique simple. C'est-à-dire qu’on divise la somme des cours des actions qui composent l’indice à un temps « t » sur le nombre d’action, pour obtenir ce qu’on appelle la moyenne équipondérés (MEP).

```math
$$Moyenne_{t} = \frac{\sum P_{i}(t)}{D(t)}$$
```

Avec :

$n$ : le nombre de titres

$P_{i}(t)$ : le prix de titre $i$ au temps $t$

$D(t)$ : le diviseur au temps $t$

## b- les indices (moyennes géométriques)

```math
$$VL(t) = VL(t-1).\sqrt[n]{\Pi[\frac{P_{i}(t)}{P_{i}(t-1)}]}
```

Avec :

$VL(t)$ et $VL(t-1)$ : les valeurs prises par l'indice à ces même instants

$P_{i}(t)$ : cours du titre $i$ au instant $t$

$n$ : nombre d'actions dans l'indice

## c- Les indices pondérés par la capitalisation boursière

Cette méthode est plus représentative, parce qu’elle tient compte du nombre d’actions émis, ainsi que leurs cours à un temps donné t=T. elle consiste à multiplier le nombre d’actions par leurs cours à la date t=T et diviser le total obtenu sur le total des actions.

```math
Indice(t)  = Indice(t-1).\frac{\sum P_{i}(t).NAC_{i}(t-1)}{\sum P_{i}(t-1).NAC_{i}(t-1)}
```

Avec :

$n$ : est le nombre de titres dans l'indice.

$P_{i}(t)$ : est le prix du titre à la période $t$.

$NAC_{i}(t-1)$ : le nombre d'actions en circulation à $t-1$.

## d- Méthode de calcul de MASI et MADEX

```math

I = \frac{\sum f_{i}(t).F_{i}(t).Q_{i}(t).C_{i}(t)}{Bo.K(t)}
```

Avec :

$t$ : instant de calcul

$n$ : nombre des valeurs de l’échantillon

$f_{i}(t)$ : facteur flottant

$F_{i}(t)$ : facteur de plafonnement

$Q_{i}(t)$ : nombre de titres total de la valeur $i$ en $t$

$C_{i}(t)$ : cours de la valeur $i$ en $t$

$Bo$ : capitalisation de base au 31/12/1991

$K(t)$ : coefficient d’ajustement en t de la capitalisation de base

## Automatisation des données

<ol>
  <li>Download this project from github
    <ol>
      <li>Click in <strong>Code</strong></li>
      <li>Click in <strong>Download ZIP</strong></li>
    </ol>
  </li>
  <li>Unzip this project</li>
  <li>Open this project in IDE like VSCode
    <ul>
      <li>You need Python to run this project, you can install it from <a href="https://www.python.org/downloads/">here<a></li>
      <li>then run this command in the terminal <strong>pip install -r requirements.txt</strong></li>
    </ul>
  </li>
  <li>Create <strong>a folder</strong> in your computer </li>
  <li>Copy the folder path</li>
  <li>run this project:
    <ul>
      <li>paste the folder path in terminal <strong>before ( location : )</strong> </li>
      <li>Tap Enter</li>
    </ul>
  </li>
</ol>

  

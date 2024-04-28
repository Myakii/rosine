# Vélib

Vélib est une application qui facilite le parcours à vélo pour les usagers de la ville de Paris. Elle permet, via l'accès aux informations des stations, de faciliter les déplacements en Velibs. Il est possible d'ajouter des stations en favoris.

## Installation

1. Créer un environnement virtuel et installer Flask dessus.
2. Installer les différentes bibliothèques Flask utilisées pour ce projet
3. Lancer le serveur Bob puis le serveur Alice
4. Se rendre sur localhost:5000

## Equipe

Sabrina Attos
Julie Luciani
Marie René
Rosine Yang
Marie-Gwenaëlle Fahem

## Commentaires de l'équipe
- Lors du chargement de la page, les marqueurs mettent un certains temps à apparaître, c'est un problème connu de notre équipe, auquel nous ne pouvons malheureusement pas remédier.

L'api de l'opendata de Paris ne permettant que d'obtenir les données de 100 stations à la fois, nous avons du faire une boucle afin d'accéder aux données des 1468 stations. Nous avons donc besoin de faire 15 appels pour récupérer toutes les données, d'où le temps d'attente avant l'affichage.
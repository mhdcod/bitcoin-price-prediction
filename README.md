# bitcoin-price-prediction

Ce projet utilise des modèles d'apprentissage profond (LSTM) pour prédire le prix futur du Bitcoin à partir de données historiques. L'application web est développée avec Flask, et elle permet aux utilisateurs de visualiser les prédictions sur une période définie ainsi que le prix actuel du Bitcoin en temps réel.

Fonctionnalités
- Prédictions des prix futurs : Utilise un modèle LSTM pré-entraîné pour prédire les prix du Bitcoin pour les 10 à 70 jours suivants.
- Prix en temps réel : Scrapp le prix actuel du Bitcoin via l'API CoinGecko.
- Interface utilisateur interactive : Les utilisateurs peuvent entrer un symbole boursier (par défaut, Bitcoin avec "BTC-USD") et la durée des prédictions souhaitées.
- Visualisation des données : Les prédictions futures sont affichées sous forme de graphiques interactifs créés avec Plotly.
- Affichage des résultats : Les utilisateurs peuvent voir à la fois les prédictions futures sous forme de tableau et de graphique, ainsi que le prix actuel du Bitcoin.

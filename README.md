# **Bitcoin-Price-Prediction**  

Ce projet utilise des modèles d'apprentissage profond (**LSTM**) pour prédire le prix futur du **Bitcoin** à partir de données historiques.  
L'application web est développée avec **Flask** et permet aux utilisateurs de :  
- Visualiser les prédictions sur une période définie.  
- Suivre le prix actuel du Bitcoin en temps réel via **l'API CoinGecko**.

## **🚀 Fonctionnalités**  

✅ **Prédictions des prix futurs** : Utilise un modèle **LSTM** pré-entraîné pour prédire les prix du Bitcoin pour les **10 à 70 jours suivants**.  
✅ **Prix en temps réel** : Récupère le prix actuel du Bitcoin via l'**API CoinGecko**.  
✅ **Interface utilisateur interactive** : Les utilisateurs peuvent entrer un **symbole boursier** (par défaut `BTC-USD`) et définir la durée des prédictions souhaitées.  
✅ **Visualisation des données** : Les prédictions sont affichées sous forme de **graphiques interactifs** avec **Plotly**.  
✅ **Affichage des résultats** : Les utilisateurs peuvent voir les **prédictions sous forme de tableau et de graphique**, ainsi que le prix actuel du Bitcoin.  


## **📁 Structure du projet**  

### **1️⃣ `app.py`**  
Ce fichier contient le **code principal** de l'application **Flask**. Il permet de :  
- **Charger le modèle LSTM** (`model.keras`).  
- **Effectuer des prédictions** basées sur les entrées utilisateur.  
- **Récupérer le prix en temps réel** du Bitcoin via **l'API CoinGecko**.  
- **Gérer l'affichage des résultats** sous forme de **graphiques et tableaux interactifs**.  

### **2️⃣ `model.keras`**  
Ce fichier contient le **modèle de réseau neuronal LSTM pré-entraîné** utilisé pour la **prédiction des prix**.  
Il a été **entraîné à partir des données historiques** du Bitcoin et est **chargé dans `app.py`** pour effectuer des **prédictions en direct**.  


### **3️⃣ `bitcoin_lstm.ipynb`**  
Ce notebook **Jupyter** documente l'ensemble du **processus d'entraînement du modèle LSTM**. Il comprend :  

- 📌 **L'importation et le prétraitement des données** (`btc_data.csv`).  
- 📌 **La normalisation des données et la création des séries temporelles**.  
- 📌 **La construction et l'entraînement du modèle LSTM**.  
- 📌 **L'évaluation des performances et l'export du modèle en tant que `model.keras`**.  


### **4️⃣ `requirements.txt`**  
Ce fichier liste toutes les **dépendances nécessaires** pour exécuter le projet.  
📌 **Installation des dépendances** :  
```bash
pip install -r requirements.txt
```

## **📚 Principales bibliothèques utilisées**  

- 🖥 **Flask** → Pour l'application web.  
- 🤖 **TensorFlow/Keras** → Pour le modèle LSTM.  
- 📊 **pandas et numpy** → Pour le traitement des données.  
- 🌐 **requests** → Pour récupérer les prix en temps réel.  
- 📈 **Plotly** → Pour la visualisation des prédictions.  

---

## **5️⃣ `btc_data.csv`**  
Ce fichier contient les **données historiques du prix du Bitcoin** utilisées pour entraîner le modèle.  

🔹 **Colonnes principales** :  
- **📅 Date** → La date de l'enregistrement.  
- **💰 Open, High, Low, Close** → Prix d'ouverture, le plus haut, le plus bas et de clôture.  
- **📊 Volume** → Volume des transactions.  

📌 **Ces données sont utilisées dans `bitcoin_lstm.ipynb` pour entraîner le modèle.**  


## **🚀 Comment exécuter le projet ?**  

### **1️⃣ Installer les dépendances** 📦  
```bash
pip install -r requirements.txt
```

### **2️⃣ Lancer l'application Flask 🚀**  
```bash
python app.py
```

### **3️⃣ Accéder à l'interface web 🌍**  
Ouvrir un navigateur et aller à :  

🔗 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)  

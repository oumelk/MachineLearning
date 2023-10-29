import streamlit as st
# Import des bibliothèques
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import Birch



def main():
    st.title("Mon application Streamlit")
    st.write("Ceci est une application Streamlit simple.")

if __name__ == "__main__":
    main(
    uploaded_file = st.file_uploader("C:/Users/ASUS/Downloads/Online Retail.csv", type=["csv"]);
    if uploaded_file is not None:
    data = pd.read_csv(uploaded_file);
    st.write("Voici les données du fichier CSV :");
    st.write(data);

    #data = pd.read_csv('C:/Users/ASUS/Downloads/Online Retail.csv');
    # Calcul de la matrice de corrélation
    correlation_matrix = rfm_data.corr();
    # Sélectionner les colonnes RFM pour le calcul de la corrélation 
    rfm_data = data[['InvoiceDate', 'Quantity', 'UnitPrice']];
    correlation_matrix = rfm_data.corr(numeric_only=True);
    mean_value = data['Quantity'].mean();
    data['Quantity'].fillna(mean_value, inplace=True);
    mean_value_UnitPrice = data['UnitPrice'].mean();
    data['UnitPrice'].fillna(mean_value_UnitPrice, inplace=True);
    # Créez un objet MinMaxScaler
    scaler = MinMaxScaler();
    data[['Quantity', 'UnitPrice']] = scaler.fit_transform(data[['Quantity', 'UnitPrice']]);
    # Lire les données en spécifiant les colonnes à exclure
    data = pd.read_csv('C:/Users/ASUS/Downloads/Online Retail.csv', usecols=[ 'Quantity', 'UnitPrice']);


    # Préparez vos données (sélectionnez les caractéristiques pertinentes)

    # Créez une instance de l'algorithme BIRCH
    birch = Birch(threshold=0.5, n_clusters=3);

    # Appliquez l'algorithme BIRCH à vos données
    birch.fit(data);

    # Observez les labels de cluster assignés à chaque point de données
    cluster_labels = birch.labels_;
    
    data['Cluster'] = cluster_labels;

    # Tracez le graphique de dispersion
    plt.scatter(data['UnitPrice'], data['Quantity'], c=data['Cluster'])
    plt.xlabel('UnitPrice');
    plt.ylabel('Quantity');
    plt.show();








    )

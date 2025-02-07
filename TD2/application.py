"""
📝 **Instructions** :
- Installez toutes les bibliothèques nécessaires en fonction des imports présents dans le code, utilisez la commande suivante :conda create -n projet python pandas numpy ..........
- Complétez les sections en écrivant votre code où c’est indiqué.
- Ajoutez des commentaires clairs pour expliquer vos choix.
- Utilisez des emoji avec windows + ;
- Interprétez les résultats de vos visualisations (quelques phrases).
"""

# https://appli-leniniven-rouxel.streamlit.app/ LIEN APPLI DEPLOYEE

### 1. Importation des librairies et chargement des données
from encodings.punycode import T
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px


# Chemin absolu
file_path = os.path.join(os.path.dirname(__file__), 'ds_salaries.csv')
df = pd.read_csv(file_path)

df = pd.read_csv(r'TD2/ds_salaries.csv')



### 2. Exploration visuelle des données
#votre code 

st.title("📊 Visualisation des Salaires en Data Science")
st.markdown("Explorez les tendances des salaires à travers différentes visualisations interactives.")

if st.checkbox("Afficher un aperçu des données"):
    st.write(df.head())  

# Create distplot with custom bin_size
#st.plotly_chart(df, use_container_width=False, sharing="streamlit", theme="streamlit")

fig = st.bar_chart(data=df, x="experience_level", y="salary", use_container_width=True)
#st.pyplot(fig)  



#Statistique générales avec describe pandas 
#votre code 

st.subheader("📌 Statistiques générales")
st.write(df.describe())

### 3. Distribution des salaires en France par rôle et niveau d'expérience, uilisant px.box et st.plotly_chart
#votre code 
st.subheader("📈 Distribution des salaires en France")
df_france = df[df['employee_residence'] == 'FR']



### 4. Analyse des tendances de salaires :
#### Salaire moyen par catégorie : en choisisant une des : ['experience_level', 'employment_type', 'job_title', 'company_location'], utilisant px.bar et st.selectbox 
category = st.selectbox("Sélectionnez la catégorie", ['experience_level', 'employment_type', 'job_title', 'company_location'])

avg_salary_by_category = df.groupby(category)['salary_in_usd'].mean().reset_index()

fig = px.bar(avg_salary_by_category, x=category, y='salary_in_usd', 
             title=f"Salaire moyen par {category}", 
             labels={category: category, 'salary_in_usd': 'Salaire moyen (USD)'})
st.plotly_chart(fig) 


### 5. Corrélation entre variables heatmap
# Sélectionner uniquement les colonnes numériques pour la corrélation
#votre code 
st.subheader("📈 Affichage de la heatmap avec seaborn")

numeric_columns = df.select_dtypes(include=[np.number]).columns

correlation_matrix = df[numeric_columns].corr()

# Affichage de la heatmap avec seaborn
fig, ax = plt.subplots(figsize=(10, 8)) 
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig) 


# Affichage du heatmap avec sns.heatmap
#votre code sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
#st.subheader("🔗 Corrélations entre variables numériques")




### 6. Analyse interactive des variations de salaire
# Une évolution des salaires pour les 10 postes les plus courants
# count of job titles pour selectionner les postes
# calcule du salaire moyen par an
#utilisez px.line
#votre code 





### 7. Salaire médian par expérience et taille d'entreprise
# utilisez median(), px.bar
#votre code 




### 8. Ajout de filtres dynamiques
#Filtrer les données par salaire utilisant st.slider pour selectionner les plages 
#votre code 




### 9.  Impact du télétravail sur le salaire selon le pays




### 10. Filtrage avancé des données avec deux st.multiselect, un qui indique "Sélectionnez le niveau d'expérience" et l'autre "Sélectionnez la taille d'entreprise"
#votre code 

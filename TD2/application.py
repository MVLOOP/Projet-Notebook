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
st.subheader("📈 Salaire moyen par post")
top_job_titles = df['job_title'].value_counts().head(10).index
df_top_jobs = df[df['job_title'].isin(top_job_titles)]

# Calculer le salaire moyen pour chaque poste
avg_salary_by_job = df_top_jobs.groupby('job_title')['salary_in_usd'].mean().reset_index()

# Afficher un graphique de la variation des salaires par poste
fig = px.bar(avg_salary_by_job, x='job_title', y='salary_in_usd')
st.plotly_chart(fig) 




### 7. Salaire médian par expérience et taille d'entreprise
# utilisez median(), px.bar
#votre code 
st.subheader("📊 Salaire médian par expérience et taille d'entreprise")

# Calcul du salaire médian par 'experience_level' et 'company_size'
median_salary = df.groupby(['experience_level', 'company_size'])['salary_in_usd'].median().reset_index()

# Utilisation de plotly pour afficher un graphique à barres
fig = px.bar(median_salary, x='experience_level', y='salary_in_usd', color='company_size',
             labels={'experience_level': 'Niveau d\'expérience','salary_in_usd': 'Salaire médian (USD)','company_size': 'Taille de l\'entreprise'})

# Affichage du graphique interactif
st.plotly_chart(fig)




### 8. Ajout de filtres dynamiques
#Filtrer les données par salaire utilisant st.slider pour selectionner les plages 
#votre code 
st.subheader("Tableau de données avec filtre sur les salaires")

min_salary, max_salary = df['salary_in_usd'].min(), df['salary_in_usd'].max()
salary_range = st.slider('Salaire', min_value=min_salary, max_value=max_salary,
                         value=(min_salary, max_salary))

# Filtrer les données selon la plage de salaire sélectionnée
df_filtered_salary = df[(df['salary_in_usd'] >= salary_range[0]) & (df['salary_in_usd'] <= salary_range[1])]

# Afficher les données filtrées
st.write(df_filtered_salary)



### 9.  Impact du télétravail sur le salaire selon le pays
st.subheader("Impact du télétravail sur le salaire selon le pays")

# Calculer le salaire moyen en fonction du ratio de télétravail et du pays
salary_telework = df.groupby(['remote_ratio', 'employee_residence'])['salary_in_usd'].mean().reset_index()

# Utiliser plotly pour afficher un graphique à barres de l'impact du télétravail sur le salaire
fig = px.bar(salary_telework, x='employee_residence', y='salary_in_usd', color='remote_ratio',
             labels={'employee_residence': 'Pays de résidence','salary_in_usd': 'Salaire moyen (USD)','remote_ratio': 'Ratio de télétravail'})

# Affichage du graphique interactif
st.plotly_chart(fig)




### 10. Filtrage avancé des données avec deux st.multiselect, un qui indique "Sélectionnez le niveau d'expérience" et l'autre "Sélectionnez la taille d'entreprise"
#votre code 
st.subheader("Filtrage avancé sur le niveau d'expérience et la taille de l'entreprise")

experience_levels = st.multiselect("Sélectionnez le niveau d'expérience", options=df['experience_level'].unique())
company_sizes = st.multiselect("Sélectionnez la taille d'entreprise", options=df['company_size'].unique())

# Filtrer les données en fonction des choix de l'utilisateur
df_filtered = df[df['experience_level'].isin(experience_levels) & df['company_size'].isin(company_sizes)]

# Afficher les données filtrées
st.write(df_filtered)
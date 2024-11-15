#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import pandas as pd
import plotly as py
import streamlit as st 
import altair as alt
import streamlit_option_menu
from streamlit_option_menu import option_menu
#from numerize.numerize import numerize 
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as plt
import warnings
import streamlit_jupyter 
import plotly.express as px
import streamlit_extras
from PIL import Image



#importation et nettoyage des données
df = pd.read_csv('ICRISAT-District Level Data.csv')
#df.isnull().sum() 
#st.write(df.head())
df = df.drop(['Dist Code', 'State Code', 'Dist Name'], axis = 1)

df1 = df.groupby('Year').sum()
df2 = df.groupby('Year').mean('WHEAT YIELD (Kg per ha)')
df_state = df.groupby(['State Name', ('Year')]).sum().reset_index()
st.set_page_config(
    page_title="Données agricoles",
    #page_icon="🧠",
    #page_icon = "🌽",
    page_icon = "C:/Users/DELL/Videos/python_1/agri_log.png" ,
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")



# Custom CSS for different themes
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"], [data-testid="stHeader"],[data-testid="stToolbar"]  {
        background-color: #0b1a3b;
        color: #ffffff;
       
    }
    [data-testid="stExpander"] {
        background-color: #2f3f61;
        color : #ffffff
    }
    
     [data-testid="stSidebar"] {
        background-color: #2f3f61;
        color : #ffffff
    }
    
     [data-testid="stSelectbox"] {
    background-color: #0000;  /* Change la couleur de fond du selectbox */
    color: #000000;             /* Change la couleur du texte dans le selectbox */
    border: 2px solid #0000;  /* Ajoute une bordure autour du selectbox */
    font-size: 16px;            /* Change la taille de la police du texte */
    border-radius: 8px;         /* Change le rayon des coins pour avoir des bords arrondis */
    padding: 10px;              /* Modifie l'espacement interne (padding) du selectbox */
}
    [data-testid="stSelectbox"] option {
    background-color: #0b1a3b;  /* Change la couleur de fond des options dans le selectbox */
    color: #ffffff;             /* Change la couleur du texte des options */
    padding: 10px;              /* Ajoute un espacement à l'intérieur de chaque option */
}
    [data-testid="stSelectbox"]:hover {
    background-color: #8dc497;  /* Change la couleur de fond du selectbox au survol */
}
 /* Change la couleur de fond du Number input */
    [data-testid="stNumberInput"] {
    background-color: #0000;  /* Change la couleur de fond du selectbox */
    color: #000000;             /* Change la couleur du texte dans le selectbox */
    border: 2px solid #0000;  /* Ajoute une bordure autour du selectbox */
    font-size: 16px;            /* Change la taille de la police du texte */
    border-radius: 8px;         /* Change le rayon des coins pour avoir des bords arrondis */
    padding: 10px;              /* Modifie l'espacement interne (padding) du selectbox */
}
    [data-testid="stNumberInput"] option {
    background-color: #0b1a3b;  /* Change la couleur de fond des options dans le selectbox */
    color: #ffffff;             /* Change la couleur du texte des options */
    padding: 10px;              /* Ajoute un espacement à l'intérieur de chaque option */
}
    [data-testid="stNumberInput"]:hover {
    background-color: #8dc497;  /* Change la couleur de fond du selectbox au survol */
}

    </style>
    """, unsafe_allow_html = True)

    
header = st.container()
sidebar = st.sidebar
data = st.expander("🌍Surface, 🚜 Production, et 🍃Rendement par an", )
figure = st.expander("Les figues")
footer = st.container()
# In[2]:

#st.image("inde.jpg", caption="Sunrise by the mountains")
img = Image.open("c:/Users/DELL/Videos/python_1/Agri_logo.png")

with header : 
    #st.title()
    st.markdown("<h1 style='text-align: center; color:white;'>L'agriculture en Inde</h1>", unsafe_allow_html=True) 
    st.toast("Agritech", icon="🌱") 
    #st.markdown("<h6 style='text-align:left; color:white;'>📅Choisi l\'année entre 1966 et 2017</h6>", unsafe_allow_html=True) 
    
with sidebar:
    st.image(img, 
             width = 300,
             use_column_width="always"
            )
      
    st.header("", divider="green")
    selected = option_menu("Menu", ['Pays','Etats','Info'], 
    icons=['globe', 'flag','rss'], menu_icon="cast", default_index=0,

    styles={
        "container": {
            "background-color": "#dbdeee",  # Couleur de fond du conteneur principal
            "padding": "10px",              # Espacement interne
            "border-radius": "10px",         # Bords arrondis
            "margin": "10px",
            "color": "#ffffff",
            "icon" :  "#ffffff"
        },
        "icon": {"color": "#054610", "font-size": "16px"},  # Style des icônes
        "nav-link": {
            "color": "#2f3f61",             # Couleur du texte des options
            "background-color": "#ffffff",  # Couleur de fond des options
            "border-radius": "5px",         # Bords arrondis pour chaque option
            "margin": "7px",                # Espacement entre les options
        },
        "nav-link-selected": {
            "background-color": "#8dc497",  # Couleur de fond de l'option sélectionnée
            "font-weight": "normal",          # Texte en gras pour l'option sélectionnée
        },
        "nav-link-hover": {
            "background-color": "#ad1c05",  # Couleur de fond au survol
            "color": "#ffffff",             # Couleur du texte au survol
        },
    }
                          )
    st.header("", divider="green")
    attribut = st.selectbox("Erea or Production", options = [" AREA","PRODUCTION"])
    #st.markdown("<h5 style='text-align: center; color:white;'>Choisie la culture</h5>", unsafe_allow_html=True)
    st.header("", divider="green")
    culture = st.selectbox("Culture",
        ["RICE", "WHEAT", "CHICKPEA", "SORGHUM", "MILLET", "MAIZE", "BARLEY", "GROUNDNUT", "SESAMUM", "COTTON", "FRUITS", "VEGETABLES", "ONION"], 
        )

    
if selected =="Pays":
    
    with header : 
        choix =  st.number_input('📅Choisi l\'année entre 1966 et 2017', min_value = 1966, max_value= 2017)
    with data: 
        st.markdown("<h3 style='text-align: center; color:white;'>Les données numériques</h3>", unsafe_allow_html=True) 
        gauche, droite = st.columns(2) 
        df3 = df1.filter( like = culture, axis = 1)
        df3 = df3.filter( like =  attribut, axis = 1)
        df21 = df2.filter( like = culture, axis = 1)
        df21 = df21.filter( like =  'YIELD', axis = 1)
        df4 = df3.loc[choix, :].values
        df22= df21.loc[choix, :].values
        df_state = df_state.loc[df_state['Year'].isin([choix]),:]
        df_states = df_state.filter(like=culture, axis=1)
        df_states = df_states.filter(like=attribut, axis = 1)
        # Liste des colonnes à sélectionner

        df_state = pd.concat([df_state["State Name"], df_states ], axis = 1)
        # Filtrer le DataFrame avec les colonnes sélectionnées
        

        #df_state = df_state.filter( like = culture, axis = 1)
        #df_state = df_state.filter( like =  attribut, axis = 1)
        
        
        #st.subheader(" Surface, production, et rendement par an")
        st.markdown("<h5 style='text-align: center; color:white;'>Surface, production, et rendement par an</h5>", unsafe_allow_html=True) 
        col1, col2 = st.columns(2)
        col1.markdown(f"""
                <div style="border: 3px solid green; padding: 10px; border-radius: 5px;text-align: center;">
                        <write style ="text-align: center" >
                        🌾  {culture}   {attribut}  IN {choix}<br />
                         📊 {int(df4[0])}<br />
                        </write>
                    </div>
                    """, unsafe_allow_html=True)
        col2.markdown(f"""
                <div style="border: 3px solid green; padding: 10px; border-radius: 5px;text-align: center;">
                        <write style ="text-align: center" >
                         🌾 {culture} YIELD IN {choix}<br />
                         📊 {int(df22[0])} Kg/ha
                        </write>
                    </div>
                    """, unsafe_allow_html=True)

        st.write ('')        
        
    with figure : 
        st.markdown("<h3 style='text-align: center; color:white;'>Les figures</h3>", unsafe_allow_html=True) 
        gau, droi = st.columns(2)
        #st.write(df4)
        #Superficie culturale emblavée par ans
        fig1 = px.line(df3, title = f'{attribut} OF  {culture} IN YEAR', )
        fig1.update_layout(
    width=500,
    paper_bgcolor="rgba(0,0,0,0)",   # Fond du papier transparent
    plot_bgcolor="rgba(0,0,0,0)",    # Fond de la zone de tracé transparent
    title=dict(
        text=f'{attribut} OF  {culture} IN YEAR',
        font=dict(
            color="rgba(255, 255, 255, 1)"  # Couleur du texte du titre en blanc
        )
    )
)

        gau.plotly_chart(fig1)
    
        #st.write(df4)
        #Rendement 
        fig2 = px.line(df21, title = f'YIELD OF {culture} IN YEAR')
        fig2.update_layout(
    width=500,
    paper_bgcolor="rgba(0,0,0,0)",   # Fond du papier transparent
    plot_bgcolor="rgba(0,0,0,0)",    # Fond de la zone de tracé transparent
    title=dict(
        text=f'{attribut} OF  {culture} IN YEAR',
        font=dict(
            color="rgba(255, 255, 255, 1)"  # Couleur du texte du titre en blanc
        )))
        fig2.update_traces(line=dict(color="rgba(211, 24, 16, 0.65)"))
                
        droi.plotly_chart(fig2)
        fig3 = px.pie(df_state, values = df_state.columns[1], names = df_state.columns[0], title = f'YIELD OF {culture} IN YEAR')
        fig3.update_layout(
    width=700,
    height=700,
    paper_bgcolor="rgba(0,0,0,0)",   # Fond du papier transparent
    plot_bgcolor="rgba(0,0,0,0)",    # Fond de la zone de tracé transparent
    title=dict(
        text=f'{attribut} OF  {culture} IN {choix}',
        font=dict(
            color="rgba(255, 255, 255, 1)"  # Couleur du texte du titre en blanc
        )
    ),
    legend=dict(
        font=dict(
            color="rgba(255, 255, 255, 1)"  # Couleur de la légende en blanc
        )
    )
)

       
        st.plotly_chart(fig3)
        #st.write(df_state)
    #with footer : 
        
        

elif selected == "Etats":
        with sidebar:
            st.header("", divider="green")
            region = st.selectbox('Les etats',
    ["Chhattisgarh","Madhya Pradesh","Andhra Pradesh","Telangana", "Assam","Bihar","Gujarat", "Haryana","Himachal Pradesh", "Jharkhand", "Kerala", "Orissa", "Punjab","Rajasthan","Tamil Nadu","Uttarakhand", "West Bengal"])

        with data: 
            st.markdown("<h3 style='text-align: center; color:white;'>Les données numériques par etats</h3>", unsafe_allow_html=True) 
            gauche, milieu, droite = st.columns(3)
            cultures = gauche.selectbox("choisis la culture",
        ["RICE", "WHEAT", "CHICKPEA", "SORGHUM", "MILLET", "MAIZE", "BARLEY", "GROUNDNUT", "SESAMUM", "COTTON", "FRUITS", "VEGETABLES", "ONION"], key ="A"
       
        ) 
            regions = milieu.selectbox('',
    ["Chhattisgarh","Madhya Pradesh","Andhra Pradesh","Telangana", "Assam","Bihar","Gujarat", "Haryana","Himachal Pradesh", "Jharkhand", "Kerala", "Orissa", "Punjab","Rajasthan","Tamil Nadu","Uttarakhand", "West Bengal"], key = "B")
            choix =  droite.number_input('Choisi l\'année entre 1966 et 2017', min_value = 1966, max_value= 2017)
            dfa = df.loc[df['State Name'].isin([region]),:]
            dfa1 = dfa.groupby('Year').sum()
            dfb1 = dfa.groupby('Year').mean("WHEAT YIELD (Kg per ha)")
            #st.write(dfa1)
            dfa2 = dfa1.filter( like = culture, axis = 1)
            dfa3 = dfa2.filter( like =  attribut, axis = 1)
            dfb1 = dfb1.filter( like = culture, axis = 1)
            dfb1= dfb1.filter( like =  'YIELD', axis = 1)
            dfa4 = dfa3.loc[choix, :].values
            dfb2 = dfb1.loc[choix, :].values
            st.markdown("<h3 style='text-align: center; color:white;'>Surface, production, et rendement par an et par Etat</h3>", unsafe_allow_html=True) 
            col1, col2 = st.columns(2)
            col1.markdown(f"""
                    <div style="border: 3px solid green; padding: 10px; border-radius: 5px;text-align: center;">
                            <write style ="text-align: center" >
                             {culture}   {attribut} IN {region} IN {choix}<br />
                             {int(dfa4[0])} 
                            </write>
                    </div>
                        """, unsafe_allow_html=True)
            
            col2.markdown(f"""
                    <div style="border: 3px solid green; padding: 10px; border-radius: 5px;text-align: center;">
                            <write style ="text-align: center" >
                             {culture} YIELD IN {region} IN {choix}<br />
                             {int(dfb2[0])} Kg/ha
                            </write>
                        </div>
                        """, unsafe_allow_html=True)

            dfas = df.loc[df['State Name'].isin([regions]),:]
            dfa1s = dfas.groupby('Year').sum()   
            dfb1s = dfas.groupby('Year').mean("WHEAT YIELD (Kg per ha)")
            dfa2s = dfa1s.filter( like = cultures, axis = 1)
            dfa3s = dfa2s.filter( like =  attribut, axis = 1)
            dfb1s = dfb1s.filter( like = cultures, axis = 1)
            dfb1s= dfb1s.filter( like =  'YIELD', axis = 1)
            dfa4s = dfa3s.loc[choix, :].values
            dfb2s = dfb1s.loc[choix, :].values
            st.write ('')        

    
            col1, col2 = st.columns(2)
            col1.markdown(f"""
                        <div style="border: 3px solid green; padding: 10px; border-radius: 5px;text-align: center;">
                                <write style ="text-align: center" >
                                 {cultures}   {attribut} IN {regions} IN {choix}<br />
                                 {int(dfa4s[0])} 
                                </write>
                        </div>
                            """, unsafe_allow_html=True)
                
            col2.markdown(f"""
                        <div style="border: 3px solid green; padding: 10px; border-radius: 5px;text-align: center;">
                                <write style ="text-align: center" >
                                 {cultures} YIELD IN {regions} IN {choix}<br />
                                 {int(dfb2s[0])} Kg/ha
                                </write>
                            </div>
                            """, unsafe_allow_html=True)
            st.write ('')        
            
            
            top=df.groupby('State Name').sum()
            top = top.filter( like = culture, axis = 1)
            top = top.filter( like = attribut, axis = 1)
            top.sort_values(by = top.columns[0], ascending=False)
            top = top.head(5)                                                                                                  
            
        
        with figure : 
            st.markdown("<h3 style='text-align: center; color:white;'>Les figures</h3>", unsafe_allow_html=True) 
            df_concat = pd.merge(dfa3, dfa3s, on='Year', how='inner')
            df_ycon = pd.merge(dfb1, dfb1s, on='Year', how='inner')
            gau, droi = st.columns(2)
            #st.write(dfa3)
            #Superficie culturale emblavée par ans
            fig1 = px.line(df_concat, title = f' {attribut} of {culture} IN YEAR')
            fig1.update_layout(
    width=500,
    paper_bgcolor="rgba(0,0,0,0)",   # Fond du papier transparent
    plot_bgcolor="rgba(0,0,0,0)",    # Fond de la zone de tracé transparent
    title=dict(
        text=f'{attribut} OF  {culture} IN YEAR',
        font=dict(
            color="rgba(255, 255, 255, 1)"  # Couleur du texte du titre en blanc
        )))
            gau.plotly_chart(fig1)
        
            #st.write(df4)
            #Rendement 
            fig2 = px.line(df_ycon, title = f'YIELD OF {culture}IN YEAR',)
            fig2.update_layout(width=500,
    paper_bgcolor="rgba(0,0,0,0)",   # Fond du papier transparent
    plot_bgcolor="rgba(0,0,0,0)",    # Fond de la zone de tracé transparent
    title=dict(
        text=f'{attribut} OF  {culture} IN YEAR',
        font=dict(
            color="rgba(255, 255, 255, 1)"  # Couleur du texte du titre en blanc
        )))
            fig2.update_traces(line=dict(color="rgba(211, 24, 16, 0.65)"))
            droi.plotly_chart(fig2)
            #top 5
            fig3 = px.bar(top, title = f'Top 5 {attribut} {culture}', color = top.index )
            fig3.update_layout(
    width=800,
    paper_bgcolor="rgba(0,0,0,0)",   # Fond du papier transparent
    plot_bgcolor="rgba(0,0,0,0)",    # Fond de la zone de tracé transparent
    title=dict(
        text=f'Top 5 {attribut} {culture}',  # Titre
        font=dict(color="rgba(255, 255, 255, 1)")  # Couleur du texte du titre en blanc
    ),
    xaxis_title='State names',  # Titre de l'axe X
    yaxis_title=f'{attribut}',  # Titre de l'axe Y
    legend=dict(
        font=dict(color="rgba(255, 255, 255, 1)")  # Couleur de la légende
    )
)

            st.plotly_chart(fig3)
            
elif selected == "Info":

        with footer : 
            st.write("FIN MERCI")
            
            








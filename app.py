import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from streamlit_option_menu import option_menu
import numpy as np
from sqlalchemy import create_engine, text

import altair as alt



st.set_page_config(page_title="Plato's Pizza", layout="wide")

# ============================================================
# CHARGEMENT DES DONNÉES
# ============================================================
# @st.cache_data
# def load_data():
#     engine = create_engine("mysql+mysqlconnector://pizza:Pa123456789@129.0.0.1:3306/pizzadb", echo=True)
#     with engine.connect() as connection:
#         with open("sql/kpi01.sql", "r") as file:
#             query = file.read()
#             df = pd.read_sql(query, connection)
#     return df


couleurs = {
    "Tué": "#C0392B",
    "Blessé hospitalisé": "#E67E22",
    "Blessé léger": "#F4D03F",
    "Indemne": "#27AE60"
}
ordres = ["o1", "o2", "o3", "o4"]

# ============================================================
# SIDEBAR : NAVIGATION
# ============================================================
with st.sidebar:
    selected_page = option_menu(
        menu_title="Navigation",
        options=[
            "Vue d'ensemble",
            "Chiffres d'affaires",
            "Analyse Supplémentaire",
            "Autres"
        ],
        icons=[
            "speedometer2",   # Vue d'ensemble
            "car-front-fill", # Véhicules
            "cloud-rain-fill",# Conditions environnementales
            "signpost-split-fill", # Type de route
            "people-fill",    # Profil usager
        ],
        default_index=0,
    )


engine = create_engine("mysql+mysqlconnector://pizza:Pa123456789@127.0.0.1:3306/pizzadb", echo=True, connect_args={'auth_plugin': 'mysql_native_password'})

# ============================================================
# PAGES
# ============================================================
if selected_page == "Vue d'ensemble":
    st.title("🍕 Vue d'ensemble ")
    with engine.connect() as connection:

        with st.container(horizontal=True, gap="medium"):

            # Ligne 1 - metrics
            cols = st.columns(1, gap="medium", width=120)
            with cols[0]:
                with open('sql/kpis/kpi01.sql', 'r') as query: 
                    df_nbrs = pd.read_sql_query(text(query.read()), connection)
                    st.metric("Commandes",  f"{df_nbrs.iloc[0, 0]}", format=None, delta="Nobre" )     
            cols = st.columns(2, gap="medium", width=380)           
            with cols[0]:
                with open('sql/kpis/kpi02.sql', 'r') as query: 
                    df_prd = pd.read_sql_query(text(query.read()), connection)
                    st.metric("Début: ",  f"{df_prd.iloc[0, 0]}", format=None , delta="Date" )       
            with cols[1]:
                with open('sql/kpis/kpi02.sql', 'r') as query: 
                    df_prd = pd.read_sql_query(text(query.read()), connection)
                    st.metric("Fin: ",  f"{df_prd.iloc[0, 1]}", format=None , delta="Date" )   
            cols = st.columns(1, gap="medium", width=190)
            with cols[0]:
                with open('sql/kpis/kpi14.sql', 'r') as query: 
                    df_nbrs = pd.read_sql_query(text(query.read()), connection)
                    st.metric("CA total",  f"{df_nbrs.iloc[0, 0]:,.2f} €", format=None, delta="Montant" )    
            cols = st.columns(1, gap="medium", width=190)
            with cols[0]:
                with open('sql/kpis/kpi10.sql', 'r') as query: 
                    df_nbrs = pd.read_sql_query(text(query.read()), connection)
                    st.metric("Commande Jour",  f"{ df_nbrs.iloc[0, 0] } ", format=None, delta="Nombre Moyenne" )   

        st.divider()

        with st.container(horizontal=True, gap="medium"):

            # Ligne 2 - Nombre Commandes par les Dattes
            cols = st.columns(1, gap="medium", width=900)
            with cols[0]:
                with open('sql/kpis/kpi03.sql', 'r') as query: 
                    df_nbrs_par_dates = pd.read_sql_query(text(query.read()), connection)
                    st.write("Nombre Commandes par les Dattes")
                    st.line_chart(df_nbrs_par_dates, x="date", y="nombre_par_date", use_container_width=True)

            # Ligne 3 - Nombre Commandes par les Mois
            cols = st.columns(1, gap="medium", width=1000)
            with cols[0]:
                with open('sql/kpis/kpi04.sql', 'r') as query: 
                    df_nbrs_par_mois = pd.read_sql_query(text(query.read()), connection)
                    month_order = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ]
                    df_nbrs_par_mois["cmd_mois"] = pd.Categorical(df_nbrs_par_mois["cmd_mois"], categories=month_order, ordered=True )
                    df_nbrs_par_mois = df_nbrs_par_mois.sort_values("cmd_mois")
                    st.write("Nombre Commandes par les Mois")
                    st.line_chart(df_nbrs_par_mois, x="cmd_mois", y="nombre_par_mois")

            # Ligne 4 - Nombre Commandes par les Heures de Travail et Nobre des commandes par les quantités commandées
            cols = st.columns(2, gap="medium", width=800)
            with cols[0]:
                with open('sql/kpis/kpi05.sql', 'r') as query: 
                    df_nbrs_par_travail = pd.read_sql_query(text(query.read()), connection)
                    st.write("Nombre Commandes par les Heures de Travail")
                    st.altair_chart(
                        alt.Chart(df_nbrs_par_travail)
                        .mark_arc()
                        .encode(
                            alt.Color("travail_périod"), 
                            alt.Theta("nobres_par_périod_du_travail"),
                            # alt.Tooltip(["travail_périod", "nobres_par_périod_du_travail"])
                        )  
                        .configure_legend(orient="bottom")
                    )
            with cols[1]:
                with open('sql/kpis/kpi06.sql', 'r') as query: 
                    df_nbrs_par_qtys = pd.read_sql_query(text(query.read()), connection)
                    st.write("Nobre des linges des commandes par les quantités pizza commandées")
                    st.dataframe(df_nbrs_par_qtys.iloc[:,0:2])


elif selected_page == "Chiffres d'affaires":
    st.title(f"€💶  Chiffres d'affaires")
    with engine.connect() as connection:
        with st.container(horizontal=True, gap="medium"):
            cols = st.columns(1, gap="medium", width=900)
            with cols[0]:
                with open('sql/kpis/kpi07.sql', 'r') as query: 
                    df_ca_pizza = pd.read_sql_query(text(query.read()), connection)
                    st.altair_chart(alt.Chart(df_ca_pizza).mark_bar().encode(x=alt.X("pizza", sort=None), y="prix_achat"))

            cols = st.columns(2, gap="medium", width=900)
            with cols[0]:
                with open('sql/kpis/kpi08.sql', 'r') as query: 
                    df_ca_taille_pizza = pd.read_sql_query(text(query.read()), connection)
                    st.write("CA par la taille des pizzas")
                    st.dataframe(df_ca_taille_pizza)
            with cols[1]:
                with open('sql/kpis/kpi09.sql', 'r') as query: 
                    df_ca_par_cat_pizza = pd.read_sql_query(text(query.read()), connection)
                    st.write("CA par la catégoreie des pizzas")
                    st.dataframe(df_ca_par_cat_pizza)

            cols = st.columns(1, gap="medium", width=900)
            with cols[0]:
                with open('sql/kpis/kpi11.sql', 'r') as query: 
                    df_ca_mois = pd.read_sql_query(text(query.read()), connection)
                    st.write("CA par les types de pizzas")
                    month_order = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ]
                    df_ca_mois["mois"] = pd.Categorical(df_ca_mois["mois"], categories=month_order, ordered=True )
                    df_ca_mois = df_ca_mois.sort_values("mois")
                    st.line_chart(df_ca_mois, x="mois", y="prix_achat")

            cols = st.columns(1, gap="medium", width=500)
            with cols[0]:
                with open('sql/kpis/kpi12.sql', 'r') as query: 
                    df_prix = pd.read_sql_query(text(query.read()), connection)
                    st.write("Les Prix")
                    st.dataframe(df_prix)

elif selected_page == "Analyse Supplémentaire":
    st.title("👥 Analyse Supplémentaire")
    with engine.connect() as connection:
        with st.container(horizontal=True, gap="medium"):
            cols = st.columns(1, gap="medium", width=900)
            with cols[0]:
                with open('sql/kpis/kpi13.sql', 'r') as query: 
                    df_nbr_ingreds = pd.read_sql_query(text(query.read()), connection)
                    st.write("Nobre d'ingrédients par les pizzas")
                    st.altair_chart(
                        alt.Chart(df_nbr_ingreds)
                        .mark_bar()
                        .encode(
                            x="pizza",
                            y="nombre_ingreds",
                            color="category",
                        )
                    )

    #---------------------

elif selected_page == "Autres":
    st.title("Autres")





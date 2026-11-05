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
            "KPI Général",
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
    st.title("📊 Vue d'ensemble ")
    with engine.connect() as connection:

        with st.container(horizontal=True, gap="medium"):
            cols = st.columns(1, gap="medium", width=200)
            with cols[0]:
                with open('sql/kpis/kpi01.sql', 'r') as query: 
                    df_nbrs = pd.read_sql_query(text(query.read()), connection)
                    st.metric("Nobre de commandes en 2015",  f"{df_nbrs.iloc[0, 0]}", format=None )     
            cols = st.columns(2, gap="medium", width=400)           
            with cols[0]:
                with open('sql/kpis/kpi02.sql', 'r') as query: 
                    df_prd = pd.read_sql_query(text(query.read()), connection)
                    st.metric("Début: ",  f"{df_prd.iloc[0, 0]}", format=None )       
            with cols[1]:
                with open('sql/kpis/kpi02.sql', 'r') as query: 
                    df_prd = pd.read_sql_query(text(query.read()), connection)
                    st.metric("Fin: ",  f"{df_prd.iloc[0, 1]}", format=None )   
            cols = st.columns(1, gap="medium", width=200)
            with cols[0]:
                with open('sql/kpis/kpi14.sql', 'r') as query: 
                    df_nbrs = pd.read_sql_query(text(query.read()), connection)
                    st.metric("CA total",  f"{df_nbrs.iloc[0, 0]:,.2f} €", format=None )    

        with st.container(horizontal=True, gap="medium"):
            cols = st.columns(1, gap="medium", width=1000)
            with cols[0]:
                with open('sql/kpis/kpi03.sql', 'r') as query: 
                    df_nbrs_par_dates = pd.read_sql_query(text(query.read()), connection)
                    st.write("Nombre Commandes par les Dattes")
                    st.line_chart(df_nbrs_par_dates, x="date", y="nombre_par_date", use_container_width=True)
            cols = st.columns(1, gap="medium", width=1000)
            with cols[0]:
                with open('sql/kpis/kpi04.sql', 'r') as query: 
                    df_nbrs_par_mois = pd.read_sql_query(text(query.read()), connection)
                    st.write("Nombre Commandes par les Mois")
                    # monthes= pd.DataFrame({"janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"})
                    st.bar_chart(df_nbrs_par_mois, x="cmd_mois", y="nobre_par_mois", use_container_width=True)

            cols = st.columns(2, gap="medium", width=600)
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
                    st.write("Nobre des commandes par les quantités commandées")
                    st.dataframe(df_nbrs_par_qtys.iloc[:,0:2])



elif selected_page == "KPI Général":
    st.title("🛣️ KPI Géneral")
    with engine.connect() as connection:
        with st.container(horizontal=True, gap="medium"):
            cols = st.columns(1, gap="medium", width=900)
            with cols[0]:
                with open('sql/kpis/kpi07.sql', 'r') as query: 
                    df_ca_pizza = pd.read_sql_query(text(query.read()), connection)
                    st.altair_chart(alt.Chart(df_ca_pizza).mark_bar().encode(x="pizza", y="prix_achat"))

elif selected_page == "Analyse Supplémentaire":
    st.title("👥 Analyse Supplémentaire")


    #---------------------

elif selected_page == "Autres":
    st.title("Autres")





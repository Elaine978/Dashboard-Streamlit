import streamlit as st
import pandas as pd
import numpy as np
import folium # type: ignore
from streamlit_folium import st_folium # type: ignore
import plotly.express as px # type: ignore

def main():
    st.title('Parceiros Potenciais')
    st.subheader('Mapa')
    df = pd.read_excel('Geolocalizacao.xlsx')
    rev = df['nome_empresarial']
    fan = df['nome_fant']
    cidade = df['municipio_text']
    lat = df['latitude']
    lon = df['longitude']
    uf = df['uf']
    
    # Crie um mapa e adicione os markers
    mapa = folium.Map(zoom_start=13)
    for c, r, f, la, lo in zip(cidade, rev, fan, lat, lon):
        tooltip_text = f"Nome Fantasia: {f} \n Razão Social: {r} \n Cidade: {c}"
        folium.Marker([la, lo], tooltip=tooltip_text).add_to(mapa)
    st_folium(mapa, width='100%', height=600)
    st.subheader('Estabelecimentos por Estados')
    uf_counts = df['uf'].value_counts().reset_index()
    uf_counts.columns = ['UF', 'Contagem']
    fig = px.bar(uf_counts, x='UF', y='Contagem', title='Número de Empresas por Estado')
    # Exiba o gráfico no Streamlit
    st.plotly_chart(fig)

main()    
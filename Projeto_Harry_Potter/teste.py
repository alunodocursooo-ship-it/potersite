import streamlit as st
import requests

# URL da API com todos os personagens
url = "https://hp-api.onrender.com/api/characters"

# Faz a requisição para pegar os dados
resposta = requests.get(url)
dados = resposta.json()
print(dados[0]['name'])
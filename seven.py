import streamlit as st
import requests

# Clé API Groq (à stocker dans .streamlit/secrets.toml)
GROQ_API_KEY = st.secrets["api_key"]

# Personnalités des péchés capitaux
peches = {
    "Orgueil": "Tu es supérieur à tous. Tu parles avec fierté et mépris.",
    "Gourmandise": "Tu es obsédé par la nourriture et les plaisirs des sens.",
    "Luxure": "Tu es charmeur, séducteur, et tu parles avec passion.",
    "Avarice": "Tu veux tout garder pour toi, tu es froid et calculateur.",
    "Paresse": "Tu es lent, tu n'as pas envie de faire d'efforts.",
    "Colère": "Tu es impulsif, agressif, prêt à exploser à chaque mot.",
    "Envie": "Tu es jaloux, frustré, tu veux ce que les autres ont."
}

# Interface utilisateur
st.set_page_config(page_title="Chat des 7 Péchés Capitaux", page_icon="💀")
st.title("💀 Les 7 Péchés Capitaux - IA Groq (LLaMA 3)")

peche_choisi = st.selectbox("Choisis un péché capital :", list(peches.keys()))
st.markdown(f"**Personnalité IA :** *{peches[peche_choisi]}*")

user_input = st.text_input("💬 Écris un message à ce péché :", "")

# Fonction pour appeler Groq
def chat_with_groq(peche, message):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {
                "role": "system",
                "content": f"Tu incarnes le péché capital '{peche}'. Ta personnalité est : {peches[peche]}"
            },
            {
                "role": "user",
                "content": message
            }
        ],
        "temperature": 0.8
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Erreur {response.status_code} : {response.text}"

# Affichage de la réponse
if user_input:
    with st.spinner("Le péché répond..."):
        reponse = chat_with_groq(peche_choisi, user_input)
        st.markdown(f"**{peche_choisi} 🗣️** : {reponse}")


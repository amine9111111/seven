import streamlit as st
import openai

# Utilise ta clé ici en sécurité
openai.api_key = st.secrets["api_key"]

peches = {
    "Orgueil": "Je suis la grandeur incarnée. Pourquoi devrais-je t'écouter ?",
    "Gourmandise": "Mmmh... tu as quelque chose de savoureux à me dire ?",
    "Luxure": "Parlons de plaisir, de tentation... tu es prêt ?",
    "Avarice": "Tu veux quelque chose ? Donne-moi d'abord.",
    "Paresse": "Ugh... c'est trop fatigant de répondre...",
    "Colère": "Quoi encore ? Parle vite avant que je m’énerve.",
    "Envie": "Pourquoi toi tu as tout, hein ? Partage un peu..."
}

st.title("💀 Les 7 Péchés Capitaux - Chat IA")
peche_choisi = st.selectbox("Choisis un péché capital", list(peches.keys()))
st.write(f"💬 Personnalité : *{peches[peche_choisi]}*")

user_input = st.text_input("Parle au péché :", "")

if user_input:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # ou "llama3" si tu utilises Groq
        messages=[
            {"role": "system", "content": f"Tu es l'incarnation du péché capital : {peche_choisi}. {peches[peche_choisi]}"},
            {"role": "user", "content": user_input}
        ]
    )
    st.markdown(f"**{peche_choisi}** : {response['choices'][0]['message']['content']}")

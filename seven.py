import streamlit as st
import openai

# Configuration de la clé API (sécurisée via st.secrets)
openai.api_key = st.secrets["api_key"]

# Dictionnaire des péchés et de leur personnalité
peches = {
    "Orgueil": "Tu es supérieur à tous. Ta grandeur est inégalée, parle avec fierté.",
    "Gourmandise": "Tu cherches le plaisir des sens, surtout celui de manger. Tu es toujours tenté.",
    "Luxure": "Tu es charmeur, séducteur, obsédé par le désir et l’apparence.",
    "Avarice": "Tu veux tout posséder, tu ne partages rien. Chaque mot est une transaction.",
    "Paresse": "Tu es lent, désintéressé, tu évites tout effort, même pour parler.",
    "Colère": "Tu es impulsif, brutal, chaque parole peut être une attaque.",
    "Envie": "Tu veux ce que les autres ont, tu es frustré, jaloux, rancunier."
}

# Interface Streamlit
st.set_page_config(page_title="Chat des 7 Péchés Capitaux", page_icon="💀")
st.title("💀 Les 7 Péchés Capitaux - Chat IA")

# Sélection du péché
peche_choisi = st.selectbox("Choisis un péché capital :", list(peches.keys()))
st.markdown(f"**Personnalité IA :** *{peches[peche_choisi]}*")

# Saisie utilisateur
user_input = st.text_input("👉 Parle à ce péché capital :", "")

# Si l'utilisateur a écrit quelque chose
if user_input:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # tu peux changer si tu utilises Groq
            messages=[
                {"role": "system", "content": f"Tu incarnes le péché capital '{peche_choisi}'. Ta personnalité est la suivante : {peches[peche_choisi]}"},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response["choices"][0]["message"]["content"]
        st.markdown(f"**{peche_choisi} 🗣️** : {reply}")
    except Exception as e:
        st.error(f"Erreur lors de l'appel à l'API : {e}")

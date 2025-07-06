
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Nom': ['Ali', 'Nadia', 'Youssef', 'Sarra', 'Salem', 'Amira'],
    'Spécialité': ['Info', 'Physique', 'Info', 'Maths', 'Physique', 'Maths'],
    'Note': [12.5, 8, 15, 17, 9.5, 11]
})

st.title("🎓 Dashboard des étudiants")

note_min = st.slider("Note minimale", 0, 20, 10)
graph_type = st.radio("Type de graphique", ['Histogramme', 'Camembert'])

df_filtré = df[df['Note'] >= note_min]

if df_filtré.empty:
    st.warning("Aucun étudiant trouvé.")
else:
    st.dataframe(df_filtré)

    fig, ax = plt.subplots(figsize=(6, 4))
    if graph_type == 'Histogramme':
        ax.bar(df_filtré['Nom'], df_filtré['Note'], color='skyblue')
        ax.set_ylim(0, 20)
        ax.set_title("Histogramme des notes")
    else:
        counts = df_filtré['Spécialité'].value_counts()
        ax.pie(counts, labels=counts.index, autopct='%1.1f%%')
        ax.set_title("Répartition par spécialité")
        ax.axis('equal')

    st.pyplot(fig)

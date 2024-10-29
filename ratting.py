import streamlit as st
import pandas as pd

# Configuração da tabela inicial com critérios, descrições e pesos
data = {
    "Critério": ["Alinhamento Estratégico", "Potencial Retorno Financeiro Anual", "Grau de Certeza de ROI"],
    "Descrição": [
        "O quanto a iniciativa está conectada a nossa Casa Estratégica (Planejamento Estratégico)",
        "Qual o valor estimado de retorno financeiro para iniciativa ao ano?",
        "Qual o grau de certeza em relação ao retorno financeiro previsto?"
    ],
    "Peso (%)": [30, 40, 30],
    "Pontuação (0-5)": [5, 4, 3]  # Pontuações iniciais padrão
}

# Converte para DataFrame
df = pd.DataFrame(data)

# Título do aplicativo
st.title("Ratting de Novas Iniciativa")

# Exibe a tabela inicial
st.write("### Critérios e Pesos")
st.dataframe(df[['Critério', 'Descrição', 'Peso (%)']])

# Interface para entrada de pontuações
st.write("### Insira a pontuação para cada critério (0 a 5)")
for i in range(len(df)):
    df.loc[i, 'Pontuação (0-5)'] = st.slider(f"{df.loc[i, 'Critério']}", 0, 5, int(df.loc[i, 'Pontuação (0-5)']))

# Calcula as notas ponderadas
df["Nota Ponderada"] = (df["Peso (%)"] / 100) * df["Pontuação (0-5)"]

# Calcula a nota final
nota_final = df["Nota Ponderada"].sum()

# Exibe a tabela com as notas ponderadas
st.write("### Resultado da Nota Ponderada")
st.write("Abaixo está a tabela com os cálculos das notas ponderadas.")
st.dataframe(df[['Critério', 'Peso (%)', 'Pontuação (0-5)', 'Nota Ponderada']])

# Exibe a nota final
st.write("### Nota Final Ponderada")
st.write(f"Nota Final: {nota_final:.2f}")

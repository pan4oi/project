import streamlit as st
import pandas as pd

st.title("📊 Класна анкета – оценки")

# Инициализация на данните
if "grades" not in st.session_state:
    st.session_state.grades = {}  # ключ = име, стойност = оценка

st.subheader("Въведи информация")

# Вход за име и оценка
name = st.text_input("Име на ученика:")
grade = st.number_input("Оценка (2–6):", min_value=2, max_value=6, step=1)

if st.button("Запази оценката"):
    if name.strip() == "":
        st.warning("Моля, въведете име!")
    else:
        st.session_state.grades[name] = grade
        st.success(f"Оценката на {name} е записана!")

st.divider()

st.subheader("📝 Резултати")

if st.session_state.grades:
    # Превръщаме речника в DataFrame
    grades_df = pd.DataFrame.from_dict(
        st.session_state.grades, orient="index", columns=["Оценка"]
    )
    grades_df.index.name = "Ученик"
    st.bar_chart(grades_df)
else:
    st.info("Все още няма записани оценки.")

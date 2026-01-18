import streamlit as st
import pandas as pd

st.set_page_config(page_title="Класен дневник")

st.title("📊 Класен дневник – оценки")

# Инициализация
if "data" not in st.session_state:
    st.session_state.data = []

st.subheader("➕ Добавяне на оценка")

name = st.text_input("👤 Име на ученика")
subject = st.selectbox(
    "📘 Предмет",
    ["Математика", "БЕЛ", "Английски", "ИТ", "Физика"]
)
grade = st.slider("⭐ Оценка", 2, 6, 4)

if st.button("Запази"):
    if name.strip() == "":
        st.warning("Моля, въведи име!")
    else:
        st.session_state.data.append(
            {
                "Ученик": name,
                "Предмет": subject,
                "Оценка": grade,
            }
        )
        st.success(f"Оценката на {name} е записана!")

st.divider()

st.subheader("📝 Таблица с оценки")

if st.session_state.data:
    df = pd.DataFrame(st.session_state.data)
    st.dataframe(df, use_container_width=True)

    st.divider()

    st.subheader("📈 Статистика")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("📊 Среден успех", round(df["Оценка"].mean(), 2))

    with col2:
        st.metric("👥 Брой оценки", len(df))

    st.divider()

    st.subheader("📊 Средна оценка по ученици")
    avg_by_student = df.groupby("Ученик")["Оценка"].mean()
    st.bar_chart(avg_by_student)

    st.subheader("📊 Разпределение на оценките")
    grade_counts = df["Оценка"].value_counts().sort_index()
    st.bar_chart(grade_counts)

else:
    st.info("Все още няма въведени оценки.")

import streamlit as st

st.set_page_config(
    page_title="Las TIC en la Sociedad",
    page_icon="💡",
    layout="wide"
)

st.title("🌐 Las TIC en la Sociedad")
st.subheader("Cómo las Tecnologías de la Información y la Comunicación transforman el mundo")

st.markdown("---")

st.markdown("""
👋 **Bienvenido/a** a este recurso multimedia interactivo.  
Aquí exploraremos cómo las **TIC** contribuyen a resolver problemas en los ámbitos **laboral, educativo y familiar**,  
tanto en **nuestra comunidad** como en **otras partes del mundo**.

📌 Usa el menú lateral para navegar por las secciones:
- 🧭 **Introducción**
- 🏘️ **TIC en mi comunidad**
- 🌏 **TIC en otra comunidad**
- 🧩 **Conclusión**
""")

st.image("static/0.gif", caption="Las TIC conectan al mundo", use_container_width=True)
st.success("✨ Explora cada sección para descubrir cómo las TIC impulsan el desarrollo social y la innovación.")

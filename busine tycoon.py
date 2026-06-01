import streamlit as st

# 1. TASARIM KISMI (CSS)
st.markdown("""
<style>
  /* Buraya dosyanızın en başındaki tüm CSS kodlarınızı yapıştırın */
  /* En son satır olan size:11px;margin-top:4px;} kısmına kadar olan her şey */
  size:11px;margin-top:4px;}
</style>
""", unsafe_allow_html=True)


# 2. OYUN KODLARI KISMI (SCRIPT)
st.components.v1.html("""
<script>
  /* Buraya da <script> yazısından başlayıp en alta kadar giden tüm oyun kodlarınızı yapıştırın */
</script>
""", height=650)

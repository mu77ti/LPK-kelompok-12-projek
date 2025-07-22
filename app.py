import streamlit as st

st.set_page_config(page_title="Kalkulator Normalitas", layout="centered")

st.title("🧪 Kalkulator Normalitas Larutan")

with st.form("form_normalitas"):
    berat = st.number_input("Berat zat (gram):", min_value=0.0, format="%.4f")
    massa_molar = st.number_input("Massa molar (g/mol):", min_value=0.0001, format="%.4f")
    volume_ml = st.number_input("Volume larutan (mL):", min_value=0.0, format="%.4f")
    valensi = st.number_input("Valensi zat:", min_value=1, step=1)

    submitted = st.form_submit_button("Hitung Normalitas")

    if submitted:
        try:
            volume_liter = volume_ml / 1000
            mol = berat / massa_molar
            normalitas = (mol / volume_liter) * valensi
            st.success(f"Normalitas larutan: *{normalitas:.4f} N*")
        except Exception as e:
            st.error("Terjadi kesalahan saat menghitung. Pastikan input valid.")
            
def tentang():
    st.markdown(
        f"""
        <style>
            .blurimg {{
                background-image: url("https://github.com/mu77ti/LPK-kelompok-12-projek/blob/main/Logo%20Pecinta%20Alam%20dan%20Petualangan%20Retro%20Krem%20dan%20Merah.png");
                background-size: cover;
                position: fixed;
                inset: 0;
                filter: blur(4px);
                background-color: rgba(0, 0, 0, 0.8); /* Transparent black overlay */
            }}
        </style>
        <div class="blurimg"></div>
        """,
        unsafe_allow_html=True
    )
    st.title("Tentang Website")
    st.markdown(
    f"""
    <style>
        p {{
            font-size: 18px;
            color: white;
        }}

import streamlit as st
from theme import STYLE

st.set_page_config(page_title="About | Chicken Nuggets Store", page_icon="🍗", layout="wide")
st.markdown(STYLE, unsafe_allow_html=True)

if "cart" not in st.session_state:
    st.session_state.cart = []

nav1, nav2, nav3, nav4, nav5 = st.columns([2, 1, 1, 1, 1])
with nav1:
    st.markdown('<div class="brand">🍗 Nuggets</div>', unsafe_allow_html=True)
with nav2:
    st.page_link("app.py", label="Home")
with nav3:
    st.page_link("pages/1_Shop.py", label="Shop")
with nav4:
    st.markdown('<div style="color:#FF7A1A; font-size:14px; font-weight:600; padding-top:6px;">About</div>', unsafe_allow_html=True)
with nav5:
    cart_count = 0
    for item in st.session_state.cart:
        cart_count = cart_count + item["qty"]
    st.page_link("pages/2_Cart.py", label="Cart (" + str(cart_count) + ")")

st.markdown('<div class="hero-title" style="font-size:32px;">About Me</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="card">
        <p>I'm Ariz — a self-taught frontend developer based in Karachi, Pakistan.
        I am currently learning Python from MITI and this is one of my Assigment.
        This store is one of my course projects, built with Streamlit.</p>
        <p>Check out my other work on GitHub:
        <a href="https://github.com/mirzamuhammadarizbaig" target="_blank" style="color:#FF7A1A;">
        github.com/mirzamuhammadarizbaig</a></p>
    </div>
    """,
    unsafe_allow_html=True,
)
import streamlit as st
from theme import STYLE

st.set_page_config(page_title="Chicken Nuggets Store", page_icon="🍗", layout="wide")
st.markdown(STYLE, unsafe_allow_html=True)

nav1, nav2, nav3, nav4, nav5 = st.columns([2, 1, 1, 1, 1])
with nav1:
    st.markdown('<div class="brand">🍗 Nuggets</div>', unsafe_allow_html=True)
with nav2:
    st.page_link("app.py", label="Home")
with nav3:
    st.page_link("pages/1_Shop.py", label="Shop")
with nav4:
    st.page_link("pages/3_About.py", label="About")
with nav5:
    cart_count = 0
    for item in st.session_state.get("cart", []):
        cart_count = cart_count + item["qty"]
    st.page_link("pages/2_Cart.py", label="Cart (" + str(cart_count) + ")")

st.markdown('<div class="tag">🍗 Made to Crunch</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-title">Nugget Sound.<br>Crispy Clear.</div>', unsafe_allow_html=True)
st.write("A wireless earbud, sold by a chicken nugget brand. Don't overthink it.")

st.page_link("pages/1_Shop.py", label="Shop Now →")

st.write("")
st.write("")

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(
        """
        <div class="card">
            <div class="card-title">Connection</div>
            <div style="font-size:20px; font-weight:700;">Bluetooth 6.0</div>
            <div style="font-size:13px; color:#999;">stable, low latency</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with c2:
    st.markdown(
        """
        <div class="card">
            <div class="card-title">Calls</div>
            <div style="font-size:20px; font-weight:700;">4-Mic ENC</div>
            <div style="font-size:13px; color:#999;">clear in noisy places</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with c3:
    st.markdown(
        """
        <div class="card">
            <div class="card-title">Case</div>
            <div style="font-size:20px; font-weight:700;">LED Display</div>
            <div style="font-size:13px; color:#999;">battery at a glance</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

import streamlit as st
from theme import STYLE

st.set_page_config(page_title="Shop | Chicken Nuggets Store", page_icon="🍗", layout="wide")
st.markdown(STYLE, unsafe_allow_html=True)

if "cart" not in st.session_state:
    st.session_state.cart = []

product_name = "Lenovo ERAZER EX216 4-Earbud Stereo LED Display HD Call ENC Bluetooth 6.0 In-Ear Wireless Earphones"
product_price = 25.99
product_old_price = 69.99
product_img = "https://ae-pic-a1.aliexpress-media.com/kf/Sa0e25427f3f3411aa84cc7e650433cf0b.jpg"
product_desc = "In-ear wireless earbuds with a charging case that has a built in LED display. 4-mic ENC keeps calls clear, Bluetooth 6.0 for a stable connection, and a secure in-ear fit for daily use."
product_colors = ["Black", "Orange"]
product_features = [
    "Bluetooth 6.0 connectivity",
    "4-mic ENC for clear calls",
    "LED display on charging case",
    "Secure in-ear fit",
    "Long battery life with the case",
]

nav1, nav2, nav3, nav4, nav5 = st.columns([2, 1, 1, 1, 1])
with nav1:
    st.markdown('<div class="brand">🍗 Nuggets</div>', unsafe_allow_html=True)
with nav2:
    st.page_link("app.py", label="Home")
with nav3:
    st.markdown('<div style="color:#FF7A1A; font-size:14px; font-weight:600; padding-top:6px;">Shop</div>', unsafe_allow_html=True)
with nav4:
    st.page_link("pages/3_About.py", label="About")
with nav5:
    cart_count = 0
    for item in st.session_state.cart:
        cart_count = cart_count + item["qty"]
    st.page_link("pages/2_Cart.py", label="Cart (" + str(cart_count) + ")")

col1, col2 = st.columns([1.4, 1])

with col1:
    st.markdown(
        '<img src="' + product_img + '" style="width:380px; max-width:100%; border-radius:16px; '
        'display:block; margin-bottom:16px; margin-left:-16px; object-fit:cover;">',
        unsafe_allow_html=True,
    )
    st.subheader(product_name)
    st.markdown(
        '<span class="price">&#36;' + str(product_price) + '</span><span class="old-price">&#36;' + str(product_old_price) + '</span>',
        unsafe_allow_html=True,
    )
    st.write(product_desc)

    color = st.selectbox("Color", product_colors)
    qty = st.number_input("Quantity", min_value=1, max_value=10, value=1)

    btn_col1, btn_col2 = st.columns(2)

    if btn_col1.button("Add to Cart", use_container_width=True):
        st.session_state.cart.append({"color": color, "qty": qty, "price": product_price})
        st.success("Added to cart")

    if btn_col2.button("Buy Now", use_container_width=True):
        st.session_state.cart.append({"color": color, "qty": qty, "price": product_price})
        st.session_state.stage = "checkout"
        st.switch_page("pages/2_Cart.py")

with col2:
    st.markdown(
        """
        <div class="card">
            <div class="card-title">Popular Colors</div>
            <div style="display:flex; gap:10px;">
                <div style="width:24px; height:24px; border-radius:50%; background-color:#111; border:2px solid #333;"></div>
                <div style="width:24px; height:24px; border-radius:50%; background-color:#FF7A1A; border:2px solid #333;"></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="card">
            <div class="card-title">Rating</div>
            <div class="price" style="font-size:26px;">4.4 / 5</div>
            <div style="font-size:12px; color:#999;">367 reviews</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    features_html = '<div class="card"><div class="card-title">Features</div>'
    for f in product_features:
        features_html += '<div class="feature-row"><span class="feature-dot">●</span> ' + f + '</div>'
    features_html += '</div>'
    st.markdown(features_html, unsafe_allow_html=True)
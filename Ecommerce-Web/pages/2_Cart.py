import streamlit as st
from theme import STYLE

st.set_page_config(page_title="Cart | Chicken Nuggets Store", page_icon="🍗", layout="wide")
st.markdown(STYLE, unsafe_allow_html=True)

if "cart" not in st.session_state:
    st.session_state.cart = []

if "stage" not in st.session_state:
    st.session_state.stage = "cart"

if "order" not in st.session_state:
    st.session_state.order = {}

product_name = "Lenovo ERAZER EX216 4-Earbud Stereo LED Display HD Call ENC Bluetooth 6.0 In-Ear Wireless Earphones"

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
    for item in st.session_state.cart:
        cart_count = cart_count + item["qty"]
    st.markdown('<div style="color:#FF7A1A; font-size:14px; font-weight:600; padding-top:6px;">Cart (' + str(cart_count) + ')</div>', unsafe_allow_html=True)

if st.session_state.stage == "cart":

    st.markdown('<div class="hero-title" style="font-size:30px;">Your Cart</div>', unsafe_allow_html=True)

    if len(st.session_state.cart) == 0:
        st.write("Cart is empty. Go grab some Nugget Buds.")
        st.page_link("pages/1_Shop.py", label="← Back to Shop")
    else:
        total = 0
        for item in st.session_state.cart:
            item_total = item["price"] * item["qty"]
            total = total + item_total
            st.markdown(
                '<div class="card">'
                '<div style="font-weight:600;">' + product_name + '</div>'
                '<div style="font-size:13px; color:#999;">' + item['color'] + ' · qty ' + str(item['qty']) + '</div>'
                '<div class="price" style="font-size:20px;">&#36;' + str(round(item_total, 2)) + '</div>'
                '</div>',
                unsafe_allow_html=True,
            )

        st.markdown('<div class="price">Total: &#36;' + str(round(total, 2)) + '</div>', unsafe_allow_html=True)
        st.write("")

        c1, c2 = st.columns(2)
        if c1.button("Checkout", use_container_width=True):
            st.session_state.stage = "checkout"
            st.rerun()
        if c2.button("Clear Cart", use_container_width=True):
            st.session_state.cart = []
            st.rerun()

elif st.session_state.stage == "checkout":

    st.markdown('<div class="hero-title" style="font-size:30px;">Checkout</div>', unsafe_allow_html=True)

    phone = st.text_input("Phone number", value="+92", max_chars=13)
    address = st.text_area("Delivery address")

    if st.button("Confirm Order"):
        if phone == "+92" or address.strip() == "":
            st.warning("Please fill in your phone number and address")
        else:
            st.session_state.order["phone"] = phone
            st.session_state.order["address"] = address
            st.session_state.stage = "review"
            st.rerun()

elif st.session_state.stage == "review":

    st.success("Order placed! It'll be delivered to " + st.session_state.order["address"])
    st.markdown('<div class="hero-title" style="font-size:30px;">Leave a Review</div>', unsafe_allow_html=True)

    rating = st.slider("Rating", 1, 5, 5)
    review_text = st.text_area("How was it?")

    if st.button("Submit Review"):
        st.session_state.order["rating"] = rating
        st.session_state.order["review"] = review_text
        st.session_state.stage = "done"
        st.rerun()

elif st.session_state.stage == "done":

    st.success("Thanks for your order and your review!")
    st.write("Rating: " + str(st.session_state.order.get("rating", "")) + " / 5")
    st.write("Review: " + st.session_state.order.get("review", ""))

    if st.button("Back to Store"):
        st.session_state.stage = "cart"
        st.session_state.cart = []
        st.switch_page("app.py")
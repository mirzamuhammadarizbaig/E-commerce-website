STYLE = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background-color: #0B0B0C;
    color: #EDEDED;
}

#MainMenu, header, footer {visibility: hidden;}
section[data-testid="stSidebar"] {display: none;}

.navbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 16px 6px;
    border-bottom: 1px solid #232323;
    margin-bottom: 34px;
}
.brand {
    font-size: 20px;
    font-weight: 700;
    color: #FF7A1A;
}

div[data-testid="stPageLink"] a {
    color: #B5B5B5 !important;
    font-size: 14px;
    font-weight: 500;
}
div[data-testid="stPageLink"] a:hover {
    color: #FF7A1A !important;
}

.tag {
    display: inline-block;
    background-color: #17171A;
    border: 1px solid #2A2A2A;
    color: #FF7A1A;
    font-size: 11px;
    font-weight: 600;
    padding: 5px 14px;
    border-radius: 20px;
    margin-bottom: 18px;
    letter-spacing: 0.5px;
}

.hero-title {
    font-size: 44px;
    font-weight: 800;
    line-height: 1.15;
    margin-bottom: 14px;
    background: linear-gradient(90deg, #FFFFFF 40%, #FF7A1A 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.card {
    background-color: #17171A;
    border: 1px solid #232323;
    border-radius: 20px;
    padding: 22px;
    margin-bottom: 18px;
    transition: border-color 0.2s ease, transform 0.2s ease;
}
.card:hover {
    border-color: #FF7A1A;
    transform: translateY(-2px);
}
.card-title {
    font-size: 11px;
    color: #999;
    margin-bottom: 10px;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    font-weight: 600;
}

.price {
    font-size: 30px;
    font-weight: 800;
    color: #FF7A1A;
}
.old-price {
    color: #6B6B6B;
    text-decoration: line-through;
    margin-left: 10px;
    font-size: 16px;
    font-weight: 500;
}

.badge {
    background-color: #FF7A1A;
    color: #0B0B0C;
    font-size: 11px;
    font-weight: 700;
    border-radius: 999px;
    padding: 1px 8px;
    margin-left: 4px;
}

.feature-row {
    display: flex;
    gap: 8px;
    align-items: center;
    margin-bottom: 10px;
    font-size: 13px;
    color: #D0D0D0;
}
.feature-dot {
    color: #FF7A1A;
    font-size: 10px;
}

div.stButton > button {
    background-color: #FF7A1A;
    color: #0B0B0C;
    border: none;
    border-radius: 10px;
    font-weight: 700;
    padding: 10px 26px;
    transition: background-color 0.2s ease, transform 0.15s ease;
}
div.stButton > button:hover {
    background-color: #ff8f3f;
    transform: translateY(-1px);
}

div[data-testid="stTextInput"] input,
div[data-testid="stTextArea"] textarea,
div[data-testid="stNumberInput"] input {
    background-color: #17171A;
    color: #EDEDED;
    border: 1px solid #2A2A2A;
    border-radius: 10px;
}

hr {
    border-color: #232323;
}
</style>
"""

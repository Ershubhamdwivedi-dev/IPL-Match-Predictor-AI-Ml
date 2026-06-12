import streamlit as st
import numpy as np

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(page_title="IPL Predictor", page_icon="🏏", layout="centered")

# ---------------------------
# Custom CSS
# ---------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #ff4b4b, #1f77b4);
}
.main {
    background-color: rgba(255,255,255,0.95);
    padding: 20px;
    border-radius: 15px;
}
h1 {
    text-align: center;
}
.stButton>button {
    background-color: #ff4b4b;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}
.stButton>button:hover {
    background-color: #e63946;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Title
# ---------------------------
st.markdown("<h1>🏏 IPL Match Predictor</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>AI + Smart Logic Based Prediction</h4>", unsafe_allow_html=True)
st.markdown("---")

# ---------------------------
# Inputs
# ---------------------------
teams = ["MI", "CSK", "RCB", "KKR"]
venues = ["Mumbai", "Chennai", "Bangalore", "Kolkata"]

col1, col2 = st.columns(2)

with col1:
    team1 = st.selectbox("🏟️ Team 1", teams)

with col2:
    team2 = st.selectbox("🏟️ Team 2", teams)

col3, col4 = st.columns(2)

with col3:
    # ✅ FIX: Toss sirf selected teams me se hi
    if team1 != team2:
        toss_winner = st.radio("🪙 Toss Winner", [team1, team2])
    else:
        toss_winner = None

with col4:
    venue = st.selectbox("📍 Venue", venues)

st.markdown("---")

# ---------------------------
# Logic
# ---------------------------
team_strength = {
    "MI": 88,
    "CSK": 92,
    "RCB": 78,
    "KKR": 82
}

venue_advantage = {
    "Mumbai": "MI",
    "Chennai": "CSK",
    "Bangalore": "RCB",
    "Kolkata": "KKR"
}

# ---------------------------
# Prediction
# ---------------------------
if st.button("🚀 Predict Winner"):

    if team1 == team2:
        st.error("❌ Please select different teams!")

    elif toss_winner not in [team1, team2]:
        st.error("❌ Toss winner must be one of the selected teams!")

    else:
        score1 = team_strength[team1]
        score2 = team_strength[team2]

        # Toss advantage
        if toss_winner == team1:
            score1 += 6
        else:
            score2 += 6

        # Venue advantage
        if venue_advantage[venue] == team1:
            score1 += 5
        elif venue_advantage[venue] == team2:
            score2 += 5

        # Random realism
        score1 += np.random.randint(0, 5)
        score2 += np.random.randint(0, 5)

        # Winner
        if score1 > score2:
            winner = team1
            prob = round((score1 / (score1 + score2)) * 100, 2)
        else:
            winner = team2
            prob = round((score2 / (score1 + score2)) * 100, 2)

        # ---------------------------
        # Result Card
        # ---------------------------
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #1f77b4, #ff4b4b);
            padding: 20px;
            border-radius: 15px;
            color: white;
            text-align: center;
        ">
            <h2>🏆 Winner: {winner}</h2>
            <h3>📊 Probability: {prob}%</h3>
        </div>
        """, unsafe_allow_html=True)

        st.progress(prob / 100)

        st.markdown("---")

        # ---------------------------
        # Score Cards
        # ---------------------------
        col5, col6 = st.columns(2)

        with col5:
            st.markdown(f"""
            <div style="
                background: #f8f9fa;
                padding: 15px;
                border-radius: 10px;
                text-align: center;
            ">
                <h3>{team1}</h3>
                <h2>{score1}</h2>
            </div>
            """, unsafe_allow_html=True)

        with col6:
            st.markdown(f"""
            <div style="
                background: #f8f9fa;
                padding: 15px;
                border-radius: 10px;
                text-align: center;
            ">
                <h3>{team2}</h3>
                <h2>{score2}</h2>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")

        st.caption("⚡ Prediction based on AI logic + toss + venue advantage")
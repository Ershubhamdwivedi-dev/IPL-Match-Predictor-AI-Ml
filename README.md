# 🏏 IPL Match Predictor

The IPL Match Predictor is a simple and interactive web application built using Python and Streamlit. It predicts the winner of an IPL match based on smart logic including team strength, toss advantage, and venue conditions.

## 🚀 Features

- 🏟️ Select two teams
- 🪙 Toss winner selection (only valid teams)
- 📍 Venue-based advantage
- 📊 Win probability calculation
- 🎨 Clean and modern UI using Streamlit
- ⚡ Fast and lightweight application

## 🧠 How It Works

The prediction is based on a scoring system:

- Each team has a predefined **strength score**
- The **toss winner gets extra advantage**
- The **home team gets venue advantage**
- A small **random factor** is added to simulate real match uncertainty
- The team with the higher score is declared the winner

## 🛠️ Tech Stack

- Python
- Streamlit
- NumPy

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🌐 Deployment

You can deploy this app easily using Streamlit Cloud by connecting your GitHub repository.

## 📌 Note

This project is based on logical scoring and not on a trained machine learning model. It is built for learning and demonstration purposes.

---

💡 Future Improvements:
- Add real IPL dataset
- Train ML model for prediction
- Add team logos and animations
- Improve UI/UX further

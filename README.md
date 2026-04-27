# 💻 Lappytol: Laptop Price Predictor

Ever wondered if you're overpaying for a laptop? I built this app 
to solve exactly that. Just enter the specs and it tells you the 
fair market price instantly.

## 🔍 Why I Built This
Laptop shopping is overwhelming — too many brands, specs, and price 
ranges. This project helps buyers get a data-driven price estimate 
based on real market data so they never overpay again.

## 📊 Dataset
- 1,300+ real laptop records scraped from e-commerce platforms
- Features used: Brand, RAM, Storage, GPU, CPU, Screen Size, OS, Weight

## 🛠️ Tech Stack
- **Language:** Python
- **ML Libraries:** Scikit-learn, XGBoost, Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Web App:** Streamlit

## 🏆 What I Tried & What Worked
I experimented with multiple models before landing on XGBoost:

| Model | R² Score | MAE |
|-------|----------|-----|
| Random Forest | 0.95 | 0.11 |
| Gradient Boosting | 0.96 | 0.10 |
| **XGBoost ✅** | **0.97** | **0.09** |

XGBoost won — 97% accuracy with the lowest error rate.

## 🚀 Want to Run It Locally?
git clone https://github.com/Bajpaisa

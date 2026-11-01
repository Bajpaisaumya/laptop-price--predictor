# 💻 Laptop Price Prediction Using Machine Learning

## 📌 Project Overview

Laptop Price Prediction is a Machine Learning project that predicts the estimated price of a laptop based on its hardware specifications and configuration.

The project uses various Machine Learning algorithms to analyze laptop features and identify patterns that influence laptop pricing. It also provides an interactive web application built using Streamlit, allowing users to enter laptop specifications and get an estimated price.

## 🎯 Problem Statement

Laptop prices vary depending on several factors, including brand, processor, RAM, storage, GPU, and other technical specifications.

The objective of this project is to develop a Machine Learning model that can predict laptop prices based on these features and help users estimate the market value of a laptop.

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Data Manipulation:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn, XGBoost
- **Web Application:** Streamlit
- **Model Serialization:** Pickle / Joblib (as implemented)

## 📂 Project Workflow

1. Data Collection
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Encoding Categorical Variables
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Model Comparison
10. Model Deployment using Streamlit

## 📊 Exploratory Data Analysis (EDA)

Exploratory Data Analysis is performed to understand the dataset and identify relationships between laptop specifications and their prices.

Key analysis areas:

- Distribution of laptop prices
- Brand-wise price comparison
- Relationship between RAM and laptop prices
- Processor and GPU impact on pricing
- Storage configuration analysis
- Correlation between numerical features

## ⚙️ Data Preprocessing

The following preprocessing techniques are used where applicable:

- Handling missing values
- Removing duplicate records
- Handling categorical variables
- Feature engineering
- Identifying and handling outliers
- Preparing data for Machine Learning models

## 🤖 Machine Learning Models

The following regression algorithms are explored in this project:

- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor

Each model is trained and evaluated to compare its predictive performance.

## 📈 Model Evaluation

The models are evaluated using regression evaluation metrics:

| Metric | Description |
|---|---|
| MAE | Mean Absolute Error |
| MSE | Mean Squared Error |
| RMSE | Root Mean Squared Error |
| R² Score | Coefficient of Determination |

The models are compared to identify the most suitable model for laptop price prediction.

## 🌐 Streamlit Web Application

An interactive Streamlit application allows users to:

- Enter laptop specifications.
- Select relevant hardware configurations.
- Get an estimated laptop price.
- Interact with the trained Machine Learning model.

## 🚀 Installation and Usage

### 1. Clone the Repository

```bash
git clone https://github.com/Bajpaisaumya/laptop-price--predictor.git
```

### 2. Navigate to the Project Directory

```bash
cd laptop-price--predictor
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
streamlit run app.py
```

Note: Update the application filename in the command if your Streamlit entry-point file has a different name.

## 📁 Project Structure

```text
Laptop-Price-Predictor/
│
├── dataset/
│   └── laptop_data.csv
│
├── notebooks/
│   └── laptop_price_prediction.ipynb
│
├── models/
│   └── trained_model.pkl
│
├── app.py
├── requirements.txt
└── README.md
```

Note: Adjust the folder structure above to match the actual repository.

## 🔮 Future Improvements

- Improve prediction accuracy through hyperparameter tuning.
- Explore additional regression algorithms.
- Integrate real-time laptop price data.
- Improve the user interface.
- Deploy the application on a cloud platform.

## 👩‍💻 Author

**Saumya Bajpai**

Computer Science Engineering | AIML

Interested in Artificial Intelligence, Machine Learning, Data Analytics, and Generative AI.

GitHub: [Bajpaisaumya](https://github.com/Bajpaisaumya)

---

⭐ If you find this project interesting, feel free to explore the repository!

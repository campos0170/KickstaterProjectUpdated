# 🎯 Kickstarter Success Prediction Dashboard

This project is an enhanced version of my original Kickstarter prediction platform. Rebuilt using **Dash and Plotly**, this interactive dashboard enables users to explore Kickstarter campaign trends and predict the likelihood of campaign success based on pre-launch features.

<p align="center">
  <img src="assets/demo-screenshot.png" alt="App Screenshot" width="80%">
</p>

---

## 🚀 Key Features

### 🔍 Exploratory Data Analysis
- Interactive bar, box, and scatter plots using Plotly
- Log scaling, percentile clipping, and category filtering for clearer insights
- EDA tab for visualizing success rates, pledge distributions, and campaign dynamics

### 🤖 Success Prediction
- Uses an **XGBoost model** trained on structured campaign metadata
- Accepts user input for pre-launch features: goal amount, category, currency, location, and more
- Predicts success probability directly from the interface
- Achieves **82% accuracy** on validation data

### 🛠️ Technical Stack
- **Dash & Plotly**: Frontend framework for dynamic web visualization
- **XGBoost + Scikit-learn Pipeline**: Robust model with preprocessing embedded
- **Pandas & NumPy**: Data manipulation and feature engineering
- **Custom CSS**: Responsive and modern UI design

---

## 📁 Project Structure


---

## 📊 Dataset

The dataset includes thousands of Kickstarter projects across various categories. It includes features such as:
- `goal`, `log_goal`, `pledged`
- `category_name`, `subcategory`
- `currency`, `country_displayable_name`, `city`
- `staff_pick`, `spotlight`, `month`
- `success` (binary target)

A total of **12.5GB** of raw Kickstarter data was cleaned, engineered, and structured for modeling.

---

## 🧠 Model Info

- **Model**: XGBoost Classifier
- **Preprocessing**: 
  - `SimpleImputer` for missing values
  - `OneHotEncoder` for categorical features
  - `StandardScaler` for numerical features
  - All combined using a `ColumnTransformer`
- **Performance**: 82% accuracy on the test set

---

## 🖥️ Running the App

### 1. Install dependencies

```bash
pip install -r requirements.txt

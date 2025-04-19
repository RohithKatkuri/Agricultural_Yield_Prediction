# 🌾 Agricultural Yield Prediction using Machine Learning

A Streamlit web application that predicts agricultural crop yield based on key input parameters. This project aims to support farmers, policymakers, and agronomists in making informed decisions for better crop planning and resource utilization.

🔗 **Live Demo**: [Click here to view the app](https://rohithkatkuri-agricultural-yield-prediction.streamlit.app/)

---

## 📌 Features

- Predicts crop yield using a trained machine learning model.
- Interactive and easy-to-use Streamlit interface.
- Accepts multiple input parameters like crop type, area, and rainfall.
- Hosted online for seamless access.

---

## 🚀 Technologies Used

- **Python**
- **Pandas, NumPy, Scikit-learn, Joblib**
- **Streamlit** for web UI
- **Jupyter Notebook** for EDA and model building

---

## 📊 Dataset

- The dataset includes features like crop type, area of land, rainfall, and yield.
- Source: https://www.kaggle.com/datasets/bhadramohit/agriculture-and-farming-dataset

---

## 🧠 Model Info

Multiple regression models were trained and evaluated:

- **Linear Regression**
- **Random Forest Regressor**
- **Gradient Boosting Regressor** ✅ *(Best performing model)*

📈 **Gradient Boosting** gave the highest prediction accuracy and was selected for deployment.  
The final model is saved using `joblib` and integrated into the Streamlit app.

---


## 🛠️ How to Run Locally

```bash
# Clone the repo
git clone https://github.com/RohithKatkuri/Agricultural_Yield_Prediction.git
cd Agricultural_Yield_Prediction

# Create virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
---

🙌 Author
Rohith Katkuri

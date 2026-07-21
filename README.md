# Car_Price_Prediction
# 🚗 Car Price Prediction

## 📌 Project Description

This is a Machine Learning web application developed using Python and Streamlit. The application predicts the selling price of a used car based on user inputs such as manufacturing year, present price, kilometers driven, owner details, fuel type, seller type, transmission type, and car model.

## ✨ Features

- Predicts used car selling price
- User-friendly Streamlit interface
- One-Hot Encoding for categorical features
- StandardScaler for numerical features
- Fast and accurate prediction

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

## 📂 Project Structure

```
CarData_Model/
│── app.py
│── CarData.csv
│── requirements.txt
│── README.md
│
└── Models/
    ├── cardata.pkl
    ├── scaler.pkl
    └── columns.pkl
```

## 📊 Input Features

- Manufacturing Year
- Present Price
- Kilometers Driven
- Number of Owners
- Fuel Type
- Seller Type
- Transmission Type
- Car Name

## 🎯 Output

The application predicts the estimated selling price of the car in Lakhs.

## ▶️ How to Run

### Clone the Repository

```bash
git clone https://github.com/codewithsamiksha/CarData_Model.git
```

### Install Required Libraries

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

## 📁 Dataset

Car Price Prediction Dataset

## 👩‍💻 Author

**Samiksha Dalu**

GitHub: https://github.com/codewithsamiksha
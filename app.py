import pandas as pd
import streamlit as st
import joblib

model = joblib.load("Models/cardata.pkl")
columns = joblib.load("Models/columns.pkl")
scaler = joblib.load("Models/scaler.pkl")

st.set_page_config(
    page_title="CarData",
    layout="centered"
)

st.title("🚗 Car Price Prediction")
st.write("Enter the car details")

Year = st.number_input(
    "Manufacturing Year",
    min_value=0,
    max_value=2025,
    value=2018
)
Present_Price = st.number_input(
    "Present Price",
    min_value=0,
    max_value=6,
    value=5
)
Kms_Driven = st.number_input(
    "Kms Driven",
    min_value=0,
    max_value=27000,
    value=5200
)
Owner = st.number_input(
    "Owner",
    min_value=0,
    max_value=5,
    value=1

)
#selection box
Fuel_Type = st.selectbox(
    "Select Fuel Type",
    [
        "Petrol",
        "Diesel",
        "Hybrid",
        "Electrical",
        "Other"
    ]
)

Seller_Type = st.selectbox(
    "Select Seller type",
    [
        "Dealer",
        "Individual"
    ]
)
Transmission = st.selectbox(
    "Select Transmission Type",
    [
        "Manual",
        "Automatic"
    ]
)

#Text_input
Car_Name = st.text_input("Model","wagon r")

#Predict button

if st.button("Predict Price"):
    input_df = pd.DataFrame({
        "Year" : [Year],
        "Present_price" : [Present_Price],
        "Kms_Driven" : [Kms_Driven],
        "Owner" : [Owner],
        "Fuel_Type" : [Fuel_Type],
        "Seller_Type" : [Seller_Type],
        "Transmission" : [Transmission]
    })

    # input_df = pd.get_dummies(input_df)
    car_col = "Car_Name_" + Car_Name
    fuel_col = "Fuel_Type_" + Fuel_Type
    seller_col = "Seller_Type_" + Seller_Type
    trans_col = "Transmission_" + Transmission

final_input = pd.DataFrame(columns=columns)
final_input.loc[0] = 0

# Numerical
final_input.loc[0, "Year"] = Year
final_input.loc[0, "Present_Price"] = Present_Price
final_input.loc[0, "Kms_Driven"] = Kms_Driven
final_input.loc[0, "Owner"] = Owner

# One Hot Encoding
car = "Car_Name_" + Car_Name
fuel = "Fuel_Type_" + Fuel_Type
seller = "Seller_Type_" + Seller_Type
trans = "Transmission_" + Transmission

if car in final_input.columns:
    final_input.loc[0, car] = 1
if fuel in final_input.columns:
    final_input.loc[0, fuel] = 1

if seller in final_input.columns:
    final_input.loc[0, seller] = 1

if trans in final_input.columns:
    final_input.loc[0, trans] = 1

# Scaling
num_col = ["Year", "Present_Price", "Kms_Driven", "Owner"]
final_input[num_col] = scaler.transform(final_input[num_col])

# Prediction
prediction = model.predict(final_input)

st.success(f"Predicted Selling Price: ₹ {prediction[0]:,.2f} Lakhs")


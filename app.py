"""
##########################################################
         SINGAPORE FLATS RESALE PRICE PREDICTION
##########################################################
"""


#-----------------MODULES-USED-------------------
import streamlit as st
import base64
from PIL import Image
import datetime
import numpy as np
import pickle
import pandas as pd



#------------------HOMEPAGE---------------------
def homepage():
    st.title("SINGAPORE RESALE FLAT PRICES PREDICTION")
    st.write("Project By Tumu Mani Sai Pavan")
    file = open("Flats_image.gif", "rb")
    contents = file.read()
    data_gif = base64.b64encode(contents).decode("utf-8")
    file.close()
    st.markdown(f'<img src="data:image/gif;base64,{data_gif}" style="width: 800px;" >',unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Overview")
    st.write("""The objective of this project is to develop a machine learning model and deploy it as a user-friendly web application that predicts 
                the resale prices of flats in Singapore. This predictive model will be based on historical data of resale flat transactions, and it 
                aims to assist both potential buyers and sellers in estimating the resale value of a flat.""")
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Skills Takeaway")
    st.write("""
                1) Data Wrangling
                2) EDA
                3) Model Building
                4) Model Deployment
                5) Streamlit 
             """)
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("About me")
    st.write(""""Self-motivated computer science student with keen interest in coding". Engineer with a passion for machine learning, With a mix of academic knowledge, practical skills, and a growth-oriented attitude, I'm eager to make my debut in the AI & ML field.""")
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Contact")
    st.write("For any queries or collaborations, feel free to reach out to me:")
    email_icon = Image.open("C:/Users/saipa/Downloads/mail.jpg")
    st.write("Email:")
    col1, col2 = st.columns([0.4, 5])
    with col1:
        st.image(email_icon, width=50)
    with col2:
        st.write("tmsaipavan@gmail.com")
    lin_icon = Image.open("C:/Users/saipa/Downloads/in.jpg")
    st.write("LinkedIn:")
    col1, col2 = st.columns([0.4, 5])
    with col1:
        st.image(lin_icon, width=50)
    with col2:
        st.write("[Sai Pavan TM](https://www.linkedin.com/in/saipavantm/)")


#------------------PREDICTION---------------------
def prediction():
    st.title("Obtain Prediction")
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    enc_months = {"January" : 1,"February" : 2,"March" : 3,"April" : 4,"May" : 5,"June" : 6,"July" : 7,"August" : 8,"September" : 9,
                "October" : 10 ,"November" : 11,"December" : 12}
    curr_year = datetime.datetime.now().year
    year = [str(year) for year in range(1990, curr_year + 1)]
    town = ['ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH','BUKIT TIMAH', 'CENTRAL AREA', 'CHOA CHU KANG', 'CLEMENTI',
            'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST','KALLANG/WHAMPOA', 'MARINE PARADE', 'QUEENSTOWN', 'SENGKANG','SERANGOON',
            'TAMPINES', 'TOA PAYOH', 'WOODLANDS', 'YISHUN','LIM CHU KANG', 'SEMBAWANG', 'BUKIT PANJANG', 'PASIR RIS','PUNGGOL']
    enc_town = {'ANG MO KIO' : 0 ,'BEDOK' : 1,'BISHAN' : 2,'BUKIT BATOK' : 3,'BUKIT MERAH' : 4,'BUKIT PANJANG' : 5,'BUKIT TIMAH' : 6,
            'CENTRAL AREA' : 7,'CHOA CHU KANG' : 8,'CLEMENTI' : 9,'GEYLANG' : 10,'HOUGANG' : 11,'JURONG EAST' : 12,'JURONG WEST' : 13,
            'KALLANG/WHAMPOA' : 14,'LIM CHU KANG' : 15,'MARINE PARADE' : 16,'PASIR RIS' : 17,'PUNGGOL' : 18,'QUEENSTOWN' : 19,
            'SEMBAWANG' : 20,'SENGKANG' : 21,'SERANGOON' : 22,'TAMPINES' : 23,'TOA PAYOH' : 24,'WOODLANDS' : 25,'YISHUN' : 26}
    flat_type = ['1 ROOM', '2 ROOM','3 ROOM', '4 ROOM', '5 ROOM', 'EXECUTIVE','MULTI GENERATION']
    enc_flat_type = {'1 ROOM': 0,'2 ROOM' : 1,'3 ROOM' : 2,'4 ROOM' : 3,'5 ROOM' : 4,'EXECUTIVE' : 5,'MULTI-GENERATION' : 6}
    flat_model = ['2-ROOM','3GEN','ADJOINED FLAT', 'APARTMENT' ,'DBSS','IMPROVED' ,'IMPROVED-MAISONETTE', 'MAISONETTE',
                        'MODEL A', 'MODEL A-MAISONETTE','MODEL A2' ,'MULTI GENERATION' ,'NEW GENERATION', 'PREMIUM APARTMENT',
                        'PREMIUM APARTMENT LOFT', 'PREMIUM MAISONETTE','SIMPLIFIED', 'STANDARD','TERRACE','TYPE S1','TYPE S2']
    enc_flat_model = {'2-ROOM' : 0,'3GEN' : 1,'ADJOINED FLAT' : 2,'APARTMENT' : 3,'DBSS' : 4,'IMPROVED' : 5,'IMPROVED-MAISONETTE' : 6,
                    'MAISONETTE' : 7,'MODEL A' : 8,'MODEL A-MAISONETTE' : 9,'MODEL A2': 10,'MULTI GENERATION' : 11,'NEW GENERATION' : 12,
                    'PREMIUM APARTMENT' : 13,'PREMIUM APARTMENT LOFT' : 14,'PREMIUM MAISONETTE' : 15,'SIMPLIFIED' : 16,'STANDARD' : 17,
                    'TERRACE' : 18,'TYPE S1' : 19,'TYPE S2' : 20}
    
    user_month = st.selectbox(label = "Month", options = months, index = None)
    user_town = st.selectbox(label = "Town", options = town, index = None)
    user_flat_type = st.selectbox(label = "Flat Type", options = flat_type, index = None)
    user_flat_model = st.selectbox(label = "Flat Model", options = flat_model, index = None)
    floor_area_sqm = st.number_input(label = "Floor area sqm (10 to 307)", min_value = 10.0)
    price_per_sqm = st.number_input(label = "Price Per sqm", min_value = 100.00)
    year = st.selectbox(label = "Year", options=year, index = None)
    block = st.number_input(label = "Block (1 to 999)", min_value = 1, max_value = 999, step = 1)
    lease_commence_date = st.text_input(label = "Year of lease commence (1966 to 2020)", max_chars = 4)
    remaining_lease = st.number_input(label="Remaining lease year (0 to 99)", min_value = 0, max_value = 99, step = 1)
    years_holding = st.number_input(label = "Years holding (0 to 99)", min_value = 0, max_value = 99, step = 1)
    storey_start = st.number_input(label = "Storey Start (1 to 50)", min_value = 1, max_value = 50)
    storey_end = st.number_input(label = "Storey End (1 to 51)", min_value = 1, max_value = 51)
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Predict"):
        with st.spinner("Predicting"):
                if not all([user_month,user_town,user_flat_type,user_flat_model,floor_area_sqm,price_per_sqm,year,block,
                            lease_commence_date,remaining_lease,years_holding,storey_start,storey_end]):
                    st.error("Please fill all the required fields.")
                else:
                    curr_rem_lease = remaining_lease-(curr_year-(int(year)))
                    age_property = curr_year - int(lease_commence_date)
                    month = enc_months[user_month]
                    tow = enc_town[user_town]
                    f_type = enc_flat_type[user_flat_type]
                    f_model = enc_flat_model[user_flat_model]
                    f_area_sqm_log = np.log(floor_area_sqm)
                    r_lease_log = np.log1p(remaining_lease)
                    price_p_sqm_log = np.log(price_per_sqm)

                    with open("DecisionTree.pkl", "rb") as file:
                        model = pickle.load(file)
                    feature_names = ["month", "town", "flat_type", "block", "flat_model", "lease_commence_date", "year", "storey_start", "storey_end", "years_holding", "current_remaining_lease",
                                     "age_of_property", "floor_area_sqm_log", "remaining_lease_log", "price_per_sqm_log"]
                    arr = np.array([[month, tow, f_type, block, f_model, lease_commence_date, year, storey_start, storey_end, years_holding, curr_rem_lease,
                                     age_property, f_area_sqm_log, r_lease_log, price_p_sqm_log]])
                    arr_df = pd.DataFrame(arr, columns = feature_names)
                    predict = model.predict(arr_df)
                    price = np.exp(predict[0])

                    st.subheader(f"Predicted Resale Price is: :blue[${price:.2f}]")


#-----------------MAIN-FUNCTION-------------------
def main():
    app_mode = st.sidebar.radio("Go to", ("Homepage", "Obtain Prediction"))
    if app_mode=="Homepage":
        homepage()
    elif app_mode=="Obtain Prediction":
        prediction()


#---------------EXECUTE-MAIN-FUNCTION--------------
main()

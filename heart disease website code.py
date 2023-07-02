import streamlit as st
st.set_page_config(
     page_title="Heart Disease Prediction",
     page_icon="❤",
     layout="wide",
     initial_sidebar_state="expanded"
 )
from streamlit_option_menu import option_menu

import numpy as np
import cv2
import pickle
import requests
from streamlit_lottie import st_lottie
import pyrebase
from datetime import datetime
import pandas as pd
from keras.models import load_model
from keras.applications.resnet import preprocess_input
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'



hide_menu_style="""
    <style>
    #MainMenu {visibility:hidden;}
    footer {visibility:hidden;}
    </style>
    """
st.markdown(hide_menu_style,unsafe_allow_html=True)

firebaseConfig = {
  'apiKey': "AIzaSyCqacatt9s45vbBDTlI5n29EUfWrex-tz0",
  'authDomain': "heart-disease-grad.firebaseapp.com",
  'projectId': "heart-disease-grad",
  'databaseURL':"https://heart-disease-grad-default-rtdb.europe-west1.firebasedatabase.app/",
  'storageBucket': "heart-disease-grad.appspot.com",
  'messagingSenderId': "44674343621",
  'appId': "1:44674343621:web:f2b673ecede314cdec46ac",
  'measurementId': "G-SN8EF67QKC"
}

firebase=pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

db=firebase.database()
storage=firebase.storage()


text=st.sidebar.error('Heart Disease Prediciton')


choice = st.sidebar.selectbox('LOGIN/SIGNUP',['Login','Signup'] )
email = st.sidebar.text_input('ENTER YOUR EMAIL ADDRESS')
password= st.sidebar.text_input('ENTER YOUR PASSWORD',type='password')


if choice== 'Signup':
    from PIL import Image
    
    image = Image.open('logo.png')
    
    st.image(image, caption='Sunrise by the mountains')
    
    handle=st.sidebar.text_input("ENTER YOUR NAME",value='default')
    submit = st.sidebar.button('CREATE ACCOUNT')
    
    if submit:
        user=auth.create_user_with_email_and_password(email, password)
        st.sidebar.success('ACCOUNT CREATED SUCCESSFULLY')
        st.info('WELCOME'+'--'+handle)
        st.caption('THANKS FOR SIGNING UP, PLEASE LOGIN TO CONTINUE')
        user=auth.sign_in_with_email_and_password(email, password)
        db.child(user['localId']).child('Handle').set(handle)
        db.child(user['localId']).child('Id').set(user['localId'])
        
if choice== 'Login':
    #from PIL import Image
        
    #image = Image.open('logo.png')
        
    #st.image(image, caption='Sunrise by the mountains')
    login=st.sidebar.checkbox('Login')
    
    if login:
        st.sidebar.success('LOGGED IN SUCCESSFULLY')
       
        user=auth.sign_in_with_email_and_password(email, password)
        
        st.write('<style>div.row-widget.stRadio>div{flex-direction:row;}</style>',unsafe_allow_html=True)
        
        
        selected2 = option_menu(None, ["Home", "PREDICT HEART DISEASE"], 
        icons=['house',"activity"], 
        menu_icon="cast", default_index=0, orientation="horizontal",
        styles={
        "container": {"padding": "0!important", "background-color": "#000000"},
        "icon": {"color": "red", "font-size": "20px"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#413839"},
        "nav-link-selected": {"background-color": "#000000"},
         })
        
    
        
        if selected2 == 'Home':
            
            
            new_title = '<p style="font-family:Georgia; color:#00FFFF; font-size: 34px;">Heart Disease Prediciton </p>'
            st.markdown(new_title, unsafe_allow_html=True)
            
            def load_lottieurl(url: str):
                r = requests.get(url)
                if r.status_code != 200:
                    return None
                return r.json()


            lottie_url_hello = "https://assets3.lottiefiles.com/packages/lf20_0ssane8p.json"
            lottie_url_download = "https://assets4.lottiefiles.com/private_files/lf30_t26law.json"
            lottie_hello = load_lottieurl(lottie_url_hello)
            lottie_download = load_lottieurl(lottie_url_download)
            st_lottie(lottie_hello, key="hello")
            
            new_title = '<p style="font-family:Open Sans; color:#FFFFFF; font-size: 24px;">The Cardio app aims at helping people by diagnosing coronary artery blockage and heart disease immediately. The main advantage is, it diagnose the disease automatically without the help of doctor. Using Artificial Intelligence(AI) the app is developed and make sure to consult the doctor for the confirmation of diseases.</p>'
            st.markdown(new_title, unsafe_allow_html=True)
            
# =============================================================================
#             new_title = '<p style="font-family:Georgia; color:#00FFFF; font-size: 34px;">HOW TO USE THE APP</p>'
#             st.markdown(new_title, unsafe_allow_html=True)
#             video_file = open('C:/Users/Kotha/Documents/Wondershare Filmora 9/Output/demo_instruc.mp4','rb')
# 
#             video_bytes = video_file.read() 
# 
#             st.video(video_bytes)
# =============================================================================
            
            
            
            
            new_title = '<p style="font-family:Georgia; color:#00FFFF; font-size: 34px;">HOW TO PREVENT HEART PROBLEMS ?</p>'
            st.markdown(new_title, unsafe_allow_html=True)
            
            st.write('⭕ Don’t smoke or use tobacco')
            st.write('⭕ Manage high cholesterol, high blood pressure and diabetes')
            st.write('⭕ Eat a heart-healthy diet.')
            
            st.write ('⭕ Limit alcohol use')
            st.write('⭕ Manage stress')
            st.write('⭕ Increase your activity level. Exercise helps you lose weight, improve your physical condition and relieve stress.')
            st.write('⭕ Do 30 minutes of walking 5 times per week or walking 10,000 steps per day')
            
            new_title = '<p style="font-family:Georgia; color:#00FFFF; font-size: 34px;">SOME FACTS ABOUT THE HEART</p>'
            st.markdown(new_title, unsafe_allow_html=True)
            st.write('⭕ The average heart is the size of a fist in an adult')
            st.write('⭕ Your heart will beat about 115,000 times each day')
            st.write('⭕ Your heart pumps about 2,000 gallons of blood every day')
            st.write('⭕ The heart pumps blood through 60,000 miles of blood vessels')
            st.write('⭕ A woman’s heart beats slightly faster than a man’s heart')
            st.write ('⭕ The heart can continue beating even when it’s disconnected from the body')
            
            st.write('⭕ Laughing is good for your heart. It reduces stress and gives a boost to your immune system')
               
                 
        if selected2  == 'PREDICT HEART DISEASE':
            loaded_model = pickle.load(open('C:/Users/osama/Desktop/sreamlit/finalized_model.sav', 'rb'))

            def heart(input_data):

                input_data_as_numpy_array = np.asarray(input_data)
                input_reshape = input_data_as_numpy_array.reshape(1,-1)
                prediction = loaded_model.predict(input_reshape)
             
                if (prediction[0]==0):
                    return st.success('This person has less chance of heart Disease')
                else:
                    return st.error('This person has more chance of heart Disease')
                    
                    
            # def main():
                
            new_title = '<p style="font-family:Georgia; color:##00FFFF; font-size: 34px;">HEART DISEASE PREDICTION</p>'
            st.markdown(new_title, unsafe_allow_html=True)
            
            BMI = st.number_input('Insert your BMI(The body mass index (BMI) is a measure that uses your height and weight to work out if your weight is healthy):')
            st.write('The current number is ', BMI)
            
            Smoking = st.checkbox("Do you Smoke?")
            if (Smoking == 1):
                st.info("Smoker")
            else:
                st.info("Non-Smoker")
               
            AlcoholDrinking = st.checkbox("Do you drink Alcohol?")
            if (AlcoholDrinking == 1):
                st.info("Does drink")
            else:
                st.info("Doesn't drink")
            
            Stroke = st.checkbox("Did you have a stroke recuntly?")
            if (Stroke == 1):
                st.info("Did have a stroke")
            else:
                st.info("Didn't have a stroke")
            
            physicalhealth   = st.number_input('physicalhealth,for how many days during the past 30 days was your physical health not good? (0-30 days)  ',step = 1)
            st.write('The current number is ', physicalhealth  )
            
            DiffWalking   = st.checkbox("Do you have Difficulty Walking?")
            if (DiffWalking == 1):
                st.info("Does have DiffWalking")
            else:
                st.info("Doesn't have DiffWalking")
            
            #Sex   = st.radio("Select gender 0: female  , 1: for male: ", (0,1))
            option = st.selectbox(
            'Select gender',
            ('Male', 'Female' ))
            if (option == 'Male'):
                Sex=1
            if (option == 'Female'):
                Sex=0
            #else:
                 #Sex=0
            st.write('You selected:', option)
        
            
            Diabetic   = st.checkbox("are you Diabetic?")
            if (Diabetic == 1):
                st.info("Diabetic")
            else:
                st.info("Not Diabetic")
            
            PhysicalActivity   = st.checkbox("Do you workout?")
            if (PhysicalActivity == 1):
                st.info("Does workout")
            else:
                st.info("Doesn't workout")
            
            GenHealth   = st.radio("GenHealth: from a scale from 1-4 how is your GenHealth:", (1,2,3,4))
            
            Asthma = st.checkbox("Do you have Asthma?")
            if (Asthma == 1):
                st.info("Does have Asthma")
            else:
                st.info("Doesn't have Asthma")
            
            KidneyDisease = st.checkbox("Do you have any Kidney Disease?")
            if (KidneyDisease == 1):
                st.info("Does have KidneyDisease")
            else:
                st.info("Doesn't have KidneyDisease")
            
            SkinCancer = st.checkbox("Do you have Skin Cancer?")
            if (SkinCancer == 1):
                st.info("Does have SkinCancer")
            else:
                st.info("Doesn't have SkinCancer")
            
            age = st.number_input('Insert your age:',step = 1)
            
            st.write('The current number is ', age)
            diagnosis = ''
         
            st.button('PREDICT')
            diagnosis = heart([BMI,Smoking,AlcoholDrinking,Stroke,physicalhealth,DiffWalking,Sex,Diabetic,GenHealth,PhysicalActivity  ,Asthma,KidneyDisease,SkinCancer,age])
            data={"BMI":BMI,"Smoking": Smoking,"AlcoholDrinking": AlcoholDrinking,"Stroke": Stroke,"physicalhealth":physicalhealth,"DiffWalking":DiffWalking,"Sex":Sex,"Diabetic":Diabetic,"GenHealth":GenHealth,"PhysicalActivity  ":PhysicalActivity  ,"Asthma":Asthma,"KidneyDisease":KidneyDisease,"SkinCancer":SkinCancer,"age":age}
            db.push(data)
# =============================================================================
#                     
#                 if __name__ == '__main__':
#                     main()  
#         
# =============================================================================

import streamlit as st
import pyrebase as pb


config = {
  'apiKey': "AIzaSyBfEwkx2NWboVcxEHpt9QFtOlKsPN_MaIw",
  'authDomain': "mrs-db-915e2.firebaseapp.com",
  'projectId': "mrs-db-915e2",
  'storageBucket': "mrs-db-915e2.appspot.com",
  'messagingSenderId': "957961658369",
  'appId': "1:957961658369:web:881c485214043bfba9a000",
  'measurementId': "G-BDBR624WPX",
  'databaseURL':"https://mrs-db-915e2-default-rtdb.asia-southeast1.firebasedatabase.app/"
}

fb = pb.initialize_app(config)
at = fb.auth()

def auths():
    
    st.title('Welcome to :violet[Recommendation System]')

    choice = st.selectbox('Login/Signup', ['Login', 'sign up'])
    
    # Add email as a parameter to the function
    def f(email,password):
        try:
            
            login = at.sign_in_with_email_and_password(email,password)
            st.success('Account created successfully!')
            
        except Exception as e:
            #print(e)
            st.warning('Incorrect Email or Passaword') 
            
    if choice == 'Login':
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')
        # Use button click as a condition to call the function
        if st.button('Login'):
            f(email,password)
    
    else:
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')
        username = st.text_input('Enter your unique username')
    
        if st.button('Create Account'):
            user = at.create_user_with_email_and_password(email,password) 
            st.success('Account created successfully!')
            st.markdown('Please Login using your email and password')
            st.balloons()

auths()

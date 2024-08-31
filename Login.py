import streamlit as st
import pyrebase as pb


# # Add CSS for background image
# def set_background():
#     # You can replace 'background.jpg' with the path to your image file
#     st.markdown(
#         """
#         <style>
#         .reportview-container {
#             background: url("") center;
#             background-size: cover;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )


# st.markdown(
#     """
#     <style>
#     .reportview-container {
#         background: url("https://images.pexels.com/photos/924824/pexels-photo-924824.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1") no-repeat center center fixed;
#         -webkit-background-size: cover;
#         -moz-background-size: cover;
#         -o-background-size: cover;
#         background-size: cover;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )


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
    
#  # Set background image
#     set_background()
    
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
            
            
            # HTML code for setting background image
# background_html = """
# <style>
# body {
#     background-image: url("https://images.pexels.com/photos/924824/pexels-photo-924824.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
#     background-size: cover;
# }
# </style>
# """

# # Display background image
# st.markdown(background_html, unsafe_allow_html=True)

auths()



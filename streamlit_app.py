import streamlit as st

st.set_page_config(
    page_title="AiFarms",
    page_icon=""
)

# st.page_link("D:\Crop_Rec\model\app.py" , lable = "Crop Prediction")

st.write("# Welcome to AiFarms")

with open('Home.css') as f:
    st.markdown(f'<style>{f.read()}</style>' , unsafe_allow_html=True)

def grid_fun(header , data , img):
    with st.container():
        st.write("---")
        left_col , right_col = st.columns((4 , 4))
        with left_col:
            st.header(header)
            st.write(data)
        with right_col:
            st.image(image=img)

st.markdown(
    """
    Our website offers cutting-edge technology to predict the most suitable crops and fertilizers for your farm.
    By leveraging our platform, you can make informed decisions to enhance your farming practices. Our goal is to empower farmers with data-driven insights, enabling you to plan your planting and fertilizing schedules with confidence. 
    ### Services Provided
    """
)

grid_fun("MultiCrop Recommendation" , "Discover the best crops for your land and climate with our advanced prediction algorithms." , "D:\Crop_Rec\model\images\crop.jpg")
grid_fun("Fertilizer Recommendations" , "Receive personalized fertilizer recommendations based on your soil type and crop selection." , "D:\Crop_Rec\model\images\Fertilizer.jpg")
grid_fun("Maximize Yield" , "Optimize your farming practices to maximize yield and minimize environmental impact." , "D:\Crop_Rec\model\images\yield.webp")
grid_fun("Join Our Community" , "Connect with other farmers, share insights, and stay updated with the latest agricultural trends." , "D:\Crop_Rec\model\images\community1.webp")

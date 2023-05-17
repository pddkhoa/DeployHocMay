import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Trang chủ",
    page_icon="	:house:",
    layout="wide"
)
SOCIAL_MEDIA_KHOA = {
    "Github": "https://github.com/pddkhoa",
    "Facebook": "https://www.facebook.com/khoadang.88.3154284/",
    "Instagram": "https://www.instagram.com/pdd.khoaa/",

}
SOCIAL_MEDIA_PHUC = {
    "Github": "https://github.com/pddkhoa",
    "Facebook": "https://www.facebook.com/khoadang.88.3154284/",
    "Instagram": "https://www.instagram.com/pdd.khoaa/",

}

image = Image.open('logo2.png')    
st.image(image,width=800)

st.write("# Chào mừng bạn đến với Website Streamlit! 👋")

st.markdown(
    """
    Đây là một website chứa các chức năng ứng dụng từ môn học Học Máy.  
    **👈 Chọn các demo từ bên sidebar** để thấy được các chức năng mà nhóm thực hiện!
    ### Nhóm thực hiện:
    """
)
col1, col2 = st.columns([1,2])
with col1:
    st.markdown("PHAN ĐẠI ĐĂNG KHOA - 20110504")
with col2:
    cols = st.columns(len(SOCIAL_MEDIA_KHOA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA_KHOA.items()):
        cols[index].write(f"[{platform}]({link})")


colP1, colP2 = st.columns([1,2])
with colP1:
    st.markdown("NGUYỄN TRƯỜNG PHÚC - 20142557")
with colP2:
    colsP = st.columns(len(SOCIAL_MEDIA_PHUC))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA_PHUC.items()):
        colsP[index].write(f"[{platform}]({link})")

st.write("---")
st.markdown(
    """
    ### Chức năng mà nhóm đã thực hiện:
    - Phát hiện khuôn mặt 👨‍🦲
    - Nhận dạng chính xác gương mặt 👍
    - Nhận dạng chữ số viết tay 🔢
    - Dự báo giá nhà California 🏡
    - Nhận dạng và phân loại các loại giống nho 🍇

    """
)

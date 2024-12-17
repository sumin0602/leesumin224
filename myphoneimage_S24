import streamlit as st
from PIL import Image
import io

# 갤럭시 S24 해상도 설정
GALAXY_S24_WIDTH = 1080
GALAXY_S24_HEIGHT = 2340

# 타이틀
st.title("📱✨ 갤럭시 S24 화면 크기 이미지 리사이저")

# 파일 업로드
uploaded_file = st.file_uploader("📤 이미지를 업로드하세요!", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 이미지 열기
    image = Image.open(uploaded_file)
    
    # 원본 이미지 표시
    st.subheader("🖼️ 원본 이미지")
    st.image(image, caption="업로드한 이미지", use_column_width=True)
    
    # 이미지 리사이즈
    res

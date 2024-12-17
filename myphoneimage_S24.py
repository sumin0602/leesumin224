import streamlit as st
from PIL import Image
from io import BytesIO

# 갤럭시 S24 화면 크기 (2400 x 1080)
TARGET_WIDTH = 1080
TARGET_HEIGHT = 2400

# 🎨 앱 제목과 설명
st.title("📱 갤럭시 S24 이미지 리사이즈 앱")
st.write("여기에서 이미지를 갤럭시 S24 화면 크기(2400 x 1080)로 리사이즈하고 다운로드할 수 있습니다. 🔄")

# 📂 이미지 파일 업로드
uploaded_file = st.file_uploader("이미지를 업로드하세요 📤", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 🖼️ 업로드한 이미지 열기
    image = Image.open(uploaded_file)
    
    # 업로드된 이미지 보여주기
    st.image(image, caption="업로드한 이미지", use_column_width=True)
    
    # 🔄 리사이즈 함수
    def resize_image(img):
        return img.resize((TARGET_WIDTH, TARGET_HEIGHT), Image.LANCZOS)

    # 🔧 이미지 리사이즈 처리
    with st.spinner("이미지 리사이징 중... ⏳"):
        resized_image = resize_image(image)
        
        # 📥 리사이즈된 이미지 표시
        st.image(resized_image, caption="리사이즈된 이미지", use_column_width=True)
        
        # 💾 다운로드 버튼 생성
        buffered = BytesIO()
        resized_image.save(buffered, format="PNG")
        st.success("✅ 이미지 리사이징 완료!")
        
        # 다운로드 버튼
        st.download_button(
            label="💾 리사이즈된 이미지 다운로드",
            data=buffered,
            file_name="resized_image.png",
            mime="image/png"
        )


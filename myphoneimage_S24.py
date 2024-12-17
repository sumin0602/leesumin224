import streamlit as st
from PIL import Image
import numpy as np
from rembg import remove
from io import BytesIO

# 갤럭시 S24 화면 크기
TARGET_WIDTH = 1080
TARGET_HEIGHT = 2400

# 🎨 단색 배경 색상 (인물사진 배경으로 사용)
DEFAULT_BG_COLOR = (128, 128, 128)  # 회색

# 🏷️ 앱 제목과 설명
st.title("📱 갤럭시 S24 이미지 리사이즈 & 배경 변경 앱")
st.write("업로드한 이미지를 갤럭시 S24 화면 크기(2400x1080)로 리사이즈합니다.")
st.write("🧍 인물사진의 경우 배경을 단색으로 변경해드립니다!")

# 📂 파일 업로드
uploaded_file = st.file_uploader("이미지를 업로드하세요:", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 🖼️ 이미지 열기
    image = Image.open(uploaded_file).convert("RGBA")
    st.image(image, caption="📥 업로드한 이미지", use_column_width=True)

    # 🛠️ 리사이즈 함수
    def resize_image(img):
        return img.resize((TARGET_WIDTH, TARGET_HEIGHT), Image.LANCZOS)

    # 🧍‍♀️ 배경 제거 및 단색 배경 추가 함수
    def process_human_image(img, bg_color=DEFAULT_BG_COLOR):
        # 배경 제거
        no_bg_img = remove(img)
        # 새로운 배경을 생성
        bg = Image.new("RGBA", no_bg_img.size, bg_color)
        # 배경과 결합
        processed_img = Image.alpha_composite(bg, no_bg_img)
        return processed_img

    # 🔄 이미지 리사이즈 처리
    with st.spinner("이미지 처리 중... 🕒"):
        # 인물 사진 여부 선택
        is_human = st.checkbox("🧍 인물 사진입니다", value=False)
        
        if is_human:
            image = process_human_image(image)
        
        # 리사이즈 수행
        resized_image = resize_image(image)
        
        # PNG로 변환
        buffered = BytesIO()
        resized_image.save(buffered, format="PNG")
        st.success("✅ 이미지 처리가 완료되었습니다!")
        
        # 결과 이미지 보여주기
        st.image(resized_image, caption="📱 편집된 이미지", use_column_width=True)

        # 💾 다운로드 링크 생성
        st.download_button(
            label="💾 이미지 다운로드",
            data=buffered,
            file_name="resized_image.png",
            mime="image/png"
        )

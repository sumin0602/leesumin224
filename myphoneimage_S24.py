import streamlit as st
from PIL import Image

# Streamlit 앱 설정
st.title("📱 갤럭시 S24 배경화면 리사이즈 🖼️")
st.write("업로드한 이미지를 갤럭시 S24에 맞는 해상도로 리사이즈합니다. 🌟")

# 갤럭시 S24 해상도
galaxy_s24_resolution = (3088, 1440)

# 이미지 업로드
uploaded_file = st.file_uploader("👉 이미지를 업로드하세요! (JPG, PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 업로드된 파일 열기
    image = Image.open(uploaded_file)
    
    # 원본 이미지 크기
    original_width, original_height = image.size

    # 비율을 유지하면서 리사이즈
    aspect_ratio = original_width / original_height
    if original_width > original_height:
        new_width = galaxy_s24_resolution[0]
        new_height = int(new_width / aspect_ratio)
    else:
        new_height = galaxy_s24_resolution[1]
        new_width = int(new_height * aspect_ratio)

    # 리사이즈된 이미지 생성
    resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    # 리사이즈된 이미지 보여주기
    st.image(resized_image, caption="📏 리사이즈된 이미지 👀", use_container_width=True)
    
    # 리사이즈된 이미지 저장
    save_button = st.button("💾 리사이즈된 이미지 다운로드")

    if save_button:
        # 리사이즈된 이미지를 저장할 경로 지정
        save_path = "/mnt/data/galaxy_s24_resized_image.png"
        resized_image.save(save_path)
        
        # 다운로드 링크 제공
        st.download_button("📥 다운로드", save_path, file_name="galaxy_s24_resized_image.png", mime="image/png")
        st.write("👉 다운로드가 완료되었습니다! 즐기세요! 🎉")

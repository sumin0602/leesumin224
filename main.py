import streamlit as st

# MBTI 선택 옵션
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# MBTI와 추천 직업 및 잘 맞는 사람 데이터
mbti_data = {
    "ISTJ": {
        "job": "📊 분석가, 🏛️ 공무원, 💼 회계사",
        "match": "✅ ESFP와 ESTP",
        "desc": "신중하고 체계적인 당신은 계획을 철저히 세우고, 규칙을 잘 지켜요. 신뢰성이 뛰어나 직업적 성공이 많답니다!"
    },
    "ISFJ": {
        "job": "🩺 간호사, 🍽️ 요리사, 🏫 교사",
        "match": "✅ ESTP와 ESFP",
        "desc": "배려심 깊고 성실한 당신은 남을 돕는 일을 할 때 행복해요. 마음이 따뜻하고 책임감이 강하답니다!"
    },
    "INFJ": {
        "job": "🧠 심리상담사, 📖 작가, 🎨 예술가",
        "match": "✅ ENFP와 ENTP",
        "desc": "직관적이고 이상주의적인 당신은 깊은 통찰력으로 세상을 이해하고, 타인을 돕는 것을 좋아해요!"
    },
    "INTJ": {
        "job": "💻 개발자, 🏗️ 엔지니어, 📈 전략가",
        "match": "✅ ENFP와 ENTJ",
        "desc": "분석적이고 독립적인 당신은 목표 지향적이에요. 지식과 논리로 무장한 전략가랍니다!"
    },
    # 다른 MBTI 유형도 여기에 추가해주세요!
}

# 스트림릿 인터페이스
st.title("🎉 나의 MBTI로 알아보는 직업과 궁합! 💼❤️")

# 드롭다운 메뉴
selected_mbti = st.selectbox("당신의 MBTI 유형을 선택하세요!", mbti_types)

# 선택한 MBTI에 따른 결과 보여주기
if selected_mbti:
    st.subheader(f"당신의 MBTI는 **{selected_mbti}** 🎯")
    st.write(f"**어울리는 직업:** {mbti_data[selected_mbti]['job']}")
    st.write(f"**잘 맞는 유형:** {mbti_data[selected_mbti]['match']}")
    st.write(f"📝 {mbti_data[selected_mbti]['desc']}")

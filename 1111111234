import streamlit as st

# 앱 제목
st.title("🧭 MBTI 진로 추천기")
st.write("안녕! 너의 MBTI를 선택하면 맞춤 진로와 관련 학과, 성격 팁을 알려줄게~")

# MBTI 옵션
mbti_options = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# MBTI 선택
selected_mbti = st.selectbox("너의 MBTI를 골라봐 👇", mbti_options)

# MBTI별 진로 추천 데이터
career_data = {
    "INTJ": [
        {"career": "데이터 분석가 📊", "major": "통계학, 컴퓨터공학", "personality": "분석적이고 계획적인 성격에게 딱!"},
        {"career": "전략 컨설턴트 💼", "major": "경영학, 경제학", "personality": "문제 해결과 전략 세우는 걸 좋아하는 사람에게 추천"}
    ],
    "INTP": [
        {"career": "연구 과학자 🔬", "major": "물리학, 화학, 수학", "personality": "호기심 많고 논리적인 성격에 잘 맞음"},
        {"career": "소프트웨어 개발자 💻", "major": "컴퓨터공학, 소프트웨어학", "personality": "창의적 문제 해결을 즐기는 사람에게 딱!"}
    ],
    "ENTJ": [
        {"career": "CEO/창업가 🚀", "major": "경영학, 경제학", "personality": "리더십 있고 추진력 있는 성격에게 추천"},
        {"career": "프로젝트 매니저 📌", "major": "경영학, 산업공학", "personality": "조직 관리와 목표 달성을 좋아하는 사람에게 추천"}
    ],
    "ENTP": [
        {"career": "마케팅 전략가 📣", "major": "경영학, 광고홍보학", "personality": "창의적 아이디어 뽑기 좋아하는 사람에게 추천"},
        {"career": "스타트업 창업가 🌟", "major": "경영학, 컴퓨터공학", "personality": "새로운 도전과 실험을 즐기는 사람에게 딱!"}
    ],
    "INFJ": [
        {"career": "상담사 🫂", "major": "심리학, 사회복지학", "personality": "남을 돕고 깊은 공감을 잘하는 사람에게 추천"},
        {"career": "작가 ✍️", "major": "문예창작, 언어학", "personality": "내면 세계가 풍부하고 표현을 좋아하는 사람에게 추천"}
    ],
    "INFP": [
        {"career": "게임 기획자 🎮", "major": "게임학, 디자인", "personality": "창의적이고 상상력이 풍부한 사람에게 추천"},
        {"career": "예술가 🎨", "major": "미술, 음악, 공연예술", "personality": "감수성이 풍부하고 자기표현을 즐기는 사람에게 추천"}
    ],
    "ENFJ": [
        {"career": "교사 👩‍🏫", "major": "교육학, 심리학", "personality": "사람과 소통하고 지도하는 걸 좋아하는 성격에게 추천"},
        {"career": "HR 전문가 🧑‍💼", "major": "경영학, 인사관리", "personality": "조직과 사람 관리에 관심 많은 사람에게 추천"}
    ],
    "ENFP": [
        {"career": "콘텐츠 크리에이터 🎬", "major": "미디어학, 디자인", "personality": "창의적이고 자유로운 사고를 즐기는 사람에게 추천"},
        {"career": "광고/마케팅 전문가 📢", "major": "경영학, 광고홍보학", "personality": "아이디어로 사람을 끌어들이는 걸 좋아하는 성격에게 추천"}
    ],
    "ISTJ": [
        {"career": "회계사 💰", "major": "회계학, 경영학", "personality": "꼼꼼하고 책임감 있는 성격에게 추천"},
        {"career": "공무원 🏛️", "major": "행정학, 법학", "personality": "규칙과 안정적인 환경을 선호하는 사람에게 추천"}
    ],
    "ISFJ": [
        {"career": "간호사 🏥", "major": "간호학, 보건학", "personality": "배려심 많고 성실한 성격에게 추천"},
        {"career": "사서 📚", "major": "문헌정보학, 도서관학", "personality": "정리정돈 잘하고 사람 돕는 걸 좋아하는 사람에게 추천"}
    ],
    "ESTJ": [
        {"career": "경영 관리자 🏢", "major": "경영학, 경제학", "personality": "리더십 있고 현실적인 성격에게 추천"},
        {"career": "군인/경찰 👮", "major": "군사학, 법학", "personality": "질서와 규율을 중시하는 사람에게 추천"}
    ],
    "ESFJ": [
        {"career": "이벤트 플래너 🎉", "major": "경영학, 호텔관광학", "personality": "사람과 어울리는 걸 즐기고 챙기는 성격에게 추천"},
        {"career": "간호사 🏥", "major": "간호학, 보건학", "personality": "배려심 많고 남을 돕는 걸 좋아하는 사람에게 추천"}
    ],
    "ISTP": [
        {"career": "엔지니어 🛠️", "major": "기계공학, 전자공학", "personality": "논리적 문제 해결과 손재주가 좋은 사람에게 추천"},
        {"career": "파일럿 ✈️", "major": "항공학, 기계공학", "personality": "모험심 있고 분석적 사고를 가진 사람에게 추천"}
    ],
    "ISFP": [
        {"career": "디자이너 🎨", "major": "시각디자인, 산업디자인", "personality": "감각적이고 창의적인 사람에게 추천"},
        {"career": "동물 관련 직업 🐾", "major": "수의학, 동물학", "personality": "자연과 동물 사랑하는 사람에게 추천"}
    ],
    "ESTP": [
        {"career": "스포츠 코치 🏀", "major": "체육학, 스포츠과학", "personality": "액티브하고 사람과 함께 활동하는 걸 좋아하는 사람에게 추천"},
        {"career": "영업 전문가 💼", "major": "경영학, 마케팅", "personality": "설득력 있고 도전적인 성격에게 추천"}
    ],
    "ESFP": [
        {"career": "연예인/퍼포머 🎤", "major": "공연예술, 미디어학", "personality": "사람들 앞에서 빛나고 싶은 성격에게 추천"},
        {"career": "여행 가이드 🌍", "major": "관광학, 외국어학", "personality": "사람과 어울리며 재미있는 경험을 좋아하는 사람에게 추천"}
    ]
}

# 진로 추천 보여주기
if selected_mbti:
    st.subheader(f"{selected_mbti} 유형에게 맞는 진로 추천 ✨")
    for item in career_data[selected_mbti]:
        st.markdown(f"**진로:** {item['career']}")
        st.markdown(f"**추천 학과:** {item['major']}")
        st.markdown(f"**어떤 성격에게 잘 맞을까:** {item['personality']}")
        st.write("---")

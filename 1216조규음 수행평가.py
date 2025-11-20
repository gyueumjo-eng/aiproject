import streamlit as st

# --- 1. MBTI별 데이터 정의 (데이터 구조 개선 및 영화/도서 포함) ---
# *실제 MBTI와 콘텐츠의 연관성은 재미를 위한 참고용입니다.*
career_data = {
    "INTJ": {
        "book": "사피엔스 (유발 하라리)",
        "movie": ["인터스텔라", "소셜 네트워크"],
        "careers": [
            {"career": "데이터 분석가 📊", "major": "통계학, 컴퓨터공학", "personality": "분석적이고 계획적인 성격에게 딱!"},
            {"career": "전략 컨설턴트 💼", "major": "경영학, 경제학", "personality": "문제 해결과 전략 세우는 걸 좋아하는 사람에게 추천"}
        ]
    },
    "INTP": {
        "book": "이기적 유전자 (리처드 도킨스)",
        "movie": ["매트릭스", "컨택트"],
        "careers": [
            {"career": "연구 과학자 🔬", "major": "물리학, 화학, 수학", "personality": "호기심 많고 논리적인 성격에 잘 맞음"},
            {"career": "소프트웨어 개발자 💻", "major": "컴퓨터공학, 소프트웨어학", "personality": "창의적 문제 해결을 즐기는 사람에게 딱!"}
        ]
    },
    "ENTJ": {
        "book": "손자병법",
        "movie": ["대부", "월스트리트"],
        "careers": [
            {"career": "CEO/창업가 🚀", "major": "경영학, 경제학", "personality": "리더십 있고 추진력 있는 성격에게 추천"},
            {"career": "프로젝트 매니저 📌", "major": "경영학, 산업공학", "personality": "조직 관리와 목표 달성을 좋아하는 사람에게 추천"}
        ]
    },
    "ENTP": {
        "book": "어떻게 원하는 것을 얻는가 (스튜어트 다이아몬드)",
        "movie": ["아이언맨", "캐치 미 이프 유 캔"],
        "careers": [
            {"career": "마케팅 전략가 📣", "major": "경영학, 광고홍보학", "personality": "창의적 아이디어 뽑기 좋아하는 사람에게 추천"},
            {"career": "스타트업 창업가 🌟", "major": "경영학, 컴퓨터공학", "personality": "새로운 도전과 실험을 즐기는 사람에게 딱!"}
        ]
    },
    "INFJ": {
        "book": "데미안 (헤르만 헤세)",
        "movie": ["쇼생크 탈출", "굿 윌 헌팅"],
        "careers": [
            {"career": "상담사 🫂", "major": "심리학, 사회복지학", "personality": "남을 돕고 깊은 공감을 잘하는 사람에게 추천"},
            {"career": "작가 ✍️", "major": "문예창작, 언어학", "personality": "내면 세계가 풍부하고 표현을 좋아하는 사람에게 추천"}
        ]
    },
    "INFP": {
        "book": "어린 왕자 (앙투안 드 생텍쥐페리)",
        "movie": ["이터널 선샤인", "아멜리에"],
        "careers": [
            {"career": "게임 기획자 🎮", "major": "게임학, 디자인", "personality": "창의적이고 상상력이 풍부한 사람에게 추천"},
            {"career": "예술가 🎨", "major": "미술, 음악, 공연예술", "personality": "감수성이 풍부하고 자기표현을 즐기는 사람에게 추천"}
        ]
    },
    "ENFJ": {
        "book": "사람은 무엇으로 사는가 (레프 톨스토이)",
        "movie": ["죽은 시인의 사회", "라라랜드"],
        "careers": [
            {"career": "교사 👩‍🏫", "major": "교육학, 심리학", "personality": "사람과 소통하고 지도하는 걸 좋아하는 성격에게 추천"},
            {"career": "HR 전문가 🧑‍💼", "major": "경영학, 인사관리", "personality": "조직과 사람 관리에 관심 많은 사람에게 추천"}
        ]
    },
    "ENFP": {
        "book": "여행의 이유 (김영하)",
        "movie": ["미드나잇 인 파리", "어바웃 타임"],
        "careers": [
            {"career": "콘텐츠 크리에이터 🎬", "major": "미디어학, 디자인", "personality": "창의적이고 자유로운 사고를 즐기는 사람에게 추천"},
            {"career": "광고/마케팅 전문가 📢", "major": "경영학, 광고홍보학", "personality": "아이디어로 사람을 끌어들이는 걸 좋아하는 성격에게 추천"}
        ]
    },
    "ISTJ": {
        "book": "아주 작은 습관의 힘 (제임스 클리어)",
        "movie": ["라이언 일병 구하기", "스포트라이트"],
        "careers": [
            {"career": "회계사 💰", "major": "회계학, 경영학", "personality": "꼼꼼하고 책임감 있는 성격에게 추천"},
            {"career": "공무원 🏛️", "major": "행정학, 법학", "personality": "규칙과 안정적인 환경을 선호하는 사람에게 추천"}
        ]
    },
    "ISFJ": {
        "book": "달려라, 토마토! (모리와키 아키라)",
        "movie": ["어거스트 러쉬", "플립"],
        "careers": [
            {"career": "간호사 🏥", "major": "간호학, 보건학", "personality": "배려심 많고 성실한 성격에게 추천"},
            {"career": "사서 📚", "major": "문헌정보학, 도서관학", "personality": "정리정돈 잘하고 사람 돕는 걸 좋아하는 사람에게 추천"}
        ]
    },
    "ESTJ": {
        "book": "성공하는 사람들의 7가지 습관 (스티븐 코비)",
        "movie": ["마션", "악마는 프라다를 입는다"],
        "careers": [
            {"career": "경영 관리자 🏢", "major": "경영학, 경제학", "personality": "리더십 있고 현실적인 성격에게 추천"},
            {"career": "군인/경찰 👮", "major": "군사학, 법학", "personality": "질서와 규율을 중시하는 사람에게 추천"}
        ]
    },
    "ESFJ": {
        "book": "관계를 맺는다는 것 (다니엘 골먼)",
        "movie": ["맘마미아", "노팅힐"],
        "careers": [
            {"career": "이벤트 플래너 🎉", "major": "경영학, 호텔관광학", "personality": "사람과 어울리는 걸 즐기고 챙기는 성격에게 추천"},
            {"career": "간호사 🏥", "major": "간호학, 보건학", "personality": "배려심 많고 남을 돕는 걸 좋아하는 사람에게 추천"}
        ]
    },
    "ISTP": {
        "book": "나는 생각이 너무 많아 (크리스텔 프티콜랭)",
        "movie": ["미션 임파서블", "본 시리즈"],
        "careers": [
            {"career": "엔지니어 🛠️", "major": "기계공학, 전자공학", "personality": "논리적 문제 해결과 손재주가 좋은 사람에게 추천"},
            {"career": "파일럿 ✈️", "major": "항공학, 기계공학", "personality": "모험심 있고 분석적 사고를 가진 사람에게 추천"}
        ]
    },
    "ISFP": {
        "book": "나는 나로 살기로 했다 (김수현)",
        "movie": ["센과 치히로의 행방불명", "라푼젤"],
        "careers": [
            {"career": "디자이너 🎨", "major": "시각디자인, 산업디자인", "personality": "감각적이고 창의적인 사람에게 추천"},
            {"career": "동물 관련 직업 🐾", "major": "수의학, 동물학", "personality": "자연과 동물 사랑하는 사람에게 추천"}
        ]
    },
    "ESTP": {
        "book": "넛지 (리처드 탈러)",
        "movie": ["울프 오브 월스트리트", "분노의 질주"],
        "careers": [
            {"career": "스포츠 코치 🏀", "major": "체육학, 스포츠과학", "personality": "액티브하고 사람과 함께 활동하는 걸 좋아하는 사람에게 추천"},
            {"career": "영업 전문가 💼", "major": "경영학, 마케팅", "personality": "설득력 있고 도전적인 성격에게 추천"}
        ]
    },
    "ESFP": {
        "book": "오늘도 펀하게 살기로 했다 (에린 무니)",
        "movie": ["킹스맨", "레미제라블"],
        "careers": [
            {"career": "연예인/퍼포머 🎤", "major": "공연예술, 미디어학", "personality": "사람들 앞에서 빛나고 싶은 성격에게 추천"},
            {"career": "여행 가이드 🌍", "major": "관광학, 외국어학", "personality": "사람과 어울리며 재미있는 경험을 좋아하는 사람에게 추천"}
        ]
    }
}

# --- 2. 앱 레이아웃 및 UI 구성 ---

# 앱 제목
st.title("🧭 MBTI 진로 & 문화 추천기")
st.write("안녕! 너의 MBTI를 선택하면 맞춤 진로, 학과, 성격 팁, **추천 도서와 영화**를 알려줄게~")

# MBTI 옵션
mbti_options = list(career_data.keys())

# MBTI 선택
# 첫 번째 값을 기본값으로 설정하여 초기 로딩 시 오류 방지
selected_mbti = st.selectbox("너의 MBTI를 골라봐 👇", mbti_options)

# --- 3. 진로 및 문화 추천 결과 보여주기 ---

if selected_mbti:
    # 선택된 MBTI 정보 가져오기
    mbti_info = career_data[selected_mbti]
    
    st.markdown("---")
    st.subheader(f"✨ **{selected_mbti}** 유형 분석 결과")
    
    # 📚 추천 문화 콘텐츠 섹션
    st.markdown("### 🍿 추천 문화 콘텐츠")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info(f"**추천 도서 📖:** **{mbti_info['book']}**")
    
    with col2:
        st.info(f"**추천 영화 🎬:** **{mbti_info['movie'][0]}** / **{mbti_info['movie'][1]}**")
    
    st.markdown("---")
    
    # 💼 추천 진로 섹션
    st.markdown("### 💼 추천 진로 및 학과")
    
    for i, item in enumerate(mbti_info['careers']):
        # st.expander를 사용하여 결과를 펼치거나 접을 수 있게 함
        with st.expander(f"**{i+1}. 추천 진로: {item['career']}**"):
            st.markdown(f"**추천 학과:** `{item['major']}`")
            st.markdown(f"**어떤 성격에게 잘 맞을까:** {item['personality']}")
            
    st.markdown("---")
    st.caption("ℹ️ 이 추천은 참고 자료일 뿐입니다. 당신의 가능성은 무궁무진하니 여러 분야를 탐색해보세요.")

import streamlit as st

st.title("📚🎬 MBTI 맞춤 미디어 추천기")
st.write("너의 MBTI를 골라줘! 그럼 너에게 딱 맞는 **책 2권**과 **영화 2편**을 추천해줄게~")

# MBTI 옵션
mbti_options = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

selected_mbti = st.selectbox("나의 MBTI는…👇", mbti_options)

# 추천 데이터 (책 2권 + 영화 2편) — 예시로 몇 개만 채워요. 필요하면 나머지 유형도 채워드릴게요.
recommendation_data = {
    "INTJ": {
        "books": [
            {"title": "Deep Work", "author": "Cal Newport", "note": "집중력과 몰입을 좋아하는 너에게 👍"},
            {"title": "Thinking in Systems", "author": "Donella Meadows", "note": "시스템적으로 생각하는 너에게 딱이에요"}
        ],
        "movies": [
            {"title": "Inception", "note": "복잡한 구조 + 반전 좋아한다면 이걸로 🎬"},  # :contentReference[oaicite:1]{index=1}
            {"title": "The Matrix", "note": "‘현실은 무엇인가?’ 이런 질문에 끌린다면 추천"}
        ]
    },
    "INFP": {
        "books": [
            {"title": "Shadow and Bone", "author": "Leigh Bardugo", "note": "상상력 풍부하고 판타지 좋아하는 너라면"},
            {"title": "Love From A to Z", "author": "S.K. Ali", "note": "감성적이고 따뜻한 이야기 찾는 너에게"}
        ],
        "movies": [
            {"title": "The Eternal Sunshine of the Spotless Mind", "note": "감정도 생각도 많다면 이 영화 추천 🧠❤️"},  # :contentReference[oaicite:2]{index=2}
            {"title": "Pan's Labyrinth", "note": "판타지 + 성장물 좋아하는 너라면 몰입될 거야"}
        ]
    },
    # … 나머지 유형도 비슷한 방식으로 추가 가능해요 …
}

if selected_mbti in recommendation_data:
    rec = recommendation_data[selected_mbti]
    st.subheader(f"{selected_mbti} 유형에게 어울리는 추천 리스트 ✨")
    st.write("**📖 책 추천 2권**")
    for b in rec["books"]:
        st.markdown(f"- **{b['title']}** by {b['author']} → {b['note']}")
    st.write("**🎥 영화 추천 2편**")
    for m in rec["movies"]:
        st.markdown(f"- **{m['title']}** → {m['note']}")
else:
    st.write("죄송해요~ 아직 이 MBTI 유형에 대한 추천이 준비 중이에요 😅")

st.write("좋아하는 책이나 영화가 생기면 꼭 메모해두고, 시간이 되면 한번씩 도전해봐! 😉")

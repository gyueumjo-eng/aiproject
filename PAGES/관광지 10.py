import streamlit as st
import folium
from streamlit_folium import st_folium

# 🌏 페이지 기본 설정
st.set_page_config(page_title="Korea Tourism Map", page_icon="🇰🇷", layout="wide")

st.title("🇰🇷 외국인이 좋아하는 한국 주요 관광지 TOP 10")
st.markdown("한국을 방문한 외국인들이 가장 많이 찾는 명소를 지도에 표시했습니다.")

# 📍 관광지 데이터
places = [
    {"name": "경복궁 (Gyeongbokgung Palace)", "lat": 37.579617, "lon": 126.977041, "desc": "조선 왕조의 중심 궁궐"},
    {"name": "명동 (Myeongdong)", "lat": 37.563757, "lon": 126.982684, "desc": "쇼핑과 먹거리의 천국"},
    {"name": "남산타워 (N Seoul Tower)", "lat": 37.551169, "lon": 126.988227, "desc": "서울 전경이 한눈에 보이는 전망대"},
    {"name": "북촌한옥마을 (Bukchon Hanok Village)", "lat": 37.582604, "lon": 126.983998, "desc": "전통과 현대가 어우러진 마을"},
    {"name": "동대문디자인플라자 (DDP)", "lat": 37.566478, "lon": 127.009220, "desc": "서울의 랜드마크 디자인 복합공간"},
    {"name": "제주 성산일출봉 (Seongsan Ilchulbong, Jeju)", "lat": 33.458390, "lon": 126.942640, "desc": "세계자연유산에 등재된 일출 명소"},
    {"name": "해운대 해수욕장 (Haeundae Beach, Busan)", "lat": 35.158698, "lon": 129.160384, "desc": "부산의 대표 해변"},
    {"name": "광안대교 (Gwangandaegyo Bridge, Busan)", "lat": 35.153261, "lon": 129.118611, "desc": "부산 야경 명소"},
    {"name": "안압지 (Donggung Palace and Wolji Pond, Gyeongju)", "lat": 35.834408, "lon": 129.226196, "desc": "신라 왕궁의 정원"},
    {"name": "전주한옥마을 (Jeonju Hanok Village)", "lat": 35.815009, "lon": 127.153977, "desc": "전통 한옥과 음식문화의 중심"}
]

# 🌐 지도 생성
m = folium.Map(location=[36.5, 127.9], zoom_start=7)

# 🗺️ 마커 추가
for p in places:
    folium.Marker(
        location=[p["lat"], p["lon"]],
        popup=f"<b>{p['name']}</b><br>{p['desc']}",
        tooltip=p["name"],
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

# 🧭 지도 표시
st_folium(m, width=900, height=600)

# pages/daily_station_rank.py

import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 현재 파일(pages/daily_station_rank.py)의 디렉토리 경로
# 이 경로를 기준으로 상위 폴더로 이동하여 CSV 파일을 찾습니다.
# os.path.dirname(__file__) == 'pages' 폴더 경로
# os.path.dirname(os.path.dirname(__file__)) == 상위 폴더 경로
CSV_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'fgyhgghghgh.txt')

# --- 데이터 로드 및 전처리 함수 ---
@st.cache_data
def load_data(path):
    """
    CSV 파일을 로드하고 필요한 전처리 (날짜 변환, 총 승객수 계산)를 수행합니다.
    """
    try:
        # 탭('\t') 구분자로 인코딩하여 파일 로드
        df = pd.read_csv(path, sep='\t', encoding='utf-8')
        
        # '사용일자' 컬럼을 datetime 형식으로 변환
        df['사용일자'] = pd.to_datetime(df['사용일자'], format='%Y%m%d')
        
        # 총 승객수 (승차 + 하차) 계산
        df['총승객수'] = df['승차총승객수'] + df['하차총승객수']
        
        return df
    except FileNotFoundError:
        st.error(f"⚠️ **파일 오류:** {path} 경로에서 파일을 찾을 수 없습니다. 경로를 확인해주세요.")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"⚠️ **데이터 로드 중 오류 발생:** {e}")
        return pd.DataFrame()

# --- Streamlit 앱 본문 ---
def app():
    st.set_page_config(
        page_title="일별 지하철 승객 순위 분석",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.title("🚇 일별 노선별 지하철 역 순위 분석 (2025년 9월)")
    st.markdown("---")

    df = load_data(CSV_PATH)
    
    if df.empty:
        st.stop()
        
    # --- 사이드바 필터 ---
    with st.sidebar:
        st.header("필터 설정")
        
        # 1. 날짜 선택 (데이터에 있는 날짜만 선택 가능하도록 제한)
        min_date = df['사용일자'].min().date()
        max_date = df['사용일자'].max().date()
        
        selected_date = st.date_input(
            "🗓️ 분석할 날짜 선택",
            value=min_date,
            min_value=min_date,
            max_value=max_date,
            format="YYYY/MM/DD"
        )
        
        # 2. 노선 선택
        unique_lines = sorted(df['노선명'].unique())
        selected_line = st.selectbox(
            "🚈 분석할 노선 선택",
            options=["전체 노선"] + unique_lines
        )
        
    # --- 데이터 필터링 ---
    # 1. 날짜로 필터링
    filtered_df = df[df['사용일자'].dt.date == selected_date]

    # 2. 노선으로 필터링
    if selected_line != "전체 노선":
        filtered_df = filtered_df[filtered_df['노선명'] == selected_line]

    if filtered_df.empty:
        st.warning(f"선택하신 날짜({selected_date})와 노선({selected_line})에 해당하는 데이터가 없습니다.")
        return
    
    # 역별 총 승객수 집계
    station_ranking = filtered_df.groupby('역명')['총승객수'].sum().reset_index()
    station_ranking = station_ranking.sort_values(by='총승객수', ascending=False)
    
    # --- 그래프 색상 설정 ---
    if not station_ranking.empty:
        # 1등 역은 빨간색
        top_station = station_ranking.iloc[0]['역명']
        
        # 나머지 역은 파란색 계열의 그라데이션
        # Plotly는 'color_discrete_sequence'에 지정된 색상을 순서대로 사용합니다.
        
        # 파란색 계열 색상표 생성 (순위가 내려갈수록 흐려지도록)
        num_stations = len(station_ranking)
        # Plotly의 'Blues' 스케일 중 가장 진한 색부터 순서대로 사용
        blue_palette = px.colors.sequential.Blues[3:] # 너무 밝은 색 피하기 위해 [3:] 사용

        # 색상 리스트: 1위는 'red', 나머지는 파란색 그라데이션
        colors = ['red'] + blue_palette[:num_stations - 1] 
        
        # 색상 데이터를 데이터프레임에 매핑
        station_ranking['color'] = ['red'] + colors[1:]

    # --- Plotly 막대 그래프 생성 ---
    fig = px.bar(
        station_ranking, 
        x='역명', 
        y='총승객수',
        title=f"**{selected_date.strftime('%Y년 %m월 %d일')}** | **{selected_line}** 노선 역별 총 승객수 순위",
        labels={'총승객수': '총 승객수 (승차+하차)', '역명': '역 이름'},
        hover_data={'총승객수': ':,', '역명': True}, # 툴팁에 쉼표 표시
        color='color', # 개별 색상 컬럼 지정
        color_discrete_map={c: c for c in station_ranking['color'].unique()} # 색상 맵핑 유지
    )
    
    # 레이아웃 커스터마이징
    fig.update_layout(
        xaxis={'categoryorder':'array', 'categoryarray':station_ranking['역명']}, # 순위 순서 유지
        title_x=0.5,
        height=600,
        yaxis_tickformat=',', # y축 값에 쉼표 적용
    )
    
    # 툴팁에 총 승객수 값 표시
    fig.update_traces(texttemplate='%{y:s}', textposition='outside')
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    st.subheader("📊 데이터 테이블 미리보기 (Top 10)")
    st.dataframe(
        station_ranking.head(10).style.format({'총승객수': "{:,.0f}"}),
        use_container_width=True
    )


if __name__ == '__main__':
    app()

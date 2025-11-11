# streamlit_mbti_app.py
# Streamlit 앱 — countriesMBTI_16types.csv 파일을 읽어 대화형 Plotly 막대그래프를 보여줍니다.
# - Streamlit Cloud에서 작동하도록 작성됨
# - 국가 선택 시 해당 국가의 MBTI 비율을 막대 그래프로 표시
# - 1등은 빨간색, 나머지는 파란색 그라데이션
# - 화면에 코드가 복사 가능하도록 st.code로 표시

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os
from textwrap import dedent

st.set_page_config(page_title='Countries MBTI Explorer', layout='wide')

st.title('🌍 Countries MBTI — Interactive Explorer')

# 파일 로드: repo에 countriesMBTI_16types.csv가 있으면 우선 사용, 없으면 업로드하도록 안내
DEFAULT_PATH = 'countriesMBTI_16types.csv'

uploaded_file = None
if os.path.exists(DEFAULT_PATH):
    df = pd.read_csv(DEFAULT_PATH)
else:
    st.info('CSV 파일이 앱 디렉터리에 없어요. 로컬 파일을 업로드하거나 Streamlit Cloud에서는 리포지토리 루트에 파일을 넣어주세요.')
    uploaded_file = st.file_uploader('countriesMBTI_16types.csv 파일 업로드', type=['csv'])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
    else:
        st.stop()

# 데이터 확인 — 간단한 표와 컬럼 설명
st.sidebar.header('데이터 정보')
st.sidebar.write(f'Rows: {len(df):,} — Columns: {len(df.columns)}')
st.sidebar.write('컬럼:')
st.sidebar.write(list(df.columns))

# 사용자가 기대하는 형식 예제:
# 한 행: Country, ISTJ, ISFJ, INFJ, ... (16 MBTI columns) — 각 값은 비율 또는 카운트
# 데이터가 세로형(long)인 경우 자동 변환 시도
MBTI_TYPES = [
    'ISTJ','ISFJ','INFJ','INTJ','ISTP','ISFP','INFP','INTP',
    'ESTP','ESFP','ENFP','ENTP','ESTJ','ESFJ','ENFJ','ENTJ'
]

# 자동 감지: MBTI 컬럼이 이미 wide 형태인지, 아니면 long인지
mbti_cols = [c for c in df.columns if c.upper() in MBTI_TYPES or c in MBTI_TYPES]

if len(mbti_cols) >= 2:
    # wide format
    wide_df = df.copy()
else:
    # 시도: long 형식으로 "Country", "MBTI", "Value" 같은 컬럼이 있는지 확인
    long_candidates = [c.lower() for c in df.columns]
    if 'mbti' in long_candidates and ('value' in long_candidates or 'count' in long_candidates or 'ratio' in long_candidates):
        mbti_col = df.columns[long_candidates.index('mbti')]
        value_col = None
        for name in ('value','count','ratio'):
            if name in long_candidates:
                value_col = df.columns[long_candidates.index(name)]
                break
        wide_df = df.pivot_table(index='Country', columns=mbti_col, values=value_col, aggfunc='first').reset_index()
        mbti_cols = [c for c in wide_df.columns if c != 'Country']
    else:
        st.error('CSV를 해석할 수 없습니다. 파일에 Country(또는 country) 열과 16개 MBTI 열(또는 long 형식의 MBTI/Value 쌍)이 있는지 확인하세요.')
        st.stop()

# 표준화: 컬럼 이름 정리
wide_df.columns = [str(c).strip() for c in wide_df.columns]
if 'Country' not in wide_df.columns and 'country' in [c.lower() for c in wide_df.columns]:
    # 소문자 country -> Country로 바꿈
    for c in wide_df.columns:
        if c.lower() == 'country':
            wide_df = wide_df.rename(columns={c:'Country'})
            break

# 재계산: 비율이 아니라 카운트일 경우, 국가별 합계로 나눠 비율 변환
mbti_cols = [c for c in wide_df.columns if c != 'Country']

# 숫자형 변환
for c in mbti_cols:
    wide_df[c] = pd.to_numeric(wide_df[c], errors='coerce')

# 결측값은 0 처리
wide_df[mbti_cols] = wide_df[mbti_cols].fillna(0)

# 만약 합이 1(또는 100)보다 크면 비율로 바꾸지 않음. 대신 합이 1보다 크고 평균이 큰 경우 백분율로 바꿔 표준화
sums = wide_df[mbti_cols].sum(axis=1)
if (sums > 1).any():
    # 정규화하여 비율(합=1)로 변경
    wide_df[mbti_cols] = wide_df[mbti_cols].div(sums, axis=0).fillna(0)

# 사용자 인터페이스: 국가 선택
countries = sorted(wide_df['Country'].astype(str).unique())
selected_country = st.selectbox('국가 선택', countries)

# 선택된 국가의 MBTI 비율 가져오기
row = wide_df[wide_df['Country'].astype(str) == selected_country]
if row.e

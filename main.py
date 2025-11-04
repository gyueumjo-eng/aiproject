import streamlit as st
st.title('나의 첫 웹페이지')
name=st.text_input('이름을 입력하시오!')
if st.button('인삿말 생성'):
  st.writte(name+'님! 안녕하세요!')

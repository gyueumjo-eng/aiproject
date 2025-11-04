import streamlit as st
st.title('나의 첫 웹페이지')
name=st.text_input('이름을 입력하시어유!')
m=st.selectbox('좋아하는 음식을 선택해주시어유~',['치킨','떡볶이','바나나'])
if st.button('인삿말 생성'):
  st.info(name+'님! 안녕하시어유!')
st.wsarning(m+'을(를)좋아하시나봐유?, 저도좋아혀유~')
st.error(반가워유~')
st.balloons()

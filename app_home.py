import pandas as pd
import streamlit as st
from PIL import Image

def run_home() :
    logo = Image.open('data/logo.jpg')
    st.image(logo)
    
    st.title('이혼 가능성 예측하기 프로젝트')
    st.subheader('왼쪽 메뉴의 EDA')
    st.text('테스트를 위해 사용한 데이터에 관한 분석을 볼 수 있습니다.')
    st.subheader('왼쪽 메뉴의 Divorce Test')
    st.text('54 문항에 대한 설문을 통해 이혼에 대한 가능성을 평가합니다.')
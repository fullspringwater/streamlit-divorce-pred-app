import pandas as pd
import streamlit as st
import joblib
import numpy as np
def run_divorce_test() :
    df1 = pd.read_csv('data/divorce_data.csv')
    df2 = pd.read_csv('data/question.csv')

    scaler = joblib.load('data/scaler.pkl')
    classifier = joblib.load('data/classifier.pkl')
    
    st.title('이혼 가능성 테스트')
    st.subheader('각 테스트 문항은 0 - 4 점으로 이루어져 있습니다')
    st.subheader('0 = 전혀 그렇지 않다, 1 = 약간 그렇지 않다, 2 = 보통이다')
    st.subheader('3 = 약간 그렇다, 4 = 항상 그렇다.')

    # 54개의 라디오를 만들고 버튼을 누를시 결과를 보여준다.
    check_list = np.arange(54)

    for i in range(54) :
        q = df2.iloc[i,0] +' : ' +  df2.iloc[i, 1]
        check_list[i] = st.radio(q, [0,1,2,3,4])
    
    if st.button('result') :
        # st.text(check_list)
        new_data = check_list.reshape(1, 54)
        new_data = scaler.transform(new_data)
        new_pred = classifier.predict(new_data)
        if new_pred[0] == 0 :
            st.subheader('당신은 이혼할 확률이 낮습니다.')
        else :
            st.subheader('당신은 이혼할 확률이 높습니다.')
        
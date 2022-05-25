import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda() :
    df = pd.read_csv('data/divorce_data.csv', sep=';')
    st.subheader('이혼 가능성 데이터 분석')
    st.subheader('각 문항에 대한 답은 0 - 5 점으로 기록')
    st.dataframe(df)

    q = pd.read_csv('data/question.csv')
    
    st.subheader('이혼 데이터와 이혼하지 않은 데이터의 개수와 비율')
    fig1 = plt.figure(figsize=(6,6))

    # 이혼 데이터와 이혼하지 않은 데이터의 개수 비교
    plt.subplot(1,3,1)    
    sns.countplot(data = df, x = 'Divorce')   



    # 이혼 데이터와 이혼하지 않은 데이터의 비율
    divorce_rate = df['Divorce'].value_counts()
    divorce_rate.rename( index = {0 : 'Not Divorce',
                              1 : 'Divorce'} , inplace = True)
    plt.subplot(1,3,3)
    plt.pie(divorce_rate, autopct = '%.1f', labels = divorce_rate.index,
       startangle = 90, wedgeprops= {'width' : 0.7})
    st.pyplot(fig1)

    # question의 분항들을 받아온다
    col_list= []
    for i in range(1,54+1) :
        col_list.append('Q' + str(i))
    
    # 선택한 문항의 내용을 보여준다.
    col_choice = st.multiselect('문항의 내용 보기', col_list)
    if len(col_choice) != 0 :
        for i in range(len(col_choice)) :
            q_context = q.loc[q['Question'] == col_choice[i], 'context'].values[0]
            st.subheader(col_choice[i] + ' : '+ q_context)

    # 두개 문항을 선택시 regplot과 상관관계 보여준다.
    choice_corr_list = st.multiselect('두개 문항의 상관관계 보기', col_list)
    if st.button('결과보기') :
        if len(choice_corr_list) == 2:
            fig2 = plt.figure()
            sns.regplot(data = df, x = choice_corr_list[0], 
                        y = choice_corr_list[1])
            st.pyplot(fig2)
            st.text('상관계수')
            st.dataframe(df[choice_corr_list].corr())
        else :
            st.warning('두개를 선택하지 않았습니다! ')
    
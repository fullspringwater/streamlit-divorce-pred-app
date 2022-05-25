import streamlit as st
from app_divorce_test import run_divorce_test
from app_eda import run_eda
from app_home import run_home

def main() : 
    menu = ['Home', 'EDA', 'Divorce Test']
    menu_choice = st.sidebar.selectbox('메뉴', menu)

    if menu_choice == menu[0] :
        run_home()
    if menu_choice == menu[1] :
        run_eda()
    elif menu_choice == menu[2] :
        run_divorce_test()

if __name__=='__main__':
    main()
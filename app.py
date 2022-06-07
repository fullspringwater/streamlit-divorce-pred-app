import streamlit as st
from app_divorce_test import run_divorce_test
from app_eda import run_eda
from app_home import run_home
from streamlit_option_menu import option_menu


def main() : 
    menu = ['Home', 'EDA', 'Divorce Test']


    with st.sidebar:
        menu_choice = option_menu("Menu", menu,
                            icons=['house', 'graph-up', 'book'],
                            menu_icon="app-indicator", default_index=0,
                            styles={
            "container": {"padding": "5!important", "background-color": "#44475A5"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#BD93F9"},
            "nav-link-selected": {"background-color": "#02ab21"},
        }
        )
    
    if menu_choice == menu[0] :
        run_home()
    if menu_choice == menu[1] :
        run_eda()
    elif menu_choice == menu[2] :
        run_divorce_test()

if __name__=='__main__':
    main()
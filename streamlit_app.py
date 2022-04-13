
import streamlit

streamlit.title('My Parent New Health Diner')


streamlit.header('BreakFast')

streamlit.text('Idly')
streamlit.text('Dosa')
streamlit.text('Pongal')
streamlit.header('Create your own smooothie')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")



# creating a multiselect to allow user to select their fruit as they wish
streamlit.multiselect("Pick Some Fruits",list(my_fruit_list.fruit))

streamlit.dataframe(my_fruit_list)

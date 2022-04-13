
import streamlit

streamlit.title('My Parent New Health Diner')


streamlit.header('BreakFast')

streamlit.text('Idly')
streamlit.text('Dosa')
streamlit.text('Pongal')
streamlit.header('Special mini Tiffin as per your request')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

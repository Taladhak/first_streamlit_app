import streamlit
streamlit.title(' My parentsNew Healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('🐟Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🥚Hard-Boiled Egg')
streamlit.text('🥑🥪 Avocado Toast')



streamlit.header('🍌🥭Build Your Own Fruit Smoothie🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt"0)
streamlit.dataframe(my_fruit_list)

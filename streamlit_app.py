import streamlit

streamlit.title('My Moms new healthy diner')

streamlit.header('breakfast menu')
streamlit.text('🥣 Omega 3 and Bluebery oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')   #streamlit.dataframe(my_fruit_list)


#lets put here pick list
fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruites_to_show = my_fruit_list.loc[fruits_selected]

#display the table on page
streamlit.dataframe(fruites_to_show)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.header('Fruityvice Fruit Advice!')
streamlit.text(fruityvice_response.json())   # writes the data on to the screen

#take the above json format data and normalize it and display
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)



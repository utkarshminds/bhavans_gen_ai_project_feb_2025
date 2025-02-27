#shopping cart

#user will buy bread, butter, jam
#price of each is Rs. 10
#quantity user will decide
#give final bill to user
import streamlit as st
bread_quantity= st.number_input("Pick a number", 0, 10, key='id1')
jam_quantity= st.number_input("Pick a number", 0, 10, key='id2')
butter_quantity= st.number_input("Pick a number", 0, 10, key='id3')

final_bill = (10 * jam_quantity) + (10 * butter_quantity) + (10 * bread_quantity)

st.write('Your bill', final_bill)
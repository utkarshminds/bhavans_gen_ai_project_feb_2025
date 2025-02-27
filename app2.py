import streamlit as st


st.title("My second website")

#rock paper scissor game

'''
user select rock, or paper or scissor in text box
computer select rock or paper or scissor
if user-rock and computer-paper then computer wins
else if user-rock and computer-scissor then user wins
else if user-scissor and computer-paper then user wins
''' 
import random
computer = random.choice(['rock','paper','scissor'])
user = st.selectbox(
    "Which to select?",
    ("rock", "paper", "scissor"),
)
st.write("You selected:", user)
st.write('Computer has selected = ',computer)

if user == 'rock' and computer == 'rock':
    st.write('tie')
elif user == 'paper' and computer == 'paper':
    st.write('tie')
elif user == 'scissor' and computer == 'scissor':
    st.write('tie')
elif user == 'rock' and computer == 'scissor':
    st.write('user is winner')
elif user == 'rock' and computer == 'paper':
    st.write('computer is winner')
elif user == 'scissor' and computer == 'rock':
    st.write('computer is winner')
elif user == 'scissor' and computer == 'paper':
    st.write('computer is winner')
elif user == 'paper' and computer == 'rock':
    st.write('user is winner')
elif user == 'paper' and computer == 'scissor':
    st.write('computer is winner')
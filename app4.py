'''
1- create a file named app4.py
2. activate environment by typing in terminal
   myenv/scripts/activate and press ENTER
3. Create a vacation planner app to allow 
   user to enter vacation destination, days, budget,
   requirements and people
4. Then with generative AI create and display the
   vacation plan

5. Create text boxes for destination, budget, 
   number of people, specific requirements,
   and submit button
'''

import streamlit as st
import google.generativeai as genai #LIBRARY OF GEN AI
genai.configure(api_key="AIzaSyBBZTmDHnqAP6p2gKqTmSfv6bbNf2gYhXM") #API KEY

dest_data = st.text_input("Enter destination")
req_data = st.text_input("Enter special requirements")
budget_data = st.text_input("Budget")
people_data = st.text_input("People travelling")
days_data = st.text_input("Days")

#true or false
click = st.button("Generate Vacation Plan")

if click:
  
    model = genai.GenerativeModel("gemini-1.5-flash")  

    response = model.generate_content(f"""Create vacation plan for {dest_data} where 
                                      number of days is {days_data} and number of people 
                                      {people_data} with total budget below {budget_data} 
                                      and also special requirments {req_data} should be 
                                      satisfied.""")  
    st.write(response.text)  
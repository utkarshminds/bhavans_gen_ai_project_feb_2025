#Create virtual environment for project
# 1 type in terminal -> python -m venv myenv (press ENTER)

# 2 THEN TYPE IN TERMINAL --> 
Set-ExecutionPolicy Bypass -Scope Process -Force  (press ENTER)

# 3 activate the VENV type in terminal -> 
                myenv/scripts/activate (press ENTER)

# 4 type in terminal ->
python.exe -m pip install --upgrade pip (press ENTER)
#type in terminal -> pip install streamlit (press ENTER)
#type in terminal -> pip install pandas (press ENTER)
#type in terminal -> pip install pipreqs (press ENTER)
#type in terminal -> pip install seaborn (press ENTER)
#type in terminal -> pip install matplotlib (press ENTER)

#type in terminal-> pip install google-generativeai (press ENTER)

# Create a folder named .streamlit and inside folder create a file named secrets.toml

# In secrets.toml write the lines
[GOOGLE_API_KEY]
GOOGLE_API_KEY = 'PASTE YOUR KEY HERE'



#create a new file named app.py

import streamlit as st
st.title('My first website')

#type in terminal -> streamlit run app.py (press ENTER)

#to close streamlit press ctrl+C

#close venv by type in terminal -> deactivate

# type in terminal -> 

# pipreqs --force --ignore myenv/ 

#
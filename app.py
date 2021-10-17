#!/usr/bin/env python3

'''
This script displays information about the applicants and let's the
user score an applicant.
'''

import streamlit as st
st.set_page_config(page_title="Simple Auth", layout="wide")

import streamlit_debug
streamlit_debug.set(flag=False, wait_for_client=True, host='localhost', port=8765)

import env
env.verify()

from authlib.auth import auth, authenticated, requires_auth
from authlib.common import trace_activity
from sqlalchemy import select
import sys

user = auth(sidebar=True, show_msgs=True)

st.title('Test App')
if authenticated():
    st.success(f'`{user}` is authenticated')
else:
    st.warning(f'Not authenticated')
    # Stop running.
    st.stop()
    sys.exit()



# Let the user input the ID of the applicant that is supposed to be displayed.
st.sidebar.title('User Selection')
applicant_id = st.sidebar.text_input('Applicant ID', value='4')
value = st.sidebar.slider('Slider', -1, 10, -1)

# Show the user id.
st.title(f'User #{applicant_id}')






st.markdown("""
<embed src="https://drive.google.com/viewerng/
viewer?embedded=true&url=https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf" width="1000" height="1000">
""", unsafe_allow_html=True)


st.markdown("""
<embed src="https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf" width="1000" height="400">
""", unsafe_allow_html=True)







db_url = st.secrets['db_url']

# Connect
import sqlalchemy
engine = sqlalchemy.create_engine(db_url)
engine.connect()

from sqlalchemy import MetaData
meta = MetaData()
meta.reflect(bind=engine)

# Show all available fields in the table.
from sqlalchemy import inspect
inspector = inspect(engine)

columns = inspector.get_columns('api_appform')

# The above items as a list.
columns = ['firstname',
           'lastname',
           'email',
           'phone',
           'languages',
           'age',
           'nationality',
           'gender',
           'resume',
           'university',
           'degree',
           'major',
           'semester',
           'hours',
           'city',
           'q1',
           'q2',
           'q3',
           'q4',
           'q5',
           'q6',
           'q7',
           'q8']

# Show the value for all columns.
for item in columns:
    table = meta.tables['api_appform']
    query = select([table.c.id, table.c[item]]).where(table.c.id == int(applicant_id))
    with engine.connect() as conn:
        result = conn.execute(query).fetchone()
    item_name_capitalized = item.capitalize()
    value = result[1] if result else None
    st.write(f'{item_name_capitalized}: {value}')




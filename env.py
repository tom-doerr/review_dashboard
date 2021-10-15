import os
from os import environ as osenv
from dotenv import load_dotenv, find_dotenv
import logging
import streamlit as st

# ======== GLOBAL SETTINGS ========

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
osenv['BASE_DIR'] = BASE_DIR

# ======== LOAD SECRET ENVIRONMENT VARS (from .env) ========

if False:
    ENV_FILE = find_dotenv()
    if ENV_FILE:
        load_dotenv(ENV_FILE)
else:
    # Read the streamlit secrets and set them as environment variables.

    #STORAGE
    #SQLITE_DB_PATH 
    #SQLITE_DB 
    #AIRTABLE_API_KEY
    #AIRTABLE_PROFILE_BASE_ID 
    #USERS_TABLE 
    #ENC_PASSWORD
    #ENC_NONCE

    os.environ['STORAGE'] = st.secrets['STORAGE']
    os.environ['SQLITE_DB_PATH'] = st.secrets['SQLITE_DB_PATH']
    os.environ['SQLITE_DB'] = st.secrets['SQLITE_DB']
    os.environ['AIRTABLE_API_KEY'] = st.secrets['AIRTABLE_API_KEY']
    os.environ['AIRTABLE_PROFILE_BASE_ID'] = st.secrets['AIRTABLE_PROFILE_BASE_ID']
    os.environ['USERS_TABLE'] = st.secrets['USERS_TABLE']
    os.environ['ENC_PASSWORD'] = st.secrets['ENC_PASSWORD']
    os.environ['ENC_NONCE'] = st.secrets['ENC_NONCE']

def verify():
    logging.info(f'>>> Environment loading status <<<')
    logging.info(f'--  Application base directory: {BASE_DIR}')
    # logging.info(f'--  Dotenv file: {ENV_FILE}\n\n')


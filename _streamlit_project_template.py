# ARTICLE_RIGHTS: CR 2022, 2023.  William W Collins, All Rights Reserved
import os
import time
import streamlit as st
import requests
import json
from dotenv import load_dotenv

PAGE_TITLE = "Template"
EXPANDER_DEFAULT = False
DEFAULT_ENGINEERING_PROMPT = f'This is a parameter to support LLM applications'
PROJECT_NAME = "[PROJECT NAME]"
ARTICLE_AUTHOR = "William W. Collins"
ARTICLE_RIGHTS = "CR William W Collins, All Rights Reserved"
PROMPT_ARTICLE_REQUEST = f"Write an informational, detailed, professional news article by {ARTICLE_AUTHOR} " \
                         f"using the following multi-article content. Create title and markdown the title in bold blue, headers, sub-headers in " \
                         f"the article.  Also Create and introduction and a summary and use examples:"
NOTICE_APP_INFO = ":blue[Free Limited Research Preview]. This app may produce inaccurate information " \
                  "about people, places, or facts"
DEFAULT_USER_NAME = 'Guest'
CURRENT_COVERLETTER = 'Coverletter'
TEST_JOB_DESCRIPTION = 'Test JD'

# Set page config
st.set_page_config(
    page_title=f'Streamlit App: {PAGE_TITLE}',
    page_icon="🌊",
    layout="centered"
)

with st.spinner(f'loading...'):
    st.caption(f'')
    time.sleep(1)

# Information for this file
import os
# st.write(os.path.abspath(__file__))
# st.write(os.path.basename(__file__))

THIS_FILE = os.path.basename(__file__)
THIS_FILE_PATH = os.path.abspath(__file__)

# Set Styles refs: https://medium.com/@avra42/streamlit-python-cool-tricks-to-make-your-web-application-look-better-8abfc3763a5b
st.set_option('deprecation.showPyplotGlobalUse', False)  # disable error gen
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# Set Styles refs: https://medium.com/@avra42/streamlit-python-cool-tricks-to-make-your-web-application-look-better-8abfc3763a5b
st.set_option('deprecation.showPyplotGlobalUse', False)  # disable error gen
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """

# todo - consider Redis integration: https://towardsai.net/p/machine-learning/a-step-by-step-guide-to-developing-a-streamlit-application-with-redis-data-storage-and-deploying-it-using-docker

# Load the dotenv file:  Convert to more secure method todo
load_dotenv()
# e.g. OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

import random
import string

def generate_random_string(length):  # use for unique key id for widgets
    characters = string.ascii_letters + string.punctuation
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

import os

def write2file(text, filename):  # writes to file locally here but only memory based in cloud, use S3 etc
    if os.path.exists(filename):
        with open(filename, "w") as file:  #overwrite, not apppend.  "a" for append
            file.write(text + "\n")
    else:
        with open(filename, "w") as file:
            file.write(text + "\n")

def show_progress_bar(sleep_time=0.1):
    progress_text = "Operation in progress. Please wait..."

    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(sleep_time)
        my_bar.progress(percent_complete + 1, text=f'Progress{percent_complete}%')

def read_python_file(filename=THIS_FILE):
    # Allow the user to input the filename
    # filename = st.text_input("Enter a Python filename")

    if filename:
        with st.expander("[code]", expanded=EXPANDER_DEFAULT):  # Read the file contents and display the code
            st.title(f'View Python Code: {filename}')
            st.caption(f'lines of code: {count_lines(filename)}')
            with open(filename, "r", encoding="utf8") as f:
                code = f.read()
            try:
                st.code(code, language="python")
            except FileNotFoundError:
                st.error("File not found. Please enter a valid filename.")

# file = open(filename, encoding="utf8")
def count_lines(file_name):
    with open(file_name, 'r', encoding="utf8") as f:
        # st.caption(f'Lines of code = {len(f.readlines())}')
        return len(f.readlines())

# Create the form using Streamlit
def main():
    col1, col2 = st.columns(2)
    with col1:
        st.sidebar.image(f'./images/you_image.jpg', 'William Collins', width=150)
    with col2:
        st.sidebar.caption(f'Location: Austin, TX' + '\n' +
                           f'\n [Email]("mailto:williamwcollinsjr@gmail.com)'
                           f'\n Phone: 940.503.8195'
                           f'\n [Tech Profile including Projects/Demos](https://wwcollins-profile.streamlit.app)'
                           f'\n [LinkedIn](https://linkedin.com/in/williamwcollins)'
                           f'\n [Discord server](https://discord.com/channels/1108234455010787330/1108234455614754870)'
                           )

    col3, col4 = st.columns(2)
    with col3:
        st.image(f'./images/tech_image_7.jpg', '', width=350)
    with col4:
        with st.spinner(f'loading main...'):
            time.sleep(1)
            st.header(f':blue[{PROJECT_NAME}]')
            st.caption(f'William Collins 2023, All Rights Reserved {NOTICE_APP_INFO}')

    with st.expander(f'What this app does...'):  # change this for each file - autogen from chatgpt
        """
        REPLACE THIS CONTENT WITH NEW CONTENT SPECIFIC TO THE CODE YOU DEVELOP
        
        This Streamlit Python code creates a web application for generating a cover letter. It uses the Streamlit library for building the user interface and interacts with the OpenAI API for generating the updated cover letter.

        Here's a breakdown of the code:
        
        1. The code imports necessary modules, including `os`, `time`, `streamlit`, `requests`, `json`, and `dotenv`.
        2. Several constants are defined, such as the API endpoint for the OpenAI API, default prompts and user information, and sample cover letter and job description texts.
        3. The code loads environment variables from a `.env` file using the `load_dotenv()` function.
        4. Some Streamlit configurations are set to hide the menu and footer.
        5. Utility functions are defined for generating a random string and writing text to a file.
        6. The `generate_cover_letter` function sends a request to the ChatGPT API to generate an updated cover letter based on a given prompt and the current cover letter. The response is parsed, and the updated cover letter is extracted.
        7. The `generate_chat_completion` function sends a request to the OpenAI API to generate a chat completion based on the provided messages, model, temperature, and max tokens. The response is parsed, and the generated message content is returned.
        8. The `main` function creates the user interface using Streamlit. It includes input fields for name, engineering prompt, current cover letter, and job description. When the "Generate Cover Letter" button is clicked, the `generate_chat_completion` function is called to generate the updated cover letter. The original and revised cover letters are displayed in separate columns, and the updated cover letter is also written to a file.
        9. The `show_progress_bar` function displays a progress bar during long-running operations.
        10. Finally, the `main` function is called to run the application.
        
        Overall, this code sets up a web application that allows users to generate an updated cover letter by interacting with the OpenAI API.
        """

    st.caption(read_python_file(THIS_FILE))  # built in expander in def

    # Create session state variables and assign defaults
    if "name" not in st.session_state:
        st.session_state.name = DEFAULT_USER_NAME
    if "prompt" not in st.session_state:
        st.session_state.prompt = DEFAULT_ENGINEERING_PROMPT
    if "cover_letter" not in st.session_state:
        st.session_state.cover_letter = CURRENT_COVERLETTER
    if "job_description" not in st.session_state:
        st.session_state.job_description = TEST_JOB_DESCRIPTION
    if "open_api_key" not in st.session_state:  # TODO looking at bitwarden for secrets solution
        st.session_state.open_api_key = ""

    # Input fields

    # Examples: initialize session variables and assign values
    st.write("Name:")
    # st.session_state.name = st.text_input("", st.session_state.name)
    st.session_state.name = st.text_input("Enter your first and last name...", st.session_state.name)

    st.write("Engineering Prompt:")
    # st.session_state.prompt = st.text_area("prompt", st.session_state.prompt, value=DEFAULT_ENGINEERING_PROMPT)
    st.session_state.prompt = st.text_area("You can use this prompt as is or edit it...", st.session_state.prompt, key=generate_random_string(10))

    # Setup sidebar
    st.sidebar.subheader(f'Settings')
    open_api_key_input = st.sidebar.text_input(f'Enter your OpenAPI key if you have one or get one at '
                                               f'https://platform.openai.com/account/api-keys',
                                               type='password', key=generate_random_string(5)) # text_input("Enter a password", type="password")
    if open_api_key_input:  # https://platform.openai.com/account/api-keys
        st.session_state.open_api_key = open_api_key_input
        st.sidebar.caption(f'Key added..')

        with st.spinner("⏳‍processing your request.."):
            f'long running code'
            time.sleep(1)


if __name__ == "__main__":
    main()

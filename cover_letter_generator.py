# ARTICLE_RIGHTS: CR 2022, 2023.  William W Collins, All Rights Reserved
import os
import time
import streamlit as st
import requests
import json
from dotenv import load_dotenv

# Set page config
st.set_page_config(
    page_title="Generative AI Coverletter Generator",
    page_icon="🌊",
    layout="centered"
)

hide_streamlit_style = """
                <style>
                div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stDecoration"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stStatusWidget"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                #MainMenu {
                visibility: hidden;
                height: 0%;
                }
                header {
                visibility: hidden;
                height: 0%;
                }
                footer {
                visibility: hidden;
                height: 0%;
                }
                </style>
                """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# todo - consider Redis integration: https://towardsai.net/p/machine-learning/a-step-by-step-guide-to-developing-a-streamlit-application-with-redis-data-storage-and-deploying-it-using-docker

API_ENDPOINT = "https://api.openai.com/v1/chat/completions"
DEFAULT_ENGINEERING_PROMPT = "create a professional updated cover letter from the current cover letter and the job description"
DEFAULT_USER_NAME = "William Collins"
CURRENT_COVERLETTER = """William W. Collins, Jr.	Austin, TX 
williamwcollinsjr@gmail.com    940.503.8195
http://www.linkedin.com/in/williamwcollins

Dear Hiring Manager:

My experience and talent will enable you to not only meet but exceed your organization and company objectives.  

I have over 15 years progressive executive experience building and managing/intelligently scaling software engineering teams and delivering complex, hybrid and SaaS-based applications.   This includes support of both VC-funded startups as well as large, established enterprises. 

Experience includes managing cloud operations for scalability, reliability, and security. Cloud experience includes Azure, AWS, Google (GCP), Oracle, Heroku cloud services and is matched with deep knowledge of supporting Coding/SDLC/STLC, DevOps/MLOps/SRE technologies used in production web applications.  Coding experience includes but not limited to C#, Python, Node, React/Typescript, SQL, GraphQL, and Elasticsearch.  Also, knowledge of best practices for QA / testing, CI/CD, Containerization, Orchestration (Kubernetes) and system design / architecture.

As an experienced and insightful leader, your requirements for this role and my experience and talents are a great match. This includes roles requiring:
 
•	Developing, deploying, improving, and managing engineering processes, applications, and oversight in Start-up and Large Enterprise environments.  Includes delivery of both cloud-based and on-premise solutions deployed at scale.
•	Experience managing teams utilizing modern programming languages, data structures & algorithms, Frameworks, APIs, Services, and Processes e.g., Agile/Scrum, CI/CD
•	Experience leading internationally located development teams: India, Ireland, Amsterdam, Brazil, Mexico City.  Also, business and technical organizational management/alignment with teams throughout the continental US,  Canada, Dubai (UAE), Scotland, London, China, Panama, Chile, Argentina.
•	Proficiency in managing product development teams and using project management skills to translate product feature requirements into prioritized (P0, P1, P2) technical deliverables in order to meet or exceed aggressive time-to-market deadlines.  Accelerated, high-quality delivery via consistent improvement in:  Matrixed communications, process efficiencies, investment in key talent and supporting systems.  Experience automating, producing and communicating weekly generated KPIs to organization and key stakeholders.
•	Strong people and communication skills, with proven ability to build, mentor and motivate teams of high-performance individuals to work together to consistently deliver differentiated and disruptive industry leading results.
•	Extensive experience working closely with Customers, Stakeholders, Sales, Marketing, 3rd Party organizations and leadership to ensure alignment around all elements of product and feature delivery.  Early assessment of risks and corresponding mitigation plans.
•	Strong oral, written  skills, with ability to make complex subjects understandable for technical and non-technical audiences.  Ability to clearly and concisely present information, gain buy in and earn commitment to actionable business strategies.
•	Focused efforts in innovation, protection of intellectual property, patents and assistance with merger and acquisitions technical assessments (as needed).

I look forward to discussing applicable role(s) and my qualifications in greater detail. Please feel free to contact me at your convenience.

Sincerely,
William W. Collins, Jr.
"""
TEST_JOB_DESCRIPTION = """Full Job Description
Title: Director of Engineering
Reports to: CTO
Location: Austin, TX (in-office ~3 days per week)

About Blue Boxing Fish

If you’ve been searching for a career with a company that values creativity, innovation and teamwork, consider this your ticket to ride.

Blue Boxing Fish is on a mission to shake up the fragmented $15 billion charter bus industry by offering the first online marketplace that connects customers to a network of more than 600 bus operators from coast to coast. Our revolutionary platform makes it possible to book a bus in just 60 seconds – eliminating the stress and hassle of coordinating group transportation for anyone from wedding parties to Fortune 500 companies. We’re introducing transparency, accountability and accessibility to an industry as archaic as phone books. By delivering real-time availability and pricing, customers can use the Blue Boxing Fish marketplace to easily compare quotes, vehicles, safety records and reviews.

We're seeking team members who are revved up and ready to use technology to make a positive impact. As part of the Blue Boxing Fish team, you'll work alongside some of the brightest minds in the technology and transportation industries. You'll help drive the future of group travel and help raise the bar for service standards in the industry, so customers can always ride with confidence.

But we're not just about getting from point A to point B – Blue Boxing Fish is also committed to sustainability. By promoting group travel, we can significantly reduce carbon emissions and help steer our planet towards a greener future. In 2022 alone, we eliminated over 1 billion miles worth of carbon emissions with 25 million miles driven.

Blue Boxing Fish is looking for passionate and driven individuals to join our team and help steer us towards a better future for group transportation. On the heels of a $60 million Series A funding round, we’re ready to kick our growth into overdrive – and we want you to be part of the ride.

About this role

Blue Boxing Fish is seeking a Director of Engineering to manage and grow a world-class team of software engineers, devops engineers, data engineers, and QA. You will be responsible for driving alignment towards critical objectives, prioritizing and sequencing team efforts, and providing direction and mentorship to team members. In this role, you will work closely with our CTO, VP of Product Management, and customer stakeholders to deliver a wide variety of customer facing and back-office software systems powering our two-sided marketplace business. Our ideal candidate has experience not only managing teams of engineers, but also experience managing engineering managers and driving engineering culture at the organization.

Compensation

Estimated base salary for this role is $175,000-$215,000
Comprehensive benefits package, including fully subsidized medical insurance for Blue Boxing Fish employees and 401(k)
Responsibilities

Ensure the team consistently achieves timeline commitments with high quality products
Drive alignment towards critical project objectives, delegating and sequencing team efforts
Work alongside your product management counterparts to create roadmaps and deliver value
Prioritize team tasks and help remove blockers
Refine agile development processes to keep each team running smoothly
Run team meetings and development cycles (e.g. sprints, standups)
Grow the team through hiring initiatives, direct mentorship, and coaching
Experience and Expertise

5+ years of experience managing teams of 20+
3+ years of experience managing managers
Strong software development background and technical knowledge
Experience growing technical organizations across a variety of company stages and sizes
Successfully track record of recruiting, mentoring and retaining strong managers and engineers
Experience partnering with cross-functional leaders to define goals, roadmaps and priorities
Comfortable with ownership and accountability for products and deliverables
Recruiting Process

Step 1 - Video call: Talent Acquisition interview & brief (~12 min.) online Wonderlic assessment
Step 2 - Hiring Manager interview
Step 3 - Team interviews
Step 4 - Offer, reference & background check
Welcome aboard!
Blue Boxing Fish Principles

At Blue Boxing Fish, we don’t compromise on quality. We hire smart, high-energy, trustworthy people and keep them as motivated and happy as possible. We do that by adhering to our principles, which are:

Customer First
We always think about how our decisions will impact our clients; earning and keeping customer trust is our top priority
We are not afraid of short-term pain for long-term customer benefit
Create an Environment for Exceptional People
We foster intellectual curiosity
We identify top performers, mentor them, and empower them to achieve
Every hire and promotion will have a higher standard
Everyone is an Entrepreneur / Owner
No team member is defined by their function or job title; no job is beneath anyone
We do more with less; we are scrappy and inventive
We think long-term
Relentlessly High Standards
We reject the status quo; we constantly innovate and question established routines
We are not afraid to be wrong; the best idea wins
We don’t compromise on quality
Clarity & Speed
When in doubt, we act; we can always change course
We focus on the key drivers that will deliver the most results
Mandate to Dissent & Commit
We are confident in expressing our opinions; it is our obligation to express our disagreement
Once we agree, we enthusiastically move together as a team
"""
DEFAULT_MODEL = "gpt-3.5-turbo"
DEFAULT_TEMPERATURE = 0.5

SHOW_SUMMARIES = True
EXPANDER_DEFAULT = False  # expands all expanders, except single article summaries (controlled by SHOW_SUMMARIES)
MAX_WEBPAGE_URL_LEN = 70  # This excludes short urls in search unrelated to search subject
PROMPT_SUMMARY_REQUEST = f"Please provide a detailed summary of the following article:"
ARTICLE_AUTHOR = "William W. Collins"
ARTICLE_RIGHTS = "CR William W Collins, All Rights Reserved"
PROMPT_ARTICLE_REQUEST = f"Write an informational, detailed, professional news article by {ARTICLE_AUTHOR} " \
                         f"using the following multi-article content. Create title and markdown the title in bold blue, headers, sub-headers in " \
                         f"the article.  Also Create and introduction and a summary and use examples:"
NOTICE_APP_INFO = ":blue[Free Limited Research Preview]. This app may produce inaccurate information " \
                  "about people, places, or facts"

# Load the dotenv file
load_dotenv()


# Set Styles refs: https://medium.com/@avra42/streamlit-python-cool-tricks-to-make-your-web-application-look-better-8abfc3763a5b
st.set_option('deprecation.showPyplotGlobalUse', False)  # disable error gen
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
button_style = """
        <style>
        .stButton > button {
            color: blue;
            background: white;
        }
        </style>
        """
st.markdown(button_style, unsafe_allow_html=True)


# st.write(f'OPENAPI KEY: {OPENAI_API_KEY}')

import random
import string

def generate_random_string(length):
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

# Function to send a request to ChatGPT and get the updated cover letter
def generate_cover_letter(prompt, cover_letter):
    # Send a POST request to the ChatGPT API
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer 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",
        },

        json={
            "messages": [
                {"role": "system", "content": "You are the candidate."},
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": cover_letter},
            ],
            "data": [
                {"model": "gpt-3.5-turbo"}
            ],
        }
    )

    with st.expander(f'json from Generative AI return'):
        st.json(response.json())

    # Extract the updated cover letter from the response
    updated_cover_letter = response.json()["choices"][0]["message"]["content"]
    return updated_cover_letter

def generate_chat_completion(messages, model=DEFAULT_MODEL, temperature=1, max_tokens=None):

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {st.session_state.open_api_key}",
    }

    data = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }

    if max_tokens is not None:
        data["max_tokens"] = max_tokens

    try:
        response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))
    except Exception as e:
        st.caption(f'Error getting response back from request: {e}')
        response = None

    # st.caption(response.status_code)
    try:
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        st.caption(f'Error with API request: {e} : {response.status_code}')

def read_python_file(filename):
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

filename = "./resumes/Resume_WCollins_05_2023.5_TechMgmt.pdf"
def download_resume(filename=filename, loc='main'):
    with open(filename, "rb") as pdf_file:
        PDFbyte = pdf_file.read()

        if loc == "sidebar" or loc == None:
            resume_download = st.sidebar.download_button(label="Download Resume",key='dufhqiew',
                           data=PDFbyte,
                           file_name=filename,
                           mime='application/octet-stream')
        else:
            resume_download = st.download_button(label="Download Resume",
                             data=PDFbyte,
                             file_name=filename,
                             mime='application/octet-stream')

        if resume_download:
            if loc == 'sidebar':
                st.sidebar.caption(f"Thank you! William Collin's resume will be in your downloads folder.")
            else:
                st.caption(f"Thank you! William Collin's resume will be in your downloads folder.")

import random

def generate_random_numbers(num_digits):
    random_numbers = [str(random.randint(1, 10)) for _ in range(num_digits)]
    return ''.join(random_numbers)

# Example usage
# random_string = generate_random_numbers(5)
# print(random_string)


# Create the form using Streamlit
def main():

    st.sidebar.subheader(f'Settings')

    open_api_key_input = st.sidebar.text_input(f':green[Enter your OpenAPI key if you have one or get one at: https://platform.openai.com/account/api-keys]', type='password') # text_input("Enter a password", type="password")

    if open_api_key_input:  # https://platform.openai.com/account/api-keys
        st.session_state.open_api_key = open_api_key_input
        st.sidebar.caption(f'✅Key added..')

    col1, col2 = st.columns(2)
    with col1:
        st.sidebar.image(f'./images/you_image.jpg', 'William Collins', width=150)
        download_resume(loc='sidebar')
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
            st.header(f':blue[AIG (Generative) Assisted Cover Letter Generator]')
            st.caption(f'William Collins 2023, All Rights Reserved {NOTICE_APP_INFO}')

    with st.expander(f'What this app does...'):
        """
        Overall, this code creates a web application that utilizes the OpenAI API to generate updated 
        cover letters and other communications with a prospective employer. It provides a user-friendly 
        interface for inputting information and displays the 
        original and revised cover letters for comparison. The application aims to assist users in 
        creating professional and tailored cover letters by leveraging a generative AI (AIG) 
        LLM (Large Language Model):

        1. The code starts by importing necessary modules such as `os`, `time`, `streamlit`, `requests`, `json`, and `dotenv`. These modules are used for various functionalities in the application.
        
        2. Constants are defined for important values such as the API endpoint for the OpenAI API, default prompts and user information, and sample cover letter and job description texts. These constants provide default values and settings for the application.
        
        3. The code loads environment variables from a `.env` file using the `load_dotenv()` function. This allows the application to access sensitive information such as API keys securely.
        
        4. Streamlit configurations are set to customize the appearance and behavior of the web application. The `st.set_page_config()` function is used to set the page title, icon, and layout.
        
        5. A CSS style is defined using HTML markup to hide unnecessary elements of the Streamlit interface. This includes hiding the toolbar, decorations, status widget, main menu, header, and footer. The `st.markdown()` function is used to apply the CSS style.
        
        6. Utility functions are defined to support various operations in the application. The `generate_random_string()` function generates a random string of specified length, which can be used for generating unique identifiers. The `write2file()` function writes text to a file, either locally or in a cloud storage service.
        
        7. The `show_progress_bar()` function displays a progress bar using the `st.progress()` function from Streamlit. This function is used to provide visual feedback during long-running operations.
        
        8. Two main functions are defined: `generate_cover_letter()` and `generate_chat_completion()`. The `generate_cover_letter()` function sends a request to the ChatGPT API to generate an updated cover letter. It takes a prompt and the current cover letter as inputs, and it returns the updated cover letter generated by the API. The `generate_chat_completion()` function sends a request to the OpenAI API to generate a chat completion based on provided messages. It takes messages, model, temperature, and max tokens as inputs, and it returns the generated message content.
        
        9. The `main()` function is the core of the web application. It creates the user interface using Streamlit. The user can input their name, engineering prompt, current cover letter, and job description through text input fields. When the "Generate My Cover Letter/Other" button is clicked, the application calls the `generate_chat_completion()` function to generate the updated cover letter based on the provided inputs. The original and revised cover letters are displayed in separate columns, and the updated cover letter is also written to a file using the `write2file()` function.
        
        10. Finally, the `main()` function is called to run the web application. It sets up the user interface, handles user inputs, and generates the updated cover letter based on the provided information.
        
        Overall, this code creates a web application that utilizes the OpenAI API to generate updated cover letters. It provides a user-friendly interface for inputting information and displays the original and revised cover letters for comparison. The application aims to assist users in creating professional and tailored cover letters by leveraging the power of generative AI."""

    st.caption(read_python_file('cover_letter_generator.py'))  # built in expander in def

    # Create session state variables and assign defaults
    if "name" not in st.session_state:
        st.session_state.name = DEFAULT_USER_NAME
    if "prompt" not in st.session_state:
        st.session_state.prompt = DEFAULT_ENGINEERING_PROMPT
    if "cover_letter" not in st.session_state:
        st.session_state.cover_letter = CURRENT_COVERLETTER
    if "job_description" not in st.session_state:
        # st.session_state.job_description = TEST_JOB_DESCRIPTION
        st.session_state.job_description = ""


    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    if OPENAI_API_KEY:
        st.session_state.open_api_key = OPENAI_API_KEY
        # st.sidebar.caption(f'key={OPENAI_API_KEY}')

    if "open_api_key" not in st.session_state:  # TODO looking at bitwarden for secrets solution
        st.session_state.open_api_key = ""
        st.sidebar.caption(f'API key not found')

    # Input fields

    # initialize session variables and assign values

    st.subheader("Name:")
    # st.session_state.name = st.text_input("", st.session_state.name)
    st.session_state.name = st.text_input(f':blue[Enter your first and last name...]', st.session_state.name)

    def on_button1_clicked():
        st.session_state.prompt = f'create a professional updated Cover Letter from the current ' \
                                  f'cover letter and the job description'

    def on_button2_clicked():
        st.session_state.prompt = f'create a professional Message from the job description and the ' \
                                  f'current cover letter regarding why {st.session_state.name} would want to in this role work at this company'

    def on_button3_clicked():
        st.session_state.prompt = f'create a 100 word or less professional THANK YOU letter regarding ' \
                                  f'from {st.session_state.name}  ' \
                                  ' regarding the role and the company'

    def on_button4_clicked():
        st.session_state.prompt = f'using the Current Coverletter and Job Description create a 100 word or ' \
                                  f'less professional THANK YOU letter from {st.session_state.name} on NOT being selected for the role at company'

    def on_button5_clicked():
        st.session_state.prompt = f'using the Current Coverletter and Job Description create a 300 ' \
                                  f'word professional letter from {st.session_state.name} that answers ' \
                                  f'the question: What type of special training or certifications do you possess? for the role at company'

    def on_button6_clicked():
        st.session_state.prompt = f'using the Current Coverletter and Job Description create a 300 ' \
                                  f'word professional interview follow-up letter from {st.session_state.name} ' \
                                  f'that communicates ' \
                                  f'a thank you for their time, getting to know them a bit and sharing ' \
                                  f'about their company and how excited I am about the role at company'

    def on_button7_clicked():
        st.session_state.prompt = f'using the Current Coverletter and Job Description create a 300 ' \
                                  f'word professional letter from {st.session_state.name} that answers ' \
                                  f'the question: What type of special training or certifications do you possess? for the role at company'

    def on_button8_clicked():
        st.session_state.prompt = f'using the Current Coverletter and Job Description create a 300 ' \
                                  f'word professional letter from {st.session_state.name} that answers ' \
                                  f'the question: What type of special training or certifications do you possess? for the role at company'

    def on_buttonJD_clicked():
        st.session_state.job_description = TEST_JOB_DESCRIPTION
    # st.text_area("Enter text", key="text")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.button("Cover Letter", on_click=on_button1_clicked)
    with col2:
        st.button("Why this Role", on_click=on_button2_clicked)
    with col3:
        st.button("Thanks-Selected", on_click=on_button3_clicked)
    with col4:
        st.button("Thank-NotSel", on_click=on_button4_clicked)

    col5, col6, col7, col8 = st.columns(4)
    with col5:
        st.button("Special training", on_click=on_button5_clicked, key='col5')
    with col6:
        st.button("Post Interview", on_click=on_button6_clicked, key='col6', disabled=False)
    with col7:
        st.button("button7", on_click=on_button7_clicked, key='col7', disabled=True)
    with col8:
        st.button("button8", on_click=on_button8_clicked, key='col8', disabled=True)

    # st.subheader("Engineering Prompt:")
    # st.session_state.prompt = st.text_area("prompt", st.session_state.prompt, value=DEFAULT_ENGINEERING_PROMPT)
    st.session_state.prompt = st.text_area(f"':blue[You can use this prompt as is or edit it...']", st.session_state.prompt, key='adfkasdf')

    st.subheader("Current Cover Letter:")
    # st.session_state.cover_letter = st.text_area("Paste your existing coverletter here or edit...", st.session_state.cover_letter, key=generate_random_string(10))
    st.session_state.cover_letter = st.text_area(f':blue[Paste your existing coverletter here or edit...]', st.session_state.cover_letter, key='werwer')

    st.button("Use Example JD", on_click=on_buttonJD_clicked, key='example_jd')

    # st.session_state.job_description = st.text_area("Paste the job description here", st.session_state.job_description, key=generate_random_string(10))
    st.session_state.job_description = st.text_area(f":blue[Paste the job description here...]", st.session_state.job_description, key='rnfenrj')

   # st.sidebar.caption(f':blue[job description]: {st.session_state.job_description}')


    # Generate updated cover letter when the button is clicked

    if st.button("Generate My Cover Letter/Other"):
        # st.sidebar.caption(f':blue[job description]: {st.session_state.job_description}')

        messages = [
            {"role": "system", "content": "You are the candidate."},
            {"role": "user", "content": st.session_state.prompt}, # {"role": "user", "content": DEFAULT_ENGINEERING_PROMPT}
            {"role": "assistant", "content": st.session_state.cover_letter},
            {"role": "assistant", "content": st.session_state.job_description}
        ]

        with st.spinner("⏳‍processing your request.."):
            updated_cover_letter = generate_chat_completion(messages, model=DEFAULT_MODEL, temperature=1, max_tokens=None)
            time.sleep(1)

        # this can also be used for a timer - perform the sleep task after calling the long running task
        # show_progress_bar()  # function for progress bar

        col1, col2 = st.columns(2)

        st.write(f'Engineering Prompt: {st.session_state.prompt}')

        with col2:
            # text_area(self, label: str, value: SupportsStr = "")
            st.header("Revised")
            st.text_area(label='updated cover letter...(you can edit this)', height=600, value=updated_cover_letter)
            st.button(label='download',key='download_cl',on_click=write2file(updated_cover_letter,
                filename=f'./resumes/cover_letter_custom.{generate_random_numbers(5)}.txt'))
        with col1:
            st.header("Original Coverleter")
            # 'latin-1' codec can't encode character '\u2019' in position 6154: todo bug
            try:
                st.write(CURRENT_COVERLETTER)
            except Exception as e:
                st.caption(f'st.write error:{e}')
                # response.content.decode('latin-1')

        try:
            with col2:
                st.caption(f'writing to file...')
            write2file(updated_cover_letter, './output/cover_letter_updated.txt')
        except Exception as e:
            st.caption (f'Error writing to file: {e}')


if __name__ == "__main__":
    main()

# ARTICLE_RIGHTS: CR 2022, 2023.  William W Collins, All Rights Reserved
# existing apps - https://podcastindex.org/apps

import os
import time
import streamlit as st
import requests
import json
from dotenv import load_dotenv

# Set page config
st.set_page_config(
    page_title="AGI Assisted RSS Feeds and Podcast with AIG (Generative AI)",
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

If you’ve been searching for a career with a company that values creativity, innovation and teamwork, consider this your ticket to ride.

CharterUP is on a mission to shake up the fragmented $15 billion charter bus industry by offering the first online marketplace that connects customers to a network of more than 600 bus operators from coast to coast. Our revolutionary platform makes it possible to book a bus in just 60 seconds – eliminating the stress and hassle of coordinating group transportation for anyone from wedding parties to Fortune 500 companies. We’re introducing transparency, accountability and accessibility to an industry as archaic as phone books. By delivering real-time availability and pricing, customers can use the CharterUP marketplace to easily compare quotes, vehicles, safety records and reviews.

We're seeking team members who are revved up and ready to use technology to make a positive impact. As part of the CharterUP team, you'll work alongside some of the brightest minds in the technology and transportation industries. You'll help drive the future of group travel and help raise the bar for service standards in the industry, so customers can always ride with confidence.

But we're not just about getting from point A to point B – CharterUP is also committed to sustainability. By promoting group travel, we can significantly reduce carbon emissions and help steer our planet towards a greener future. In 2022 alone, we eliminated over 1 billion miles worth of carbon emissions with 25 million miles driven.

CharterUP is looking for passionate and driven individuals to join our team and help steer us towards a better future for group transportation. On the heels of a $60 million Series A funding round, we’re ready to kick our growth into overdrive – and we want you to be part of the ride.

About this role

CharterUP is seeking a Director of Engineering to manage and grow a world-class team of software engineers, devops engineers, data engineers, and QA. You will be responsible for driving alignment towards critical objectives, prioritizing and sequencing team efforts, and providing direction and mentorship to team members. In this role, you will work closely with our CTO, VP of Product Management, and customer stakeholders to deliver a wide variety of customer facing and back-office software systems powering our two-sided marketplace business. Our ideal candidate has experience not only managing teams of engineers, but also experience managing engineering managers and driving engineering culture at the organization.

Compensation

Estimated base salary for this role is $175,000-$215,000
Comprehensive benefits package, including fully subsidized medical insurance for CharterUP employees and 401(k)
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
CharterUP Principles

At Company, we don’t compromise on quality. We hire smart, high-energy, trustworthy people and keep them as motivated and happy as possible. We do that by adhering to our principles, which are:

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

PODCAST_INDEX_API_KEY = os.getenv("PODCAST_INDEX_API_KEY")
PODCAST_INDEX_API_SECRET = os.getenv("PODCAST_INDEX_API_SECRET")


# Set Styles refs: https://medium.com/@avra42/streamlit-python-cool-tricks-to-make-your-web-application-look-better-8abfc3763a5b
st.set_option('deprecation.showPyplotGlobalUse', False)  # disable error gen
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


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

# Function to fetch and parse the RSS feed
import feedparser
def parse_feed(feed_url):
    feed = feedparser.parse(feed_url)
    return feed

def split_string(string):
    # Split the string into sentences
    sentences = string.split('.')  # Assuming sentences end with a period followed by a space

    # Initialize variables
    first_100_words = ""
    remainder = ""

    # Loop through the sentences
    word_count = 0
    for sentence in sentences:
        # Split each sentence into words
        words = sentence.split()

        # Check if adding the current sentence exceeds the word limit
        if word_count + len(words) <= 100:
            # Add the sentence to the first 100 words variable
            first_100_words += sentence + '. '
            word_count += len(words)
        else:
            # Add the remaining sentences to the remainder variable
            remainder += sentence + '. '

    return first_100_words.strip(), remainder.strip()


# Function to display the parsed feed
def display_feed(feed):
    st.caption(f'{len(feed.entries)} feeds found...')
    i = 1
    try:
        for entry in feed.entries:
            first_100, remaining = split_string(entry.content[0].value)
            st.subheader(f'Article {i}. {entry.title}')
            st.write(f'**:blue[URL:]** {entry.link}')
            st.sidebar.caption(f'Article {i}. {entry.title} [link]({entry.link})')
            # st.caption(f'Summary: {entry.summary}')

            with st.expander(f'full report...'):
                html = f'{entry.content[0].value}'
                st.markdown(f'{html}', unsafe_allow_html=True)
                i += 1
            st.caption('---')
    except Exception as e:
        st.caption(f'Error: {e}')


def display_rss_feed_xml(url):
    # Parsing the RSS feed
    feed = feedparser.parse(url)

    # Displaying feed information
    st.title(feed.feed.title)
    st.write(feed.feed.description)

    # Displaying feed items
    for entry in feed.entries:
        st.subheader(entry.title)
        st.write(entry.published)
        st.write(entry.summary)
        # st.write(entry.value)  # throws exception
        st.write(entry.link)
        with st.expander("full report..."):
            st.caption(entry)  #  todo feature enhance -
            # return successful for limited test but need to find urls with this text using bs4 beautiful soup
        st.write("---")

def check_url_xml(url):
    if url.find('.xml') != -1:
        display_rss_feed_xml(url)
        # st.sidebar.error("xml type URL '.xml'. found")
        return True
    else:
        return False

filename = "./resumes/Resume_WCollins_05_2023.3_TechMgmt.pdf"
def download_resume(filename=filename, loc='main'""):
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

# Call the function to execute the code
# download_resume()


# Create the form using Streamlit

def main():

    st.sidebar.subheader(f'Settings')

    open_api_key_input = st.sidebar.text_input(f':green[Optional: Enter your OpenAPI key if you have one or get one at: https://platform.openai.com/account/api-keys]', type='password') # text_input("Enter a password", type="password")
    if open_api_key_input:  # https://platform.openai.com/account/api-keys
        st.session_state.open_api_key = open_api_key_input
        st.sidebar.caption(f'✅Key added..')

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
        download_resume(loc='sidebar')

    col3, col4 = st.columns(2)
    with col3:
        st.image(f'./images/tech_image_7.jpg', '', width=350)
    with col4:
        with st.spinner(f'loading main...'):
            time.sleep(1)
            st.header(f':blue[AGI Assisted RSS Feeds and Podcast]')
            st.caption(f'William Collins 2023, All Rights Reserved {NOTICE_APP_INFO}')

    with st.expander(f'What this app does...'):
        """This code creates a web application that functions as an RSS feed reader and podcast reader. 
        It allows users to upload RSS feed files or enter individual RSS feed URLs to fetch and display the feed content. The code utilizes the `feedparser` library to parse the RSS feeds and extract relevant information such as article titles, publication dates, and summaries.

The main functionality of the code can be summarized as follows:

1. Importing necessary modules: The code imports modules such as `os`, `time`, `streamlit`, `requests`, `json`, and `dotenv` to support various functionalities in the application.

2. Setting up Streamlit configurations: The code uses the `st.set_page_config()` function to set the page title, icon, and layout of the Streamlit web application. It also defines a CSS style using HTML markup to hide unnecessary elements of the Streamlit interface.

3. Defining utility functions: The code defines utility functions such as `generate_random_string()`, `write2file()`, `show_progress_bar()`, `generate_cover_letter()`, and `generate_chat_completion()`. These functions are used for tasks such as generating random strings, writing text to files, displaying progress bars, and interacting with the OpenAI API to generate cover letters.

4. Creating the main function: The `main()` function is the core of the web application. It sets up the user interface using Streamlit and handles user inputs. Users can input their name, engineering prompt, current cover letter, and job description through text input fields. When the "Generate My Cover Letter/Other" button is clicked, the application calls the `generate_chat_completion()` function to generate the updated cover letter based on the provided inputs. The original and revised cover letters are displayed in separate columns, and the updated cover letter is also written to a file using the `write2file()` function.

5. Running the web application: Finally, the `main()` function is called to run the web application. It sets up the user interface, handles user inputs, and fetches and displays the RSS feed content based on the provided URLs or uploaded files.

Overall, this code provides a simple and interactive web application for reading and accessing RSS feeds. Users can easily fetch and view articles from various RSS feeds by entering the feed URLs or uploading feed files.
"""

    st.caption(read_python_file(os.path.basename(__file__))) # built in expander in def

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

    st.title("RSS Feed Reader")
    uploaded_files = st.file_uploader("📂Upload RSS feed files.  Note that you will need to "
                                      "create local file(s) with your target rss feed urls", accept_multiple_files=True)
    st.caption(f'{len(uploaded_files)} files selected')
    if uploaded_files:
        for file in uploaded_files:

            if file.type:  # todo a check for this initially did not work. create more elegant code if poss
                content = file.read().decode('utf-8')
                urls = content.split('\n')
                st.caption(f'{len(urls)} urls found in file {file}')
                for url in urls:
                    st.caption(f'processing {url}...')
                    # check to see if url ends with .xml
                    st.caption(f'XML check {check_url_xml(url)}')
                    if check_url_xml(url):
                        st.caption(f'encountered an xml file...')
                        display_rss_feed_xml(url)
                        continue
                    url = url.strip()
                    if url:

                        try:
                            feed = parse_feed(url)
                            display_feed(feed)
                        except Exception as e:
                            st.caption(f'Error: {e}')
                    else:
                        st.warning("Empty URL found in the file.")
            else:
                st.warning("Invalid file format. Please upload a text file.")

    st.write(f'**:blue[OR...]**')

    feed_url = st.text_input("Enter RSS feed URL")

    if st.button("Fetch"):
        if feed_url:
            try:
                feed = parse_feed(feed_url)
                display_feed(feed)
            except Exception as e:
                st.caption(f'Error: {e}')
        else:
            st.warning("Please enter a valid RSS feed URL")







if __name__ == "__main__":
    main()

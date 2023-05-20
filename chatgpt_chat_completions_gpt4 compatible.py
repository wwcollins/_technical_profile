import requests
import json
import streamlit as st

OPENAI_API_KEY = "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"
API_KEY = OPENAI_API_KEY
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"
OPENAI_API_KEY = "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"
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"
DEFAULT_MODEL = "gpt-3.5-turbo"
DEFAULT_TEMPERATURE = 0.5

DEFAULT_ENGINEERING_PROMPT = "create a professional updated cover letter from the following current cover letter and the job description:"
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

About CharterUP

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

At CharterUP, we don’t compromise on quality. We hire smart, high-energy, trustworthy people and keep them as motivated and happy as possible. We do that by adhering to our principles, which are:

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

def generate_chat_completion(messages, model=DEFAULT_MODEL, temperature=1, max_tokens=None):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    data = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }

    if max_tokens is not None:
        data["max_tokens"] = max_tokens

    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))
    st.caption(response.status_code)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Translate the following English text to French: 'Hello, how are you?'"}
]

messages = [
                {"role": "system", "content": "You are the candidate."},
                {"role": "user", "content": DEFAULT_ENGINEERING_PROMPT},
                {"role": "assistant", "content": CURRENT_COVERLETTER},
                {"role": "assistant", "content": TEST_JOB_DESCRIPTION}
]

response_text = generate_chat_completion(messages)

print(response_text)

col1, col2 = st.columns(2)

st.write(DEFAULT_ENGINEERING_PROMPT)
with col2:
   st.header("Revised")
   # st.image("https://static.streamlit.io/examples/cat.jpg")
   st.write(response_text)

with col1:
   st.header("Original Coverleter")
   # st.image("https://static.streamlit.io/examples/dog.jpg")
   st.write(CURRENT_COVERLETTER)


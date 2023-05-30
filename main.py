
ARTICLE_RIGHTS = f'CR 2022, 2023.  William W Collins, All Rights Reserved'
# ARTICLE_RIGHTS: CR 2022, 2023.  William W Collins, All Rights Reserved
# This is a sample Python script.
# This site: wwcollins-profile.streamlit.app

import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)
import streamlit.components.v1 as components

# Page functions
def home_page():
    col1, col2, col3 = st.columns(3, gap="large")
    with col1:
        st.image(f'./images/home_sidebar_img.jpg', width=250)
    with col2:
        st.caption(f'')
    with col3:
        st.caption(f'')

    st.title("Welcome")
    st.write(
        """This profile site provides basic information about William and covers core beliefs with respect 
        to **Leadership** and **Technology** as well as thoughts and efforts regarding **Innovation** and 
        recent **Projects** William is and has been creating and fine tuning. Beyond understanding and implementing best of breed architecture and coding patterns, William 
             is focused on **architecting**, **integrating** and **building** out technologies related to **Generative 
             AI** as an extended platform across both engineering and non-engineering organizations.
        """
             )

def about_page():
    st.image(f'./images/you_image.jpg', 'William Collins', width=200)
    # st.image(f'./images/tech_image_6.jpg', width=250)
    st.title("About")
    st.write(
        """
        **Innovative Transformational Leader | Multi-Industry Experience | AI & SaaS Expert | Generative AI | DevOps, AIOps, SRE & Cloud Technologies**
        """
    )
    st.write(f'**William Collins** is a highly experienced executive with a proven track record in building and managing software engineering teams and delivering complex applications. He has worked with both VC-funded startups and large enterprises, and has expertise in AI platform development, cloud operations, and various coding languages. His skills include managing engineering processes, leading international teams, and translating product requirements into technical deliverables. William is an excellent communicator and has a strong focus on innovation and protecting intellectual property. He is well-suited for roles requiring leadership, technical expertise, and the ability to drive results.')
    with st.expander(f'more...'):
        st.write(
        """
        William W. Collins is a technology and software engineering management professional based in Austin, Texas. He has over 15 years of experience leading global product development, software/solutions teams, and providing pre-sales engineering support. His expertise includes web app development, APIs, cloud computing, AI machine learning, IoT, and sales engineering support.
        
        William is known for his strategic and innovative thinking, with the ability to articulate a vision and effectively communicate it to others. He has a hands-on approach and a track record of success in guiding global business strategy for both established and emerging organizations. He excels in managing and launching products and programs related to hardware, software, data, pre-sales, and service solutions.
        
        His technical skillset includes a focus on leading-edge technologies such as generative AI, SaaS web app development, APIs, microservices, Kubernetes/containerization, DevOps/AI/MLOps, SRE, AI/machine learning LP/computer vision, and IoT/edge computing. William has industry experience in various sectors including insurance/banking, manufacturing, marketing/digital agency/MarTech, legal, fintech, and automated business processing.
        
        Throughout his career, William has held positions in notable companies and made significant contributions. At Alkemie Technologies LLC, he delivered integrated generative AI solutions and SaaS web app products for insurance and banking industries. He also served as the VP of Software Engineering at PFL.com, where he improved processes, migrated legacy code to microservices/cloud infrastructure, and implemented cloud app consolidation plans.
        
        Prior to that, William worked as a Senior Director of Cloud Innovation and Solution Engineering at Oracle, driving innovation and developing capabilities in information management, predictive analytics, IoT, and chatbots. He has also held leadership roles at Retriever Services LLC, Dun and Bradstreet, LaunchWorks, and Dell Inc., where he managed development teams, oversaw solution architecture, and contributed to revenue growth.
        
        William holds a Bachelor of Science degree in Chemistry with a minor in Biology from the University of California, Irvine. He continuously engages in professional development, focusing on management and leadership, AI, leading-edge technologies, and modern software development methodologies.
        
        In summary, William W. Collins Jr. is a seasoned technology and software engineering management professional with a diverse skillset and extensive experience leading global teams and driving innovation in various industries. He is a strategic thinker, hands-on leader, and expert in emerging technologies, and he has a strong track record of success in product development, software engineering, and pre-sales support.
         """)

def resume_page():
    col1, col2 = st.columns(2, gap='small')
    with col1:
        st.image(f'./images/you_image.jpg', 'William Collins', width=200)
    with col2:
        st.write(f'')
        download_resume()  # fn which downloads resume for the user

    st.write(
        """
        **Innovative Transformational Leader | Multi-Industry Experience | AI & SaaS Expert | Generative AI | DevOps, AIOps, SRE & Cloud Technologies**
        """
    )
    st.title("Resume")
        # st.write("You can reach us through the contact page.")

    # Resume rendered as Streamlit Component
    components.html(
        """<!DOCTYPE html>
<html>
<head>
  <title>William W. Collins, Jr.</title>
  <script src="script.js"></script>
  <style>
    /* Add your CSS styles here */
  </style>
</head>
<body>
  <h1>William W. Collins, Jr.</h1>
  <p>Email: <a href="mailto:williamwcollinsjr@gmail.com">williamwcollinsjr@gmail.com</a></p>
  <p>m: 940-503-8195</p>
  <p>m: 512-294-7573</p>
  <p>alternate: 760-512-3195</p>
  <p>LinkedIn: <a href="http://www.linkedin.com/in/williamwcollins">http://www.linkedin.com/in/williamwcollins</a></p>

  <h2>Technology Profile and Portfolio</h2>
  <p>Technology and Software Engineering Management</p>
  <p>15+ years’ success leading global product, software/solutions development, and pre-sales engineering support teams.</p>
  <p>Management | Web App Development | APIs | Cloud | AI Machine Learning | IoT | Sales Engineering Support | Innovation</p>

  <h3>Technology Profile and Portfolio</h3>
  <p>Strategic/Innovative thinker. Able to articulate vision - and effectively impart that vision to others. Hands-on, Transformational Leader with repeated success guiding global business strategy within both established and emerging organizations. Talent for managing and launching products and programs related to hardware, software, data, pre-sales, and service solutions. Expert presenter and business professional; able to forge solid relationships with strategic partners. Innovative manager skilled at building top-performing teams, analyzing technology and market trends; scaling and growing businesses. Also, excellence in Engineering Organization, Technical and Professional transformation, and maturation.</p>

  <p>Possesses a broad technology skillset but currently focused on leading-edge technologies including Generative AI and associated technologies, modern SaaS Web App Development, API, microservices technologies and implementations, Kubernetes/Containerization, DevOPs/AI/MLOps, SRE, AI/Machine Learning/NLP/Computer Vision, IoT/Edge/FOG computing.</p>

  <p>Industry experience in Insurance/Banking, Manufacturing, Marketing/Digital Agency/MarTech, Legal, Manufacturing, FinTech and Automated Business Processing Industries and Applications including associated cloud service technologies and platforms: AWS, Azure, AWS, Oracle, GCP, Heroku, SaaS, PaaS, IaaS, and DaaS. Deep understanding of modern programming languages, platforms and Dev, DevOps, AI/MLOps, SRE, Observability, Tools/code including but not limited to Python, C#, Java, Node, React, Flask, Django, FastAPI, GraphQL, Kafka, Sonar Cloud, DataDog, TeamCity, Cypress, PyTest, Jest, CircleCI, Kubernetes, New Relic, Amazon CloudWatch. Experienced in state-of-the-art SDLC methodologies including converged DevOps/AI/MLOps, CI/CD, Scrum, and Agile, modern observability tooling e.g., Prometheus, OpenTelemetry, Grafana and physical deployments. Big data platform and pipelines.</p>

  <h3>Highlights of Expertise</h3>
  <ul>
    <li>Management: Global Technical Team Leadership (15+ years)</li>
    <li>Generative AI, Web App Development: SaaS Cloud and Hybrid solutions</li>
    <li>Software Development, Architecture and Platforms/Frameworks</li>
    <li>RESTful APIs /GraphQL/ Microservices</li>
    <li>Product, Program and Project Management</li>
    <li>SDLC/STLC - CI/CD, (Dev/ML) Ops, SRE, Kubernetes, Observability/Tooling, Test Automation</li>
    <li>AI/Machine Learning - Computer Vision/Object Detection/Classification/NLP</li>
    <li>IoT/Edge IoT programming, embedded AI/ML, Sensors/Actuators</li>
    <li>Technical Pre/Post-Sales Support</li>
  </ul>

  <h3>Career Experience</h3>
  <h4>Alkemie Technologies LLC (January 2023 to Current)</h4>
  <p>Delivery of integrated, Generative AI Solutions, SaaS Web App Products, APIs/microservices Systems Design and Architecture and Development for multi-industry deliverables include AI/ML, Natural Language Processing (NLP), Computer Vision/Image Classification, Sentiment Analysis/Text Classification, Geolocation, and mapping, RESTful/GraphQL</p>
  <p>Chief Technology Officer</p>
  <ul>
    <li>Technology visionary for company. Responsible for managing and improving efficiency of engineering team and internal support for the systems and architecture of the company.</li>
    <li>Anticipate new technology including incorporation of Generative AI within the engineering team across the organization to ensure marketplace relevancy competitive advantage. Responsible for understanding and determining monetization strategies via data analysis, assessments, prototype generation and testing, including required changes to the system architecture.</li>
    <li>Ensures technological decisions address business strategy including balancing innovation with the existing deliverables commitments and timelines, architecture and capabilities. Ensure ideation is vetted and executable with the current systems and talent in place – expands capability within budget to maximize ROI.</li>
    <li>Acting External Facing Technologist representing the product to clients and making pivotal decisions regarding delivering differentiated, disruptive technologies to market without disruption of the overall delivery of product(s). Tracking technology performance metrics and assessing internal and external impact and making decisions about the overall direction of the company.</li>
    <li>Design and Delivery of Customer Solutions focusing efforts across Dev, DevOps, SRE, AI including solutions for Generative AI integration for streamlined automation leverage of Generative AI as another tool to enable automation solutions for customers on at least 2 fronts: Rapid deployment and dynamically adjustable semi-customized AI-driven apps combined with rapid integration of customer-specific data (structured/unstructured) into Generative AI platforms to provide customer business-specific insights.</li>
  </ul>

  <h4>PFL.com</h4>
  <p>Responsible for the organizational engineering efforts supporting the growth of a Marketing Technology SaaS (Software as a Service) company that continues to pioneer and lead the Hybrid Experience category. Efforts include technical design, development through implementation and monitoring of all applications that facilitate effective interaction with our customers and support efficient business process and operations.</p>
  <p>VP of SOFTWARE ENGINEERING (May 2022 to Dec 2022)</p>
  <ul>
    <li>Improved processes and team structure supporting accelerated delivery of MVP to market in 4 months.</li>
    <li>Migration of on-prem legacy code leveraging microservices/cloud infrastructure.</li>
    <li>Move from REST to GraphQL to increase code speed/efficiency. Also move from legacy angular to React frontend.</li>
    <li>Leverage of Kubernetes orchestration to automate/accelerate build/deployment.</li>
    <li>Delivery of Cloud (Azure) app consolidation plan that reduced costs by ~$50K per month.</li>
    <li>Implemented/Executed initiatives across Dev, QA, SRE and Data Maturation Models resulting in:</li>
    <ul>
      <li>QA maturation level of ~1.6 to 3 and Automation from zero to 54% in 6 months.</li>
      <li>SRE team/Ops from maturation level of ~1.8 to 3 out of 5 in 4 months including introduction of advanced AI features.</li>
      <li>Data/AI/ML: Delivered multi-threaded, cloud-based pipeline and process to deliver E2E build of ML models including real-time data capability, actionable insights.</li>
    </ul>
  </ul>

  <h4>Alkemie Technologies, LLC</h4>
  <p>Delivery of integrated, Generative AI Solutions, SaaS Web App Products, APIs/microservices Systems Design and Architecture and Development for Insurance, Banking, Digital Agency Web Applications. Deliverables include AI/ML, Natural Language Processing (NLP), Computer Vision/Image Classification, Sentiment Analysis/Text Classification, Geolocation, and mapping, RESTful/GraphQL Weather/Astronomy products and integrations, microservices. On-premise, Hybrid and Cloud-based Solutions. Also, development of AI-embedded IoT edge devices connected to cloud-based SaaS applications.</p>
  <p>VP of SOFTWARE ENGINEERING (August 2019 to April 2022)</p>
  <ul>
    <li>Design and Delivery of Customer Solutions focusing efforts across Dev, DevOps, SRE, AI including solutions for Generative AI integration for streamlined automation leverage of Generative AI as yet another tool to enable automation solutions for customers on at least 2 fronts: Rapid deployment and dynamically adjustable semi-customized Prompt Engineering driven apps and rapid integration of customer-specific data (structured/unstructured) into Generative AI platforms to provide customer business-specific insights.</li>
    <li>Delivery and Execution of initiatives addressing QA, SRE, DevOps and, AI/MLOps Model Maturation, Architectural improvements including leverage of Microservices, Front-end/Backend performance improvements, Focus on enhanced Security, Technology/Monitoring Maturation, and Innovation. Delivery of multi-tenant Geo application that includes custom algorithms, multiple real-time RESTful calls: geo-location, weather, astronomy, solunar data to perform predictive weather/tide/astronomical analysis. Solution supported by API product also delivered as an additional monetized product.</li>
    <li>Development of Python/Flask and Node web applications and APIs, PHP Applications, Microservices for Windows, and Linux systems. Integration with MySQL, Postgres, Maria DB, Mongo DB, and other SQL/no-SQL Databases. Implementation of React/Hooks, Node API, Redis/Postgres/CouchDB (noSQL/JSON) Solutions, DevOps, and Infrastructure (primarily AWS, Azure, Heroku). SDLC, DevOps and Application Monitoring e.g., PyTest, Jest, CircleCI, New Relic, Amazon CloudWatch, DataDog, GitHub Security.</li>
  </ul>

  <h4>Oracle, Austin, Texas</h4>
  <p>Driving innovation with, and for customers looking to build in the Oracle Public Cloud - specifically Information Management, Predictive Analytics including supporting AI (Machine Learning, Image Capture and Classification), IoT and Chatbots. Also, building the next generation workforce at Oracle, and developing new capabilities with a focus on agility, scale and showing the 'art of the possible' with the Oracle Public Cloud.</p>
  <p>SENIOR DIRECTOR of CLOUD INNOVATION & SOLUTION ENGINEERING (June 2018 to August 2019)</p>
  <ul>
    <li>Scaled (by 1100%), Trained and Mentored Solution Architect team. Oversaw technical software development teams and off-site support service.</li>
    <li>Worked with Ops team to guide and help deliver and Automated Reporting process that improve time-to-delivery by approximately 800%.</li>
    <li>Improved relationships, process, and operational efficiency globally within Hub, Field/Internal sales, Oracle Consulting Group.</li>
  </ul>

  <h4>Retriever Services LLC, Austin, Texas</h4>
  <p>Provide senior-level leadership for Austin-based startup with full accountability for and direct management of technology initiatives: Software and Solution Development, Information Security, Enterprise Integration, and Data Center Virtualization.</p>
  <p>VP of ENGINEERING AND DEVELOPMENT (2016 to 2019)</p>
  <ul>
    <li>Direct all corporate operations encompassing multiple platforms and services including microcomputer based IoT sensor network/other solutions, SaaS applications, security appliances. Leverage of AWS Cloud. Python, Node, PHP, JavaScript, Bootstrap, JQuery and modern, relevant tools/platforms for development, deployment, and monitoring.</li>
    <li>Oversee technical software development teams and off-site support service.</li>
    <li>Create operational process and toolset for startup services and software development programs.</li>
    <li>Deliver Commercial Solutions for Classified (CSfC) architecture for Federal sales partners.</li>
    <li>Architect and Deliver Internet of Things (IoT) software and hardware solutions.</li>
  </ul>

  <h4>Dun and Bradstreet, Austin, TX</h4>
  <p>Established state-of-the-art enterprise solutions. Oversaw platform architecture, demo development and pre-sales engineering support for Data as a Service (DaaS/REST API), SaaS, PaaS, e-commerce, advertising, and subscription products. Leverage of AWS Cloud, Java, Python, .Net, Node, MongoDB, Angular, React and relevant platforms/tools.</p>
  <p>SENIOR DIRECTOR, PLATFORM SOFTWARE DEVELOPMENT (2014 to 2016)</p>
  <ul>
    <li>Normalized programming languages and architectures to responsive front-end, modular OOP back-end architecture.</li>
    <li>Improved process documentation of use and test case automation.</li>
    <li>Implemented JIRA/KanBan, Confluence, Git, etc. and supplied overall process improvement.</li>
    <li>Decreased defects by 97%.</li>
    <li>Increased testing automation by 340%.</li>
    <li>Implemented common platform solutions for Search, Identity Management, Monitoring, Corporate Linkage, and other core technologies reducing cross-product redundancy and development complexity by at least 420%.</li>
  </ul>

  <h4>LaunchWorks, Boerne, Texas</h4>
  <p>Supported complex projects and client relationships in business intelligence and portal technologies.</p>
  <p>VP of SOFTWARE DEVELOPMENT (2013 to 2014)</p>
  <ul>
    <li>Managed both technical and sales staff of small startup. Migrated Java and .Net Business Intelligence products from non-modular to object-oriented modular framework; delivered on-premise and cloud/SaaS-based embedded solutions. Implemented agile development process, unit/product/system test and code review.</li>
    <li>Reduced defect escapes by 117%.</li>
    <li>Improved customer satisfaction from 37% to 92% based on Net Promoter score.</li>
    <li>Increased company revenue by 212%.</li>
  </ul>

  <h4>Dell Inc., Austin, Texas (Total of 13 years in various roles), Round Rock, TX</h4>
  <p>Managed development, integration, testing, and pre-sales support for multiple hardware and software solutions.</p>
  <p>REGIONAL DIRECTOR, HW/SW SOLUTION DEVELOPMENT AND PRESALES SUPPORT (2009 to 2013)</p>
  <ul>
    <li>Startup of Dell Solution Global Solution Centers including the design, architecture, and simultaneous development/delivery of 20+ solutions across all Dell Industry verticals and contributing to $548M global revenue. Scaled and managed a global team from inception to 60+ hardware engineers, software developers, and solution architects and managers.</li>
    <li>Reduced time-to-market for twenty industry solutions by 52%, increased market share by 40% with corresponding revenue of $600 million.</li>
    <li>Launched six cutting-edge customer service facilities in Austin, Chicago, Washington DC, New York, California, Ireland, India, Brazil, and Mexico. Supported smaller Solution Centers in Panama, Chile, and Argentina.</li>
    <li>Implemented a customer engagement process which delivered over 1800 briefings, workshops, and proofs-of-concept contributing to $200+ million in revenue.</li>
  </ul>

  <h4>ADDITIONAL EXPERIENCE (WHILE EMPLOYED BY DELL/EMC)</h4>
  <p>Director, Global Enterprise Solutions Development (2007 to 2009) Global Enterprise Solutions, Dell, Inc., Round Rock, Texas. Global Product architecture and delivery of ERP Oracle, PeopleSoft, Siebel products/solutions per customer specifications contributing to $100M Americas and $400M global revenue.</p>
  <p>Senior Development Manager Global Product Development and Managed Services (2006 to 2007) Dell, Inc., Round Rock, Texas. Delivery of twenty-three internal and customer-facing Managed Services, Service Desk Capability products contributing $80M in Dell global revenue.</p>
  <p>Development Manager Global Product Development Group (2002 to 2006) Dell, Inc., Round Rock, Texas. Software Design, Development, and implementation of key software programs in Dell’s enterprise product group.</p>
  <p>Software Lead Global Product Group (2000 to 2002) Dell, Inc., Round Rock, Texas. Design and implementation of key hardware/software development programs in Dell’s enterprise product group.</p>

  <h3>Education & Credentials</h3>
  <p>University of California, Irvine, California</p>
  <p>BACHELOR OF SCIENCE – CHEMISTRY</p>
  <p>MINOR - BIOLOGY</p>
  <p>Professional Development: Continuous Study and Practice of: Management and Leadership. AI and leading-edge technologies. Global Distributed Management, Modern SDLC, DevOps, CI/CD, Scrum/Agile/Kanban. BPI (Six Sigma) Yellow Belt, Social Media Accreditation. Internet of Things (IoT) industry and development expertise leveraging SBCs, Python, Node, and PHP programming. Big Data, Analytics, and AI/Machine Learning, Computer Vision/Detection/Classification, and NLP).</p>
  <p>Technical/Management, Experience & Proficiencies: Generative AI. Cloud App Development; Oracle, AWS, Heroku, MS Azure, Google (GCP). DevOps, Docker, Kubernetes (AKS), IoT, Information Management, Advanced Analytics, Integrated Hardware/Software Server Solutions, Network and Storage solutions, Secure VDI, HIED ERP/LMS/LIMS Energy/SMARTGRID, Connected Classroom/Next Gen Learning, Mobile Video Evidence Management and Video Surveillance, VDI/Private Cloud, Digital Forensics, Mobile Clinical Computing, Big Data. Linux, Windows, SalesForce Integration, Waterfall and Agile development environments, Object-Oriented Programming, RESTful Web Services, Microservices, Mapping, Geolocation, MERN Stack MongoDB, Express, React, Node.js, Flask/Python, Jupyter Notebook. React, PHP, Java, C++, C, .Net, AJAX, JavaScript, Bootstrap, and JQuery. Sensor Networks, Single Board Computers, automated testing tools and environments, JMeter, Junit, JIRA/Kanban, Confluence, SourceTree, VNC, Git, WAMP/LAMP, APIs, Microservices, Dynamically Scalable Systems (Cloud Elastic), Agile/Scrum/Kanban, AI/ML/Deep Learning, Neural Networks, Predictive Analytics (on-premise and cloud), Leverage of Data Science Libraries/Technologies, NumPy, Pandas, matplotlib/Seaborn, SciPy, Scikit-Learn, Scikit-image, Tensorflow, Keras, spaCy/NLTK, Gensim, Pydicom, MedPy, DLTK, MIRTK, SimpleTK, Pytorch, Keras, OpenCV. Testing and Monitoring tools: TestRail, SauceLabs, Confluent, Postman, Launch Darkly, Insomnia, Swagger, Jira, Confluence, Cucumber, Sonar Cloud, Jest (Unit Test), Selenium, C#/Python automation, Postman, Cypress.</p>
  <p>Current Areas of Focused Study: Generative AI and the next generation of Software Development. Scalable, Sustainable Web App Development and RESTful API Development, HW/SW/Embedded Development, AI/ML/Deep Learning/Neural Networks; Image Classification, Computer Vision, Text Analysis (NLP), Algorithms; Cloud, Python/Flask/Django/FastAPI, Node, REST APIs, Microservices, DevOps, AI/MLOps.</p>
  <p>Interests and Affiliations:</p>
  <ul>
    <li>Generative AI. Innovation, Technology, Cloud, Web App System Design, Architecture and Programming, APIs, Microservices, AI/ML/NLP, IoT.</li>
    <li>IoT Planet, Member, IoT Council, HIMMS, HIE Watch, CIO Network, Data and Text Analytics Professionals.</li>
    <li>Personal: Technology and Innovation, Avid Outdoorsman, Archery/Bow Hunting, Surfing, Fly Fishing/Fly Tying, Writing non-fiction/fiction.</li>
  </ul>
</div>
</body>
</html>

"""
        , height=10000)

    # html = f"""<html><head><title>Yearly Symbol Prices</title></head><frameset><frame src='{app_path}'></frameset></html>"""

    # st.components.iframe(html, width=None, height=None, scrolling=False)

    # embed streamlit docs in a streamlit app
    # components.iframe("https://docs.streamlit.io/en/latest")

    # embed streamlit docs in a streamlit app
    # components.iframe("https://docx-to-markdown.streamlit.app")

def project_page():
    st.image('./images/tech_image_4.jpg', width=250)
    st.title("Technology Portfolio")
    st.header("Projects and Demos")
    # st.write("check out this [link](https://share.streamlit.io/mesmith027
    # /streamlit_webapps/main/MC_pi/streamlit_app.py)")

    st.subheader(f'AI including Generative AI')
    st.write(f'✅ Generative AI: Automated Coverletter Generation [link](https://wwcollins--technical-profile-cover-letter-generator-45le46.streamlit.app)')
    st.write(f'✅ Generative AI: Automated Article Generation [link](https://summaries.streamlit.app)')
    st.write(f'✅ Generative AI: Generative AI Search with Context Awareness [link](https://genchat.streamlit.app)')
    st.write(f'🍵 Generative AI: Personal Job Search Assistant: Search, Match, Scoring and Reporting')

    st.subheader(f'Microservices and APIs')
    st.write(f'🍵 Weather and Geolocation Microservices ')
    st.write(f'🍵 AWS Microservices: AWS S3 Microservice')
    st.write(f'🧪 Rapid Prototyping Process and Framework: Microservices/FastAPI')
    st.write(f'🍵 Building a Streamlit,Redis Application microservices Framework')

    st.write(f'🧬 Generative AI: Creating Custom LLMs and Fine Tuning')
    st.write(f'💭🧬 Generative AI: LLM models in a Hybrid/Distributed Infrastructure')

    st.subheader(f'Other Projects')
    st.write(f'✅ Convert docx file to markdown: [link](https://docx-to-markdown.streamlit.app)')
    st.write(f'✅ Streamlit Geodataframe and Plot of Weather Stations: [link](https://wwcollins-sl-noaa-weather-and-tides-plot-stations-pbwehq.streamlit.app)')

    st.write(f':green[Legend]: 💭=Innovating 🧬=In design 🍵= in development 🧪=in review ✅=Released')

def questions_answered():
    st.image('./images/tech_image_3.jpg', width=250)
    st.title("Questions and Answers")

    st.subheader("Answers to Common Questions")
    components.html(
        """
    <h2>Common Questions</h2>
        
    <h3>❔Question: Considering that Articulate is a diverse organization employing people from all over the world and with diverse backgrounds, talk about ways that you have worked to make others feel included.</h3>
        <p>William: In general, understanding social profiles, cultural backgrounds, work backgrounds and history, and including time zone differences. Where remote, ensuring that regular 1/1s and collective meetings are held where I can, and the team can get to know people and teams on an individual and collective basis. Pairing global team members to work on initiatives. Where budget allows, travel to meet with people 1/1, team building, sharing meals. Reading about related cultures and dynamics and how they affect people’s ability to relate to each other and team dynamics. Knowing each individual well, with 1/1s as well as skip levels up, down, and across the organization.</p>
        
    <h3>❔Question: Our culture is results-driven, what does that mean to you and how do you measure your own success?</h3>
        <p>William: Results-driven. Starting with the customer. What are our external internal customers experiencing? What are the metrics e.g attrition rates, NPS scores, individual discussions telling us? - Are we showing by action that we are "Customer Obsessed". Measure of success: Performing required planning, execution, and monitoring of results via completed milestones, meaningful OKRs/KPIs and not just reporting, but generating actionable insights that can be executed against. Be fluid and agile, assess and adjust as needed. Communicate results to all necessary parties, request ongoing feedback "in process", including customers, stakeholders, contributors.</p>
        <p>My Own Success: Are we producing according to plan and schedule, risk/mitigation awareness, resource assessment and flex, adequate communications/feedback, tracking tactical as well as strategic longer-term goals. Team morale is observed, measured e.g., standup automated recurring feedback. Are we celebrating wins? Are we celebrating reasonable failures and learning from them? Are we encouraging and allotting time for innovation? Are we automating? Are we making overall progress and enhancing the company, culture, and individual experience?</p>
        
    <h3>❔Question: When you’ve joined a team in the past, what have you done to earn the trust of others?</h3>
        <p>William: To earn team trust. Listening carefully and absorbing everything that is said, also things that are not said. Exercise empathy. Do not be overly prescriptive with solutions - have the team come up with and "own" the solution. Practice what you preach. Critical - get to know your people, beyond just work. Get to know them as people. Work hard but play hard. Support their efforts. Be flexible. Work alongside them when possible. Know where they each want to go in their careers - assist them via mentoring/support. Show appreciation. Paint a strong vision for the future of the organization, the company, the individual.</p>
    
    <h3>❔What is the biggest technical or product challenge you have experienced? How did you overcome it?</h3>
        <p>William: One of the biggest technical or product challenges was initiated from a customer using our SaaS Martech Services product.  The customer, banking vertical, was leveraging data from our app as well as exercising our new API.  The customer was in the banking industry so the information required accurate output for this customers use.  Challenges were primarily centered around project status and deliverables status.  This was during my 2 month as VP of Engineering.  Tech support and legal were already involved in a situation.  I met with all parties including the customer CTO and the customer’s users.  After intake, I met with the team within about 2h had scripts generated and running to assess event status/handling in several areas key relevant to the customer issues. The RCA resulted in several defects around event handling, one group of events required a short term fix and a re-architecture and code re-write/re-factor.  The effort including architecture and code review also exposed instances of Poor Component Design, code changes to optimizing React Performance, Inefficient State Management and Security Vulnerabilities in both modernized but primarily legacy code dependencies.  This effort was successfully accomplished. However, results of the investigation generated several additional key focus areas and initiatives as well as a thorough investigation into more robust code instrumentation and observability tooling.
    
    <h3>❔The CTO will guide the engineering and product teams to sync harmoniously during development to incorporate user needs into the new product during development. Describe how you would positively influence all stakeholders to achieve this.</h3>
        <p>William: From CxO, Product Team/Owner and other key stakeholders, the most important aspect of this effort is understanding customer needs, product features (prioritized) and then iteratively working with Prod/Engineering to articulate these into technical feature deliverables, with care to understand dependencies and technical debt required to deliver these to market.  To positively influence all stakeholders the effort above need to vetted and coordinated with all key stakeholders in order to balance need, priority, and timeline.  Once the plan has been vetted, plan execution begins leveraging agile, /kanban models and the status and metrics pertinent to company OKRs and the status re. deliverables needs to be transparently and routinely communicated.  With respect to “all” customers, demonstratable key milestones and feedback mechanisms need to be in place to ensure that the original plan tracks along with the potential for change requests to ensure optimal delivery of product per the agreed upon roadmap.
    
    <h3>❔Do you have experience interviewing engineering candidates and teaching your Team leaders how to interview and set interview processes?</h3>
        <p>William: Yes.  Including the need to hiring to scale during several roles.  For example, Dell, from 2 to 60+ including 4 managers over 18mos.  Other examples as well.  In each role, working not only with the team but internal and external recruiters and setting clear expectations is critical in order to attract the right candidates.  I personally sit in on many interviews to assess interview preparedness, structure, culture and ability for the interviewers to ask the right questions, as well as follow-up questions, and to ensure that the interviewers environment is one where all feel as comfortable and as at ease as possible.  Being in these interviews not only allows you to observe, but also to lead by example.  Teaching moments often come later in 1/1s or feedback to managers so that they can mentor accordingly.  I a recent case where the sheer volume of resumes was overwhelming and the engineering staff were maxed out, I spent a few weekend hours writing automation code to compare all Resumes to JDs using AI/NLP to score and stack rank all candidates.  These eased my organization’s burden of having to go though all of the resumes manually.  HR/Recruiting were aware of the effort and were able to leverage the code as well.
    <h3>❔Think of one instance where conflict arose during a project you were managing. Describe the situation, actions you took, and the result.</h3>
        <p>William: Using STAR:
        Situation:  Assuming the conflicts was between people, one relatively recent issue arose around the product team strongly attempting to introduce new/enhanced features (scope creep) which if not handled quickly, would have jeopardized an already tight engineering schedule.  
        Tasks:  Since enough trust was in place among engineering staff and management, we heard about the pressure early enough to address it.  We determined that a quick assessment of current sprint progress, roadmap, defect count (overall technical debt/timeline), along with the changes Prod had requested.  We leveled the project plan with under both scenarios which showed that are deadlines could not be met.  We discussed options such as adding resources, extending timelines but these were found lacking or not an option.  We decided to short-list a few items that seemed extremely important and had a reasonable ROI.  The process was then followed correctly at that point introducing CRs as stretch goals into the ticketing system (Jira).  Stakeholders were presented with situation and the proposed actions.  Progress was closely monitored and reported.  
        Result:  The plan was a win/win, product released slightly ahead of schedule, stakeholders received support for features beyond original scope, and was an example to all organizations and members that conflicts can be navigated around so that we all have the best chance of winning.
    <h3>❔Describe a time where you managed change during the migration of one technology to another.</h3>
        <p>William: Worked with team to move of code from legacy on prem systems to hybrid/cloud via microservices (including traditional ASP to C#), migration of angular to React, API to GraphQL, and increased use of Kubernetes to more efficiently support deployment.  This was a large effort and was planned carefully and was going well.  Not part of the plan was a new and urgent finance request to significantly reduce Azure cloud services cost.  We determined application pooling would be challenging but would offer the best ROI, but came with med to high risk.  The plan was executed over one weekend resulting in failure.  However, knowing that this was a possibility, the mitigation plan was put in place.  Initially, there was a rollback, then a decision to consolidate to multiple vs one pool.  In parallel, a RCA was performed, resulting in fixes for applications/environment that improved connection pooling resource sharing and a closer look at application’s configuration and find tuning.  The effort saved this smaller company around 50K/per month and showed where are code was week and could be made more efficient and robust.
        """, height=10000)

def beliefs_page():
    st.image('./images/tech_image_3.jpg', width=250)
    st.title("Core Beliefs")

    st.subheader("On Leadership")

    with st.expander(f'Leadership Checklist', expanded=True):
        st.write(""":blue[Successful Leadership]
               \n◻**Start with the customer**: Prioritize understanding and meeting their needs to foster trust, loyalty, and long-term relationships.
               \n◻**Ownership mindset**: Embrace a forward-thinking approach, seeking opportunities for innovation and automation to simplify processes and optimize efficiency.
               \n◻**Value diverse perspectives**: Actively seek insights from others to broaden understanding and make informed decisions.
               \n◻**Exercise strong judgment**: Seek out diverse viewpoints, constantly learn and expand knowledge, and raise the performance bar for teams.
               \n◻**Pursue excellence**: Set high standards, think big, inspire others to exceed expectations, and embrace a bias for action.
               \n◻**Resourceful and frugal**: Maximize impact while responsibly managing resources.
               \n◻**Build trust**: Actively listen, engage in open and candid conversations, treat others with respect, and create an inclusive environment.
               \n◻**Dive deep into details**: Challenge decisions when necessary, ensuring thorough analysis informs choices.
               \n◻**Wholehearted commitment**: Once a decision is made, fully dedicate efforts to its successful implementation.
               \n◻**Deliver exceptional results**: Focus on achieving outstanding outcomes and becoming the best possible employer.
               \n◻**Prioritize well-being and development**: Foster a safe, productive, and diverse work environment that supports continuous growth.
               \n◻**Mindful of impact**: Consider the effect on local communities, the environment, and future generations.
               \n◻**Strive for improvement**: Continually challenge oneself to do better and be better for customers, employees, and partners.
               """)
    components.html(
        """
        <h2>On Leadership Principles</h2>
        
        <p>Leadership Principles are not just a list of business objectives, but rather, they are foundational beliefs that are ingrained in how we operate in our daily lives. As a leader, it is important to start with the customer and obsess over their needs. Additionally, leaders must be owners who think long term and seek to innovate and automate wherever possible. They should always strive to simplify and streamline processes while also seeking insight from others to broaden their perspective.</p>
        
        <p>Leaders must have strong judgment and seek out diverse perspectives, while still being able to learn and be curious. To truly succeed, leaders need to hire and develop exceptional talent while also raising the performance bar for their teams. They must insist on the highest standards and continuously think big to inspire results. Leaders must also have a bias for action and be frugal, seeking to do more with less.</p>
        
        <p>It's important for leaders to build trust by listening attentively, speaking candidly, and treating others with respect. They should also dive deep into details, challenge decisions when necessary, and commit wholeheartedly once a decision is made.</p>
        
        <p>Ultimately, leaders must focus on delivering results and strive to be the best possible employer. They should work to create a safe, productive, and diverse work environment while also being mindful of their impact on their local communities, the planet, and future generations. Leaders need to continually strive to do better and be better for their customers, employees, and partners.</p>
        """
        , height=300
    )


    st.subheader("On Technology")
    components.html(
        """
        <h1>Being a Leader in Technology: Navigating the Frontiers of Innovation</h1>

        <p>In today's rapidly evolving digital landscape, being a leader in technology requires more than just technical expertise. It demands a unique set of skills, a visionary mindset, and the ability to navigate through complex challenges. As technology continues to reshape industries and drive unprecedented advancements, leaders in this field must embrace innovation, strategic planning, and transformative thinking to stay ahead of the curve.</p>
        
        <h2>The Power of Innovation and Vision</h2>
        
        <p>At the heart of technology leadership lies innovation. Leaders in technology must constantly seek out new ideas, challenge the status quo, and drive breakthroughs that push the boundaries of what is possible. They must foster a culture of innovation within their organizations, encouraging their teams to think creatively and experiment with novel approaches to problem-solving. By fostering an environment that nurtures innovation, leaders enable their teams to uncover new opportunities and drive meaningful change.</p>
        
        <p>Moreover, being a leader in technology requires a visionary perspective. Visionaries possess the ability to see beyond the present and anticipate future trends and challenges. They have the foresight to identify emerging technologies and their potential impact on the industry. By aligning their vision with business objectives, technology leaders can guide their organizations towards strategic initiatives that capitalize on disruptive technologies.</p>
        
        <h2>Strategic Planning and Architecture</h2>
        
        <p>A leader in technology must possess strong strategic planning skills. They understand the importance of formulating a clear roadmap that aligns technology initiatives with business goals. By establishing a strategic vision, leaders can drive organizational alignment and ensure that technology investments support long-term growth and success.</p>
        
        <p>Architecture plays a crucial role in technology leadership. Leaders must develop robust and scalable architectures that can adapt to changing business needs and technological advancements. This requires a deep understanding of emerging trends, cloud services, and microservices architecture. By leveraging cloud services and microservices, leaders can build flexible and scalable systems that enable agility, efficiency, and innovation.</p>
        
        <h2>Embracing Artificial Intelligence and Generative AI</h2>
        
        <p>Artificial intelligence (AI) has become a transformative force across industries. Technology leaders must embrace AI and recognize its potential to revolutionize processes, improve efficiency, and unlock new insights. They must stay abreast of AI advancements, understand its ethical implications, and identify opportunities for its integration within their organizations.</p>
        
        <p>Generative AI, in particular, holds great promise. This cutting-edge technology enables systems to generate novel and creative outputs, paving the way for innovation and groundbreaking solutions. Leaders in technology must explore the possibilities of generative AI, harnessing its power to drive transformation and create unique value propositions.</p>
        
        <h2>Leading Organizations through Digital Transformation</h2>
        
        <p>Digital transformation has become imperative for businesses to thrive in the digital age. Technology leaders play a pivotal role in driving this transformation. They must guide their organizations through the process of adopting new technologies, modernizing legacy systems, and reimagining business models.</p>
        
        <p>One of the critical aspects of digital transformation is the ability to attract, hire, and grow key talent. Technology leaders must identify individuals with the right skills and mindset to drive innovation and navigate the digital landscape. By fostering a culture of continuous learning and providing opportunities for professional growth, leaders can cultivate a team of talented individuals who can effectively execute the organization's digital transformation strategy.</p>
        
        <h2>Conclusion</h2>
        
        <p>Being a leader in technology requires a unique blend of technical expertise, visionary thinking, and strategic acumen. Innovation, planning, architecture, development, cloud services, microservices, artificial intelligence, and generative AI are all vital components of this role. By embracing these elements and leading organizations through digital
        
         transformation, technology leaders can shape the future and drive meaningful impact in an increasingly technology-driven world.</p>
 """, height=800
    )

    st.subheader("Answers to Common Questions")
    components.html(
    """
    <h2>Common Questions</h2>

<h3>Question: Considering that Articulate is a diverse organization employing people from all over the world and with diverse backgrounds, talk about ways that you have worked to make others feel included.</h3>
<p>William: In general, understanding social profiles, cultural backgrounds, work backgrounds and history, and including time zone differences. Where remote, ensuring that regular 1/1s and collective meetings are held where I can, and the team can get to know people and teams on an individual and collective basis. Pairing global team members to work on initiatives. Where budget allows, travel to meet with people 1/1, team building, sharing meals. Reading about related cultures and dynamics and how they affect people’s ability to relate to each other and team dynamics. Knowing each individual well, with 1/1s as well as skip levels up, down, and across the organization.</p>

<h3>Question: Our culture is results-driven, what does that mean to you and how do you measure your own success?</h3>
<p>William: Results-driven. Starting with the customer. What are our external internal customers experiencing? What are the metrics e.g attrition rates, NPS scores, individual discussions telling us? - Are we showing by action that we are "Customer Obsessed". Measure of success: Performing required planning, execution, and monitoring of results via completed milestones, meaningful OKRs/KPIs and not just reporting, but generating actionable insights that can be executed against. Be fluid and agile, assess and adjust as needed. Communicate results to all necessary parties, request ongoing feedback "in process", including customers, stakeholders, contributors.</p>
<p>My Own Success: Are we producing according to plan and schedule, risk/mitigation awareness, resource assessment and flex, adequate communications/feedback, tracking tactical as well as strategic longer-term goals. Team morale is observed, measured e.g., standup automated recurring feedback. Are we celebrating wins? Are we celebrating reasonable failures and learning from them? Are we encouraging and allotting time for innovation? Are we automating? Are we making overall progress and enhancing the company, culture, and individual experience?</p>

<h3>Question: When you’ve joined a team in the past, what have you done to earn the trust of others?</h3>
<p>William: To earn team trust. Listening carefully and absorbing everything that is said, also things that are not said. Exercise empathy. Do not be overly prescriptive with solutions - have the team come up with and "own" the solution. Practice what you preach. Critical - get to know your people, beyond just work. Get to know them as people. Work hard but play hard. Support their efforts. Be flexible. Work alongside them when possible. Know where they each want to go in their careers - assist them via mentoring/support. Show appreciation. Paint a strong vision for the future of the organization, the company, the individual.</p>
    """, height=1000)

def innovation_page():
    st.image(f'./images/tech_image_innovation.jpg', width=250)
    st.title("Innovation")
    st.write("Innovative moments and thoughts on innovation.")

    components.html(
        """<!DOCTYPE html>
<html>

<head>
  <title>Nurturing Innovation Technology Leadership: Balancing Continuous Progress and Core Deliverables</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.5;
    }

    h1 {
      color: #333;
      text-align: center;
      font-size: 32px;
      margin-bottom: 30px;
    }

    h2 {
      color: #333;
      font-size: 24px;
      margin-bottom: 20px;
    }
    
    h3 {
      color: blue;
      text-align: center;
      font-size: 18px;
      margin-bottom: 20px;
    }

    p {
      color: #555;
      font-size: 18px;
      margin-bottom: 15px;
    }

    blockquote {
      background-color: #f9f9f9;
      border-left: 10px solid #333;
      padding: 15px;
      margin: 0 0 20px;
      
    }

    blockquote:before {
      color: #777;
      content: open-quote;
      font-size: 80px;
      line-height: 0.1em;
      margin-right: 5px;
      vertical-align: -0.4em;
    }

    blockquote p {
      display: inline;
    }
    
        .signature {
      font-family: cursive;
      font-size: 18px;
      padding: 10px;
      display: inline-block;

    }
    
    .name {
      display: block;
    }
    
    .date {
      display: block;
      font-size: 18px;
      margin-top: 5px;
    }

  </style>
</head>

<body>
  <h1>Technology Leadership and Nurturing Innovation : Balancing Continuous Progress and Core Deliverables</h1>
    <h3>William Collins, 2023</h3>
  <p>Introduction:</p>
  
  <blockquote>
    <p>"Innovation is seeing what everybody has seen and thinking what nobody has thought." - Elon Musk</p>
  </blockquote>  

  <p>These words epitomize the essence of technological progress and the critical role of innovation in driving growth and success. In today's fast-paced and competitive landscape, organizations need visionary leaders who can foster a culture of constant innovation while effectively managing the delivery of core engineering and product commitments. This article explores the significance of innovation technology leadership and how collaboration with engineering and other teams can ensure a seamless integration of innovation into everyday workflows.</p>

  <h2>The Role of Innovation Technology Leadership</h2>

  <p>Innovation technology leadership encompasses the ability to identify emerging trends, leverage cutting-edge technologies, and create an environment that encourages experimentation and breakthrough thinking. It requires a visionary mindset, strategic decision-making, and effective communication to align diverse teams towards a common goal. A strong innovation leader understands the importance of balancing the pursuit of new ideas with the need to deliver on existing commitments.</p>

  <h2>Cultivating a Culture of Innovation</h2>
  
  <blockquote>
    <p>  "Leadership in the digital age requires a deep understanding of technology and the ability to leverage it to create new opportunities and value for the organization." - Sheryl Sandberg</p>
  </blockquote>

  <p>To foster a culture of innovation, leaders must create an environment that encourages curiosity, risk-taking, and collaboration. This can be achieved through initiatives such as dedicated innovation labs, cross-functional brainstorming sessions, hackathons, or regular knowledge-sharing forums. By empowering team members to explore new possibilities and providing them with the necessary resources and support, leaders can unleash their creative potential.</p>

  <h2>Collaboration on Innovation between External and Engineering Teams</h2>
  
    <blockquote>
  <p>"A leader's role is not to control people or outcomes, but to create an environment where innovation and creativity can flourish." - Richard Branson</p>
  </blockquote>
    
  <p>Collaboration between external and engineering teams is crucial for seamless integration of new ideas into existing products and processes. Regular communication and alignment of goals help ensure that innovation initiatives are in sync with engineering timelines and milestones. Leaders can facilitate collaboration by promoting open dialogue, establishing feedback loops, and fostering a culture of mutual respect and trust. Engaging engineering teams early in the innovation process allows for efficient planning and resource allocation.</p>

  <h2>Agile Frameworks for Innovation</h2>

  <p>Adopting agile methodologies can significantly enhance innovation while minimizing disruption to core deliverables. Agile frameworks, such as Scrum or Kanban, enable iterative development, continuous feedback, and rapid prototyping. By breaking down innovation projects into smaller, manageable tasks, leaders can facilitate parallel progress, allowing engineering teams to balance their commitments effectively. Regular retrospectives and adaptability to changing priorities ensure that innovation efforts remain aligned with organizational objectives.</p>

  <h2>Maintaining Focus on Core Engineering and Product Deliverables</h2>

  <p>While fostering innovation is crucial, leaders must not lose sight of the importance of delivering on core engineering and product commitments. Striking the right balance requires effective prioritization, resource allocation, and clear communication of expectations. Leaders should set realistic timelines, ensure sufficient support for ongoing projects, and empower teams to manage their workloads effectively. By establishing a culture of accountability and providing necessary tools and frameworks, leaders can maintain momentum in innovation while ensuring timely delivery of key deliverables.</p>

  <p>Conclusion:</p>
  <blockquote>
    <p>"Innovation distinguishes between a leader and a follower." - Steve Jobs</p>
  </blockquote>

  <p>Finally, as we strive toward having an innovative and collective mindset, it's good to also remember the words of Steve Jobs, "Innovation is not about saying yes to everything. It's about saying no to all but the most crucial features." Embracing this mindset, innovation technology leaders can guide their teams towards transformative breakthroughs, driving organizations to new heights of achievement and excellence.</p>

  <div class="signature">
    <span class="name">-William Collins, 2023</span>
  </div>
  
</body>

</html>
""", height=10000
    )

def utilities_page():
    st.image(f'./images/tech_image_innovation.jpg', width=250)
    st.title("Utilities")
    st.write("Useful utilities/code to manage your site...")
    st.write(f'Convert docx file to markdown: [link](https://docx-to-markdown.streamlit.app)')
    st.write(f'Streamlit Deployment Options [link](https://discuss.streamlit.io/t/streamlit-deployment-guide-wiki/5099)')
    st.caption(f'...more coming soon!')

def articles_page():
    st.image('./images/tech_image_5.jpg', width=250)

    st.title("Articles:  Author:  William Collins")
    with st.expander(f'Article: :blue[Pandas AI: Revolutionizing Generative AI with a Powerful Python Library]'):
        st.write("""**Title: Pandas AI: Revolutionizing Generative AI with a Powerful Python Library**
over**Introduction**

Generative Artificial Intelligence (AI) has emerged as a groundbreaking technology, enabling machines to create new and original content. It has found applications in various domains, including art, music, and text generation. Pandas AI, a Python library, has rapidly gained recognition for its ability to support Generative AI tasks. This article explores the impact of Pandas AI on the field of Generative AI, highlighting its capabilities and discussing its potential for revolutionizing data analysis and content generation.

**1. Understanding Pandas AI and Its Key Features**

Pandas AI is an open-source Python library developed specifically to facilitate Generative AI tasks. It builds upon the foundation of the popular pandas library, which is widely used for data manipulation and analysis. Pandas AI extends pandas' capabilities by incorporating advanced algorithms for generative modeling, making it an ideal tool for generating new data based on existing patterns and structures.

The key features of Pandas AI include:
a) Generative Models: Pandas AI provides implementations of various generative models, including autoencoders, generative adversarial networks (GANs), and variational autoencoders (VAEs). These models enable the generation of realistic and high-quality content by learning the underlying patterns from a given dataset.
b) Deep Learning Integration: The library seamlessly integrates with deep learning frameworks like TensorFlow and PyTorch, allowing users to leverage the power of deep neural networks for generative modeling.
c) Data Manipulation: Leveraging the core functionalities of pandas, Pandas AI offers comprehensive data manipulation tools that facilitate preprocessing and transformation tasks essential for generative modeling.
d) Evaluation Metrics: The library incorporates evaluation metrics such as inception score, Frechet Inception Distance (FID), and reconstruction loss, enabling users to assess the quality and performance of generated content.

**2. Impact of Pandas AI on Generative AI**

Pandas AI has had a significant impact on the field of Generative AI, revolutionizing the way data analysis and content generation are approached. Here are some key areas where Pandas AI has made a difference:

**a) Enhanced Data Analysis:** By combining the power of pandas for data manipulation and Pandas AI for generative modeling, analysts and data scientists can gain deeper insights into their datasets. Pandas AI enables the generation of synthetic data that follows similar patterns as the original data, helping to expand limited datasets for more robust analysis.

**b) Creative Content Generation:** Generative AI is not limited to data analysis alone; it has opened up new avenues for creative content generation. With Pandas AI, artists, musicians, and writers can harness the potential of generative models to create unique and novel content. For instance, musicians can generate melodies, writers can create stories, and artists can produce original artwork, all based on existing patterns and styles.

**c) Rapid Prototyping and Simulation:** Pandas AI simplifies the process of prototyping and simulating data-driven systems. It allows developers and researchers to generate synthetic datasets that resemble real-world data, facilitating testing and evaluation of algorithms and models before deployment. This feature is particularly valuable in domains such as autonomous driving, robotics, and simulations.

**d) Democratization of Generative AI:** Pandas AI's user-friendly interface and extensive documentation make it accessible to a wide range of users, including those without extensive machine learning expertise. This democratization of Generative AI empowers professionals from diverse backgrounds to leverage the capabilities of generative modeling, thereby fostering innovation and creativity.

**3. Future Implications and Conclusion**

Pandas AI has already made a significant impact on Generative AI by enabling enhanced data analysis, creative content generation, rapid prototyping, and democratization of generative modeling. Looking ahead, it is""")
    with st.expander(f'Article: :blue[Harnessing the Power of Generative AI]: Revolutionizing Collaboration between Product and Engineering Teams'):
        st.write("""Harnessing the Power of Generative AI: Revolutionizing Collaboration between Product and Engineering Teams

Accelerating Iterative Processes, Visualization, and Stakeholder Engagement

William Collins, CR 2023 – All Rights Reserved.  Publish date: 05/26/2023

Introduction:
Effective collaboration between product and engineering teams is the backbone of successful product development. With the advent of generative AI, this collaboration can reach new heights, enabling accelerated iteration, enhanced visualization, and deeper engagement with stakeholders and customers. In this article, we will explore how generative AI can revolutionize the way product and engineering teams work together, fostering innovation, efficiency, and customer-centricity.

Streamlining Iterative Processes:
Generative AI tools offer a transformative way to streamline iterative processes within product and engineering teams. By leveraging machine learning algorithms, these tools can analyze vast amounts of data, user feedback, and market trends to generate valuable insights and recommendations. Product managers can use generative AI to uncover patterns, identify user preferences, and refine product requirements with greater precision.

Through iterative discussions facilitated by generative AI, product managers and engineering teams can quickly iterate on design concepts, features, and functionality. Real-time collaboration platforms powered by generative AI allow for seamless communication and feedback exchange, enabling teams to iterate rapidly and make informed decisions throughout the product development lifecycle.

Rapid Prototyping and Visualization:
Generative AI tools provide powerful capabilities for rapid prototyping and visualization, enabling product and engineering teams to bring concepts to life swiftly. With the ability to generate visual representations of product features, interfaces, and user interactions, teams can better understand the proposed solutions and identify potential issues early on.

Using generative AI, product managers and engineering teams can create interactive prototypes that simulate user experiences, allowing stakeholders and customers to provide valuable feedback. These prototypes can be iteratively refined based on feedback, ensuring that the final product meets user expectations.

Enhanced Stakeholder and Customer Engagement:
Generative AI facilitates deeper engagement with stakeholders and customers throughout the product development process. By generating data-driven insights, product managers can present compelling arguments to stakeholders, backed by quantitative evidence. This empowers them to advocate for product decisions and secure buy-in from key stakeholders.

Furthermore, generative AI tools can help product managers capture and analyze user feedback at scale, enabling them to identify emerging trends, pain points, and areas for improvement. By integrating this feedback into the development cycle, product and engineering teams can enhance the user experience and ensure that the final product aligns with customer needs.

Conclusion:
Generative AI represents a paradigm shift in how product and engineering teams collaborate, iterate, and engage with stakeholders and customers. By harnessing the power of machine learning and data-driven insights, teams can streamline iterative processes, rapidly prototype and visualize solutions, and create stronger connections with stakeholders and customers.

The adoption of generative AI empowers product and engineering teams to drive innovation, make informed decisions, and deliver products that truly meet customer expectations. As the possibilities of generative AI continue to expand, the collaboration between product and engineering teams will become even more efficient, leading to groundbreaking products that shape the future.

""")
    st.write("Article: [IoT and Smart Dust](https://www.linkedin.com/pulse/internet-things-smart-dust-you-risk-william-collins-jr-/)")
    st.write("Article: [The Internet of Things and its Application by Industry](https://www.linkedin.com/pulse/internet-things-its-application-industry-william-collins-jr-/)")
    st.write("Article: [IoT Technologies and Communication Protocols - A Brief Overview and Reference](https://www.linkedin.com/pulse/iot-technologies-communication-protocols-brief-william-collins-jr-/)")
    st.write("Article: [The Internet of Things and the Wine Industry - From Vineyard to Market](https://www.linkedin.com/pulse/internet-things-wine-industry-william-collins-jr-/)")

def app_todos():
    """


    """

def contact_page():
    st.image('./images/tech_image_2.jpg', width=250)
    st.title("Contact Page")
    # st.image(f'./images/you_image.jpg', 'William Collins', width=100)
    download_resume()  # fn which downloads resume for the user
    st.write(f'Location: Austin, TX\n'
                       f' Email: [link](williamwcollinsjr@gmail.com)\n '
                       f' Phone: 940.503.8195\n'
                       f' LinkedIn: LinkedIn [link](linkedin.com/in/williamwcollins)\n'
                       f' Schedule a meeting on my calendar: [link](https://calendly.com/wwcjr/meeting)'
                       f' discord server: [link](discord.com/channels/1108234455010787330/1108234455614754870)'
                       f' This application: [link](https://wwcollins--technical-profile-main-rtehnf.streamlit.app)')

# Other functions
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

# Sidebar navigation
pages = {
    "Home": home_page,
    "About": about_page,
    "📃Resume": resume_page,
    "📖Questions Answered": questions_answered,
    "📃Technology Portfolio": project_page,
    "💡Innovation": innovation_page,
    "📖Core Beliefs": beliefs_page,
    "⚙ Utilities": utilities_page,
    "📑Articles": articles_page,
    "✍Contact": contact_page

}

# Streamlit app
def main():
    # st.image(f'./images/home_sidebar_img.jpg')

    st.sidebar.image(f'./images/you_image.jpg', 'William Collins', width=100)
    download_resume(loc='sidebar')
    st.sidebar.caption(f'Location: Austin, TX    '
               f'[Email]("mailto:williamwcollinsjr@gmail.com)    '
               f'Phone: 940.503.8195  '
               f' Schedule a meeting on my calendar: [link](https://calendly.com/wwcjr/meeting)'
               f'[LinkedIn](https://linkedin.com/in/williamwcollins)    '
               f'[Discord server](https://discord.com/channels/1108234455010787330/1108234455614754870)  '
               f'[Technical Profile](https://wwcollins-profile.streamlit.app)  ')

    # st.sidebar.title("Navigation")
    page = st.sidebar.radio(f"**Navigation**", tuple(pages.keys()))

    # Styles Modifications
    expander = """
    <style>
    ul.streamlit-expander {
        border: 0 !important;
    </style>
    """

    st.markdown(expander, unsafe_allow_html=True)

    # Execute the selected page function
    pages[page]()

    hide_streamlit_style = """
                <style>
                # MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if __name__ == "__main__":
    main()



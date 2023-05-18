# This is a sample Python script.
# This site: wwcollins-profile.streamlit.app

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

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
        """This profile site provides basic information about William and covers core beliefs with respect"
             " to **Leadership** and **Technology** as well as thoughts and efforts regarding **Innovation** and "
             "recent **Projects** William is and has been creating and fine tuning. Beyond understanding and implementing best of breed architecture and coding patterns, William 
             is focused on **architecting**, **integrating** and **building** out technologies related to **Generative 
             AI** as an extended platform across both engineering and non-engineering organizations.
        """
             )

def about_page():
    st.image(f'./images/tech_image_6.jpg', width=250)
    st.title("About")
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
    st.image('./images/tech_image_2.jpg', width=250)
    st.title("Resume")
    # st.write("You can reach us through the contact page.")

    # Resume rendered as Streamlit Component
    components.html(

        """
    <!DOCTYPE html>
    <html>
    <head>
    <title>William W. Collins, Jr.</title>
    </head>
    <body>
    <h1>William W. Collins, Jr.</h1>
    <p>Austin, TX 78717</p>
    <p>Email: <a href="mailto:williamwcollinsjr@gmail.com">williamwcollinsjr@gmail.com</a></p>
    <p>Mobile: 940-503-8195</p>
    <p>Mobile: 512-294-7573</p>
    <p>LinkedIn: <a href="http://www.linkedin.com/in/williamwcollins">http://www.linkedin.com/in/williamwcollins</a></p>

    <h2>Technology and Software Engineering Management</h2>
    <p>15+ years’ success leading global product, software/solutions development, and pre-sales engineering support teams.</p>
    <p>Management | Web App Development | APIs | Cloud | AI Machine Learning | IoT | Sales Engineering Support | Innovation</p>

    <h2>Summary</h2>
    <p>Strategic/Innovative thinker. Able to articulate vision - and effectively impart that vision to others. Hands-on, Transformational Leader with repeated success guiding global business strategy within both established and emerging organizations. Talent for managing and launching products and programs related to hardware, software, data, pre-sales, and service solutions. Expert presenter and business professional; able to forge solid relationships with strategic partners. Innovative manager skilled at building top-performing teams, analyzing technology and market trends; scaling and growing businesses. Also, excellence in Engineering Organization, Technical and Professional transformation, and maturation.</p>

    <p>Possesses a broad technology skillset but currently focused on leading edge technologies including Generative AI and associated technologies, modern SaaS Web App Development, API, microservices technologies and implementations, Kubernetes/Containerization, DevOPs/AI/MLOps, SRE, AI/Machine Learning/NLP/Computer Vision, IoT/Edge/FOG computing.</p>

    <p>Industry experience in Insurance/Banking, Manufacturing, Marketing/Digital Agency/MarTech, Legal, Manufacturing, FinTech and Automated Business Processing Industries and Applications including associated cloud service technologies and platforms: AWS, Azure, AWS, Oracle, GCP, Heroku, SaaS, PaaS, IaaS, and DaaS. Deep understanding of modern programming languages, platforms and Dev, DevOps, AI/MLOps, SRE, Observability, Tools/code including but not limited to Python, C#, Java, Node, React, Flask, Django, FastAPI, GraphQL, Kafka, Sonar Cloud, DataDog, TeamCity, Cypress, PyTest, Jest, CircleCI, Kubernetes, New Relic, Amazon CloudWatch. Experienced in state-of-the-art SDLC methodologies including converged DevOps/AI/MLOps, CI/CD, Scrum, and Agile, modern observability tooling e.g., Prometheus, OpenTelemetry, Grafana and physical deployments. Big data platform and pipelines.</p>

    <h2>Highlights of Expertise</h2>
    <ul>
      <li>Management: Global Technical Team Leadership (15+ years)</li>
      <li>Generative AI, Web App Development: SaaS Cloud and Hybrid solutions</li>
      <li>Software Development, Architecture and Platforms/Frameworks</li>
      <li>RESTful APIs /GraphQL/ Microservices</li>
      <li>Product, Program and Project Management</li>
      <li>SDLC/STLC - CI/CD, (Dev/ML) Ops, SRE, Kubernetes, Observability/Tooling, Test Automation</li>
      <li>AI/Machine Learning - Computer Vision/Object Detection/Classification/NLP

    </li>
      <li>IoT/Edge IoT programming, embedded AI/ML, Sensors/Actuators</li>
      <li>Technical Pre/Post-Sales Support</li>
    </ul>

    <h2>Career Experience</h2>
    <h3>Alkemie Technologies LLC (January 2023 to Current)</h3>
    <p>Delivery of integrated, Generative AI Solutions, SaaS Web App Products, APIs/microservices Systems Design and Architecture and Development for Insurance, Banking. Deliverables include AI/ML, Natural Language Processing (NLP), Computer Vision/Image Classification, Sentiment Analysis/Text Classification, Geolocation, and mapping, RESTful/GraphQL</p>
    <p>IT ENGINEERING CONSULTANT,</p>
    <ul>
      <li>Information Technology, Strategy, Operations consulting</li>
      <li>Design and Delivery of Customer Solutions focusing efforts across Dev, DevOps, SRE, AI including solutions for Generative AI integration for streamlined automation leverage of Generative AI as yet another tool to enable automation solutions for customers on at least 2 fronts: Rapid deployment and dynamically adjustable semi-customized Prompt Engineering driven apps and rapid integration of customer specific data (structured/unstructured) into Generative AI platforms to provide customer business specific insights.</li>
      <li>Delivery and Execution of initiatives addressing QA, SRE, DevOps and, AI/MLOps Model Maturation, Architectural improvements including leverage of Microservices, Front-end/Backend performance improvements, Focus on enhanced Security, Technology/Monitoring Maturation, and Innovation.</li>
    </ul>

    <h3>PFL.com</h3>
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

    <h3>Alkemie Technologies, LLC</h3>
    <p>Delivery of integrated, Generative AI Solutions, SaaS Web App Products, APIs/microservices Systems Design and Architecture and Development for Insurance, Banking, Digital Agency Web Applications. Deliverables include AI/ML, Natural Language Processing (NLP), Computer Vision/Image Classification, Sentiment Analysis/Text Classification, Geolocation, and mapping,

     RESTful/GraphQL Weather/Astronomy products and integrations, microservices. On-premise, Hybrid and Cloud-based Solutions. Also, development of AI-embedded IoT edge devices connected to cloud-based SaaS applications.</p>
    <p>VP of SOFTWARE ENGINEERING (August 2019 to April 2022)</p>
    <ul>
      <li>Design and Delivery of Customer Solutions focusing efforts across Dev, DevOps, SRE, AI including solutions for Generative AI integration for streamlined automation leverage of Generative AI as yet another tool to enable automation solutions for customers on at least 2 fronts: Rapid deployment and dynamically adjustable semi-customized Prompt Engineering driven apps and rapid integration of customer specific data (structured/unstructured) into Generative AI platforms to provide customer business specific insights.</li>
      <li>Delivery and Execution of initiatives addressing QA, SRE, DevOps and, AI/MLOps Model Maturation, Architectural improvements including leverage of Microservices, Front-end/Backend performance improvements, Focus on enhanced Security, Technology/Monitoring Maturation, and Innovation. Delivery of multi-tenant Geo application that includes custom algorithms, multiple real-time RESTful calls: geo-location, weather, astronomy, solunar data to perform predictive weather/tide/astronomical analysis. Solution supported by API product also delivered as additional monetized product.</li>
      <li>Development of Python/Flask and Node web applications and APIs, PHP Applications, Microservices for Windows, and Linux systems. Integration with MySQL, Postgres, Maria DB, Mongo DB, and other SQL/no-SQL Databases. Implementation of React/Hooks, Node API, Redis/Postgres/CouchDB (noSQL/JSON) Solutions, DevOps, and Infrastructure (primarily AWS, Azure, Heroku). SDLC, DevOps and Application Monitoring e.g., PyTest, Jest, CircleCI, New Relic, Amazon CloudWatch, DataDog, GitHub Security.</li>
    </ul>

    <h3>Oracle, Austin, Texas</h3>
    <p>Driving innovation with, and for customers looking to build in the Oracle Public Cloud - specifically Information Management, Predictive Analytics including supporting AI (Machine Learning, Image Capture and Classification), IoT and Chatbots. Also, building the next generation workforce at Oracle, and developing new capabilities with a focus on agility, scale and showing the 'art of the possible' with the Oracle Public Cloud.</p>
    <p>SENIOR DIRECTOR of CLOUD INNOVATION & SOLUTION ENGINEERING (June 2018 to August 2019)</p>
    <ul>
      <li>Scaled (by 1100%), Trained and Mentored Solution Architect team. Oversaw technical software development teams and off-site support service.</li>
      <li>Worked with Ops team to guide and help deliver and Automated Reporting process that improve time-to-delivery by approximately 800%.</li>
      <li>Improved relationships, process, and operational efficiency globally within Hub, Field/Internal sales, Oracle Consulting Group.</li>
    </ul>

    <h3>Retriever Services LLC, Austin, Texas</h3>
    <p>Provide senior-level leadership for Austin-based startup with full accountability for and direct management of technology initiatives: Software and Solution Development, Information Security, Enterprise Integration, and Data Center Virtualization.</p>
    <p>VP of ENGINEERING AND DEVELOPMENT (2016 to 2019)</p>
    <ul>
      <li>Direct all corporate operations encompassing multiple platforms and services including microcomputer based IoT sensor network/other solutions, SaaS applications, security appliances. Leverage of AWS Cloud. Python, Node, PHP, JavaScript, Bootstrap, JQuery and modern, relevant tools/platforms for development, deployment, and monitoring.</li>
      <li

    >Oversee technical software development teams and off-site support service.</li>
      <li>Create operational process and toolset for startup services and software development programs.</li>
      <li>Deliver Commercial Solutions for Classified (CSfC) architecture for Federal sales partners.</li>
      <li>Architect and Deliver Internet of Things (IoT) software and hardware solutions.</li>
    </ul>

    <h3>Dun and Bradstreet, Austin, TX</h3>
    <p>Established state-of-the art enterprise solutions. Oversaw platform architecture, demo development and pre-sales engineering support for Data as a Service (DaaS/REST API), SaaS, PaaS, e-commerce, advertising, and subscription products. Leverage of AWS Cloud, Java, Python, .Net, Node, MongoDB, Angular, React and relevant platforms/tools.</p>
    <p>SENIOR DIRECTOR, PLATFORM SOFTWARE DEVELOPMENT (2014 to 2016)</p>
    <ul>
      <li>Normalized programming languages and architectures to responsive front-end, modular OOP back-end architecture.</li>
      <li>Improved process documentation of use and test case automation.</li>
      <li>Implemented JIRA/KanBan, Confluence, Git, etc. and supplied overall process improvement.</li>
      <li>Decreased defects by 97%.</li>
      <li>Increased testing automation by 340%.</li>
      <li>Implemented common platform solutions for Search, Identity Management, Monitoring, Corporate Linkage, and other core technologies reducing cross-product redundancy and development complexity by at least 420%.</li>
    </ul>

    <h3>LaunchWorks, Boerne, Texas</h3>
    <p>Supported complex projects and client relationships in business intelligence and portal technologies.</p>
    <p>VP of SOFTWARE DEVELOPMENT (2013 to 2014)</p>
    <ul>
      <li>Managed both technical and sales staff of small startup.</li>
      <li>Migrated Java and .Net Business Intelligence products from non-modular to object oriented modular framework; delivered on premise, and cloud/SaaS-based embedded solutions.</li>
      <li>Implemented agile development process, unit/product/system test and code review.</li>
      <li>Reduced defect escapes by 117%.</li>
      <li>Improved customer satisfaction from 37% to 92% based on Net Promoter score.</li>
      <li>Increased company revenue by 212%.</li>
    </ul>

    <h3>Dell Inc., Austin, Texas (Total of 13 years in various roles), Round Rock, TX</h3>
    <p>Managed development, integration, testing, and pre-sales support for multiple hardware and software solutions.</p>
    <p>REGIONAL DIRECTOR, HW/SW SOLUTION DEVELOPMENT AND PRESALES SUPPORT (2009 to 2013)</p>
    <ul>
      <li>Startup of Dell Solution Global Solution Centers including the design, architecture, and simultaneous development/delivery of 20+ solutions across all Dell Industry verticals and contributing to $548M global revenue.</li>
      <li>Scaled and managed global team from inception to 60+ hardware engineers, software developers and solution architects and managers.</li>
      <li>Reduced time-to-market for twenty industry solutions by 52%, increased market share by 40% with corresponding revenue of $600 million.</li>
      <li>Launched six cutting-edge customer service facilities in Austin, Chicago, Washington DC, New York, California, Ireland, India, Brazil, and Mexico. Supported smaller Solution Centers in Panama, Chile, and Argentina.</li>
      <li>Implemented a customer engagement process which delivered over 1800 briefings, workshops and proofs-of-concept contributing

     to $200+ million in revenue.</li>
    </ul>

    <h3>ADDITIONAL EXPERIENCE (WHILE EMPLOYED BY DELL/EMC)</h3>
    <p>Director, Global Enterprise Solutions Development (2007 to 2009) Global Enterprise Solutions, Dell, Inc., Round Rock, Texas. Global Product architecture and delivery of ERP Oracle, PeopleSoft, Siebel products/solutions per customer specifications contributing to $100M Americas and $400M global revenue.</p>
    <p>Senior Development Manager Global Product Development and Managed Services (2006 to 2007) Dell, Inc., Round Rock, Texas. Delivery of twenty-three internal and customer facing Managed Services, Service Desk Capability products contributing $80M in Dell global revenue.</p>
    <p>Development Manager Global Product Development Group (2002 to 2006) Dell, Inc., Round Rock, Texas. Software Design, Development, and implementation of key software programs in Dell’s enterprise product group.</p>
    <p>Software Lead Global Product Group (2000 to 2002) Dell, Inc., Round Rock, Texas. Design and implementation of key hardware/software development programs in Dell’s enterprise product group.</p>

    <h2>Education & Credentials</h2>
    <p>University of California, Irvine, California</p>
    <p>BACHELOR OF SCIENCE – CHEMISTRY</p>
    <p>MINOR - BIOLOGY</p>
    <p>Professional Development: Continuous Study and Practice of: Management and Leadership. AI and leading-edge technologies. Global Distributed Management, Modern SDLC, DevOps, CI/CD, Scrum/Agile/Kanban. BPI (Six Sigma) Yellow Belt, Social Media Accreditation. Internet of Things (IoT) industry and development expertise leveraging SBCs, Python, Node and PHP programming. Big Data, Analytics, and AI/Machine Learning, Computer Vision/Detection/Classification and NLP).</p>
    <p>Technical/Management, Experience & Proficiencies: Generative AI. Cloud App Development; Oracle, AWS, Heroku, MS Azure, Google (GCP). DevOps, Docker, Kubernetes (AKS), IoT, Information Management, Advanced Analytics, Integrated Hardware/Software Server Solutions, Network and Storage solutions, Secure VDI, HIED ERP/LMS/LIMS Energy/SMARTGRID, Connected Classroom/Next Gen Learning, Mobile Video Evidence Management and Video Surveillance, VDI/Private Cloud, Digital Forensics, Mobile Clinical Computing, Big Data. Linux, Windows, SalesForce Integration, Waterfall and Agile development environments, Object Oriented Programming, RESTful Web Services, Microservices, Mapping, Geolocation, MERN Stack MongoDB, Express, React, Node.js, Flask/Python, Jupyter Notebook. React, PHP, Java, C++, C, .Net, AJAX, JavaScript, Bootstrap, and JQuery. Sensor Networks, Single Board Computers, automated testing tools and environments, JMeter, Junit, JIRA/Kanban, Confluence, SourceTree, VNC, Git, WAMP/LAMP, APIs, Microservices, Dynamically Scalable Systems (Cloud Elastic), Agile/Scrum/Kanban, AI/ML/Deep Learning, Neural Networks, Predictive Analytics (on-premise and cloud), Leverage of Data Science Libraries/Technologies, NumPy, Pandas, matplotlib/Seaborn, SciPy, Scikit-Learn, Scikit-image, Tensorflow, Keras, spaCy/NLTK, Gensim, Pydicom, MedPy, DLTK, MIRTK, SimpleTK, Pytorch, Keras, OpenCV. Testing and Monitoring tools: TestRail, SauceLabs, Confluent, Postman, Launch Darkly, Insomnia, Swagger,

     Jira, Confluence, Cucumber, Sonar Cloud, Jest (Unit Test), Selenium, C#/Python automation, Postman, Cypress</p>
    <p>Current Areas of Focused Study: Generative AI and the next generation of Software Development. Scalable, Sustainable Web App Development and RESTful API Development, HW/SW/Embedded Development, AI/ML/Deep Learning/Neural Networks; Image Classification, Computer Vision, Text Analysis (NLP), Algorithms; Cloud, Python/Flask/Django/FastAPI, Node, REST APIs, Microservices, DevOps, AI/MLOps.</p>

    <h2>Interests and Affiliations</h2>
    <ul>
      <li>Generative AI. Innovation, Technology, Cloud, Web App System Design, Architecture and Programming, APIs, Microservices, AI/ML/NLP, IoT.</li>
      <li>IoT Planet, Member, IoT Council, HIMMS, HIE Watch, CIO Network, Data and Text Analytics Professionals.</li>
      <li>Personal: Technology and Innovation, Avid Outdoorsman, Archery/Bow Hunting, Surfing, Fly Fishing/Fly Tying, Writing non-fiction/fiction.</li>
    </ul>

    """
        , height=10000)

    # html = f"""<html><head><title>Yearly Symbol Prices</title></head><frameset><frame src='{app_path}'></frameset></html>"""

    # st.components.iframe(html, width=None, height=None, scrolling=False)

    # embed streamlit docs in a streamlit app
    # components.iframe("https://docs.streamlit.io/en/latest")

    # embed streamlit docs in a streamlit app
    # components.iframe("https://docx-to-markdown.streamlit.app")

def beliefs_page():
    st.image('./images/tech_image_3.jpg', width=250)
    st.title("Core Beliefs")

    st.subheader("Leadership")
    components.html(
        """
        <p><strong>William W. Collins, Jr.</strong><br>
Austin, TX 78717<br>
Email: williamwcollinsjr@gmail.com<br>
Phone: 940-503-8195<br>
LinkedIn: <a href="http://www.linkedin.com/in/williamwcollins">http://www.linkedin.com/in/williamwcollins</a></p>

<h2>Technology and Software Engineering Executive Management</h2>
<p>15+ years’ success leading global product, software/solutions development, and pre-sales engineering support teams.</p>
<p>Management | Web App Development | APIs | Cloud | AI Machine Learning | IoT | Sales Engineering Support | Innovation</p>

<h2>On Leadership Principles</h2>

<p>Leadership Principles are not just a list of business objectives, but rather, they are foundational beliefs that are ingrained in how we operate in our daily lives. As a leader, it is important to start with the customer and obsess over their needs. Additionally, leaders must be owners who think long term and seek to innovate and automate wherever possible. They should always strive to simplify and streamline processes while also seeking insight from others to broaden their perspective.</p>

<p>Leaders must have strong judgment and seek out diverse perspectives, while still being able to learn and be curious. To truly succeed, leaders need to hire and develop exceptional talent while also raising the performance bar for their teams. They must insist on the highest standards and continuously think big to inspire results. Leaders must also have a bias for action and be frugal, seeking to do more with less.</p>

<p>It's important for leaders to build trust by listening attentively, speaking candidly, and treating others with respect. They should also dive deep into details, challenge decisions when necessary, and commit wholeheartedly once a decision is made.</p>

<p>Ultimately, leaders must focus on delivering results and strive to be the best possible employer. They should work to create a safe, productive, and diverse work environment while also being mindful of their impact on their local communities, the planet, and future generations. Leaders need to continually strive to do better and be better for their customers, employees, and partners.</p>
""", height=480
    )

    st.subheader("Technology")
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
 """, height=10000
    )

def project_page():
    st.image('./images/tech_image_4.jpg', width=250)
    st.title("Technical Projects and Demos")
    st.header("Projects and Demos.")
    # st.write("check out this [link](https://share.streamlit.io/mesmith027
    # /streamlit_webapps/main/MC_pi/streamlit_app.py)")
    st.write(f'-Generative AI: Automated Article Generation [link](https://summaries.streamlit.app)')
    st.write(f'-Demo: Streamlit Geodataframe and Plot of Weather Stations: [link](https://wwcollins-sl-noaa-weather-and-tides-plot-stations-pbwehq.streamlit.app)')
    st.write(f'-Demo: Generative AI Search with Context Awareness [link](genchat.streamlit.app)')
    st.caption(f'More coming soon...')

def innovation_page():
    st.image(f'./images/tech_image_innovation.jpg', width=250)
    st.title("Innovation")
    st.write("Innovative moments and thoughts on innovation.")

def utilities_page():
    st.image(f'./images/tech_image_innovation.jpg', width=250)
    st.title("Utilities")
    st.write("Useful utilities to manage your profile site...")
    st.write (f'Convert docx file to markdown: [link](https://docx-to-markdown.streamlit.app)')
    st.caption(f'Streamlit Deployment Options [link](https://discuss.streamlit.io/t/streamlit-deployment-guide-wiki/5099)')

def articles_page():
    st.image('./images/tech_image_5.jpg', width=250)
    st.title("Articles")
    st.write("List of current Articles and those in progress.")

def contact_page():
    st.image('./images/tech_image_2.jpg', width=250)
    st.title("Contact Page")
    st.write("You can reach us through the contact page.")


# Sidebar navigation
pages = {
    "Home": home_page,
    "About": about_page,
    "Resume": resume_page,
    "Innovation": innovation_page,
    "Core Beliefs": beliefs_page,
    "Projects/Demos": project_page,
    "Utilities": utilities_page,
    "Articles": articles_page,
    "Contact": contact_page

}

# Streamlit app
def main():
    # st.image(f'./images/home_sidebar_img.jpg')


    st.sidebar.image(f'./images/you_image.jpg', 'William Collins', width=100)

    st.sidebar.caption(f'Location: Austin, TX\n'
               f'Email: [link](williamwcollinsjr@gmail.com)\n'
               f'Phone: 940.503.8195\n'
               f'LinkedIn: LinkedIn [link](linkedin.com/in/williamwcollins)\n'
               f'discord server: [link](discord.com/channels/1108234455010787330/1108234455614754870)'
               f'This application: [link](https://wwcollins--technical-profile-main-rtehnf.streamlit.app)')

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", tuple(pages.keys()))

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



# This is a sample Python script.
# This site: wwcollins-profile.streamlit.app

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)

# Page functions
def home_page():
    st.image(f'./images/home_sidebar_img.jpg', width=250)
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

def beliefs_page():
    st.image('./images/tech_image_3.jpg', width=250)
    st.title("Core Beliefs")
    st.write("You can reach us through the contact page.")

def project_page():
    st.image('./images/tech_image_4.jpg', width=250)
    st.title("Technical Projects and Demos")
    st.write("Projects and Demos.")
    # st.write("check out this [link](https://share.streamlit.io/mesmith027
    # /streamlit_webapps/main/MC_pi/streamlit_app.py)")
    st.caption("Generative AI: Automated Article Generation [link](https://summaries.streamlit.app)")
    st.caption(f'Demo: Streamlit Geodataframe and Plot of Weather Stations')
    st.caption(f'Demo: Generative AI Search with Context Awareness [link](genchat.streamlit.app)')

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

    st.caption(f'This application: [link](https://wwcollins--technical-profile-main-rtehnf.streamlit.app)')

    st.sidebar.caption(f'Location: Austin, TX\n'
               f'Email: [link](williamwcollinsjr@gmail.com)\n'
               f'Phone: 940.503.8195\n'
               f'LinkedIn: LinkedIn [link](linkedin.com/in/williamwcollins)\n'
               f'discord server: [link](discord.com/channels/1108234455010787330/1108234455614754870)')

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



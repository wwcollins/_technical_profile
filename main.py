# This is a sample Python script.
# This site: wwcollins-profile.streamlit.app

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)

# Page functions
def home_page():

    st.columns(2,)
    st.image(f'./images/home_sidebar_img.jpg', width=250)
    st.title("Welcome")
    st.write(f"This profile site provides basic information about William and covers core beliefs with respect"
             " to **Leadership** and **Technology** as well as thoughts and efforts regarding **Innovation** and "
             "recent **Projects** William is and has been working on.")

def about_page():
    st.image(f'./images/tech_image_6.jpg', width=250)
    st.title("About")
    st.write(f'**William Collins** is a highly experienced executive with a proven track record in building and managing software engineering teams and delivering complex applications. He has worked with both VC-funded startups and large enterprises, and has expertise in AI platform development, cloud operations, and various coding languages. His skills include managing engineering processes, leading international teams, and translating product requirements into technical deliverables. William is an excellent communicator and has a strong focus on innovation and protecting intellectual property. He is well-suited for roles requiring leadership, technical expertise, and the ability to drive results.')

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



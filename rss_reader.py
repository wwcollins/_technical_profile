import os
import feedparser
import streamlit as st
import streamlit.components.v1 as components

import dotenv


hide_streamlit_style = """
<style>
ul.streamlit-expander {
    border: 0 !important;
}
div[data-testid="stToolbar"],
div[data-testid="stDecoration"],
div[data-testid="stStatusWidget"],
#MainMenu,
header,
footer {
    visibility: hidden;
    height: 0%;
    position: fixed;
}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# Function to fetch and parse the RSS feed
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
        st.write("---")

def check_url_xml(url):
    if url.endswith(".xml"):
        #display_rss_feed_xml(url)
        st.sidebar.error("xml type URL '.xml'. found")
        return True
    else:
        return False


# todo https://podcastindex.org
# todo research https://github.com/tbowers/python-podcastindex-org-lambda/blob/main/README.md
# todo https://podcastindex-org.github.io/docs-api/#overview--example-code

# Main function
def main():
    st.title("RSS Feed Reader")
    uploaded_files = st.file_uploader("Upload RSS feed files", accept_multiple_files=True)
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
                    if check_url_xml(url):
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

    feed_url = st.text_input("Enter RSS feed URL")
    st.sidebar.caption(f'Articles for {feed_url}')

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

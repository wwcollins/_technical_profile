import feedparser
import streamlit as st
import streamlit.components.v1 as components

hide_streamlit_style = """
                <style>
                ul.streamlit-expander {
                border: 0 !important;}
                
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


# Example usage
# input_string = "This is the first sentence. This is the second sentence. This is the third sentence. This is the fourth sentence."
# first_100, remaining = split_string(input_string)
# print("First 100 words:", first_100)
# print("Remaining sentences:", remaining)


# Function to display the parsed feed
def display_feed(feed):
    # st.write(f'{feed}')

    st.caption(f'{len(feed.entries)} feeds found...')
    i=1
    try:
        for entry in feed.entries:
            first_100, remaining = split_string(entry.content[0].value)
            st.subheader(f'Article {i}. {entry.title}')
            st.write(f'**:blue[URL:]** {entry.link}')
            # st.subheader(f'{i}. {first_100}')
            # st.markdown(f'{first_100}...', unsafe_allow_html=True)
            st.sidebar.caption(f'Article {i}. {entry.title} [link]({entry.link})')
            #     st.write(f'Streamlit Deployment Options [link](https://discuss.streamlit.io/t/streamlit-deployment-guide-wiki/5099)')

            # components.html(entry.content[0].value)  # Display the HTML content of the entry
            # st.write(f'{entry.content[0].value}')
            # only return the first sentence or 2 from content then more... for expander

            with st.expander(f'full report...'):
                html = f'{entry.content[0].value}'
                st.markdown(f'{html}', unsafe_allow_html=True)
                i+=1
            st.caption('---')
    except Exception as e:
        st.caption(f'Error: {e}')


# Main function
def main():
    st.title("RSS Feed Reader")
    # Enter the RSS feed URL
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

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import string

def analyze_word_frequency(text):
    # Tokenize the text and remove non-text characters
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word.isalpha()]

    # Remove common connecting words
    stop_words = set(stopwords.words("english"))
    tokens = [word for word in tokens if word not in stop_words]

    # Perform word frequency analysis
    freq_dist = FreqDist(tokens)
    total_words = len(tokens)

    # Create a dataframe with word, frequency count, and percent occurrence
    data = {'Word': [], 'Frequency': [], 'Percent Occurrence': []}

    for word, frequency in freq_dist.items():
        percent_occurrence = (frequency / total_words) * 100
        data['Word'].append(word)
        data['Frequency'].append(frequency)
        data['Percent Occurrence'].append(round(percent_occurrence, 2))

    df = pd.DataFrame(data)

    # Sort the dataframe by frequency count in descending order
    df = df.sort_values(by='Frequency', ascending=False)

    return df, set(df['Word'].head(10))

def highlight_keywords(text, keywords):
    highlighted_text = text
    for keyword in keywords:
        highlighted_text = highlighted_text.replace(keyword, f'<span style="color: blue;">{keyword}</span>')
    return highlighted_text

# Plotting function
def plot_word_frequency(df):
    top_10_df = df.head(10)

    fig, ax = plt.subplots()
    ax.bar(top_10_df['Word'], top_10_df['Frequency'])
    ax.set_xlabel('Word')
    ax.set_ylabel('Frequency')
    ax.set_title('Top 10 Word Frequency Analysis')
    plt.xticks(rotation=90)
    st.pyplot(fig)

# Streamlit app
def main():
    st.title("Word Frequency Analysis")

    # Choose between file upload or input text
    option = st.radio("Choose Input Option:", ("File Upload", "Enter Text"))

    if option == "File Upload":
        # File upload
        uploaded_file = st.file_uploader("Upload a file", type=["txt"])
        if uploaded_file is not None:
            text = uploaded_file.read().decode("utf-8")
    else:
        # Input text
        text = st.text_area("Enter some text")

    if st.button("Analyze"):
        # Perform word frequency analysis
        result_df, top_keywords = analyze_word_frequency(text)

        # Highlight top keywords in blue
        highlighted_text = highlight_keywords(text, top_keywords)

        # Display the resulting dataframe
        st.table(result_df)

        # Display the highlighted text
        st.markdown(f"<p style='color: black;'>{highlighted_text}</p>", unsafe_allow_html=True)

        # Plot the top 10 word frequency analysis
        plot_word_frequency(result_df)

# Run the Streamlit app
if __name__ == "__main__":
    main()
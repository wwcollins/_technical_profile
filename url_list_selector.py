import streamlit as st
import requests
from bs4 import BeautifulSoup
import random
import time

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 OPR/76.0.4017.123",
]


def generate_checkbox_list(urls):
    checkbox_list = []
    for url in urls:
        checkbox = st.checkbox(url)
        checkbox_list.append(checkbox)

        # Display summary below each URL
        summary = get_summary(url)  # Retrieve the summary using Beautiful Soup
        st.write(summary)

    return checkbox_list


def get_summary(url):
    delay = random.uniform(0.5, 1)  # Random delay between 0.5 and 1 second
    time.sleep(delay)

    user_agent = random.choice(USER_AGENTS)
    headers = {"User-Agent": user_agent}

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        text = soup.get_text().strip()
    except requests.RequestException:
        return "Error retrieving summary for {}".format(url)

    return "Summary for {}:\n{}".format(url, text[:200])  # Display first 200 characters of the text


def main():
    st.title("URL Checkbox List")

    # Example list of URLs
    urls = [
        "https://www.cognilytica.com/ai-today-podcast/",
        "https://www.allinpodcast.co/",
        "https://www.ailab.mit.edu/podcast"
    ]

    checkbox_list = generate_checkbox_list(urls)

    # You can access the checkbox values
    selected_urls = [url for url, checkbox in zip(urls, checkbox_list) if checkbox]
    st.write("Selected URLs:", selected_urls)


if __name__ == "__main__":
    main()

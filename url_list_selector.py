import streamlit as st


def generate_checkbox_list(urls):
    checkbox_list = []
    for url in urls:
        checkbox = st.checkbox(url)
        checkbox_list.append(checkbox)

        # Display summary below each URL
        summary = get_summary(url)  # Replace this with your own function to get summaries
        st.write(summary)

    return checkbox_list


def get_summary(url):
    # Replace this with your own function to get summaries
    # You can use libraries like Beautiful Soup or requests to fetch the URL content
    # and extract the summary
    return f"Summary for {url}"


def main():
    st.title("URL Checkbox List")

    # Example list of URLs
    urls = [
        "https://example.com/page1",
        "https://example.com/page2",
        "https://example.com/page3"
    ]

    checkbox_list = generate_checkbox_list(urls)

    # You can access the checkbox values
    selected_urls = [url for url, checkbox in zip(urls, checkbox_list) if checkbox]
    st.write("Selected URLs:", selected_urls)


if __name__ == "__main__":
    main()

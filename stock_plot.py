# pip install streamlit-extras
# https://blog.streamlit.io/discover-and-share-useful-bits-of-code-with-the-streamlit-extras-library/
from streamlit_extras.altex import line_chart, get_stocks_data

stocks = get_stocks_data()
line_chart(
    data=stocks.query("symbol == 'GOOG'"),  # data is a dataframe, applying .query
    x="date",
    y="price",
    title="G",
)
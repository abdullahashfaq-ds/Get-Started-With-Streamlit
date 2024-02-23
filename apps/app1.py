"""
Setting the page configurations.
Displaying titles, sidebars, headers, text, markdown, messages, dataframes, JSON, and code.
Utilizing spinners for asynchronous operations.
"""
import time
import datetime
import pandas as pd
import streamlit as st


# Setting the page configurations
st.set_page_config(
    page_title="My Streamlit App",
    page_icon=":chart_with_upwards_trend:"
)

# displaying a title
st.title("Welcome to Streamlit")

# displaying sidebar
st.sidebar.header("Sidebar")
st.sidebar.text("Lorem ipsum dolor sit amett.")

st.sidebar.date_input("Today's Date", datetime.datetime.now())
st.sidebar.time_input("Time Intervals", datetime.time())

# displaying a header and sub-header
st.header("This is a header")
st.subheader("This is a sub-header")

# displaying text
st.text("Text: Lorem ipsum dolor sit amet, consectetur adipiscing elit.")

# displaying markdown text
st.markdown("### Markdown Text")
st.markdown("**Markdown Strong Text**")

# displaying different flags
st.success("This is a success message.")
st.info("This is an information message.")
st.warning("This is a warning message.")
st.error("This is an error message.")
st.exception("NameError ('pd' is not defined)")

# displaying write
st.write("Here's a simple string.")
st.write("Function Result:", list(range(10, 15)))

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
st.write(df)

# displaying JSON data
st.write("JSON Data")
st.json(data)

# displaying code
st.write("Raw Code (Method 01)")
st.code("import numpy as np")

st.write("Raw Code (Method 02)")
with st.echo():
    import numpy as np
    import pandas as pd
    import streamlit as st

# displaying spinner
with st.spinner("Waiting..."):
    time.sleep(5)

st.success("Finished!")

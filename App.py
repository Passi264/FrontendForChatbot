
import streamlit as st

# CSS to create full-width containers and custom styles for the titles
st.markdown(
    """
    <style>
    .title-container {
        width: 100%;
        text-align: center;
        margin-top: 0;
    }

    .title-container h1 {
        font-size: 2.8rem;
        margin-bottom: 0.5rem;
    }

    .subtitle-container {
        width: 100%;
        text-align: center;
    }

    .subtitle-container h2 {
        font-size: 2.1rem;
        margin-bottom: 2rem;
    }

    iframe {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 450px;
        height: 500px;
        border: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# First container for the main title
st.markdown('<div class="title-container"><h1>Meet the Currency Converter: John Wick</h1></div>',
            unsafe_allow_html=True)

# Second container for the subtitle text
st.markdown('<div class="subtitle-container"><h2>Use it to convert currency in real time</h2></div>',
            unsafe_allow_html=True)

# Display the chatbot iframe
st.markdown("""
<iframe
allow="microphone;"
width="350"
height="430"
src="https://console.dialogflow.com/api-client/demo/embedded/26e691ee-8def-4a70-a4a9-01b0084ba3e1">
</iframe>
""", unsafe_allow_html=True)

unsafe_allow_html=True







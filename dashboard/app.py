import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/predict"  #FastAPI endpoint

st.set_page_config(page_title="AI-Powered Review Rating", page_icon="⭐", layout="centered")

st.title("Rating Customer Review using AI")
st.write("Type a review below and let the ML/AI model predict the rating (1–5 stars).")

with st.form("prediction_form"):
    text = st.text_area("Enter Review:", height=150, placeholder="Write a customer review here...")
    submitted = st.form_submit_button("Predict Rating")

    if submitted:
        if not text.strip():
            st.warning("Please enter some text.")
        else:
            try:
                response = requests.post(API_URL, json={"text": text})
                response.raise_for_status()
                result = response.json()
            except Exception as e:
                st.error(f"Error calling API: {e}")
            else:
                st.subheader("Prediction")
                st.markdown(f"**Stars:** {result['stars_text']}")
                #st.markdown(f"**Label ID:** `{result['label_id']}`  |  **Label Name:** `{result['label_name']}`")
                st.markdown(f"**Confidence:** `{result['confidence']:.3f}`")

                st.progress(min(result["confidence"], 1.0))

st.sidebar.header("Sample reviews")
if st.sidebar.button("Very positive"):
    st.session_state["review_example"] = "Rashedul is awesome; his video helped me a lot in completing my thesis."

if st.sidebar.button("Very negative"):
    st.session_state["review_example"] = "Terrible experience. I waited for hours, and nobody cared about my problem."

if st.sidebar.button("Mixed review"):
    st.session_state["review_example"] = "The service was okay. Not great, not terrible either. Room for improvement."

if "review_example" in st.session_state:
    st.info("Copy/paste the demo comment into the main area to test quickly.")
    st.code(st.session_state["review_example"], language="text")

import streamlit as st
import requests

st.set_page_config(
    page_title="AI Property Listing Analyzer",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 AI Property Listing Quality & SEO Analyzer")

st.write(
    "Paste a real estate listing below to analyze quality, SEO, missing information, and improvement suggestions."
)

listing_text = st.text_area(
    "Property Listing",
    height=200,
    placeholder="Example: 2 bed apartment in Dallas. Nice location. Contact now."
)

if st.button("Analyze Listing"):
    if not listing_text.strip():
        st.warning("Please enter a property listing.")
    else:
        with st.spinner("Analyzing listing..."):
            response = requests.post(
                "http://127.0.0.1:8000/analyze",
                json={"listing_text": listing_text}
            )

            if response.status_code == 200:
                result = response.json()

                st.subheader("Analysis Results")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric("Quality Score", result.get("quality_score", "N/A"))

                with col2:
                    st.metric("SEO Score", result.get("seo_score", "N/A"))

                st.subheader("Missing Information")
                missing = result.get("missing_fields", [])
                if missing:
                    for item in missing:
                        st.write(f"- {item}")
                else:
                    st.success("No major missing fields detected.")

                st.subheader("AI Explanation")
                explanation = result.get("explanation", [])
                if explanation:
                    for item in explanation:
                        st.write(f"- {item}")
                else:
                    st.write("No explanation provided.")

                st.subheader("Improved SEO-Friendly Listing")
                st.write(result.get("improved_listing", "No improved listing generated."))

            else:
                st.error("Something went wrong. Make sure FastAPI is running.")

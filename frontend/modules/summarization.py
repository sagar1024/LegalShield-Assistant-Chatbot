import streamlit as st
from utils.api import summarize_document

def render():
    """Render the Summarization/Review Page."""
    st.title("Document Review")
    st.markdown(
        """
        Upload your document to generate a concise review.
        Supported formats: **PDF**, **Word**, **Excel**, **PowerPoint**.
        """
    )

    uploaded_file = st.file_uploader("Upload a document", type=["pdf", "docx", "xlsx", "pptx"])

    if uploaded_file:
        st.info("File uploaded successfully!")

        # Customization options
        st.subheader("Customization Options")
        summary_length = st.slider("Select word limit", 10, 500, 100, step=10)
        focus_sections = st.text_input("Focus on specific sections (optional)", placeholder="e.g., Executive Summary, Conclusion")
        language = st.selectbox("Select language", ["English", "Spanish", "French", "German", "Others"])
        if language == "Others":
            language = st.text_input("Enter language")

        # Generate Summary Button
        if st.button("Generate Basic Review"):
            st.info("Generating...")

            #Call the backend API to generate the summary
            summary = summarize_document(
                document=uploaded_file,
                summary_length=summary_length,
                focus_sections=focus_sections,
                language=language
            )

            if summary and "summary" in summary:
                st.subheader("Generated Review of Document")
                st.write(summary["summary"])
            else:
                st.error("Failed to generate summary. Please try again.")
                
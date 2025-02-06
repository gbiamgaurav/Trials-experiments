import streamlit as st
import base64
from io import BytesIO
from PyPDF2 import PdfReader  # For reading PDFs

# Function to display PDF in the sidebar
def displayPDF_in_sidebar(file):
    # Convert the file to base64 string for embedding in the iframe
    base64_pdf = base64.b64encode(file.read()).decode('utf-8')
    
    # Embed PDF using iframe in HTML
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="400" type="application/pdf"></iframe>'
    
    # Display the PDF in the sidebar using markdown
    st.sidebar.markdown(pdf_display, unsafe_allow_html=True)

# Function to display images in the sidebar
def display_image_in_sidebar(file):
    # Display the image in the sidebar
    st.sidebar.image(file, use_container_width=True)

# Main app function
def main():
    st.title("Document Previewer")

    uploaded_file = st.file_uploader("Upload your PDF or Image file", type=['pdf', 'jpg', 'jpeg', 'png'])

    if uploaded_file is not None:
        # Convert the uploaded file to a BytesIO object (in-memory file)
        file = BytesIO(uploaded_file.read())
        
        # Check file type and display accordingly in the sidebar
        if uploaded_file.type == 'application/pdf':
            # Display PDF if it's a PDF file
            st.sidebar.info("PDF Preview")
            displayPDF_in_sidebar(file)
        elif uploaded_file.type.startswith('image/'):
            # Display image if it's an image file
            st.sidebar.info("Image Preview")
            display_image_in_sidebar(file)

# Ensure to run the app only if this file is the main module
if __name__ == "__main__":
    main()

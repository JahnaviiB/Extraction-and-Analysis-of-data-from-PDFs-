import streamlit as st
import random
from model import Model_CNN
# from bing_image_downloader import downloader
# '''
# - File upload
#     - upload button
#     - text
#
# - Prediction window
#     - category
#
# '''

st.title("PDF Extraction and Analysis")
st.markdown(
    "To process the PDF files"
)

uploaded_pdf_file = st.file_uploader(label='upload a PDF file',
                                       type='pdf',
                                       accept_multiple_files=False,
                                       key='pdf_file_uploader',
                                       help='upload a PDF file'
                                       )

# pdf model
# Model_CNN_obj = Model_CNN()

if uploaded_pdf_file:
    # pdf text extraction

    # pre processing
    # analysis by various factors
    # display text and charts
    pass

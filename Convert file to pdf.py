import streamlit as st
import pandas as pd
import pptx2pdf
import docx2pdf

st.title("***** Convert file to pdf *****")
st.write()

s1, s2 = st.columns(2)
a1, a2, a3 = st.columns(3)

all_file_name = []
with s1:
    convert_type = ["Select", "Word to PDF", "PowerPoint to PDF"]
    type_selected = st.selectbox("Select file's type you want to convert:", convert_type)
with s2:
    if type_selected == "Select":
        st.write("Please select file's type you want to convert")
    elif type_selected == "Word to PDF":
        uploaded_files = st.file_uploader("Upload file", type=["docx"], accept_multiple_files=True)
    elif type_selected == "PowerPoint to PDF":
        uploaded_files = st.file_uploader("Upload file", type=["pptx"], accept_multiple_files=True)

    if type_selected != "Select":
        for uploaded_file in uploaded_files:
            file_name = uploaded_file.name
            index_dau_cham = len(file_name)-file_name[::-1].index(".")
            all_file_name.append("D:/Downloads/" + file_name[: index_dau_cham] + "pdf")
st.write(all_file_name)

with a2:
    clicked = st.button("Convert to PDF")
    if clicked:
        # if convert_type == "Word to PDF":
        #     for i in range(len(uploaded_files)):
        #         docx2pdf.convert(uploaded_files[i], all_file_name[i])
        # else:
        for i in range(len(uploaded_files)):
            pptx2pdf.convert(uploaded_files[i], all_file_name[i])

if clicked:
    st.write("The converted files has been stored in your D:/Downloads folder")


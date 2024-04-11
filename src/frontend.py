import streamlit as st

class ExcelValidorUI:

    def __init__(self):
        self.set_page_config()

    def set_page_config(self):
        st.set_page_config(
            page_title="Excel schema validator")
    
    def display_header(self):
        st.title("Excel schema validator")

    def upload_file(self):
        return st.file_uploader("Upload your Excel file here", type=["xlsx"])
    
    def display_results(self, result, error):
        if error:
            st.error(f"Erro na validação: {error}")
        else:
            st.success("O schema do arquivo Excel está correto!")

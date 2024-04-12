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
            st.error(f"Validation error: {error}")
        else:
            st.success("The Excel file schema is correct!")

    def display_save_button(self):
        return st.button("Save to database")
    
    def display_wrong_message(self):
        return st.error("The spreadsheet needs to be corrected!")
    
    def display_sucess_message(self):
        return st.success("Data successfully saved in the database!")
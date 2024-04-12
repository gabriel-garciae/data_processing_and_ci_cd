from frontend import ExcelValidorUI
from backend import process_excel, excel_to_sql

def main():
    ui = ExcelValidorUI()
    ui.display_header()

    upload_file = ui.upload_file()

    if upload_file:
        df, result, error = process_excel(upload_file)
        ui.display_results(result, error)

        if error:
            ui.display_wrong_message()
        elif ui.display_save_button():
            excel_to_sql(df)
            ui.display_sucess_message()


if __name__ == "__main__":
    main()
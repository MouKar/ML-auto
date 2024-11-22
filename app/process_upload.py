
def process_upload(file_csv):
    
    with st.form("my_form"):
        uploaded_file = st.file_uploader("Choose a CSV file")
        submitted=st.form_submit_button()

import unittest
import io
import pandas as pd
# from app.test_m import process_upload  # Assuming process_uploaded_file is your processing function

class TestFileUpload(unittest.TestCase):
    def test_valid_file_upload(self):
        # Create a mock CSV file
        valid_csv = io.StringIO("MedInc,HouseAge,AveRooms,AveBedrms,Population,AveOccup,Latitude,Longitude,Target\n11.6812,25,4.192200557,1.022284123,1392,3.877437326,36.06,-119.01,0.477")
        valid_csv.name = "housing.csv"
        
        # Simulate reading the file
        uploaded_file = st.file_uploader(valid_csv)
        submitted=st.form_submit_button()
        df = uploaded_file
        
        # Check if the file is processed correctly
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (1, 9))  # Two rows, three columns

    def test_invalid_file_upload(self):
        # Simulate invalid file upload
        invalid_file = io.StringIO("This is not a CSV")
        invalid_file.name = "invalid.txt"
        
        with self.assertRaises(ValueError):  # Assume your function raises ValueError for invalid files
            process_upload(invalid_file)

if __name__ == "__main__":
    unittest.main()

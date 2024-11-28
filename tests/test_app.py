import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import io
from src.app import process_upload

class TestFileUpload(unittest.TestCase):

    def test_valid_file_upload(self):
        # Simulate a valid CSV file upload using StringIO
        valid_csv = io.StringIO("MedInc,HouseAge,AveRooms,AveBedrms,Population,AveOccup,Latitude,Longitude,Target\n11.6812,25,4.192200557,1.022284123,1392,3.877437326,36.06,-119.01,0.477")
        valid_csv.name = "housing.csv"
        
        # Call the function directly without Streamlit interaction
        mse, shape = process_upload(valid_csv)
        
        # Check the output from the function
        self.assertEqual(mse, 0.0)  # Expecting MSE close to 0 for a valid example
        self.assertEqual(shape, (1, 9))  # One row, nine columns (including Target)

    def test_invalid_file_upload(self):
        # Simulate invalid file upload (non-CSV content)
        invalid_file = io.StringIO("This is not a CSV")
        invalid_file.name = "invalid.txt"
        
        # Expecting ValueError because the content is invalid for CSV processing
        with self.assertRaises(ValueError):
            process_upload(invalid_file)

if __name__ == "__main__":
    unittest.main()

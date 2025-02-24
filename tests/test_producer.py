import unittest
import requests
from unittest.mock import patch

API_URL = "http://localhost:8000/enqueue/"

class TestProducer(unittest.TestCase):
    @patch("requests.post")
    def test_producer_api_call(self, mock_post):
        """Test if producer successfully calls the API."""
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"message": "Job enqueued", "job_id": "test_123"}

        response = requests.post(API_URL, json={"job_data": "Test job"})
        
        self.assertEqual(response.status_code, 200)
        self.assertIn("job_id", response.json())

if __name__ == "__main__":
    unittest.main()

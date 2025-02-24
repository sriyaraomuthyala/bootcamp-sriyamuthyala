import unittest
import requests
from unittest.mock import patch

DEQUEUE_URL = "http://localhost:8000/dequeue/"
MARK_DONE_URL = "http://localhost:8000/mark_done/"


class TestConsumer(unittest.TestCase):
    @patch("requests.get")
    def test_consumer_dequeue(self, mock_get):
        """Test if consumer successfully retrieves a job."""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"job_id": "test_123", "job_data": "Test job"}

        response = requests.get(DEQUEUE_URL)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn("job_id", response.json())

    @patch("requests.post")
    def test_consumer_mark_done(self, mock_post):
        """Test if consumer successfully marks a job as done."""
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"message": "Job test_123 marked as done"}

        response = requests.post(f"{MARK_DONE_URL}test_123")
        
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())

if __name__ == "__main__":
    unittest.main()

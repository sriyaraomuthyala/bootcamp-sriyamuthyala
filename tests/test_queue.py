import unittest
from persistent_queue.persistent_queue import PersistentQSQLite

class TestQueue(unittest.TestCase):
    def setUp(self):
        """Set up a fresh queue for each test."""
        self.queue = PersistentQSQLite()

    def test_enqueue(self):
        """Test that a job is added to the queue."""
        job_id = "test_123"
        self.queue.enqueue(job_id, "Test job data")
        job = self.queue.dequeue()
        self.assertIsNotNone(job)
        self.assertEqual(job[0], job_id)

    def test_dequeue(self):
        """Test that a job can be dequeued."""
        job_id = "test_456"
        self.queue.enqueue(job_id, "Test job data")
        job = self.queue.dequeue()
        self.assertEqual(job[0], job_id)

    def test_mark_done(self):
        """Test that a job can be marked as done."""
        job_id = "test_789"
        self.queue.enqueue(job_id, "Test job data")
        self.queue.mark_done(job_id)
        job = self.queue.dequeue()
        self.assertIsNone(job)

if __name__ == "__main__":
    unittest.main()

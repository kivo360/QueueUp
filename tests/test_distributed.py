import unittest
import uuid
from queueup import Queue


class DistributedQueueTest(unittest.TestCase):
    def setUp(self):
        new_active = uuid.uuid4().hex
        self.queue = Queue(url="redis://", queue_name=new_active)

    def tearDown(self):
        self.queue.close()


    def test_one_queue(self):
        self.queue.put(1)
        size = len(self.queue)
        self.assertEqual(1, size)

    def test_not_one_queue(self):
        self.queue.put(1)
        self.queue.put(1)
        size = len(self.queue)
        self.assertIsNot(1, size)

    def test_is_zero(self):
        self.queue.put(1)
        self.queue.put(1)
        so = self.queue.qsize()
        print(so)
        size = len(self.queue)
        self.assertIsNot(1, size)

if __name__ == "__main__":
    unittest.main()

    
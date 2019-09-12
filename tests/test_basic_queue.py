import unittest

from queueup import Queue


class BasicQueueTest(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

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


if __name__ == "__main__":
    unittest.main()

    
import unittest


class ExampleTest(unittest.TestCase):

    def test_an_example(self):
        foo = 'bar'
        self.assertEqual('bar', foo)
import unittest
from unittest.mock import MagicMock, patch

import Foo

class TestMockMethod(unittest.TestCase):

    # replace the mothed you want to mock
    def test_under_the_hood(self):
        Foo.foo = MagicMock()
        Foo.foo.return_value = "bar"
        self.assertEqual(Foo.bar(), "bar")

    # patch with `return_value`
    @patch('Foo.foo')
    def test_return_value(self, mock_foo):
        mock_foo.return_value = "bar"
        self.assertEqual(mock_foo(), "bar")
    
    # patch with `side_effect`
    # Using patch to return different values on successive calls
    def test_side_effect(self):
        with patch('Foo.foo') as mock_foo:
            mock_foo.side_effect = [1, 2]

            result_1 = mock_foo()  # First call, returns 1
            result_2 = mock_foo()  # Second call, returns 2
            self.assertEqual(result_1, 1)
            self.assertEqual(result_2, 2)

# reference https://www.pythontutorial.net/python-unit-testing/python-patch/
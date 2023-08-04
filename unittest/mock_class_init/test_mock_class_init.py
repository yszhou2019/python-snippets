from unittest import TestCase
from unittest.mock import patch

import patched_class

class TestMockClassInit(TestCase):

    @patch("patched_class.Foo.__init__")
    def test_patched_init(self, mock_init):
        mock_init.return_value = None # mock init do nothing
        foo = patched_class.Foo()

        self.assertFalse(hasattr(foo, 'value'))

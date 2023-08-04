from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch

import patched_class

class TestMockClassMethod(TestCase):

    def test_magic_mock_foo(self):
        mock_foo = MagicMock()
        mock_foo.return_value = "bar"
        patched_class.Foo.foo = mock_foo
        
        foo = patched_class.Foo()
        self.assertEqual(foo.foo(), "bar")
    
    def test_magic_mock_bar(self):
        mock_bar = MagicMock()
        mock_bar.return_value = "foo"
        patched_class.Foo.bar = mock_bar
        
        foo = patched_class.Foo()
        self.assertEqual(foo.bar(), "foo")
    
    @patch('patched_class.Foo.foo')
    def test_patch_decorator_foo(self, mock_foo):
        mock_foo.return_value = "bar"
        foo = patched_class.Foo()
        self.assertEqual(foo.foo(), "bar")
    
    @patch('patched_class.Foo.bar')
    def test_patch_decorator_bar(self, mock_bar):
        mock_bar.return_value = "foo"
        foo = patched_class.Foo()
        self.assertEqual(foo.bar(), "foo")
    
    def test_patch_context_manager_foo(self):
        with patch('patched_class.Foo.foo') as mock_foo:
            mock_foo.return_value = "bar"
            foo = patched_class.Foo()
            self.assertEqual(foo.foo(), "bar")
    
    def test_patch_context_manager_bar(self):
        with patch('patched_class.Foo.bar') as mock_bar:
            mock_bar.return_value = "foo"
            foo = patched_class.Foo()
            self.assertEqual(foo.bar(), "foo")

import unittest
from unittest.mock import MagicMock, Mock, patch

import requests
from Requests import get_holidays

class TestMockRequests(unittest.TestCase):

    def test_under_the_hood(self):
        mock_get = MagicMock()
        mock_get.side_effect = requests.exceptions.Timeout
        requests.get = mock_get

        # first call
        with self.assertRaises(requests.exceptions.Timeout):
            get_holidays()

    @patch('requests.get')
    def test_patch_decorator(self, mock_get):
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            '12/25': 'Christmas',
            '7/4': 'Independence Day',
        }
        mock_get.side_effect = [requests.exceptions.Timeout, response_mock]

        # first call
        with self.assertRaises(requests.exceptions.Timeout):
            get_holidays()
        # second call
        self.assertEqual(get_holidays()['12/25'], 'Christmas')
        self.assertEqual(requests.get.call_count, 2)

    def test_patch_context_manager(self):
        with patch('requests.get') as mock_get:
            response_mock = Mock()
            response_mock.status_code = 200
            response_mock.json.return_value = {
                '12/25': 'Christmas',
                '7/4': 'Independence Day',
            }
            mock_get.side_effect = [requests.exceptions.Timeout, response_mock]

            # first call
            with self.assertRaises(requests.exceptions.Timeout):
                get_holidays()
            # second call
            self.assertEqual(get_holidays()['12/25'], 'Christmas')
            self.assertEqual(requests.get.call_count, 2)

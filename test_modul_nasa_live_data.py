import unittest
from unittest.mock import patch, MagicMock
from modul_nasa_live_data import NasaHorizonsAPI, Modul_Nasa_Live_Data

class TestNasaLiveDataModule(unittest.TestCase):

    @patch('modul_nasa_live_data.requests.get')
    def test_fetch_distance_au_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        # Mock NASA API text response structure
        mock_response.text = (
            "$$SOE\n"
            "2026-Oct-28 00:00, 1.234, 0.0025\n"
            "$$EOE\n"
        )
        mock_get.return_value = mock_response

        distance = NasaHorizonsAPI.fetch_distance_au('301')
        self.assertEqual(distance, 0.0025)

    @patch('modul_nasa_live_data.requests.get')
    def test_fetch_distance_au_api_error(self, mock_get):
        mock_get.side_effect = Exception("API connection error")
        distance = NasaHorizonsAPI.fetch_distance_au('301')
        self.assertIsNone(distance)

    @patch('modul_nasa_live_data.requests.get')
    def test_fetch_distance_au_no_data(self, mock_get):
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        # No $$SOE or $$EOE
        mock_response.text = "Some random text response"
        mock_get.return_value = mock_response

        distance = NasaHorizonsAPI.fetch_distance_au('301')
        self.assertIsNone(distance)

    @patch('modul_nasa_live_data.NasaHorizonsAPI.fetch_distance_au')
    def test_modul_nasa_live_data_analiz(self, mock_fetch):
        mock_fetch.side_effect = [0.002426507, 0.99] # Mock returning 0.002426507 AU for Moon and 0.99 AU for Sun

        mock_const = MagicMock()
        mock_const.EARTH_SUN_DIST = 149600000

        mock_colors = MagicMock()
        mock_colors.HEADER = ""
        mock_colors.CYAN = ""
        mock_colors.ENDC = ""
        mock_colors.GREEN = ""
        mock_colors.WARNING = ""
        mock_colors.FAIL = ""
        mock_colors.GOLD = ""

        modul = Modul_Nasa_Live_Data(mock_const, mock_colors)

        # We just want to make sure it runs without exceptions
        try:
            modul.analiz()
            success = True
        except Exception as e:
            success = False

        self.assertTrue(success)

if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import Mock, patch
import weather_service


class TestWeatherService(unittest.TestCase):
    def test_get_weather_success(self):
        mock_data = {"city": "London", "temperature": 25, "condition": "sunny", "humidity": 60}
        with patch("weather_service.api_client.fetch_weather_data", return_value=mock_data):
            result = weather_service.get_weather("London")
            self.assertEqual(result["city"], "London")
            self.assertEqual(result["temperature"], 25)

    def test_get_weather_api_error(self):
        with patch("weather_service.api_client.fetch_weather_data", side_effect=ConnectionError("API down")):
            with self.assertRaises(ConnectionError):
                weather_service.get_weather("London")

    def test_get_weather_timeout(self):
        with patch("weather_service.api_client.fetch_weather_data", side_effect=TimeoutError("Request timed out")):
            with self.assertRaises(TimeoutError):
                weather_service.get_weather("London")

    @patch("weather_service.api_client.fetch_forecast")
    def test_get_forecast_with_patch(self, mock_fetch):
        mock_fetch.return_value = [
            {"day": 1, "temperature": 20, "condition": "sunny"},
            {"day": 2, "temperature": 22, "condition": "cloudy"},
        ]
        result = weather_service.get_forecast("Paris", days=2)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["temperature"], 20)
        mock_fetch.assert_called_once_with("Paris", 2)

    @patch("weather_service.api_client.get_current_hour", return_value=9)
    def test_greeting_morning(self, mock_hour):
        greeting = weather_service.get_greeting_based_on_time()
        self.assertEqual(greeting, "Good morning")

    @patch("weather_service.api_client.get_current_hour", return_value=14)
    def test_greeting_afternoon(self, mock_hour):
        greeting = weather_service.get_greeting_based_on_time()
        self.assertEqual(greeting, "Good afternoon")


if __name__ == "__main__":
    unittest.main()

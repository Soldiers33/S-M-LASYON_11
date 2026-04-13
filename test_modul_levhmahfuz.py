import sys
from unittest.mock import MagicMock
import unittest
from datetime import date, datetime, timedelta

# Mock dependencies to avoid ModuleNotFoundError when importing simulasyon_11
sys.modules['pandas'] = MagicMock()
sys.modules['numpy'] = MagicMock()
sys.modules['scipy'] = MagicMock()
sys.modules['scipy.stats'] = MagicMock()

# Import the module under test
try:
    from simulasyon_11 import Modul_LevhMahfuzTarama
except ImportError:
    sys.path.append('.')
    from simulasyon_11 import Modul_LevhMahfuzTarama

class TestModulLevhMahfuzTarama(unittest.TestCase):
    def setUp(self):
        self.modul = Modul_LevhMahfuzTarama()

    def test_calculate_shift_date_zero_shift(self):
        """Test that a shift of 0 years returns the original date."""
        target_date = date(2023, 1, 1)
        result = self.modul.calculate_shift_date(target_date, 0)
        self.assertEqual(result, target_date)

    def test_calculate_shift_date_positive_one_year(self):
        """Test a positive shift of 1 year.

        Formula: target_date - timedelta(days=1 * 365.2422)
        timedelta(days=365.2422) creates a timedelta of 365 days, 5 hours, 48 minutes.

        CRITICAL NOTE:
        When subtracting a timedelta from a standard Python `date` object (not `datetime`),
        the fractional day/time component of the timedelta is ignored/truncated by the `date` class arithmetic.
        It effectively subtracts `timedelta.days` (365).

        This behavior is verified by Python's `datetime` module documentation and experimentation.
        If `datetime` objects were used, the time component would be adjusted correctly.
        """
        target_date = date(2023, 1, 1)
        result = self.modul.calculate_shift_date(target_date, 1)

        # Expected: 2023-01-01 - 365 days = 2022-01-01
        # The 0.2422 days (5.8 hours) are ignored by date subtraction.
        expected = target_date - timedelta(days=365)
        self.assertEqual(result, expected)

    def test_calculate_shift_date_negative_one_year(self):
        """Test a negative shift of 1 year.

        Formula: target_date - timedelta(days=-1 * 365.2422)
        timedelta(days=-365.2422) normalizes to days=-366 and seconds=65954.

        When subtracting from a `date` object, only `timedelta.days` (-366) is considered.
        target_date - (-366 days) = target_date + 366 days.
        """
        target_date = date(2023, 1, 1)
        result = self.modul.calculate_shift_date(target_date, -1)

        # Expected: 2023-01-01 + 366 days = 2024-01-02
        expected = target_date + timedelta(days=366)
        self.assertEqual(result, expected)

    def test_calculate_shift_date_fractional_positive(self):
        """Test fractional positive shift (0.5 years).
        0.5 * 365.2422 = 182.6211
        timedelta(days=182.6211) -> days=182, seconds=...
        date subtraction uses days=182.
        """
        target_date = date(2023, 1, 1)
        result = self.modul.calculate_shift_date(target_date, 0.5)
        expected = target_date - timedelta(days=182)
        self.assertEqual(result, expected)

    def test_calculate_shift_date_fractional_negative(self):
        """Test fractional negative shift (-0.5 years).
        -0.5 * 365.2422 = -182.6211
        timedelta(days=-182.6211) -> days=-183, seconds=...
        date subtraction uses days=-183.
        """
        target_date = date(2023, 1, 1)
        result = self.modul.calculate_shift_date(target_date, -0.5)
        expected = target_date + timedelta(days=183)
        self.assertEqual(result, expected)

    def test_calculate_shift_date_with_datetime(self):
        """Test with datetime object to verify time precision is preserved.
        Unlike 'date', 'datetime' operations respect the full resolution of timedelta.
        """
        target_dt = datetime(2023, 1, 1, 12, 0, 0)
        shift = 1

        result = self.modul.calculate_shift_date(target_dt, shift)

        # Calculate manually with full precision
        shift_days = 1 * 365.2422
        expected = target_dt - timedelta(days=shift_days)

        self.assertEqual(result, expected)
        # Verify the time component has changed due to the fractional day subtraction
        self.assertNotEqual(result.time(), target_dt.time())

if __name__ == '__main__':
    unittest.main()

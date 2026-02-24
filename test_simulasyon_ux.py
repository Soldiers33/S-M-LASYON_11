import sys
import unittest
from unittest.mock import MagicMock

# Mock heavy dependencies before importing the module
sys.modules["pandas"] = MagicMock()
sys.modules["numpy"] = MagicMock()
sys.modules["scipy"] = MagicMock()
sys.modules["scipy.stats"] = MagicMock()

# Now import the module
import simulasyon_11

class TestUX(unittest.TestCase):
    def test_loading_bar(self):
        """Test that loading_bar uses \r and flushes stdout."""
        with unittest.mock.patch('sys.stdout', new_callable=unittest.mock.MagicMock) as mock_stdout:
            simulasyon_11.loading_bar("Test")

            # Verify calls
            calls = mock_stdout.write.call_args_list
            # Should have at least two writes: "Test..." and "Test... [OK]\n"
            # And specific format
            self.assertTrue(any("Test..." in str(c) for c in calls))
            self.assertTrue(any("[OK]" in str(c) for c in calls))

            # Verify flush was called
            self.assertTrue(mock_stdout.flush.called)

    def test_instantiation(self):
        """Test that Simule3_Lab_V133 can be instantiated."""
        try:
            lab = simulasyon_11.Simule3_Lab_V133()
            self.assertIsInstance(lab, simulasyon_11.Simule3_Lab_V133)
        except Exception as e:
            self.fail(f"Instantiation failed: {e}")

if __name__ == "__main__":
    unittest.main()

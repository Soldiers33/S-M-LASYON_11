import unittest
import sys
from unittest.mock import MagicMock

# --- MOCKING DEPENDENCIES BEFORE IMPORT ---
# Mock pandas
mock_pd = MagicMock()
mock_pd.set_option = MagicMock()
sys.modules['pandas'] = mock_pd

# Mock numpy
mock_np = MagicMock()
# Configure numpy mocks to return usable values
mock_np.array.side_effect = lambda *args, **kwargs: args[0] if args else [] # pass through lists
# corrcoef needs to return a matrix where [0,1] is a float
# We can mock the return value to be a list of lists or a mock that supports indexing
mock_corr_matrix = MagicMock()
mock_corr_matrix.__getitem__.return_value = 0.99 # access to [0,1] returns 0.99 directly?
# No, matrix[0,1] is usually matrix[0][1] or __getitem__((0,1)) depending on numpy version/usage.
# In numpy, m[0,1] calls __getitem__ with tuple (0,1).
mock_corr_matrix.__getitem__.side_effect = lambda idx: 0.99 if isinstance(idx, tuple) else [0.99, 0.99]

mock_np.corrcoef.return_value = mock_corr_matrix
mock_np.abs.side_effect = abs # Use python's abs
mock_np.log.side_effect = lambda x: 1.0 # return dummy float
mock_np.sqrt.side_effect = lambda x: 1.0 # return dummy float

sys.modules['numpy'] = mock_np

# Mock scipy and scipy.stats
mock_scipy = MagicMock()
mock_stats = MagicMock()
mock_scipy.stats = mock_stats
# pearsonr returns (correlation, p-value)
mock_stats.pearsonr.return_value = (0.99, 0.001)
# ttest_1samp returns (statistic, pvalue)
mock_stats.ttest_1samp.return_value = (1.5, 0.05)
sys.modules['scipy'] = mock_scipy
sys.modules['scipy.stats'] = mock_stats

# Now import the module under test
try:
    import simulasyon_11
except ImportError as e:
    # If import fails due to other missing deps, fail the test setup
    print(f"Failed to import simulasyon_11: {e}")
    sys.exit(1)

class TestSimulasyon(unittest.TestCase):

    def setUp(self):
        # Create a mock for constants to pass to modules
        self.mock_const = MagicMock()
        self.mock_const.R11 = 11111111111
        # Set other constants that might be needed
        self.mock_const.OP_LEN = 1.0
        self.mock_const.OP_TIME = 1.0
        self.mock_const.OP_LIGHT = 1.0
        self.mock_const.OP_ANGLE = 1.0

    def test_constants_r11(self):
        """Test that the main constant R11 is correct."""
        self.assertEqual(simulasyon_11.Simule3_Constants.R11, 11111111111)

    def test_module_time_packets_v130(self):
        """Test Modul_Time_Packets_V130 initialization and analiz method."""
        module = simulasyon_11.Modul_Time_Packets_V130(self.mock_const)
        self.assertIsInstance(module, simulasyon_11.Modul_Time_Packets_V130)

        # Test analiz method
        try:
            module.analiz()
        except Exception as e:
            self.fail(f"Modul_Time_Packets_V130.analiz() raised {e}")

    def test_simule3_lab_v133_init(self):
        """Test initialization of the main lab class."""
        try:
            lab = simulasyon_11.Simule3_Lab_V133()
            self.assertIsInstance(lab, simulasyon_11.Simule3_Lab_V133)
        except Exception as e:
            self.fail(f"Simule3_Lab_V133 initialization raised {e}")

    def test_simule3_lab_v133_run_all(self):
        """Test run_all method execution with mocked print."""
        lab = simulasyon_11.Simule3_Lab_V133()

        # We need to ensure that the mocked methods return values that don't crash format strings
        # We've set up numpy/scipy mocks globally, but if individual modules do specific things
        # we might need more detailed mocks.
        # For this high-level test, we rely on the global mocks.

        with unittest.mock.patch('builtins.print') as mock_print:
            # We also mock input just in case there are any prompts (though unlikely in a simulation script)
            with unittest.mock.patch('builtins.input', return_value=''):
                 try:
                    lab.run_all()
                 except Exception as e:
                    self.fail(f"Simule3_Lab_V133.run_all() raised {e}")

            # Verify that print was called
            self.assertTrue(mock_print.called)

if __name__ == '__main__':
    unittest.main()

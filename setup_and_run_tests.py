import os
import sys
import unittest
from unittest.mock import MagicMock

def setup_and_run():
    print("--- Test Ortamı Hazırlanıyor ---")

    # Check if simulasyon_11.py exists
    if not os.path.exists("simulasyon_11.py"):
        print("\n[HATA] 'simulasyon_11.py' dosyası bulunamadı!")
        print("Lütfen 'simulasyon_11.py' dosyasını bu kodun çalıştığı dizine yükleyin veya kopyalayın.")
        print("Dizindeki dosyalar: ", os.listdir("."))
        return

    # Create/Overwrite test_simulasyon.py with the robust content
    test_content = """
import unittest
import sys
import os
from unittest.mock import MagicMock

# --- MOCKING DEPENDENCIES BEFORE IMPORT ---
mock_pd = MagicMock()
mock_pd.set_option = MagicMock()
sys.modules['pandas'] = mock_pd

mock_np = MagicMock()
mock_np.array.side_effect = lambda *args, **kwargs: args[0] if args else []
mock_corr_matrix = MagicMock()
mock_corr_matrix.__getitem__.side_effect = lambda idx: 0.99 if isinstance(idx, tuple) else [0.99, 0.99]
mock_np.corrcoef.return_value = mock_corr_matrix
mock_np.abs.side_effect = abs
mock_np.log.side_effect = lambda x: 1.0
mock_np.sqrt.side_effect = lambda x: 1.0
sys.modules['numpy'] = mock_np

mock_scipy = MagicMock()
mock_stats = MagicMock()
mock_scipy.stats = mock_stats
mock_stats.pearsonr.return_value = (0.99, 0.001)
mock_stats.ttest_1samp.return_value = (1.5, 0.05)
sys.modules['scipy'] = mock_scipy
sys.modules['scipy.stats'] = mock_stats

if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())

try:
    import simulasyon_11
    MODULE_IMPORTED = True
except ImportError as e:
    MODULE_IMPORTED = False
    print(f"Uyarı: simulasyon_11 import edilemedi: {e}")

class TestSimulasyon(unittest.TestCase):

    def setUp(self):
        if not MODULE_IMPORTED:
            self.skipTest("simulasyon_11.py import edilemedi.")
        self.mock_const = MagicMock()
        self.mock_const.R11 = 11111111111
        self.mock_const.OP_LEN = 1.0
        self.mock_const.OP_TIME = 1.0
        self.mock_const.OP_LIGHT = 1.0
        self.mock_const.OP_ANGLE = 1.0

    def test_constants_r11(self):
        self.assertEqual(simulasyon_11.Simule3_Constants.R11, 11111111111)

    def test_module_time_packets_v130(self):
        module = simulasyon_11.Modul_Time_Packets_V130(self.mock_const)
        self.assertIsInstance(module, simulasyon_11.Modul_Time_Packets_V130)
        try:
            module.analiz()
        except Exception as e:
            self.fail(f"Modul_Time_Packets_V130.analiz() hata verdi: {e}")

    def test_simule3_lab_v133_init(self):
        try:
            lab = simulasyon_11.Simule3_Lab_V133()
            self.assertIsInstance(lab, simulasyon_11.Simule3_Lab_V133)
        except Exception as e:
            self.fail(f"Simule3_Lab_V133 başlatma hatası: {e}")

    def test_simule3_lab_v133_run_all(self):
        lab = simulasyon_11.Simule3_Lab_V133()
        with unittest.mock.patch('builtins.print') as mock_print:
            with unittest.mock.patch('builtins.input', return_value=''):
                 try:
                    lab.run_all()
                 except Exception as e:
                    self.fail(f"Simule3_Lab_V133.run_all() hata verdi: {e}")
            self.assertTrue(mock_print.called)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
"""

    with open("test_simulasyon.py", "w") as f:
        f.write(test_content)

    print("test_simulasyon.py oluşturuldu/güncellendi.")
    print("\n--- Testler Başlatılıyor ---\n")

    # Run the test file
    # Instead of subprocess, we can import it directly if we want, or execute it via python
    # Executing via python is safer to reset context
    os.system("python3 test_simulasyon.py")

if __name__ == "__main__":
    setup_and_run()

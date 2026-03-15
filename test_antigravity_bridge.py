import unittest
from antigravity_bridge import AntigravityDataBridge

class TestAntigravityDataBridge(unittest.TestCase):
    def setUp(self):
        self.bridge = AntigravityDataBridge()

    def test_process_entry_all_fields(self):
        entry = {
            "value": 123.45,
            "source": "TestSource",
            "unit": "TestUnit",
            "confidence": 0.95
        }
        result = self.bridge.process_entry(entry)

        self.assertTrue(result["processed"])
        self.assertEqual(result["value"], 123.45)
        self.assertEqual(result["source"], "TestSource")
        self.assertEqual(result["unit"], "TestUnit")
        self.assertEqual(result["confidence"], 0.95)
        self.assertIn("match", result)
        self.assertIn("timestamp", result)

    def test_process_entry_missing_fields(self):
        entry = {
            "value": 678.90
        }
        result = self.bridge.process_entry(entry)

        self.assertTrue(result["processed"])
        self.assertEqual(result["value"], 678.90)
        self.assertEqual(result["source"], "unknown")
        self.assertEqual(result["unit"], "")
        self.assertEqual(result["confidence"], 0.0)

    def test_process_entry_non_numeric_value(self):
        entry = {
            "value": "not_a_number",
            "source": "TextSource"
        }
        result = self.bridge.process_entry(entry)

        self.assertTrue(result["processed"])
        self.assertEqual(result["value"], "not_a_number")
        self.assertEqual(len(self.bridge.patterns_found), 0)

    def test_process_entry_exact_match(self):
        # IDEAL_EARTH_RADIUS is 6666
        entry = {
            "value": 6666,
            "source": "ExactSource"
        }
        result = self.bridge.process_entry(entry)

        matches = result["match"]
        self.assertTrue(any(m["type"] == "exact" and m["constant"] == "IDEAL_EARTH_RADIUS" for m in matches))

    def test_process_entry_divisibility_by_11(self):
        entry = {
            "value": 33,  # Divisible by 11
            "source": "DivisibleSource",
            "confidence": 0.8
        }
        result = self.bridge.process_entry(entry)

        self.assertEqual(len(self.bridge.patterns_found), 1)
        pattern = self.bridge.patterns_found[0]
        self.assertEqual(pattern["value"], 33)
        self.assertEqual(pattern["type"], "11-divisible")
        self.assertEqual(pattern["source"], "DivisibleSource")
        self.assertEqual(pattern["confidence"], 0.8)

if __name__ == '__main__':
    unittest.main()

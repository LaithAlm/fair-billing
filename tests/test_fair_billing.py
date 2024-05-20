import unittest
from datetime import datetime
from src.fair_billing import calculate_billing, parse_log_line

class TestFairBilling(unittest.TestCase):

    def setUp(self):
        # Create a temporary log file for testing
        self.test_log_content = (
            "14:02:03 ALICE99 Start\n"
            "14:02:05 CHARLIE End\n"
            "14:02:34 ALICE99 End\n"
            "14:02:58 ALICE99 Start\n"
            "14:03:02 CHARLIE Start\n"
            "14:03:33 ALICE99 Start\n"
            "14:03:35 ALICE99 End\n"
            "14:03:37 CHARLIE End\n"
            "14:04:05 ALICE99 End\n"
            "14:04:23 ALICE99 End\n"
            "14:04:41 CHARLIE Start\n"
        )
        with open('test_log.txt', 'w') as f:
            f.write(self.test_log_content)

    def tearDown(self):
        import os
        os.remove('test_log.txt')

    def test_parse_log_line(self):
        # Test a valid log line
        self.assertEqual(parse_log_line("14:02:03 ALICE99 Start\n"), (datetime(1900, 1, 1, 14, 2, 3), 'ALICE99', 'Start'))
        # Test an invalid log line
        self.assertIsNone(parse_log_line("Invalid log line"))

    def test_calculate_billing(self):
        results = calculate_billing('test_log.txt')
        self.assertEqual(results["ALICE99"]["total_time"], 240)
        self.assertEqual(results["CHARLIE"]["total_time"], 37)
        self.assertEqual(results["ALICE99"]["sessions"], 4)
        self.assertEqual(results["CHARLIE"]["sessions"], 3)

if __name__ == "__main__":
    unittest.main()

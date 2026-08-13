import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_v03 import validate_v03


class V03ReleaseCandidateValidationTests(unittest.TestCase):
    def test_v03_release_candidate_passes(self):
        path = ROOT / "data" / "raw" / "mena-observatory-v0.3.0-rc1.csv"
        self.assertEqual(validate_v03(path), [])


if __name__ == "__main__":
    unittest.main()

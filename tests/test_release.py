import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from validate_release import validate


class ReleaseValidationTests(unittest.TestCase):
    def test_v02_release_passes(self):
        path = Path(__file__).resolve().parents[1] / 'data' / 'raw' / 'mena-observatory-pilot-2026-08-07.csv'
        self.assertEqual(validate(path), [])


if __name__ == '__main__':
    unittest.main()

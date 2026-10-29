import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import merge


class TestMerger(unittest.TestCase):
    def test_dedupe_by_serial(self):
        merged, conflicts = merge({"S1": {"serial": "S1"}}, {"S1": {"serial": "S1"}, "S2": {"serial": "S2"}})
        self.assertEqual(len(merged), 2)
        self.assertEqual(conflicts, [])

    def test_conflict_reported(self):
        merged, conflicts = merge({"S1": {"serial": "S1", "owner": "A"}}, {"S1": {"serial": "S1", "owner": "B"}})
        self.assertEqual(conflicts, ["S1"])
        self.assertEqual(merged["S1"]["owner"], "B")

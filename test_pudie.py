"""谱牒（PUDIE）算子单测：名帖完整、行为达标、只增不覆盖。"""
import unittest

from pudie import Pudie


class TestPudie(unittest.TestCase):
    def setUp(self):
        self.op = Pudie()

    def test_describe(self):
        d = self.op.describe()
        self.assertEqual(d["repo"], "pudie")
        self.assertEqual(d["code"], "PUDIE")
        self.assertTrue(d["anchor"].startswith("Ω₀⊂⊙∞⊂Ω"))
        self.assertTrue(d["mingwen"])

    def test_classify_lineage(self):
        self.op.classify({"id": "宗", "kind": "root", "parent": None})
        self.op.classify({"id": "支", "kind": "branch", "parent": "宗"})
        out = self.op.classify({"id": "叶", "kind": "leaf", "parent": "支"})
        self.assertEqual(out["parent"], "支")
        self.assertEqual(self.op.lineage("叶"), ["叶", "支", "宗"])
        with self.assertRaises(KeyError):
            self.op.lineage("无有")


if __name__ == "__main__":
    unittest.main()

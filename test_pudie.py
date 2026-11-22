"""谱牒（PUDIE）算子骨架单测：名帖完整、桩位齐整、只增不覆盖。"""
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

    def test_classify_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.classify(None)

    def test_lineage_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.lineage(None)


if __name__ == "__main__":
    unittest.main()

import unittest

import simon_says as core


class FixedRng:
    def __init__(self, values):
        self.values = list(values)

    def choice(self, seq):
        return self.values.pop(0)


class TestCore(unittest.TestCase):
    def test_config_falls_back_to_normal(self):
        self.assertEqual(core.config("missing"), core.config("normal"))

    def test_add_step(self):
        sequence = []
        self.assertEqual(core.add_step(sequence, FixedRng(["red"])), ["red"])

    def test_build_sequence(self):
        self.assertEqual(core.build_sequence(3, FixedRng(["red", "blue", "green"])), ["red", "blue", "green"])

    def test_normalize_token(self):
        self.assertEqual(core.normalize_token(" R "), "red")
        self.assertEqual(core.normalize_token("blue"), "blue")

    def test_parse_answer(self):
        self.assertEqual(core.parse_answer("r,b green"), ["red", "blue", "green"])

    def test_answer_matches(self):
        sequence = ["red", "blue", "green"]
        self.assertTrue(core.answer_matches(sequence, "r b g"))
        self.assertFalse(core.answer_matches(sequence, "r g b"))

    def test_sequence_text(self):
        self.assertEqual(core.sequence_text(["red", "blue"]), "red blue")

    def test_hint_text(self):
        self.assertEqual(core.hint_text([]), "")
        self.assertEqual(core.hint_text(["red", "blue"]), "first: red, length: 2")

    def test_score_for(self):
        self.assertEqual(core.score_for("easy", 2, 3), 55)
        self.assertEqual(core.score_for("normal", 2, 3), 110)
        self.assertEqual(core.score_for("easy", 2, 3, used_hint=True), 27)

    def test_final_rating(self):
        self.assertEqual(core.final_rating(8, 8), "perfect")
        self.assertEqual(core.final_rating(6, 8), "great")
        self.assertEqual(core.final_rating(4, 8), "good")
        self.assertEqual(core.final_rating(1, 8), "try_again")


if __name__ == "__main__":
    unittest.main()

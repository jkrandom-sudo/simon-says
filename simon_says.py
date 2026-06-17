"""Core logic for Simon Says."""
import random

COLORS = ("red", "blue", "green", "yellow")
SHORTCUTS = {"r": "red", "b": "blue", "g": "green", "y": "yellow"}
DIFFICULTY_CONFIG = {
    "easy": {"rounds": 6, "start": 1, "growth": 1, "bonus": 1},
    "normal": {"rounds": 8, "start": 2, "growth": 1, "bonus": 2},
    "hard": {"rounds": 10, "start": 3, "growth": 1, "bonus": 3},
}


def config(difficulty):
    return DIFFICULTY_CONFIG.get(difficulty, DIFFICULTY_CONFIG["normal"])


def add_step(sequence, rng=None):
    rng = rng or random
    sequence.append(rng.choice(COLORS))
    return sequence


def build_sequence(length, rng=None):
    sequence = []
    for _ in range(length):
        add_step(sequence, rng)
    return sequence


def normalize_token(token):
    token = token.strip().lower()
    return SHORTCUTS.get(token, token)


def parse_answer(text):
    return [normalize_token(part) for part in text.replace(",", " ").split()]


def answer_matches(sequence, answer_text):
    return parse_answer(answer_text) == list(sequence)


def sequence_text(sequence):
    return " ".join(sequence)


def hint_text(sequence):
    if not sequence:
        return ""
    return f"first: {sequence[0]}, length: {len(sequence)}"


def score_for(difficulty, round_index, streak, used_hint=False):
    base = 20 + round_index * 10 + streak * 5
    if used_hint:
        base //= 2
    return base * config(difficulty)["bonus"]


def final_rating(completed, total):
    if completed == total:
        return "perfect"
    if completed >= max(1, total * 3 // 4):
        return "great"
    if completed >= max(1, total // 2):
        return "good"
    return "try_again"

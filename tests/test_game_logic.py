from logic_utils import check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug 1: hint messages used to be reversed ---------------------------------
# A guess that is too high must tell the player to go LOWER, and vice versa.
# The outcome label was always correct, so these assert on the *message*.

def test_too_high_hint_says_go_lower():
    _, message = check_guess(60, 50)
    assert "LOWER" in message
    assert "HIGHER" not in message


def test_too_low_hint_says_go_higher():
    _, message = check_guess(40, 50)
    assert "HIGHER" in message
    assert "LOWER" not in message


def test_reported_scenario_guess_25_secret_45():
    # The exact glitch the player hit: guessing 25 with a secret of 45
    # used to say "go lower". It must say go higher.
    outcome, message = check_guess(25, 45)
    assert outcome == "Too Low"
    assert "HIGHER" in message


# --- Bug 2: secret was cast to str on even attempts ---------------------------
# String comparison is lexicographic: "9" > "45" is True even though 9 < 45.
# These cases pass only when the comparison is numeric.

def test_single_digit_guess_below_two_digit_secret():
    outcome, message = check_guess(9, 45)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_single_digit_guess_above_two_digit_secret():
    outcome, message = check_guess(5, 12)
    assert outcome == "Too Low"
    assert "HIGHER" in message

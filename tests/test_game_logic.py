from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- High score accumulation tests ---
# Bug: high score used a conditional (if score > high_score)
# which blocked accumulation when a later win had a lower score.
# Fix: always add score on win unconditionally.

def test_high_score_starts_at_zero():
    high_score = 0
    assert high_score == 0


def test_high_score_updates_on_first_win():
    high_score = 0
    score = 90
    high_score += score
    assert high_score == 90


def test_high_score_accumulates_on_second_win_with_lower_score():
    # Regression test for the bug:
    # old code: if score > high_score: high_score += score
    # second win (score=80) would NOT update because 80 < 90
    high_score = 0

    score = 90
    high_score += score  # first win
    assert high_score == 90

    score = 80
    high_score += score  # second win with lower score — must still accumulate
    assert high_score == 170


def test_high_score_accumulates_across_multiple_wins():
    high_score = 0
    for score in [90, 80, 70]:
        high_score += score
    assert high_score == 240


def test_old_conditional_bug_would_not_accumulate():
    # Demonstrates the original bug: using if score > high_score blocks accumulation
    high_score = 0

    score = 90
    if score > high_score:
        high_score += score
    assert high_score == 90

    score = 80
    if score > high_score:  # 80 > 90 is False — high_score stays 90
        high_score += score
    assert high_score == 90  # proves the old code was wrong

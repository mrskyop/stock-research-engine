from app.analysis.ratio_scoring import normalize_relative_score


def test_score():

    assert normalize_relative_score(0) == 50
    assert normalize_relative_score(0.30) == 65
    assert normalize_relative_score(-0.40) == 30
    assert normalize_relative_score(2.0) == 100
    assert normalize_relative_score(-2.0) == 0


if __name__ == "__main__":
    test_score()
    print("Ratio scoring tests passed")
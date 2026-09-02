from app.analysis.growth_scoring import (
    score_growth_rate,
    score_growth_stability,
    calculate_growth_quality_score,
)


def test_growth_scoring():

    assert score_growth_rate(0) == 50
    assert score_growth_rate(10) == 70

    assert score_growth_stability(0) == 100
    assert score_growth_stability(10) == 50

    score = calculate_growth_quality_score(
        average_growth=10,
        volatility=10,
    )

    assert score == 62.0


if __name__ == "__main__":
    test_growth_scoring()
    print("Growth scoring tests passed")
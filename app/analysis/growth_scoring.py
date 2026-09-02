def score_growth_rate(average_growth: float) -> float:
    """
    Score average annual growth on a 0-100 scale.

    0% growth  -> 50
    10% growth -> 70
    20% growth -> 90
    25%+       -> capped at 100
    """

    score = 50 + (average_growth * 2)

    return max(0.0, min(100.0, score))


def score_growth_stability(volatility: float) -> float:
    """
    Score growth stability on a 0-100 scale.

    Lower volatility = higher score.

    0% volatility  -> 100
    5% volatility  -> 75
    10% volatility -> 50
    20%+           -> 0
    """

    score = 100 - (volatility * 5)

    return max(0.0, min(100.0, score))


def calculate_growth_quality_score(
    average_growth: float,
    volatility: float,
) -> float:
    """
    Combine growth strength and growth stability.

    Growth strength: 60%
    Growth stability: 40%
    """

    growth_score = score_growth_rate(average_growth)
    stability_score = score_growth_stability(volatility)

    return (
        growth_score * 0.60
        + stability_score * 0.40
    )
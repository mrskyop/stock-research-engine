from app.analysis.metrics import calculate_income_metrics
from app.analysis.growth_metrics import (
    calculate_average_growth,
    calculate_growth_volatility,
)
from app.analysis.growth_scoring import (
    calculate_growth_quality_score,
)


def calculate_growth_quality(company_id: int) -> dict:
    """
    Calculate revenue and PAT growth quality.
    """

    metrics = calculate_income_metrics(company_id)

    revenue_growth = [
        row["revenue_growth"]
        for row in metrics
        if row["revenue_growth"] is not None
    ]

    pat_growth = [
        row["pat_growth"]
        for row in metrics
        if row["pat_growth"] is not None
    ]

    result = {}

    if len(revenue_growth) >= 2:
        average_revenue_growth = calculate_average_growth(
            revenue_growth
        )

        revenue_growth_volatility = calculate_growth_volatility(
            revenue_growth
        )

        result["average_revenue_growth"] = average_revenue_growth
        result["revenue_growth_volatility"] = revenue_growth_volatility

        result["revenue_growth_score"] = (
            calculate_growth_quality_score(
                average_revenue_growth,
                revenue_growth_volatility,
            )
        )

    if len(pat_growth) >= 2:
        average_pat_growth = calculate_average_growth(
            pat_growth
        )

        pat_growth_volatility = calculate_growth_volatility(
            pat_growth
        )

        result["average_pat_growth"] = average_pat_growth
        result["pat_growth_volatility"] = pat_growth_volatility

        result["pat_growth_score"] = (
            calculate_growth_quality_score(
                average_pat_growth,
                pat_growth_volatility,
            )
        )

    return result
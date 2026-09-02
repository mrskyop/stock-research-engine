from sqlalchemy import text

from app.database import engine
from app.analysis.ratio_scoring import normalize_relative_score


HIGHER_IS_BETTER = {
    "ROE",
    "ROCE",
    "ROA",
}

LOWER_IS_BETTER = {
    "P/E",
    "P/B",
    "EV/EBITDA",
}


def get_latest_key_ratios(company_id: int) -> list[dict]:
    """
    Fetch the latest key-ratio snapshot for a company.
    """

    query = text("""
        SELECT
            ratio_name,
            company_value,
            sector_value,
            as_of_date
        FROM key_ratios
        WHERE company_id = :company_id
          AND as_of_date = (
              SELECT MAX(as_of_date)
              FROM key_ratios
              WHERE company_id = :company_id
          )
        ORDER BY ratio_name
    """)

    with engine.connect() as connection:
        rows = connection.execute(
            query,
            {"company_id": company_id}
        ).mappings().all()

    return [dict(row) for row in rows]


def calculate_ratio_analysis(company_id: int) -> list[dict]:
    """
    Compare each supported ratio with its sector benchmark
    and calculate a normalized 0-100 score.
    """

    ratios = get_latest_key_ratios(company_id)

    results = []

    for ratio in ratios:

        ratio_name = ratio["ratio_name"]
        company_value = ratio["company_value"]
        sector_value = ratio["sector_value"]

        if company_value is None or sector_value is None:
            continue

        if sector_value == 0:
            continue

        if ratio_name in HIGHER_IS_BETTER:
            direction = "HIGHER_IS_BETTER"

        elif ratio_name in LOWER_IS_BETTER:
            direction = "LOWER_IS_BETTER"

        else:
            # We deliberately skip ratios that require
            # more business context.
            continue

        relative_difference = (
            company_value - sector_value
        ) / sector_value

        if direction == "LOWER_IS_BETTER":
            relative_difference = -relative_difference

        score = normalize_relative_score(relative_difference)

        results.append({
            "ratio_name": ratio_name,
            "company_value": company_value,
            "sector_value": sector_value,
            "relative_difference": relative_difference,
            "score": score,
        })

    return results
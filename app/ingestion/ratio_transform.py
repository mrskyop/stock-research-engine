from datetime import date


def transform_key_ratios(
    company_id: int,
    api_response: dict,
    as_of_date: date,
) -> list[dict]:

    rows = []

    for ratio in api_response["data"]:
        rows.append(
            {
                "company_id": company_id,
                "as_of_date": as_of_date,
                "ratio_name": ratio["name"],
                "company_value": parse_ratio_value(
                    ratio["company_value"]
                ),
                "sector_value": parse_ratio_value(
                    ratio["sector_value"]
                ),
            }
        )

    return rows


def parse_ratio_value(value: str | None):
    if value is None:
        return None

    value = value.strip()

    if value.endswith("%"):
        return float(value[:-1])

    return float(value)
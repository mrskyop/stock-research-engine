def validate_key_ratio(row: dict):
    required_fields = [
        "company_id",
        "as_of_date",
        "ratio_name",
    ]

    for field in required_fields:
        if row.get(field) is None:
            raise ValueError(
                f"Missing required field: {field}"
            )

    if row["company_value"] is not None:
        if not isinstance(
            row["company_value"],
            (int, float),
        ):
            raise ValueError(
                "company_value must be numeric"
            )

    if row["sector_value"] is not None:
        if not isinstance(
            row["sector_value"],
            (int, float),
        ):
            raise ValueError(
                "sector_value must be numeric"
            )
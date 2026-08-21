def validate_income_statement(row: dict):
    required_fields = [
        "company_id",
        "period",
        "period_type",
        "statement_type",
        "units_in",
    ]

    for field in required_fields:
        if row.get(field) is None:
            raise ValueError(
                f"Income statement missing required field: {field}"
            )

    numeric_fields = [
        "revenue",
        "other_income",
        "total_revenue",
        "total_expenses",
        "profit_before_tax",
        "tax",
        "profit_after_tax",
        "eps_basic",
        "eps_diluted",
    ]

    for field in numeric_fields:
        value = row.get(field)

        if value is not None and not isinstance(
            value,
            (int, float),
        ):
            raise ValueError(
                f"{field} must be numeric, got {type(value).__name__}"
            )


def validate_balance_sheet(row: dict):
    required_fields = [
        "company_id",
        "period",
        "period_type",
        "statement_type",
        "units_in",
    ]

    for field in required_fields:
        if row.get(field) is None:
            raise ValueError(
                f"Balance sheet missing required field: {field}"
            )

    numeric_fields = [
        "non_current_assets",
        "current_assets",
        "total_assets",
        "current_liabilities",
        "net_current_asset",
        "non_current_liabilities",
        "equity_capital",
        "total_equity_and_liabilities",
    ]

    for field in numeric_fields:
        value = row.get(field)

        if value is not None and not isinstance(
            value,
            (int, float),
        ):
            raise ValueError(
                f"{field} must be numeric, got {type(value).__name__}"
            )


def validate_cash_flow(row: dict):
    required_fields = [
        "company_id",
        "period",
        "period_type",
        "statement_type",
        "units_in",
    ]

    for field in required_fields:
        if row.get(field) is None:
            raise ValueError(
                f"Cash flow missing required field: {field}"
            )

    numeric_fields = [
        "profit_before_tax",
        "income_before_wc_changes",
        "change_in_assets",
        "change_in_liabilities",
        "change_in_wc",
        "operating_cash_flow",
        "investing_cash_flow",
        "financing_cash_flow",
        "total_cash_flow",
        "cash_start_of_year",
        "cash_end_of_year",
    ]

    for field in numeric_fields:
        value = row.get(field)

        if value is not None and not isinstance(
            value,
            (int, float),
        ):
            raise ValueError(
                f"{field} must be numeric, got {type(value).__name__}"
            )


def validate_shareholding(row: dict):
    required_fields = [
        "company_id",
        "period",
        "category",
        "percentage",
    ]

    for field in required_fields:
        if row.get(field) is None:
            raise ValueError(
                f"Shareholding missing required field: {field}"
            )

    percentage = row["percentage"]

    if not isinstance(percentage, (int, float)):
        raise ValueError(
            "Shareholding percentage must be numeric"
        )

    if not 0 <= percentage <= 100:
        raise ValueError(
            f"Shareholding percentage out of range: {percentage}"
        )
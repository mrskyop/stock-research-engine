from datetime import date
import re


def parse_period(period: str) -> date:
    """
    Convert a provider period such as 'Mar 2026'
    into a PostgreSQL-friendly date.
    """

    match = re.fullmatch(
        r"([A-Za-z]{3}) (\d{4})",
        period.strip(),
    )

    if not match:
        raise ValueError(
            f"Unsupported financial period: {period}"
        )

    month_text, year_text = match.groups()

    month_map = {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "Jul": 7,
        "Aug": 8,
        "Sep": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12,
    }

    month = month_map[month_text]

    return date(
        int(year_text),
        month,
        1,
    )

def transform_income_statement(
    company_id: int,
    api_response: dict,
) -> list[dict]:
    data = api_response["data"]

    statement_type = data["type"]
    period_type = data["time_period"]
    units_in = data["units_in"]

    rows = {}

    for item in data["full_statement"]:
        particular = item["particular"]

        for history in item["history"]:
            period = parse_period(history["period"])

            row = rows.setdefault(
                period,
                {
                    "company_id": company_id,
                    "period": period,
                    "period_type": period_type,
                    "statement_type": statement_type,
                    "units_in": units_in,
                },
            )

            value = history["value"]

            field_map = {
                "Revenue": "revenue",
                "Other Income": "other_income",
                "Total Revenue": "total_revenue",
                "Total Expenses": "total_expenses",
                "Profit Before Tax": "profit_before_tax",
                "Tax": "tax",
                "Profit After Tax": "profit_after_tax",
                "EPS - Basic": "eps_basic",
                "EPS - Diluted": "eps_diluted",
            }

            field = field_map.get(particular)

            if field is not None:
                row[field] = value

    return list(rows.values())

def transform_balance_sheet(
    company_id: int,
    api_response: dict,
) -> list[dict]:
    data = api_response["data"]

    statement_type = data["type"]
    period_type = data["time_period"]
    units_in = data["units_in"]

    rows = {}

    field_map = {
        "Non-Current Assets": "non_current_assets",
        "Current Assets": "current_assets",
        "Total Assets": "total_assets",
        "Current Liabilities": "current_liabilities",
        "Net Current Asset": "net_current_asset",
        "Non-Current Liabilities": "non_current_liabilities",
        "Equity Capital": "equity_capital",
        "Total Equity & Liabilities": "total_equity_and_liabilities",
    }

    for item in data["full_statement"]:
        field = field_map.get(item["particular"])

        if field is None:
            continue

        for history in item["history"]:
            period = parse_period(history["period"])

            row = rows.setdefault(
                period,
                {
                    "company_id": company_id,
                    "period": period,
                    "period_type": period_type,
                    "statement_type": statement_type,
                    "units_in": units_in,
                },
            )

            row[field] = history["value"]

    return list(rows.values())

def transform_cash_flow(
    company_id: int,
    api_response: dict,
) -> list[dict]:
    data = api_response["data"]

    statement_type = data["type"]
    period_type = data["time_period"]
    units_in = data["units_in"]

    rows = {}

    field_map = {
        "Profit before tax": "profit_before_tax",
        "Income before WC changes": "income_before_wc_changes",
        "Change in Assets": "change_in_assets",
        "Change in Liabilities": "change_in_liabilities",
        "Change in WC": "change_in_wc",
        "Cash flow from Operations": "operating_cash_flow",
        "Cash flow from Investing": "investing_cash_flow",
        "Cash flow from Financing": "financing_cash_flow",
        "Total Cash Flow": "total_cash_flow",
        "Cash (Start of the year)": "cash_start_of_year",
        "Cash (End of the year)": "cash_end_of_year",
    }

    for item in data["full_statement"]:
        field = field_map.get(item["particular"])

        if field is None:
            continue

        for history in item["history"]:
            period = parse_period(history["period"])

            row = rows.setdefault(
                period,
                {
                    "company_id": company_id,
                    "period": period,
                    "period_type": period_type,
                    "statement_type": statement_type,
                    "units_in": units_in,
                },
            )

            row[field] = history["value"]

    return list(rows.values())

def transform_shareholding(
    company_id: int,
    api_response: dict,
) -> list[dict]:
    rows = []

    for category_data in api_response["data"]:
        category = category_data["category"]

        for history in category_data["history"]:
            rows.append(
                {
                    "company_id": company_id,
                    "period": parse_period(
                        history["period"]
                    ),
                    "category": category,
                    "percentage": history["value"],
                }
            )

    return rows

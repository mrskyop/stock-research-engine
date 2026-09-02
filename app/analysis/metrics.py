from sqlalchemy import text

from app.database import engine


def get_income_statement_history(company_id: int):
    query = text("""
        SELECT
            period,
            revenue,
            profit_after_tax
        FROM income_statements
        WHERE company_id = :company_id
        ORDER BY period;
    """)

    with engine.connect() as connection:
        return connection.execute(
            query,
            {"company_id": company_id},
        ).mappings().all()


def calculate_growth(current: float, previous: float):
    if previous == 0:
        return None

    return ((current - previous) / previous) * 100


def calculate_pat_margin(
    profit_after_tax: float,
    revenue: float,
):
    if revenue == 0:
        return None

    return (profit_after_tax / revenue) * 100

def calculate_income_metrics(company_id: int):
    history = get_income_statement_history(company_id)

    metrics = []

    for index in range(1, len(history)):
        previous = history[index - 1]
        current = history[index]

        revenue_growth = calculate_growth(
            current["revenue"],
            previous["revenue"],
        )

        pat_growth = calculate_growth(
            current["profit_after_tax"],
            previous["profit_after_tax"],
        )

        pat_margin = calculate_pat_margin(
            current["profit_after_tax"],
            current["revenue"],
        )

        metrics.append(
            {
                "period": current["period"],
                "revenue_growth": revenue_growth,
                "pat_growth": pat_growth,
                "pat_margin": pat_margin,
            }
        )

    return metrics

def get_cash_flow_history(company_id: int):
    query = text("""
        SELECT
            period,
            operating_cash_flow
        FROM cash_flows
        WHERE company_id = :company_id
        ORDER BY period;
    """)

    with engine.connect() as connection:
        return connection.execute(
            query,
            {"company_id": company_id},
        ).mappings().all()


def calculate_cash_conversion(
    operating_cash_flow: float,
    profit_after_tax: float,
):
    if profit_after_tax == 0:
        return None

    return (
        operating_cash_flow / profit_after_tax
    ) * 100
def get_profit_cash_history(company_id: int):
    query = text("""
        SELECT
            i.period,
            i.profit_after_tax,
            c.operating_cash_flow
        FROM income_statements i
        JOIN cash_flows c
            ON c.company_id = i.company_id
            AND c.period = i.period
            AND c.period_type = i.period_type
            AND c.statement_type = i.statement_type
        WHERE i.company_id = :company_id
        ORDER BY i.period;
    """)

    with engine.connect() as connection:
        return connection.execute(
            query,
            {"company_id": company_id},
        ).mappings().all()

def calculate_cash_metrics(company_id: int):
    history = get_profit_cash_history(company_id)

    metrics = []

    for row in history:
        cash_conversion = calculate_cash_conversion(
            row["operating_cash_flow"],
            row["profit_after_tax"],
        )

        metrics.append(
            {
                "period": row["period"],
                "cash_conversion": cash_conversion,
            }
        )

    return metrics

def get_balance_sheet_history(company_id: int):
    query = text("""
        SELECT
            period,
            total_assets,
            current_liabilities,
            equity_capital
        FROM balance_sheets
        WHERE company_id = :company_id
        ORDER BY period;
    """)

    with engine.connect() as connection:
        return connection.execute(
            query,
            {"company_id": company_id},
        ).mappings().all()


def calculate_asset_growth(
    current_assets,
    previous_assets,
):
    if previous_assets == 0:
        return None

    return (
        (current_assets - previous_assets)
        / previous_assets
    ) * 100

def calculate_balance_metrics(company_id: int):
    history = get_balance_sheet_history(company_id)

    metrics = []

    for index in range(1, len(history)):
        previous = history[index - 1]
        current = history[index]

        asset_growth = calculate_asset_growth(
            current["total_assets"],
            previous["total_assets"],
        )

        metrics.append(
            {
                "period": current["period"],
                "asset_growth": asset_growth,
                "current_liabilities": current[
                    "current_liabilities"
                ],
                "equity_capital": current[
                    "equity_capital"
                ],
            }
        )

    return metrics


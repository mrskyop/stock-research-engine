import logging

from app.ingestion.financial_load import (
    save_balance_sheets,
    save_cash_flows,
    save_income_statements,
    save_shareholding,
)
from app.ingestion.financial_transform import (
    transform_balance_sheet,
    transform_cash_flow,
    transform_income_statement,
    transform_shareholding,
)
from app.ingestion.financial_validation import (
    validate_balance_sheet,
    validate_cash_flow,
    validate_income_statement,
    validate_shareholding,
)
from app.ingestion.prices import get_security
from app.providers.fundamentals import (
    get_balance_sheet,
    get_cash_flow,
    get_income_statement,
    get_shareholding,
)

logger = logging.getLogger(__name__)


def ingest_financials(symbol: str):
    security = get_security(symbol)

    if security is None:
        raise RuntimeError(
            f"Security not found for {symbol}"
        )

    company_id = security.company_id
    isin = security.isin

    logger.info(
        "Starting financial ingestion for %s",
        symbol,
    )

    # Income statement
    income_response = get_income_statement(
        isin=isin,
        statement_type="consolidated",
        time_period="yearly",
        detailed=True,
    )

    income_rows = transform_income_statement(
        company_id=company_id,
        api_response=income_response,
    )

    for row in income_rows:
        validate_income_statement(row)

    income_count = save_income_statements(
        income_rows
    )

    logger.info(
        "%s: loaded %s income-statement rows",
        symbol,
        income_count,
    )

    # Balance sheet
    balance_response = get_balance_sheet(
        isin=isin,
        statement_type="consolidated",
        time_period="yearly",
        detailed=True,
    )

    balance_rows = transform_balance_sheet(
        company_id=company_id,
        api_response=balance_response,
    )

    for row in balance_rows:
        validate_balance_sheet(row)

    balance_count = save_balance_sheets(
        balance_rows
    )

    logger.info(
        "%s: loaded %s balance-sheet rows",
        symbol,
        balance_count,
    )

    # Cash flow
    cash_response = get_cash_flow(
        isin=isin,
        statement_type="consolidated",
        time_period="yearly",
        detailed=True,
    )

    cash_rows = transform_cash_flow(
        company_id=company_id,
        api_response=cash_response,
    )

    for row in cash_rows:
        validate_cash_flow(row)

    cash_count = save_cash_flows(
        cash_rows
    )

    logger.info(
        "%s: loaded %s cash-flow rows",
        symbol,
        cash_count,
    )

    # Shareholding
    shareholding_response = get_shareholding(
        isin=isin
    )

    shareholding_rows = transform_shareholding(
        company_id=company_id,
        api_response=shareholding_response,
    )

    for row in shareholding_rows:
        validate_shareholding(row)

    shareholding_count = save_shareholding(
        shareholding_rows
    )

    logger.info(
        "%s: loaded %s shareholding rows",
        symbol,
        shareholding_count,
    )

    return {
        "income_statements": income_count,
        "balance_sheets": balance_count,
        "cash_flows": cash_count,
        "shareholding": shareholding_count,
    }


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )

    result = ingest_financials("RELIANCE")

    print("\nFinancial ingestion summary")
    print("---------------------------")

    for dataset, count in result.items():
        print(f"{dataset}: {count}")


if __name__ == "__main__":
    main()
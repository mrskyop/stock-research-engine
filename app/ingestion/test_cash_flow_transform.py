from app.ingestion.financial_transform import (
    transform_cash_flow,
)
from app.providers.fundamentals import get_cash_flow


def main():
    response = get_cash_flow(
        isin="INE002A01018",
        statement_type="consolidated",
        time_period="yearly",
        detailed=True,
    )

    rows = transform_cash_flow(
        company_id=1,
        api_response=response,
    )

    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
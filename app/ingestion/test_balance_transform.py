from app.ingestion.financial_transform import (
    transform_balance_sheet,
)
from app.providers.fundamentals import get_balance_sheet


def main():
    response = get_balance_sheet(
        isin="INE002A01018",
        statement_type="consolidated",
        time_period="yearly",
        detailed=True,
    )

    rows = transform_balance_sheet(
        company_id=1,
        api_response=response,
    )

    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
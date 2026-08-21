from app.ingestion.financial_transform import (
    transform_income_statement,
)
from app.providers.fundamentals import get_income_statement


def main():
    response = get_income_statement(
        isin="INE002A01018",
        statement_type="consolidated",
        time_period="yearly",
        detailed=True,
    )

    rows = transform_income_statement(
        company_id=1,
        api_response=response,
    )

    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
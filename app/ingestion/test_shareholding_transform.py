from app.ingestion.financial_transform import (
    transform_shareholding,
)
from app.providers.fundamentals import get_shareholding


def main():
    response = get_shareholding(
        isin="INE002A01018"
    )

    rows = transform_shareholding(
        company_id=1,
        api_response=response,
    )

    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
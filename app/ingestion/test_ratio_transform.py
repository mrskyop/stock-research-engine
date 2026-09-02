from datetime import date

from app.ingestion.ratio_transform import (
    transform_key_ratios,
)
from app.providers.fundamentals import get_key_ratios


def main():
    response = get_key_ratios(
        isin="INE002A01018"
    )

    rows = transform_key_ratios(
        company_id=1,
        api_response=response,
        as_of_date=date.today(),
    )

    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
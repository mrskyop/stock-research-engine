from app.ingestion.financial_load import save_shareholding
from app.ingestion.financial_transform import transform_shareholding
from app.ingestion.financial_validation import validate_shareholding
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
        validate_shareholding(row)

    loaded = save_shareholding(rows)

    print(f"Loaded {loaded} shareholding rows.")


if __name__ == "__main__":
    main()
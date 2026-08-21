from app.ingestion.financial_validation import (
    validate_shareholding,
)


bad_row = {
    "company_id": 1,
    "period": "2026-06-01",
    "category": "promoters",
    "percentage": 150,
}


def main():
    try:
        validate_shareholding(bad_row)
    except ValueError as error:
        print(f"Validation failed: {error}")


if __name__ == "__main__":
    main()
from app.ingestion.prices import get_company, save_prices
from app.ingestion.transform import transform_candles
from app.providers.upstox import get_historical_daily_data


INSTRUMENT_KEY = "NSE_EQ|INE002A01018"

FROM_DATE = "2018-01-01"
TO_DATE = "2026-08-14"


def main():
    company = get_company("RELIANCE")

    if company is None:
        raise RuntimeError(
            "RELIANCE was not found in companies table"
        )

    print(
        f"Loading historical prices for "
        f"{company.symbol}..."
    )

    response = get_historical_daily_data(
        instrument_key=INSTRUMENT_KEY,
        from_date=FROM_DATE,
        to_date=TO_DATE,
    )

    candles = response["data"]["candles"]

    print(f"Received {len(candles)} candles.")

    prices = transform_candles(candles)

    print(f"Transformed {len(prices)} candles.")

    save_prices(
        company_id=company.id,
        prices=prices,
    )

    print(
        f"Loaded {len(prices)} records into PostgreSQL."
    )


if __name__ == "__main__":
    main()
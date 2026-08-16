from datetime import date

from app.ingestion import prices
from app.ingestion.prices import (
    get_last_price_date,
    get_security,
    save_prices,
)
from app.ingestion.transform import transform_candles
from app.providers.upstox import get_historical_daily_data


def ingest_prices(symbol: str):
    security = get_security(symbol)

    if security is None:
        raise RuntimeError(
            f"Security not found for {symbol}"
        )

    last_date = get_last_price_date(
        security.company_id
    )

    if last_date is None:
        raise RuntimeError(
            f"No historical prices found for {symbol}. "
            "Run the initial backfill first."
        )

    today = date.today()

    print(f"Symbol: {symbol}")
    print(f"Last stored date: {last_date}")
    print(f"Fetching through: {today}")

    response = get_historical_daily_data(
        instrument_key=security.instrument_key,
        from_date=last_date.isoformat(),
        to_date=today.isoformat(),
    )

    candles = response["data"]["candles"]

    print(f"Received {len(candles)} candles.")

    prices = transform_candles(candles)

    save_prices(
        company_id=security.company_id,
        prices=prices,
    )

    print(
        f"Loaded {len(prices)} records for {symbol}."
    )

    return len(prices)

if __name__ == "__main__":
    ingest_prices("RELIANCE")
from providers.upstox import get_historical_daily_data


INSTRUMENT_KEY = "NSE_EQ|INE002A01018"


data = get_historical_daily_data(
    instrument_key=INSTRUMENT_KEY,
    from_date="2018-01-01",
    to_date="2026-08-14",
)

print(data)
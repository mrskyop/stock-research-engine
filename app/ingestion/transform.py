from datetime import datetime
def transform_candle(candle: list) -> dict:
    return {
        "trade_date": datetime.fromisoformat(
            candle[0]
        ).date(),
        "open": candle[1],
        "high": candle[2],
        "low": candle[3],
        "close": candle[4],
        "volume": candle[5],
    }
def transform_candles(candles: list) -> list[dict]:
    return [
        transform_candle(candle)
        for candle in candles
    ]
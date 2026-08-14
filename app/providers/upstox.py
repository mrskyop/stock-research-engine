import os

import requests
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("UPSTOX_ACCESS_TOKEN")

if not ACCESS_TOKEN:
    raise RuntimeError("UPSTOX_ACCESS_TOKEN is not set")


def get_historical_daily_data(
    instrument_key: str,
    from_date: str,
    to_date: str,
):
    url = (
        f"https://api.upstox.com/v3/historical-candle/"
        f"{instrument_key}/days/1/{to_date}/{from_date}"
    )

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}",
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=30,
    )

    response.raise_for_status()

    return response.json()
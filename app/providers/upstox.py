import os

import requests
from dotenv import load_dotenv

from app.providers.exceptions import (
    UpstoxAuthenticationError,
    UpstoxBadRequestError,
    UpstoxRateLimitError,
    UpstoxServerError,
)

load_dotenv()

ACCESS_TOKEN = os.getenv("UPSTOX_ACCESS_TOKEN")

if not ACCESS_TOKEN:
    raise RuntimeError("UPSTOX_ACCESS_TOKEN is not set")


RETRYABLE_STATUS_CODES = {429, 500, 502, 503, 504}


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

    status = response.status_code

    if status == 401:
        raise UpstoxAuthenticationError(
            "Upstox authentication failed"
        )

    if status == 400:
        raise UpstoxBadRequestError(
            f"Invalid Upstox request: {response.text}"
        )

    if status == 429:
        raise UpstoxRateLimitError(
            "Upstox rate limit exceeded"
        )

    if status in {500, 502, 503, 504}:
        raise UpstoxServerError(
            f"Upstox server error: HTTP {status}"
        )

    response.raise_for_status()

    return response.json()
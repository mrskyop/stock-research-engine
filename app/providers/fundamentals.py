import os

import requests
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("UPSTOX_ACCESS_TOKEN")

if not ACCESS_TOKEN:
    raise RuntimeError("UPSTOX_ACCESS_TOKEN is not set")


def get_income_statement(
    isin: str,
    statement_type: str = "consolidated",
    time_period: str = "yearly",
    detailed: bool = True,
):
    url = f"https://api.upstox.com/v2/fundamentals/{isin}/income-statement"

    params = {
        "type": statement_type,
        "time_period": time_period,
        "fs": str(detailed).lower(),
    }

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}",
    }

    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=30,
    )

    response.raise_for_status()

    return response.json()

def get_balance_sheet(
    isin: str,
    statement_type: str = "consolidated",
    time_period: str = "yearly",
    detailed: bool = True,
):
    url = f"https://api.upstox.com/v2/fundamentals/{isin}/balance-sheet"

    params = {
        "type": statement_type,
        "time_period": time_period,
        "fs": str(detailed).lower(),
    }

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}",
    }

    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=30,
    )

    response.raise_for_status()

    return response.json()

def get_cash_flow(
    isin: str,
    statement_type: str = "consolidated",
    time_period: str = "yearly",
    detailed: bool = True,
):
    url = f"https://api.upstox.com/v2/fundamentals/{isin}/cash-flow"

    params = {
        "type": statement_type,
        "time_period": time_period,
        "fs": str(detailed).lower(),
    }

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}",
    }

    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=30,
    )

    response.raise_for_status()

    return response.json()

def get_shareholding(isin: str):
    url = f"https://api.upstox.com/v2/fundamentals/{isin}/share-holdings"
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

def get_key_ratios(isin: str):
    url = f"https://api.upstox.com/v2/fundamentals/{isin}/key-ratios"

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

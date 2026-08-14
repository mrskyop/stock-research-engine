from app.ingestion.prices import save_price


sample_price = {
    "trade_date": "2018-01-25",
    "open": 461.3,
    "high": 463.25,
    "low": 455.7,
    "close": 460.35,
    "volume": 13112506,
}
save_price(
    company_id=1,
    price=sample_price,
)

print("Price inserted successfully.")
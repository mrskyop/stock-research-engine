from sqlalchemy import text

from app.database import engine


def get_security(symbol: str):
    query = text("""
        SELECT
            c.id AS company_id,
            c.symbol,
            c.company_name,
            c.isin,
            s.exchange,
            s.instrument_key
        FROM companies c
        JOIN securities s
            ON s.company_id = c.id
        WHERE c.symbol = :symbol
          AND s.exchange = 'NSE';
    """)

    with engine.connect() as connection:
        row = connection.execute(
            query,
            {"symbol": symbol},
        ).fetchone()

    return row


def get_last_price_date(company_id: int):
    query = text("""
        SELECT MAX(trade_date)
        FROM prices_daily
        WHERE company_id = :company_id;
    """)

    with engine.connect() as connection:
        return connection.execute(
            query,
            {"company_id": company_id},
        ).scalar_one()


def save_prices(company_id: int, prices: list[dict]):
    query = text("""
        INSERT INTO prices_daily (
            company_id,
            trade_date,
            open,
            high,
            low,
            close,
            volume
        )
        VALUES (
            :company_id,
            :trade_date,
            :open,
            :high,
            :low,
            :close,
            :volume
        )
        ON CONFLICT (company_id, trade_date)
        DO UPDATE SET
            open = EXCLUDED.open,
            high = EXCLUDED.high,
            low = EXCLUDED.low,
            close = EXCLUDED.close,
            volume = EXCLUDED.volume;
    """)

    records = [
        {
            "company_id": company_id,
            **price,
        }
        for price in prices
    ]

    with engine.begin() as connection:
        connection.execute(query, records)
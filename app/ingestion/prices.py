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
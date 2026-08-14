from sqlalchemy import text
from app.database import engine
def main():
    query = text("""
        SELECT id, symbol, company_name, isin
        FROM companies
        ORDER BY symbol;
    """)

    with engine.connect() as connection:
        result = connection.execute(query)

        for row in result:
            print(
                f"ID: {row.id} | "
                f"Symbol: {row.symbol} | "
                f"Company: {row.company_name} | "
                f"ISIN: {row.isin}"
            )


if __name__ == "__main__":
    main()
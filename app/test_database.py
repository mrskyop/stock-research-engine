from sqlalchemy import text
from app.database import engine
def main():
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT current_database();")
        )

        database_name = result.scalar_one()

        print(f"Connected to database: {database_name}")
if __name__ == "__main__":
    main()
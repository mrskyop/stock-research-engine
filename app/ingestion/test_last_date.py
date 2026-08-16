from app.ingestion.prices import get_last_price_date
def main():
    last_date = get_last_price_date(1)

    print(f"Last stored price date: {last_date}")
if __name__ == "__main__":
    main()
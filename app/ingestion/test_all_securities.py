from app.ingestion.prices import get_all_securities
def main():
    securities = get_all_securities()

    print(f"Found {len(securities)} securities.")

    for security in securities:
        print(
            f"{security.symbol} | "
            f"{security.exchange} | "
            f"{security.instrument_key}"
        )
if __name__ == "__main__":
    main()
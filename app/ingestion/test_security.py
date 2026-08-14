from app.ingestion.prices import get_security


def main():
    security = get_security("RELIANCE")

    if security is None:
        raise RuntimeError("Security not found")

    print(f"Company ID: {security.company_id}")
    print(f"Symbol: {security.symbol}")
    print(f"ISIN: {security.isin}")
    print(f"Exchange: {security.exchange}")
    print(f"Instrument: {security.instrument_key}")


if __name__ == "__main__":
    main()
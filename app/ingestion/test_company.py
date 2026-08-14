from app.ingestion.prices import get_company


def main():
    company = get_company("RELIANCE")

    if company is None:
        raise RuntimeError("Company not found")

    print(
        f"ID: {company.id}\n"
        f"Symbol: {company.symbol}\n"
        f"ISIN: {company.isin}"
    )


if __name__ == "__main__":
    main()
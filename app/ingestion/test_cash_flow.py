from app.providers.fundamentals import get_cash_flow


def main():
    data = get_cash_flow(
        isin="INE002A01018",
        statement_type="consolidated",
        time_period="yearly",
        detailed=True,
    )

    print(data)


if __name__ == "__main__":
    main()
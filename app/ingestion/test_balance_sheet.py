from app.providers.fundamentals import get_balance_sheet


def main():
    data = get_balance_sheet(
        isin="INE002A01018",
        statement_type="consolidated",
        time_period="yearly",
        detailed=True,
    )

    print(data)


if __name__ == "__main__":
    main()
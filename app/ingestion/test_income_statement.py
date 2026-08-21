from app.providers.fundamentals import get_income_statement


def main():
    data = get_income_statement(
        isin="INE002A01018",
        statement_type="consolidated",
        time_period="yearly",
        detailed=True,
    )

    print(data)


if __name__ == "__main__":
    main()
from app.providers.fundamentals import get_income_statement


def main():
    print("=== YEARLY ===")

    yearly = get_income_statement(
        isin="INE002A01018",
        statement_type="consolidated",
        time_period="yearly",
        detailed=True,
    )

    for item in yearly["data"]["full_statement"]:
        if item["particular"] == "Revenue":
            for history in item["history"]:
                print(
                    history["period"],
                    history["value"],
                )

    print("\n=== QUARTERLY ===")

    quarterly = get_income_statement(
        isin="INE002A01018",
        statement_type="consolidated",
        time_period="quarterly",
        detailed=False,
    )

    for item in quarterly["data"]["income_statement"]:
        if item["category"] == "revenue":
            for history in item["history"]:
                print(
                    history["period"],
                    history["value"],
                )


if __name__ == "__main__":
    main()
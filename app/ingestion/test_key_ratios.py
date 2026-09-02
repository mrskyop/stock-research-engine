from app.providers.fundamentals import get_key_ratios


def main():
    data = get_key_ratios(
        isin="INE002A01018"
    )

    print(data)


if __name__ == "__main__":
    main()
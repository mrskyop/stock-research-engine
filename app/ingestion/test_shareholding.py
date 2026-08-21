from app.providers.fundamentals import get_shareholding


def main():
    data = get_shareholding(
        isin="INE002A01018"
    )

    print(data)


if __name__ == "__main__":
    main()
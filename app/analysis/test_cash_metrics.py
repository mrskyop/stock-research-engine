from app.analysis.metrics import calculate_cash_metrics


def main():
    metrics = calculate_cash_metrics(1)

    for metric in metrics:
        print(metric)


if __name__ == "__main__":
    main()
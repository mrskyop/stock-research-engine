from app.analysis.metrics import calculate_balance_metrics


def main():
    metrics = calculate_balance_metrics(1)

    for metric in metrics:
        print(metric)


if __name__ == "__main__":
    main()
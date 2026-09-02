from app.analysis.metrics import calculate_income_metrics


def main():
    metrics = calculate_income_metrics(
        company_id=1
    )

    for metric in metrics:
        print(metric)


if __name__ == "__main__":
    main()
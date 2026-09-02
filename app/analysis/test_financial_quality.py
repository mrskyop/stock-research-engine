from app.analysis.financial_quality import calculate_growth_quality


if __name__ == "__main__":

    result = calculate_growth_quality(company_id=1)

    print("Financial Growth Quality")
    print("------------------------")

    print(
        f"Average Revenue Growth: "
        f"{result['average_revenue_growth']:.2f}%"
    )

    print(
        f"Revenue Growth Volatility: "
        f"{result['revenue_growth_volatility']:.2f}%"
    )

    print(
        f"Revenue Growth Score: "
        f"{result['revenue_growth_score']:.2f}"
    )

    print()

    print(
        f"Average PAT Growth: "
        f"{result['average_pat_growth']:.2f}%"
    )

    print(
        f"PAT Growth Volatility: "
        f"{result['pat_growth_volatility']:.2f}%"
    )

    print(
        f"PAT Growth Score: "
        f"{result['pat_growth_score']:.2f}"
    )
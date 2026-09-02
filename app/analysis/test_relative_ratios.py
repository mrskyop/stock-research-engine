from app.analysis.relative_ratios import calculate_ratio_analysis


if __name__ == "__main__":

    results = calculate_ratio_analysis(company_id=1)

    for result in results:
        print(
            f"{result['ratio_name']:10} | "
            f"Company: {result['company_value']} | "
            f"Sector: {result['sector_value']} | "
            f"Relative: {result['relative_difference']:.2%} | "
            f"Score: {result['score']:.2f}"
        )
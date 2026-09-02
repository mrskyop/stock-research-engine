from app.analysis.growth_metrics import (
    calculate_average_growth,
    calculate_growth_volatility,
)


def test_growth_metrics():
    growth_values = [5.0, 10.0, 15.0]

    average = calculate_average_growth(growth_values)
    volatility = calculate_growth_volatility(growth_values)

    assert average == 10.0
    assert round(volatility, 2) == 5.0


if __name__ == "__main__":
    test_growth_metrics()

    print("Growth metrics tests passed")
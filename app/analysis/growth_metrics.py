from decimal import Decimal
import statistics


def calculate_average_growth(
    growth_values: list[float | Decimal]
) -> float:
    """
    Calculate the arithmetic average of growth rates.
    """

    if not growth_values:
        raise ValueError("growth_values cannot be empty")

    values = [float(value) for value in growth_values]

    return sum(values) / len(values)


def calculate_growth_volatility(
    growth_values: list[float | Decimal]
) -> float:
    """
    Calculate the standard deviation of growth rates.

    Lower value = more stable growth
    Higher value = more volatile growth
    """

    if len(growth_values) < 2:
        raise ValueError(
            "At least two growth observations are required"
        )

    values = [float(value) for value in growth_values]

    return statistics.stdev(values)
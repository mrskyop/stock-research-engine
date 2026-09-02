from decimal import Decimal

def normalize_relative_score(relative_value: float | Decimal) -> float:
    """
    Convert a relative ratio value into a 0-100 score.

    0    = very poor relative position
    50   = roughly equal to sector
    100  = very strong relative position
    """

    relative_value = float(relative_value)

    capped = max(-1.0, min(1.0, relative_value))

    return (capped + 1.0) * 50
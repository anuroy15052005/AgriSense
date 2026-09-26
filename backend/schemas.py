import math


def validate_input(data):

    required_fields = [
        "N",
        "P",
        "K",
        "temperature",
        "humidity",
        "ph",
        "rainfall"
    ]

    for field in required_fields:
        if field not in data:
            return False, f"Missing field: {field}"

        try:
            value = float(data[field])
        except (ValueError, TypeError):
            return False, f"Invalid value for: {field}"

        if not math.isfinite(value):
            return False, f"Invalid value for: {field}"

    return True, None
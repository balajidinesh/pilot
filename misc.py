def convert_percent_to_decimal(percent):
    try:
        # Remove the '%' sign and convert to float
        decimal_value = float(percent)

        # Convert to decimal (e.g., 20% -> 0.20)
        return decimal_value
    except ValueError as e:
        print(f"[convert_percent_to_decimal] error: {e}")
        return None

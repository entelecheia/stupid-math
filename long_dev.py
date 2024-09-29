def stupid_long_div(dividend, divisor):
    """
    Performs long division on the given `dividend` and `divisor` values, returning the quotient and remainder.

    This function implements a step-by-step long division algorithm, printing out the intermediate steps of the division process. It is intended for educational purposes and should not be used for production code that requires efficient division operations.

    Args:
        dividend (int): The number to be divided.
        divisor (int): The number to divide by.

    Returns:
        Tuple[int, int]: The quotient and remainder of the division.
    """
    if divisor == 0:
        return "Error: Division by zero"

    quotient = ""
    remainder = 0
    steps = []

    dividend_str = str(dividend)
    current_dividend = ""

    def guess_quotient(dividend, divisor):
        for i in range(1, 10):
            if i * divisor > dividend:
                return i - 1
        return 9

    for i, digit in enumerate(dividend_str):
        current_dividend += digit
        current_dividend_int = int(current_dividend)

        if current_dividend_int < divisor:
            if i > 0:
                quotient += "0"
            continue

        step_quotient = guess_quotient(current_dividend_int, divisor)
        step_product = step_quotient * divisor
        step_remainder = current_dividend_int - step_product

        quotient += str(step_quotient)
        remainder = step_remainder

        steps.append(
            {
                "current_dividend": current_dividend_int,
                "step_quotient": step_quotient,
                "step_product": step_product,
                "step_remainder": step_remainder,
            }
        )

        current_dividend = str(step_remainder)

    # Print the long division process
    print(f"{dividend} ÷ {divisor}")
    print("-" * 20)

    for i, step in enumerate(steps):
        print(f"Step {i + 1}:")
        print(f"  Current dividend: {step['current_dividend']}")
        print(f"  Quotient digit: {step['step_quotient']}")
        print(f"  Product: {step['step_product']}")
        print(f"  Remainder: {step['step_remainder']}")
        print()

    print(f"Final result: {quotient} R {remainder}")

    return int(quotient), remainder


# Example usage
dividend = 5297
divisor = 43
quotient, remainder = stupid_long_div(dividend, divisor)

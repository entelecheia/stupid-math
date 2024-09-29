# Long Division Algorithm

This repository contains a Python implementation of a long division algorithm. The main script `long_dev.py` provides a function `stupid_long_div` that performs long division and displays the step-by-step process.

## Features

- Performs long division for positive integers
- Displays detailed steps of the division process
- Handles division by zero error
- Returns both quotient and remainder

## Usage

To use the long division function, import it from `long_dev.py` and call it with a dividend and divisor:

from long_dev import stupid_long_div

dividend = 5297
divisor = 43
quotient, remainder = stupid_long_div(dividend, divisor)

The function will print the step-by-step process and return the quotient and remainder.

## Function Details

### `stupid_long_div(dividend, divisor)`

Parameters:

- `dividend`: The number to be divided (integer)
- `divisor`: The number to divide by (integer)

Returns:

- A tuple containing the quotient (integer) and remainder (integer)

Raises:

- Returns an error message string if division by zero is attempted

## Example Output

When running the example in the script:

## 5297 ÷ 43

Step 1:
Current dividend: 52
Quotient digit: 1
Product: 43
Remainder: 9

Step 2:
Current dividend: 99
Quotient digit: 2
Product: 86
Remainder: 13

Step 3:
Current dividend: 137
Quotient digit: 3
Product: 129
Remainder: 8

Final result: 123 R 8

## Notes

This implementation is meant for educational purposes and may not be the most efficient method for performing division in practice.

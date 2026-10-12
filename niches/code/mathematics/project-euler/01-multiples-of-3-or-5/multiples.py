# 01-multiples-of-3-or-5/multiples.py - Sum multiples of 3 or 5
# Usage: python3 multiples.py
#
# Print the answer for numbers below 1000 when run directly

# Add each matching positive number below the limit once
def sum_multiples(limit=1000):
    return sum(
        number
        for number in range(1, limit)
        if number % 3 == 0 or number % 5 == 0
    )


# Print the result without printing anything when this module is imported
if __name__ == "__main__":
    print(sum_multiples())

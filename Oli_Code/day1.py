import sys

product = 1

with open("input.txt") as input:
    numbers = [int(x) for x in input.readlines()]

    for idx1, val1 in enumerate(numbers):
        for idx2, val2 in enumerate(numbers):
            for idx3, val3 in enumerate(numbers):
                if idx1 == idx2 or idx1 == idx3 or idx2 == idx3:
                    continue

                print(f"[{idx1}]:{val1} + [{idx2}]:{val2} + [{idx3}]:{val3}")

                if val1 + val2 + val3 == 2020:
                    print(f"success! {val1}, {val2} and {val3} sum to 2020.")
                    product = val1 * val2 * val3
                    print(f"their product is {product}")
                    sys.exit()

import decimal


def percentage_from(number: decimal, percent: int) -> decimal:
    return (number * percent) / 100

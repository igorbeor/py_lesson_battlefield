from math import exp, fsum, log


def geometric_mean(xs: list) -> float:
    return exp(fsum(log(x) for x in xs) / len(xs))

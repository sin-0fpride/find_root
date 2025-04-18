def find_root_bounds(x, power):
    """
    x: a float, power a positive int
    return low, high such that low*power < x and high*power > x
    """
    low = min(1.0, x)
    high = max(1.0, x)
    return low, high

def bisection_solve(x, power, epsilon, low, high):
    """
    x, epsilon, low, high are floats
    epsilon > 0
    low <= high and there is an ans between low and high such that
        ans**power is within epsilon of x
    Returns ans such that ans**power is within epsilon of x
    """
    ans = (high + low) / 2.0
    while abs(ans**power - x) > epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    return ans

def find_root(x, power, epsilon):
    """
    Assumes x and epsilon int or float, power an int,
    epsilon > 0 & power >= 1
    Returns float y such that y**power is within epsilon of x.
    If such a float does not exist, it returns None.
    """
    if x < 0 and power % 2 == 0:
        return None  # Negative number has no even-powered roots
    low, high = find_root_bounds(x, power)
    return bisection_solve(x, power, epsilon, low, high)
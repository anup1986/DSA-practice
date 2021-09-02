"""
For example, given [0, 1, 3, 4, 9, 50, 75, 200],
lower = 0 and upper = 99,
return ["2", "4->49", "51->74", "76->99"]
"""

def find_missing_range_numbers(a, l, u):
    """
    a is the given list
    lower_bound is the lower range
    upper_bound is the upper range
    :param a: given list
    :param lower_bound: lower range in integer
    :param upper_bound: upper range in integer
    :return:
    """
    # Sanity check
    assert len(a) > 0, "Please enter numbers in the list in ascending order"
    assert u > l, " The u should be less then l. u = upper bound and l = lower bound"
    
    result = []
    for pos, val in enumerate(a):
        if pos < len(a) - 1 and val <= u:
            if pos == len(a) - 2:
                l_val = val
                u_val = a[pos+1]
                diff = u_val - l_val
                if l_val not in [l,u]:
                    if diff > 1:
                        result.append(f"{l_val+1}->{u}")
            else:
                l_val = val
                u_val = a[pos+1]
                if u_val <= 99 and l_val >= 0:
                    if (u_val - l_val) > 1:
                        x = u_val - 1
                        y = l_val + 1
                        if x == y:
                            st = f"{x}"
                        else:
                            st = f"{y}->{x}"
                        result.append(st)
    return result


if __name__ == '__main__':
    a = [0, 1, 3, 9, 50, 75, 201]
    l = 0
    u = 99
    print(find_missing_range_numbers(a, l, u))

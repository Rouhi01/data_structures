import re
import array as arr


def polynomial(poly):
    """Store a polynomial in one-dimensional array"""
    poly = poly.replace(' ', '')
    print(poly)

    terms = re.findall(r'([-+]?\d*)x*\^?(\d*)', poly)
    print(terms)
    max_power = max([int(power) for _, power in terms if power])
    print(max_power)
    array = arr.array('i', [0] * (max_power + 1))
    print(array)

    for multiple, power in terms[:-1]:
        if power:
            if multiple == '+':
                array[int(power)] = 1
            elif multiple == '-':
                array[int(power)] = -1
            else:
                array[int(power)] = int(multiple)
        else:
            array[0] = int(multiple)

    return array


# poly_example = '3x^4 + x^2 - 5'
# print(polynomial(poly_example))

import re
import array as arr


def polynomial(poly):
    """Store a polynomial in one-dimensional array"""
    poly = poly.replace(' ', '')

    terms = re.findall(r'([-+]?\d*)x*\^?(\d*)', poly)

    max_power = max([int(power) for _, power in terms if power])

    array = arr.array('i', [0] * (max_power + 1))

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

def polynomial_2(poly):
    """Store a polynomial in 2 arrays"""
    poly = poly.replace(' ', '')

    terms = re.findall(r'([-+]?\d*)x*\^?(\d*)', poly)

    # handle => 5x == 5x^1
    term = re.findall(r'\b([-+]?\d*)x(?!\^)', poly)
    if term:
        x = term[0]
        i = 0
        for multiple, power in terms[:-1]:
            if power == '' and multiple == x:
                terms[i] = (terms[i][0], '1')
            else:
                i += 1

    powers_array = arr.array("i", [int(power) if power else 0 for _, power in terms[:-1]])

    multiples_array = arr.array("i", [0] * (len(terms) - 1))

    i = 0
    for multiple, power in terms[:-1]:
        """change +/-/'' to 1/-1"""
        if multiple == '+' or multiple == '':
            multiples_array[i] = 1
            i += 1
        elif multiple == '-':
            multiples_array[i] = -1
            i += 1
        else:
            multiples_array[i] = int(multiple)
            i += 1
    return multiples_array, powers_array


# poly_example = 'x^6 - 4x^4 + x^3 + x + 5'
# print(polynomial_2(poly_example))

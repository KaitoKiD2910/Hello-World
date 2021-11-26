from utils.utils import *

if __name__ == '__main__':
    a, b = 15, 7
    c, d = 1.4, 4.5
    result_int = adder_int(a, b)
    result_float = adder_float(a, b)
    print(f'Sum of int {a} + {b} = {result_int}')
    print(f'Sum of float {c} + {d} = {result_float}')
    compare_two_number_int(a, b)

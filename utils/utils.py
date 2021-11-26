def adder_int(a: int, b: int) -> int:
    """
    Day la ham tich tong 2 so ...
    :param a:
    :param b:
    :return:
    """
    result = a + b
    return result


def adder_float(a, b) -> float:
    result = a + b
    return result


def compare_two_number_int(a: int, b: int):
    if a == b:
        print(f'A {a} equals B {b}')
    elif a > b:
        print(f'A {a} greater than B {b}')
    else:
        print(f'A {a} less than B {b}')

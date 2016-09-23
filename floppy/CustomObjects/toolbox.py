from decimal import *


def error_string_to_decimal(string):
    """
    Changes a string number such as 1.23(4) into 1.23 and 0.004.
    :param string: string, wwhich gets converted
    :return: (decimal, decimal), value and error
    """
    string = string.strip()
    value = 0
    error = 0
    if '(' in string:
        precission = string.index('.')
        length = string.index('(')
        value = Decimal(string[:length])
        error = Decimal(string[length+1:-1]) * Decimal(10) ** Decimal(-(length - precission - 1))
    else:
        value = Decimal(string)
    return value, error
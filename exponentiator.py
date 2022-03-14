def exponentitate(x, y):
    """
    :param x: first integer
    :param y: second integetr
    :return: x raised to the y power
    """
    return x ** y


def raise_to_fourth_power(z):
    """
    :param z: integer to be exponetitated
    :return: z raised to the 4th power
    """
    return exponentitate(z, 4)


square = lambda x: exponentitate(x, 2)
cube = lambda x: exponentitate(x, 3)

print(str(square(2)))
print(str(cube(2)))
print(str(raise_to_fourth_power(2)))

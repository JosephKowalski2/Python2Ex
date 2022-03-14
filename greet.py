def greet(name):
    """
    :param name: name
    :return: prints Hello followed by name parameter
    """
    print("Hello " + name)

def name_input():
    """
    :return: name input from user
    """
    return input("Please enter your name \n")

greet(name_input())

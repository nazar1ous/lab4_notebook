from menu import *


if __name__ == "__main__":
    print(Menu)
    menu = Menu()
    print(menu, "This is an object of a class")
    print(menu.__init__, menu.__init__(), "__init__ method of menu object")
    print(menu.__str__, menu.__str__(), "__str__ method of menu object")
    print(dir(menu), len(dir(menu)), "These are all attributes"
                                     " including all methods")
    print(menu.__getattribute__('__init__'), "Getting the __init__ method")
    print(menu.__dict__, "Object in a form of dict")

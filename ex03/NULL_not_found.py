
def NULL_not_found(object: any) -> int:

    typ = type(object)
    name = type(object).__name__
    print(name)
    if name == "NoneType":
        print("Nothing")
    elif isinstance(object, float) and object != object:  # Check for NaN
        return "Cheese: nan <class 'float'>"
    elif object == 0:
        return "Zero: 0 <class 'int'>"
    elif object == '':
        return "Empty: <class 'str'>"
    elif object is False:
        return "Fake: False <class 'bool'>"
    else:
        return "Type not Found"
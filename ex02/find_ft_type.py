
def all_thing_is_obj(object: any) -> int:
        
    name = type(object).__name__
    if (name == "str"):
        print(object, 'is in the ktchen :', type(object))
    elif (name == "int"):
        print("Type not found")
    else: 
        print(name.capitalize(), ":", type(object))
    return 42
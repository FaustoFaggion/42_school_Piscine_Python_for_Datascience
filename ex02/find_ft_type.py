
def all_thing_is_obj(object: any) -> int:
        
    name = type(object).__name__
    if (name == "str"):
        print(object, 'is in the ktchen :', type(object))
        return 42
    if (name == "int"):
        print("Type not found")
        return 42
     
    print(name.capitalize(), ":", type(object))
    return 42
import inspect

def NULL_not_found(object: any) -> int:

    # Get the current frame and the caller's local variables
    frame = inspect.currentframe()
    try:
        # print(frame.f_back.f_globals)
        caller_locals = frame.f_back.f_locals
        # Find the variable name that matches the value
        var_name = [name for name, value in caller_locals.items() 
                    if value is object and not name.startswith("__")]
        
        if (not var_name):
            print('Type not Found')
            return 1
        else:
            response = var_name[0] + ":"
    finally:
        del frame  # Clean up to avoid reference cycles
    
    print(response, object, type(object))
    return 0

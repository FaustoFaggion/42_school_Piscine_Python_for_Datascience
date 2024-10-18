def callLimit(limit: int):
    count = 0
    def callLimiter(function):

        def limit_function(*args: any, **kwds: any):
            return print("haha")
    
        return limit_function
    
    return callLimiter
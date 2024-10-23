def callLimit(limit: int):
    count = 0
    def callLimiter(function):

        def limit_function(*args: any, **kwds: any):
            nonlocal count
            if count >= limit:
                print("Error: call too many times")
                return
            function()
            count += 1
            print("count ", count)
    
        return limit_function
    
    return callLimiter
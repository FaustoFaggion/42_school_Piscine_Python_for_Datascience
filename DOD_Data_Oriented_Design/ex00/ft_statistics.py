import numpy as np

def ft_statistics(*args: any, **kwargs: any) -> None:
    
    
    for kwarg in kwargs.values():
        if len(args) == 0:
            print("ERROR")
        elif str(kwarg).lower() == "mean":
            print(f"mean: {np.mean(args)}")
        elif str(kwarg).lower() == "median":
            print(f"median: {np.median(args)}")
        elif str(kwarg).lower() == "quartile":
            print(f"quantile: {np.quantile(args, .50)}")
        elif str(kwarg).lower() == "std":
            print(f"std: {np.std(args)}")
        elif str(kwarg).lower() == "var":
            print(f"var: {np.var(args)}")
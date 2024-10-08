
class Calculator:

    def __init__(self) -> None:
        pass
        
    def dotproduct(V1:list[float], V2: list[float]) -> None:
        
        assert len(V1) == len(V2), "List must have the same length" 

        lst = [a * b for a, b in zip(V1, V2)]
        result = sum(lst)
        return print(f"The scalar product is: {result}")
    
    # add_vec(V1:list[float], V2: list[float]) -> None:
    #     pass

    # sous_vec(V1: list[float], V2: list[float]) -> None:
    #     pass
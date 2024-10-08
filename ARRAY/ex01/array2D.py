import numpy as np

def slice_me(family: list, start: int, end: int) -> list:

    assert isinstance(family, list), "is not a list"
    
    for elem in family:
        assert isinstance(elem, list), "element is not a list"
        assert np.ndim(family[0]) == np.ndim(elem), "lists have different lengths"
        assert len(family[0]) == len(elem), "lists have different lengths"

    arr = np.array(family)
    print(f"My shape is: {arr.shape}")
    new_arr = arr[start:end]
    print(f"My new shape is {new_arr.shape} {new_arr}")
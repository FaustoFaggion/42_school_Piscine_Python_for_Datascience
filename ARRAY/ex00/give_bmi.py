
def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    #BMI=weight in kilograms / (height in meters)2​
    height_pow = [pow(elem, 2) for elem in height]
    return [a / b for a, b in zip(weight, height_pow)]

def apply_limit(bmi: list[int, float], limit: int) -> list[bool]:
    return [elem > limit for elem in bmi]
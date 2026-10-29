def add(a, b, c):
    res = a + b + c
    return res

# call function
# print(add(1, 2, 3))

def addition(nums):
    """Return sum of all the numbers passed as arguments
    parameters:
    integers or floats or a mix of integers and floats
    Returns:
        """
    total = sum(nums)
    return total

# print(addition([1, 2, 3]))

def build_profile(kwargs):
    for k, w in kwargs.items():
        print(f"{k} : {w}")

def fancy_functions(name, nums, kwargs):
    print(name)
    print(nums)
    print(kwargs)

# def square(num):
#     return num * num
#
# result = square(5)
# print(result)

square = lambda num: num * num
print(square(5))
res = square(2.9)
print(res)

surface_area_cylinder = lambda r, h: 22/7 * r ** 2 * 2 + 22 / 7 *2 * r * h
print(surface_area_cylinder(7, 20))

people = [
    {"name": "Alex", "age": 30},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 33},
]

sorted_by_age = sorted(people, key=lambda x: x["age"])
print(sorted_by_age)
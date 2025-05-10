def division(a,b): 
    try: return f"{a}/{b} = {a/b}"
    except TypeError: return "Error: Unsupported type(s) for division!"
    except ZeroDivisionError: return "Error: Division by 0!"
print(division(10, 2))
print(division("10", 2))
print(division(10, 0))
print(division(10, "b"))
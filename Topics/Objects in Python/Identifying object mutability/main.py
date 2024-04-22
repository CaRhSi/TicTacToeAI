def is_mutable(obj):
    try:
        # Attempt to modify the object
        obj.__hash__()
        return 'Immutable'
    except TypeError:
        return 'Mutable'


# Input handling
input_str = input().strip()
# Attempt to evaluate the input string
try:
    input_obj = eval(input_str)
except:
    input_obj = input_str

result = is_mutable(input_obj)
print(result)

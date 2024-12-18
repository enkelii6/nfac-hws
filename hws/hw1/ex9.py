def is_even(x):
    if type(x) != int:
        return False
    return x % 2 == 0

a = 78
b = 9
c = -9.5
d = "LVII"

print(is_even(a))
print(is_even(b))
print(is_even(c))
print(is_even(d))

def swap_first_last(s):
    if len(s) <= 1:
        return s
    return s[-1] + s[1:len(s)-1] + s[0]

a = "0123456789"
b = "No"
c = "7"

print(swap_first_last(a))
print(swap_first_last(b))
print(swap_first_last(c))

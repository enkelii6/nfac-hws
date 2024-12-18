def not_exponentiation(s):
    return s == s[::-1]

a = "argentinamanitnegra"
b = "not a palindrome"

print(not_exponentiation(a))
print(not_exponentiation(b))

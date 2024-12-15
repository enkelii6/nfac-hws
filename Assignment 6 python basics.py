# Ex1
num1, num2  = 5, 7
print("Sum:", num1 + num2)

# Ex2
original_string = "hello"
reversed_string = original_string[::-1]
print("Reversed String:", reversed_string)

# Ex3
string_to_measure = "hello world"
string_length = len(string_to_measure)
print("String Length:", string_length)

# Ex4
string1 = "hello"
string2 = " world"
concatenated_string = string1 + string2
print("Concatenated String:", concatenated_string)

# Ex5
char = 'a'
is_vowel = char.lower() in 'aeiou'
print("Is Vowel:", is_vowel)

# Ex6
string_to_swap = "hello"
if len(string_to_swap) > 1:
    swapped_string = string_to_swap[-1] + string_to_swap[1:-1] + string_to_swap[0]
else:
    swapped_string = string_to_swap
print("Swapped String:", swapped_string)

# Ex7
string_to_upper = "hello world"
uppercase_string = string_to_upper.upper()
print("Uppercase String:", uppercase_string)

# Ex8
length = 5
width = 3
area = length * width
print("Rectangle Area:", area)

# Ex9
number = 10
is_even = number % 2 == 0
print("Is Even:", is_even)

# Ex10
string_to_extract = "hello"
first_three = string_to_extract[:3]
print("First Three Characters:", first_three)

# Ex11
name = "Alice"
age = 30
message = f"My name is {name} and I am {age} years old."
print("Message:", message)

# Ex12
string_to_slice = "hello world"
sliced_string = string_to_slice[2:6]
print("Sliced String:", sliced_string)

# Ex13
number_as_string = "123"
converted_number = int(number_as_string)
print("Converted Number:", converted_number)

# Ex14
string_to_repeat = "hello"
repeated_string = string_to_repeat * 3
print("Repeated String:", repeated_string)

# Ex15
num1 = 10
num2 = 3
quotient = num1 // num2
remainder = num1 % num2
print("Quotient:", quotient)
print("Remainder:", remainder)

# Ex16
num1 = 10
num2 = 4
float_division_result = num1 / num2
print("Float Division Result:", float_division_result)

# Ex17
string_to_check = "hello"
count_of_l = string_to_check.count('l')
print("Count of 'l':", count_of_l)

# Ex18
escaped_string = "She said \"Hello\" to everyone."
print("Escaped String:", escaped_string)

# Ex19
multi_line_string = """This is a
multi-line
string."""
print("Multi-line String:", multi_line_string)

# Ex20
base = 2
exponent = 3
exponentiation_result = base ** exponent
print("Exponentiation Result:", exponentiation_result)

# Ex21
palindrome_string = "acae"
is_palindrome = palindrome_string == palindrome_string[::-1]
print("Is Palindromic:", is_palindrome)

# Ex22
string1 = "listen"
string2 = "silent"
are_anagrams = sorted(string1.lower()) == sorted(string2.lower())
print("Are Anagrams:", are_anagrams)
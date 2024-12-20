"""
💎 Exercise-1 (Longest Consecutive Sequence):
Write a function "longest_consecutive(my_list: list[int]) -> int" that takes a 
list of integers and returns the length of the longest consecutive elements 
sequence in the list. The list might be unsorted.

Example:

longest_consecutive([100, 4, 200, 1, 3, 2]) -> 4
"""

def longest_consecutive(my_list: list[int]) -> int:
    my_list.sort()
    combo = 0
    max_combo = 0

    for i in range(len(my_list)):
        if i == 0 or my_list[i] != my_list[i - 1]:
            combo += 1
        if i == len(my_list) - 1 or my_list[i] + 1 < my_list[i + 1]:
            max_combo = max(combo, max_combo)
            combo = 0

    return max_combo
        

"""
💎 Exercise-2 (Find missing number):
Write a function "find_missing(my_list: list[int]) -> int" that takes a 
list of integers from 1 to n. The list can be unsorted and have one 
number missing. The function should return the missing number.

Example:

find_missing([1, 2, 4]) -> 3
"""

def find_missing(my_list: list[int]) -> int:
    n = len(my_list) + 1
    
    match n % 4:
        case 0:
            xor = n
        case 1:
            xor = 1
        case 2:
            xor = n + 1
        case _:
            xor = 0

    for i in my_list:
        xor ^= i

    if xor == n:
        return None

    return xor


"""
💎 Exercise-3 (Find duplicate number):
Write a function "find_duplicate(my_list: list[int]) -> int" that takes a list 
of integers where each integer is in the range of 1 to n (n is the size of the list). 
The list can have one number appearing twice and the function should return this number.

Example:

find_duplicate([1, 3, 4, 2, 2]) -> 2
"""

def find_duplicate(my_list: list[int]) -> int:
    n = len(my_list) - 1
    
    match n % 4:
        case 0:
            xor = n
        case 1:
            xor = 1
        case 2:
            xor = n + 1
        case _:
            xor = 0

    for i in my_list:
        xor ^= i

    return xor


"""
💎 Exercise-4 (Group Anagrams):
Write a function "group_anagrams(words: list[str]) -> list[list[str]]" that 
takes a list of strings (all lowercase letters), groups the anagrams together, 
and returns a list of lists of grouped anagrams.

An Anagram is a word or phrase formed by rearranging the letters of 
a different word or phrase, typically using all the original letters exactly once.

group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) 
-> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
"""

def group_anagrams(words: list[str]) -> list[list[str]]:
    anams = dict()
    for i in words:
        s = ''.join(sorted(i))
        if not(anams.get(s)):
            anams[s] = []
        anams[s].append(i)

    result = []
    for (key, val) in anams.items():
        result.append(val)

    return result


    

def check_anagrams(s, t):
    cnt = [0] * 26 #assuming that strings contain only english letters
    for i in s:
        cnt[ord(i.lower()) - ord('a')] += 1
    for i in t:
        cnt[ord(i.lower()) - ord('a')] -= 1

    return cnt.count(0) == 26

a = "spar"
b = "rasp"

print(check_anagrams(a, b))

a = "abacaba"
b = "aaabbc"

print(check_anagrams(a, b))

a = "RASPberry"
b = "beRRyspar"

print(check_anagrams(a, b))

a = "Bababooey"
b = "bobobaaet"

print(check_anagrams(a, b))

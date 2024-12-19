# 💎 Exercise 22: check-anagrams
#
# Declare 2 strings
# Check if the strings are anagrams (ignoring case)
# Print the result
#
# *Anagram - a word, phrase, or name formed by rearranging the letters of another, such as spar, formed from rasp.

def solution(word1, word2):
    return sorted(word1) == sorted(word2)

print(solution('lfywlaqpgotebagxokgwflwnhijvmhbsarrqxohpswofzbtyjfxszfbtsmytouybtyuuiydjduqnbngntxoftfjstfgcrcomuzql', 'lfywlaqpgotebagxokgwflwnhijvmhbsarrqxohpswofzbtyjfxszfbtsmytouybtyuuiydjduqnbngntxoftfjstfgcrcomuzqq'))

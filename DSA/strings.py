# Reverse a string without using [::-1].
name = "manoj"
result = ""
for i in name:
    result = i + result
print(result)    
# Check if two strings are anagrams (same letters, different order).
s1 = "silent"
s2 = "listen"
if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not anagram")    
# Find first non-repeating character in a string.
s = "understand"
for i in s:
    if s.count(i) ==1 :
        print(i)
# Remove all duplicates from a string keeping order.
s = "banana"
result = ""
for i in s:
    if i not in result:
        result +=i
print(result)        
# Check if string is palindrome ignoring case and non-alphanumeric chars.
s = "civic"
result = ""
for i in s:
    if i.isalnum():
     result +=i.lower()
if result == result[:: -1]:
        print("is polindrome")    
else:
        print("not a polindrome")    
# Find longest substring without repeating characters.
# Count frequency of each character in a string.
# Implement string compression ("aabcccccaaa" → "a2b1c5a3").
# Check if one string is rotation of another ("abcde" → "cdeab").
# Find all substrings that are palindromes in a string.
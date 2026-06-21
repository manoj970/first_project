def reverse_string(s):
    i, j = 0, len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    print(s)
reverse_string(["h","e","l","l","o"])        



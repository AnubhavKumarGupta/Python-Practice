def pangrams(s):
    # s.strip()
    # s = set(s)

    # if len(s) == 26:
    #     return "pangram"
    # else:
    #     return "not pangram"

    s = set(s)
    s.discard(" ")
    return "pangram" if len(s) == 26 else "not pangram"


s = "The quick brown fox jumps over the lazy dog"

print(pangrams(s))

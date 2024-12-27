def numberOfSpecialChars(word) -> int:
    special_chars = set()
    lowercase_seen = set()
        
    for char in word:
        if char.lower() == char.upper():
            continue
        if char.lower() not in lowercase_seen:
            lowercase_seen.add(char.lower())
        elif char.lower() in lowercase_seen and char.upper() == char:
            special_chars.add(char.lower())
        
    return len(special_chars)

s =  "AbBCab"
print(numberOfSpecialChars(s))
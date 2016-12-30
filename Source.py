words = ["apple", "pear"]

def unique(string):
    char_set = [False for _ in range(128)]
    for char in string:
        val  = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True

    return True

for w in words:
    print(unique(w))

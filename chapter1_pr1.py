def has_unique_char(string):
    alph = [False for x in range(129)]

    for char in string:
        if(alph[ord(char)]):
            return False
        alph[ord(char)] = True

    return True

print(has_unique_char('apple'))
print(has_unique_char('pear'))

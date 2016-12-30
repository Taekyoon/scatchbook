
def is_able_palindrome_permutation(string):
    alph = [0 for i in range(129)]

    for char in string:
        char_ascii = ord(char)

        if(char_ascii is not ord(' ')):
            alph[char_ascii] += 1

    odd_count = 0
    for num in alph:
        if num % 2 is 1:
            odd_count += 1
            if odd_count > 1:
                return False

    return True

print(is_able_palindrome_permutation('tacyyt coa'))


def compress_string(string):
    ret = ''
    pre_char = ''

    count = 1
    for char in string:
        if(pre_char != '' and pre_char != char):
            ret += pre_char + str(count)
            pre_char = char
            count = 1
        elif(pre_char == char):
            count += 1
        elif(pre_char == ''):
            pre_char = char

    ret += pre_char + str(count)

    return ret

print(compress_string('aabcccccaaa'))

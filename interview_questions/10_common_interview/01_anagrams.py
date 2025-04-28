'''

Annagram maker



An anagram is when 2 or more words all have the same occurances of the same letters


Example EOD and doe
'''
def is_anagram(s1, s2):
    s1_dict = {}
    s2_dict = {}

    for letter in s1:
        if letter not in s1_dict:
            s1_dict[letter] = 1
        else:
            s1_dict[letter] += 1

    for letter in s2:
        if letter not in s2_dict:
            s2_dict[letter] = 1
        else:
            s2_dict[letter] += 1

    print(s1_dict)
    print(s2_dict)
    return s1_dict == s2_dict


if __name__ == '__main__':
    print(is_anagram('eod','doe'))


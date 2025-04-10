def vowel_counter(string):
    """
    :param string:
    :return: Number of vowels in string:
    """
    vowels = 0 #Start w/ 0 vowels
    for char in string:
        if char in 'aeiou':
            vowels += 1
    return vowels

def rev_string(string):
    """
    :param string:
    :return string in reverse order without non-alpha characters:
    """
    for i in string:
        if not i.isalpha():
            string = string.replace(i, '')
    if len(string) <= 1:
        return string
    return rev_string(string[1:]) + string[0]

def palindrome_checker(string):
    """
    :param string:
    :return True if string is palindrome, False otherwise--ignores non alpha characters:
    """
    for i in string:
        if not i.isalpha():
            string = string.replace(i, '')
    rev = rev_string(string)
    if len(string) <= 1:
        return True
    if rev == string:
        print(string)
        return True
    else:
        return False



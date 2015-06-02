""" Implement an algorithm to determine if a string has all unique characters.
What if you can not use additional data structures? """


def main(string):
    # Assuming checker is a 26 bit number
    # and assuming that only chars from 'a' to 'z' can occur
    # Each bit position in checker corresponds to one character
    checker = 0
    for s in string:
        val = ord(s) - ord('a')  # gets us a number between 0 and 26
        # 1 << val is shifting 1 val times i.e.
        # setting the val'th bit of checker to 1
        # it is was already 1 (the & check) then it has a duplicate character
        # hence we return False
        if (checker & (1 << val)) != 0:
            return False
        # Else we set the val'th bit of checker for future checks
        else:
            checker |= (1 << val)
    return True


if __name__ == '__main__':
    assert main('sas') is False
    assert main('abcd') is True

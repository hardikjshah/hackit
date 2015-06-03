"""Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become
a2blc5a3. If the "compressed" string would not become smaller than the original
string, your method should return the original string."""


def compress_string(string):
    compressed_string = ""
    curr_char = string[0]
    curr_count = 1  # Maintains the repetition count of the current character
    for c in string[1:]:
        if c == curr_char:
            curr_count += 1  # incr counter if same char
        else:
            # else add to the compressed string char+count
            # and reset
            compressed_string += "%s%d" % (curr_char, curr_count)
            curr_char = c
            curr_count = 1

    # need to do it once more for the last character
    compressed_string += "%s%d" % (curr_char, curr_count)

    # compare to original string
    # Note: we can be more efficient about counting length of compressed
    # string as we iterate through the for loop
    if len(compressed_string) < len(string):
        return compressed_string
    else:
        return string


if __name__ == '__main__':
    assert compress_string('aabcccccaaa') == "a2b1c5a3"
    assert compress_string('abcde') == 'abcde'

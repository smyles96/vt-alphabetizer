#!/usr/bin/env python3

from sys import argv, stdin, stdout

'''
def _merge_sort(input_string):
    # Perform a stable recursive merge sort on the given string

    sublist_len = len(input_string)

    # Base cases
    if sublist_len == 0:
        # Empty string was entered
        return ''
    elif sublist_len == 1:
        # Sublist with one element reached

        # Count non-alphanumeric characters as empty strings.
        return input_string if input_string.isalpha() else ''
    
    # Split the sublist recursively
    mid_index = sublist_len // 2
    
    left_side = _merge_sort(input_string[:mid_index])
    right_side = _merge_sort(input_string[mid_index:])

    # Now merge both sublists
    merged = ""

    left_index = 0
    right_index = 0

    left_side_len = len(left_side)
    right_side_len = len(right_side)

    # Loop until either sublist reaches its last index
    while left_index < left_side_len and right_index < right_side_len:
        left_char = left_side[left_index].lower()
        right_char = right_side[right_index].lower()

        if left_char <= right_char:
            # Left side char comes before, or is same as, right side
            merged += left_side[left_index]
            left_index += 1
        else:
            # Right side char comes before left
            merged += right_side[right_index]
            right_index += 1

    # Append any remaining elements one of the sublists may have
    while left_index < left_side_len:
        merged += left_side[left_index]
        left_index += 1

    while right_index < right_side_len:
        merged += right_side[right_index]
        right_index += 1

    return merged


def alphabetize(input_string):
    # Alphabetize the characters in the given string using merge sort
    return _merge_sort(input_string)
'''

def alphabetize(input_str):
    ''' Alphabetize the characters in the given string using TimSort '''

    # Change input_str into a list and remove non-letters in the process
    # Then do an in-place sort (saves memory) by comparing the letters
    # based on their lowercase values
    filtered_list = [char for char in input_str if char.isalpha()]
    filtered_list.sort(key = str.lower)

    return "".join(filtered_list)

if __name__ == "__main__":
    if len(argv) > 1:
        print('''
        Alphabetizer Program
        Usage:
            ./alphabetizer.py
        Summary:
            Starts the program and continues to ask for strings
            to alphabetize until CTRL-C is pressed.
        Returns:
            Upon entering a string, the program outputs the
            letters of that string in alphabetical order.

            Non-letter characters are discarded in the
            process.
        Examples:
            ./alphabetizer.py
               Enter a string to alphabetize (or CTRL-C to stop): Virginia Tech
               aceghiiinrTV
               Enter a string to alphabetize (or CTRL-C to stop): 3 Blind Mice
               BcdeiilMn
               Enter a string to alphabetize (or CTRL-C to stop): Turtle
               elrTtu
               Enter a string to alphabetize (or CTRL-C to stop): <CTRL-C>
               Exiting...
        ''')

        exit(0)

    try:
        while True:
            input_str = input("Enter a string to alphabetize (or CTRL-C to stop): ")
            print(alphabetize(input_str))
            
    except (EOFError, KeyboardInterrupt):
        # EOFError raised when a a file that is piped in as stdin is closed
        pass
    finally:
        print("\nExiting...")
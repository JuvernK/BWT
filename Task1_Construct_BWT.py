import sys

def cyclic_rotations(s):
    '''
    This is a naive approach to build cyclic rotations of given string s.
    You may consider more efficient approach for this task.
    '''

    # append the input string with terminal $
    s = s + '$'
    # Create a list to hold all the cyclic rotations
    rotations = []
    # Loop through each character of the string and add it to the end of the string
    for i in range(len(s)):
        rotations.append(s[i:] + s[:i])

    # Return the list of cyclic rotations
    return rotations

def bwt(s):
    '''
    This is a BWT implementation which uses a naive approach to find the Suffix Array.
    You may consider more efficient approach such as prefix-doubling or Ukonnen's algorithm
    '''

    # Get all the cyclic rotations of the string
    rotations = cyclic_rotations(s)
    # Sort the cyclic rotations in lexicographic order
    sorted_rotations = sorted(rotations)
    # Get the last character of each cyclic rotation and join them together to get the BWT
    bwt = ''.join([rotation[-1] for rotation in sorted_rotations])

    # Create a list of the starting indices of the sorted rotations
    suffix_arr = []
    for rotation in sorted_rotations:
        suffix_arr.append(rotations.index(rotation))     # Since $ is unique in all cyclic rotations, we can use .index to get the index of the rotation 

    return bwt, suffix_arr



if __name__ == '__main__':
    # Read file
    _, filename = sys.argv
    f = open(filename)
    string = f.read()
    f.close()

    print('Input String: ', string)

    # Construct BWT String (Naive Approach)
    bwt_str, suffix_arr = bwt(string)

    # write BWT string to file
    f = open("bwt_string.txt", "w")
    n = f.write(bwt_str)
    f.close()

    # print results
    print('Str: ', string)
    print('BWT: ', bwt_str)
    print('SA :' , suffix_arr)






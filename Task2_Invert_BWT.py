import sys
def compute_rank(bwt_string: str):
	# build the noccurrence_exclusive array
    # noccurrence_exclusive[i] stores the number of times bwt_string[i] occurs before position i
    nOccurrence= [[0] * len(bwt_string) for _ in range(91)]    
    frequency = [0]*91  # Where frequency[0] will be "$"
    rank = [None] * 91  # build a rank array using frequency, O(91)
    for i in range(len(bwt_string)):
        char = bwt_string[i]
        pos = ord(char) - 36
        frequency[pos] += 1   
        if i < len(bwt_string) - 1:
            nOccurrence[pos][i+1] = frequency[pos]


    unique_chars_set = set(bwt_string)  # O(N), N is the length of bwt_string
    for chars in unique_chars_set:
        pos = ord(chars) - 36
        for i in range(1, len(bwt_string)):
            if nOccurrence[pos][i-1] > nOccurrence[pos][i]:
                nOccurrence[pos][i] = nOccurrence[pos][i-1]

    rank[0] = 1
    prev_freq = 1
    prev_rank = 1
    for i in range(1, len(frequency)):
        if frequency[i] > 0:
            rank[i] = prev_freq + prev_rank
            prev_freq = frequency[i]
            prev_rank = rank[i]

    return rank, nOccurrence, frequency


def invert_bwt(bwt_string):
    """
    time complexity: O(N) where N is the length of the bwt_string
    space complexity: O(N) for noOcurrence array, rank and text
    Assumption: bwt_string contains only printable ASCII characters from 36(inclusive) to 126(inclusive) 
    """
    rank, nOccurrence, _ = compute_rank(bwt_string)

    # LF mapping implementation
        # pos = rank[x] + nOccurrence[x] -1
    text = "$" # this is used to reconstruc the original string in reverse give BWT
    pos = 0
    while bwt_string[pos] != "$":
        text = bwt_string[pos] + text
        pos = rank[ord(bwt_string[pos]) - 36] + nOccurrence[ord(bwt_string[pos]) - 36][pos] - 1

    return text

bwt_str = "enhbaalsbua$"
rank, nOcc, freq = compute_rank(bwt_str)
# uniq = set(bwt_str)
# for c in uniq:
#     print("Char: {}, Rank: {}, Occ: {}".format(c ,rank[ord(c) - 36], nOcc[ord(c) - 36]))
print(invert_bwt(bwt_str))

# if __name__ == '__main__':
#     # Read file containing BWT string (from Task-1)
#     _, filename = sys.argv
#     f = open(filename)
#     bwt_str = f.read()
#     f.close()

#     # Invert BWT String (LF-Mapping)
#     string = invert_bwt(bwt_str)
#     print("Inverted String: {}".format(string))
#     # write BWT string to file
#     f = open("recovered.txt", "w")
#     n = f.write(string)
#     f.close()

#     # print results
#     print('BWT: ', bwt_str)
#     print('Str: ', string)


import sys
from Task1_Construct_BWT import bwt

def compute_rank(bwt_string: str):
	# build the noccurrence_exclusive array
    # noccurrence_exclusive[i] stores the number of times bwt_string[i] occurs before position i
    nOccurrence= [[0] * (len(bwt_string)+1) for _ in range(91)]    
    frequency = [0]*91  # Where frequency[0] will be "$"
    rank = [None] * 91  # build a rank array using frequency, O(91)
    for i in range(len(bwt_string)):
        char = bwt_string[i]
        pos = ord(char) - 36
        frequency[pos] += 1   
        if i < len(bwt_string) - 1:
            nOccurrence[pos][i+1] = frequency[pos]
    # Take into account of last character
    nOccurrence[ord(bwt_string[-1]) - 36][len(bwt_string)] = frequency[ord(bwt_string[-1]) - 36]

    rank[0] = 0
    prev_rank = 0
    prev_freq = 1
    for i in range(1, len(frequency)):
        if frequency[i] > 0:
            rank[i] = prev_freq + prev_rank
            prev_freq = frequency[i]
            prev_rank = rank[i]

    unique_chars_set = set(bwt_string)  # O(N), N is the length of bwt_string
    for chars in unique_chars_set:
        pos = ord(chars) - 36
        # print("Char: {}, Rank: {}".format(chars, rank[pos]))
        # Carry the value in nOcccurance to the end
        for i in range(1, len(bwt_string)+1):
            if nOccurrence[pos][i-1] > nOccurrence[pos][i]:
                nOccurrence[pos][i] = nOccurrence[pos][i-1]


    return rank, nOccurrence, frequency


def bwt_pattern_matching(pattern, bwt_str, suff_arr):
    '''
    This implementation make use of previously constructed BWT string and Suffix Array. 
    You need to compute the Rank array and nOccurrence_exclusives array to be used in the update process
    of the pointers sp and ep.
    '''
    print("Bwt: {}, Suff: {}".format(bwt_str, suff_arr))

    sp = 0 # initial sp
    ep = len(bwt_str) - 1 # initial ep
    i = len(pattern) - 1 # pointer to iterate over pat chars reversely 
    res = []
    rank, nOccurrence, _ = compute_rank(bwt_str)

    # uniq = set(bwt_str)
    # for c in uniq:
    #     print("Char: {}, Rank: {}, Occ: {}".format(c ,rank[ord(c) - 36], nOccurrence[ord(c) - 36]))

    while sp <= ep:
        # You may need another helper function to compute the "cumulative nOccurrences" of a given char in the Last column. 
        # Make sure to return the pat occurences from suff_arr. If pat is not existed, return empty list. 
        if i >= 0:
            char = pattern[i]
            pos = ord(char) - 36
            # Check if the char exists
            if rank[pos] == None:
                return "No pattern matched"
            sp = rank[ord(char) - 36] + nOccurrence[ord(char) - 36][sp] 
            ep = rank[ord(char) - 36] + nOccurrence[ord(char) - 36][ep + 1] - 1
            print("Sp: {}, Ep: {}".format(sp, ep))
            # When they overlap, if suffix array is > i, it means the len of text for comparison is smaller than the pattern, hence not possible to match
            # if sp == ep and suff_arr[sp] < i:
            #     return "No pattern matched"
            i -= 1
        else:
            res = suff_arr[sp:ep+1]
            break

    return res  # return the position of pat in the original string

ori_text = "panamabanana"
pat = "an"

# text= "panamabanana"
# bwt_str, suff_arr = bwt(text)
# r, Occ_exclu, Occ_inclue = compute_rank(bwt_str)

# for index, value in enumerate(r):
#     if value != None:
#         print("Char: {}, Rank: {}".format(chr(index+36), value))


# ori_text = "abaaaababa" 
# pat = "aba"

s_bwt, s_suffix_arr = bwt(ori_text)
# print(s_bwt, s_suffix_arr)
print(bwt_pattern_matching(pat, s_bwt, s_suffix_arr))


# if __name__ == '__main__':
#     # Read files containing string and pattern
#     _, str_filename, pat_filename = sys.argv
#     # Read string file
#     f = open(str_filename)
#     string = f.read()
#     f.close()
#     # Read pattern file
#     f = open(pat_filename)
#     pattern = f.read()
#     f.close()

#     # Construct BWT String (Naive Approach)
#     bwt_str, suffix_arr = bwt(string)

#     # Run pattern matching algorithm
#     pat_occurences = bwt_pattern_matching(pattern, bwt_str, suffix_arr)

#     # write Pattern occurences to file
#     output_file = open("output.txt", "w")
#     output_file.write('\n'.join([str(i) for i in pat_occurences]))
#     output_file.close()

#     # print results
#     print('str: ', string)
#     print('pat: ', pattern)
#     print('occ: ', pat_occurences)






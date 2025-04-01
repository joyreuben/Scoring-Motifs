# Insert your Count(Motifs) function here from the last Code Challenge.
def Count(Motifs):
    count = {} # initializing the count dictionary
    # your code here
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

# Input:  A list of kmers Motifs
# Output: the profile matrix of Motifs, as a dictionary of lists.
def Profile(Motifs):
    t = len(Motifs)
    profile = {}
    k = len(Motifs[0])
    count = Count(Motifs)
    num_motifs = len(Motifs)
    # insert your code here
    profile = {nucleotide: [] for nucleotide in count.keys()}  
    for nucleotide in count:  
        profile[nucleotide] = [count[nucleotide][i] / num_motifs for i in range(len(count[nucleotide]))]  

    return profile  

if _name_  == "__main__":  
    motifs = [  
        "AACGTA",  
        "CCCGTT",  
        "CACCTT",  
        "GGATTA",  
        "TTCCGG"  
    ]  
    profile_matrix = Profile(motifs)  
    print(profile_matrix)  
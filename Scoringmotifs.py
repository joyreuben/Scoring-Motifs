def Consensus(Motifs):
    # insert your code here
    k = len(Motifs[0])
    count = Count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus
# Copy your Count(Motifs) function here.
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
# Input:  A set of k-mers Motifs
# Output: The score of these k-mers.
def Score(Motifs):
    # Insert code here
    consensus_string = Consensus(Motifs) # Use the existing Consensus function  
    score = 0  
    k = len(Motifs[0])
    t = len(Motifs)
    for j in range(k):
        for i in range(t):
            if Motifs[i][j] != consensus_string[j]:
                score += 1
    return score

if __name__ == "__main__":
    sample_input = ["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"]
    result = Score(sample_input)
print(result)


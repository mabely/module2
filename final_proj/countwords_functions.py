# ?? IS THE WAY COUNTS HAS BEEN INITIALISED WITH FUNCTION CALL IN MAIN CORRECT?

# counts = {}

# counts num of occurrences of words into dict
def count_words(input_txt):
    counts = {}
    for sentence in input_txt:
        list = sentence.split()
        for word in list:
            word.strip()
            # print(word)
            # if word 
                if word not in counts:
                    counts[word] = 1
                else:
                    counts[word] += 1
    # print(counts)
    return counts

# retrieves top 20 of a dict
def print_top20(counts):
    # counts = count_words(input_txt)
    counts_sorted = sorted(counts.items(), key=lambda kv:kv[1], reverse=True)
    # print(counts_sorted)
    print(counts_sorted[0:5])


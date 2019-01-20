# counts num of occurrences of words into dict
def count_words(input_file, input_stop_file):
    # specifies the path of the file to be analysed
    path = 'text_data/{}'.format(input_file)
    input_txt = open(path, 'r')
    stop_words_list = read_stop_words(input_stop_file)

    counts = {}
    stop_words_count = 0

    for sentence in input_txt:
        txt_words = sentence.split()
        for word in txt_words:
            word = word.strip()
            # print(word)
            if word not in stop_words_list:
                if word not in counts:
                    counts[word] = 1
                else:
                    counts[word] += 1
            elif word in stop_words_list:
                stop_words_count += 1

    # print(counts)
    return counts

# retrieves top 20 of a dict
def print_top20(counts):
    counts_sorted = sorted(counts.items(), key=lambda kv:kv[1], reverse=True)
    # returns top 20 in a list without num of occurrences
    top20 = []
    for item in counts_sorted[0:20]:
        top20.append(item)
    return top20

# returns list of stripped stop words
def read_stop_words(input_stop_file):
    path = 'text_data/{}'.format(input_stop_file)
    input_stop_txt = open(path,'r')
    stop_words_list = []
    for word in input_stop_txt:
        word = word.rstrip()
        stop_words_list.append(word)
    return stop_words_list

def similarity(original_txt, comparison_txt, input_stop_file):
    original_txt = count_words(original_txt, input_stop_file)
    comparison_txt = count_words(comparison_txt, input_stop_file)
    # to find number of overlapping words in the 2 dicts
    overlap_count = 0
    for key in original_txt:
        if key in comparison_txt:
            overlap_count += 1
    # to compute similarity score
    score = float(overlap_count) / (len(original_txt) + len(comparison_txt) - overlap_count)
    print('{:.3f}'.format(round(score, 3)))
    return score




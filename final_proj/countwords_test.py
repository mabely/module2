from countwords_functions import *

def main(input_file, input_stop_file):
    counts = count_words(input_file, input_stop_file)
    top20 = print_top20(counts)
    read_stop_words(input_stop_file)
    print(top20)
    return counts, top20

# when function called, name of txt file needs to be given as arg
# main('mobydick.txt', 'stopwords.txt')

similarity('george01.txt', 'george02.txt', 'stopwords.txt')
similarity('george01.txt', 'george03.txt', 'stopwords.txt')
similarity('george01.txt', 'george04.txt', 'stopwords.txt')
similarity('george02.txt', 'george03.txt', 'stopwords.txt')
similarity('george02.txt', 'george04.txt', 'stopwords.txt')
similarity('george03.txt', 'george04.txt', 'stopwords.txt')



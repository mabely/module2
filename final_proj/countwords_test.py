from countwords_functions import *

def main(input_file):
    # specifies the path of the file to be analysed
    path = 'text_data/{}'.format(input_file)
    input_txt = open(path)

    # calling funcs 
    counts = count_words(input_txt)
    # calls func that'll retrieve top 20 of a dict
    print_top20(counts)

# when function called, name of txt file needs to be given as arg
main('mobypara.txt')


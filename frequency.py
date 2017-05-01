""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string
import operator


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    #Open file
    f = open(file_name, 'r')
    lines = f.readlines()
    curr_line = 0

    #Create Dictionary
    wordDict = {}
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
      curr_line += 1
    lines = lines[curr_line+1:]

    #loop through lines and words
    for i in lines:
        line = i.split()
        for j in line:

            #Get rid of punctuation
            word = j.strip(string.punctuation)

            #If key exists
            try:
                #Increment
                wordDict[word] += 1
            #Else
            except KeyError:
                #Create Key
                wordDict[word] = 0
    #Return items in dictionary as tuple
    return wordDict.items()




def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    #Sort list according to second value of tuple
    sortedList = sorted(word_list, key=operator.itemgetter(1))
    #Reverse list
    sortedList = sortedList[::-1]
    #Return 1st hundred positions
    return sortedList[:n]

if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    wordlist = get_word_list("pg32325.txt")
    print(get_top_n_words(wordlist, 100))

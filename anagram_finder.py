"""
Anagram Finder

Program to find the anagram of the user entered word from the words available
in the dictionary provided.
"""

import sys
from datetime import datetime
from os import path


def _load_file(filename):
    "Load the dictionary file and return the dict with word length as key"
    try:
        with open(filename, "r") as w_d:
            words = w_d.read().split("\n")
            len_large_word = len(max(words, key=len))
            d_words = dict()
            for i in range(1, len_large_word + 1):
                d_words[i] = list()
            for d_word in words:
                idx = len(d_word)
                if idx > 0:
                    d_words[idx].append(d_word)
            return d_words
    except IOError:
        raise Exception("File {} is not accessible".format(filename))


def _find_anagrams(word, word_dict):
    "Find the matching anagrams for the provided word from the dictionary"
    word_len_list = word_dict[len(word)]
    anagram_list = []
    for d_word in word_len_list:
        if sorted(word.lower()) == sorted(d_word.lower()):
            anagram_list.append(d_word)
    if(len(anagram_list)>1):
        return anagram_list


def _anagram_main(args):
    if len(args) == 2:
        dict_file = args[1]
        if not path.isfile(dict_file):
            raise Exception("Provided file {} doesn't exist".format(dict_file))
        if path.isfile(dict_file):
            try:
                # Checking access to the file
                with open(dict_file, "r") as d_f:
                    d_f.readlines()
            except IOError:
                raise Exception("File {} is not accessible".format(dict_file))
    elif len(args) == 1:
        raise Exception("Expecting the path to dictionary file as an argument")
    else:
        raise Exception("Invalid Arguments: Expecting only one argument")

    print()
    print("Welcome to the Anagram Finder")
    print("-----------------------------")
    start = datetime.now()
    words_dict = _load_file(dict_file)
    end = datetime.now()
    print("Initialized in {} ms\n".format(round((end-start).total_seconds()*1000, 2)))
    max_word_len_dict = (max(k for k, v in words_dict.items()))

    # Get input from user
    user_word = input("AnagramFinder>")

    # Break the loop when user enters "exit"
    while user_word.lower() != "exit":
        if not user_word:
            print("You entered an empty string, try again. Or enter exit to quit\n")
            user_word = input("AnagramFinder>")
        elif not user_word.isalpha():
            print("You entered non alphabetic characters, try again. Or enter exit to quit\n")
            user_word = input("AnagramFinder>")
        elif len(user_word) > max_word_len_dict:
            start = datetime.now()
            end = datetime.now()
            comp_time = round((end-start).total_seconds()*1000, 2)
            print("No anagrams found for {} in {}ms\n".format(user_word, comp_time))
            user_word = input("AnagramFinder>")
        else:
            start = datetime.now()
            anagrams = _find_anagrams(user_word, words_dict)
            end = datetime.now()
            comp_time = round((end-start).total_seconds()*1000, 2)
            if not anagrams or len(anagrams) == 1:
                print("No anagrams found for {} in {}ms\n".format(user_word, comp_time))
            else:
                print("{} Anagrams found for {} in {}ms".format(len(anagrams),
                                                                user_word, comp_time))
                print(",".join(anagrams), "\n")
            user_word = input("AnagramFinder>")


if __name__ == '__main__':
    _anagram_main(sys.argv)

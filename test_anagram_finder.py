"""
Unit Test for Anagram Finder application
"""

from collections import Counter
import pytest
import anagram_finder


def test_load_file():
    # pylint: disable=W0212
    "Whether _load_file module returns dictionary"
    assert isinstance(anagram_finder._load_file("dictionary.txt"), dict) is True


def test_load_file_exceptions():
    # pylint: disable=W0212
    "Whether exception is thrown correctly when file is not accessible"
    with pytest.raises(Exception, match="File dictionary.txt.1 is not accessible"):
        anagram_finder._load_file("dictionary.txt.1")


def test_find_anagrams():
    # pylint: disable=W0212
    "Whether anagrams are found properly"
    computed_list = anagram_finder._find_anagrams("stop",
                                                  anagram_finder._load_file("dictionary.txt"))
    expected_list = ["post", "spot", "stop", "tops"]
    assert Counter(computed_list) == Counter(expected_list)


def test_find_anagrams_empty():
    # pylint: disable=W0212
    "Whether anagrams are not returned for invalid text"
    computed_list = anagram_finder._find_anagrams("asdfg",
                                                  anagram_finder._load_file("dictionary.txt"))
    assert len(computed_list) == 0


def test_anagram_main_no_dict_file():
    # pylint: disable=W0212
    "Whether missing argument exception is raised"
    with pytest.raises(Exception, match="Expecting the path to dictionary file as an argument"):
        anagram_finder._anagram_main(["arg1"])


def test_anagram_main_more_args():
    # pylint: disable=W0212
    "Whether additional arguments exception is raised"
    with pytest.raises(Exception, match="Invalid Arguments: Expecting only one argument"):
        anagram_finder._anagram_main(["arg1", "arg2", "arg3"])


def test_anagram_main_file_not_exists():
    # pylint: disable=W0212
    "Whether file not available exception is raised"
    with pytest.raises(Exception, match="Provided file dictionary.txt.1 doesn't exist"):
        anagram_finder._anagram_main(["arg1", "dictionary.txt.1"])

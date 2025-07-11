from collections import defaultdict

def word_count (file_contents) :
    word_list = file_contents.split()
    list_length = len (word_list)
    return list_length

def character_count (file_contents) :
    lowercase_contents = file_contents.lower()
    contents_dict = defaultdict(int)
    for char in lowercase_contents :
        contents_dict[char] += 1
    return dict(contents_dict)

def sort_on(items) :
    return items["num"]

def sort_counts (contents_dictionary) :
    character_count_list = list(contents_dictionary.items())
    list_of_dicts_for_sorting = []
    for char, num in character_count_list :
        dictionarylist = {"char": char, "num" : num}
        list_of_dicts_for_sorting.append(dictionarylist)
    return sorted(list_of_dicts_for_sorting, reverse=True, key=sort_on)
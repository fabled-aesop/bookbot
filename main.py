from stats import word_count
from stats import character_count
from stats import sort_counts
import sys

#filepath = "books/frankenstein.txt"
#print (sys.argv)
if len (sys.argv) == 2 :
    filepath = sys.argv [1]
    def get_book_text (filepath) :
        with open(filepath) as f :
            file_contents = f.read()
        return file_contents

    def main () :
        file_contents = get_book_text(filepath)
        list_length = word_count(file_contents)
        contents_dictionary = character_count (file_contents)
        sorted_list = sort_counts(contents_dictionary)
        
        print ("============ BOOKBOT ============")
        print (f"Analyzing book found at {filepath}...")
        print ("----------- Word Count ----------")
        print (f"Found {list_length} total words")
        print ("--------- Character Count -------")
        for item_dict in sorted_list :
            current_char = item_dict["char"]
            current_num = item_dict["num"]
            if current_char.isalpha() :
                print(f"{current_char}: {current_num}")
        print ("============= END ===============")
else : 
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main ()

import sys
from stats import get_num_words
from stats import count_chars
from stats import create_sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + sys.argv[1])
    print("----------- Word Count ----------")
    franky = get_book_text(sys.argv[1])
    # print(franky)
    get_num_words(franky)    
    total_chars = count_chars(franky)
    # print(total_chars)
    srtd_list = create_sorted_list(total_chars)
    print("--------- Character Count -------")
    for item in srtd_list:
        ch = item["char"]
        count = item["num"]
        if ch.isalpha():
            print(f"{ch}: {count}")

main()

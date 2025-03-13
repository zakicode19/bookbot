from stats import get_num_words, get_char_count
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file):

    with open(path_to_file) as f:
        file_contents = f.read()
    
    return file_contents



def main():
    path_file = sys.argv[1]
    book_content = get_book_text(path_file)
    nbr_word = get_num_words(book_content)
    count_char = get_char_count(book_content)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_file}...")
    print("----------- Word Count ----------")
    print(f"Found {nbr_word} total words")
    print("--------- Character Count -------")
    order_count = dict(sorted(count_char.items(), key=lambda item: item[1], reverse=True))
    #print(order_count)
    for k, v in order_count.items():
        if k.isalpha():
            print(f"{k}: {v}")
main()



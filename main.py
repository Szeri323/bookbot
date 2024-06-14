
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    lowered_text = text.lower()
    letters = {}
    for letter in lowered_text:
            if letter.islower():
                try:
                    if letters[letter] >= 1:
                        letters[letter] += 1
                except:
                    letters[letter] = 1
            else:
                pass

    return letters

def sort_on(letters_count):
    def sort_dict(dict):
        return dict["count"]
    
    letters_sorted = []
    for item in letters_count:
        test = {}
        test['letter'] = item
        test['count'] = letters_count[item]
        letters_sorted.append(test)
    letters_sorted.sort(reverse=True, key=sort_dict)
    return letters_sorted

def print_report(path_to_file, words_count, letters_sorted):
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{words_count} words found in the document")
    print()
    for i in range(len(letters_sorted)):
        print(f"The {letters_sorted[i]['letter']} character was found {letters_sorted[i]['count']} times")
    print("--- End report ---")
    

def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    words_count = count_words(text)
    letters_count = count_letters(text)
    letters_sorted = sort_on(letters_count)
    print_report(path_to_file, words_count, letters_sorted)

if __name__=="__main__":
    main()
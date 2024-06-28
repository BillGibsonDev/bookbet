def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    word_count = word_counter(text)
    letters_dict = get_letters_dict(text)
    sorted_letters = sort_letters(letters_dict)

    print(f"--- Begin report of {book} ---")
    print(f"{word_count} words found in the document")
    print()
    
    for item in sorted_letters:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
        return file_contents

def word_counter(text):
    words = text.split()
    return len(words)

def get_letters_dict(text):
    letters = {}
    for letter in text:
        lowered = letter.lower()
        if lowered in letters:
            letters[lowered] += 1
        else:
            letters[lowered] = 1
    return letters

def sort_letters(letters_dict):
    sorted_list = []
    for ch in letters_dict:
        sorted_list.append({"char": ch, "num": letters_dict[ch]})
        sorted_list.sort(reverse=True, key=sort_by)
    return sorted_list

def sort_by(d):
    return d["num"]


main()
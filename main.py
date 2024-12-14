def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wc = word_count(book_path)
    chars = char_count(book_path)

    print(f"--- Begin report of {book_path} ---")
    print(f"{wc} words found in the documnet \n")
    report(book_path)
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(path):
    words = get_book_text(path).split()
    return len(words)

def char_count(path):
    chars = {}
    words = get_book_text(path).lower()
    for char in words:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def report(path):
    for char in char_count(path):
        amount = char_count(path)[char.sort()]
        print(f"The '{char}' character was found {amount} times")

main()

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    chars_dictionary = character_count(file_contents)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dictionary)
    
    print("---Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print()
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")


def count_words(string):
    count = len(string.split())
    return count

def character_count(string):
    chars = {}
    for char in string:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

if __name__ == "__main__":
    main()




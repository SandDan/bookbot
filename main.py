def main():
    with open('books/frankestein.txt') as f:
        file_contents = f.read()
        print(file_contents)
        word_count = count_words(file_contents)
        characters_dict = chars_dict(file_contents)
        print(characters_dict)

        chars_sorted_list = chars_dict_to_sorted_list(characters_dict)
        for item in chars_sorted_list:
            if not item["char"].isalpha():
                continue
            print(f"The {item['char']} character was found {item['num']} times")

        print("End report")


# Take book text as a string, return number of words in the string. (77986)
def count_words(text):
    words = text.split()
    print(len(words))

# Cout number of times each character appears in the string. Converto to lowercase, no duplicates.
# Dictionary since need character and count.
# character.lower to turn all chars to lowercase. 
def chars_dict(text):
    chars = {}
    for character in text:
        lowered = character.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

#Let's aggregate all the word and character data into a nice report that we can print to the console!
#Convert your dictionary of characters into a list of dictionaries and then use the .sort() method to sort by the number of occurrences.
def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
main()
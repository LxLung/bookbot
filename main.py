with open("./books/frankenstein.txt") as f:
    file_contents = f.read()

def NumOfWords(string):
    return len(string.split())

# If not in dictionary add it
# If in dictionary increment it
# dict ("a": 0)
def CountCharacters(my_string):
    chars = my_string.lower()
    freq = {}
    for c in chars:
        c.isalpha
        if c.isalpha():
            if c not in freq:
                freq[c] = 1
            else:
                freq[c] += 1
    return freq

if __name__ == '__main__':
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{NumOfWords(file_contents)} words found in the document\n")
    char_dict = CountCharacters(file_contents) # dict
    char_list = sorted(char_dict.items(), key=lambda item: item[1], reverse=True) # sorted converts a dict to a list
    for char_key, char_value in char_list:
        print(f"The '{char_key}' character was found {char_value}")
    print("--- End report ---")

def number_of_words(text):
    words = text.split()
    num_words = 0
    for word in words:
        num_words += 1
    return num_words

def number_of_chars(text):
    chars_counter = {}
    for char in text:
        char_lower = char.lower()
        if char_lower in chars_counter:
            chars_counter[char_lower] += 1
        else:
            chars_counter[char_lower] = 1
    return chars_counter

def sort_on(items):
    return items["num"]

def char_list_of_dicts(chars_lower_dict):
    listed = []
    for key in chars_lower_dict:
        listed.append({"char": key, "num": chars_lower_dict[key]})
    return listed



def get_num_words(text):
    words = text.split()
    counter = 0
    for word in words:
        counter += 1
    return counter # Return the word count

def get_character_count(text):
    char_counts = {}
    for char in text:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sorted_dict(char_counts):
    chars_list = []
    for char, count in char_counts.items():
        char_dict = {"char": char, "count": count}
        chars_list.append(char_dict)
    def sort_on(dict):
        return dict["count"]
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
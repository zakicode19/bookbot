def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    input_text = text.lower()
    count = dict()
    for char in input_text:
        if char in count:
            count[char] +=1
        else:
            count[char] = 1
    return count
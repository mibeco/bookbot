
def get_num_words(text):
    text = text.split()
    count = 0
    for word in text:
        count += 1
    print(f"Found {count} total words")

def count_chars(text):
    counts = {}
    for c in text:
        c = c.lower()
        if c not in counts:
            counts[c] = 0
        counts[c] += 1
    return counts

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["num"]

def create_sorted_list(dct):
    srtd_lst = []
    for key, value in dct.items():
        tmp_dct = {}
        tmp_dct["char"] = key
        tmp_dct["num"] = value
        srtd_lst.append(tmp_dct)
    srtd_lst.sort(reverse = True, key=sort_on)
    return srtd_lst


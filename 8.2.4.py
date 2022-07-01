def sort_anagrams(list_of_strings):
    final_str = []
    new_str = []
    for n in list_of_strings:
        for f in list_of_strings:
            if f not in new_str and sorted(n) == sorted(f):
                new_str.append(f)
        if new_str not in final_str:
            final_str.append(new_str)
        new_str = []
    return final_str





#list_of_words = ['deltas', 'desalt', 'slated']
list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
print(sort_anagrams(list_of_words))
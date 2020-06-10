from itertools import combinations
from itertools import permutations
from itertools import chain

def return_substrings(word):
    all_combnations = [''.join(l) for i in range(len(word)) for l in combinations(word, i+1)]
    return list(reversed(list(dict.fromkeys(all_combnations))))

def return_permutations(substring):
    all_permutations = [''.join(i) for i in permutations(substring)]
    return all_permutations

def join_lists(all_permutations):
    all_permutations = chain.from_iterable(all_permutations)
    return set(list(all_permutations))

def get_words_from_file():
    word_list = []
    with open('kotusSanat.txt','r') as f:
        for word in f:
            word_list.append(word.strip())
    return word_list

def find_matches(all_permutations,word_list):
    matches = []
    for index,permutation in enumerate(all_permutations):
        if index % 300 == 0:
            print(f'{index} / {len(all_permutations)}')
        if permutation in word_list and len(permutation) > 2:
            matches.append(permutation)
    return matches

#define variables
all_permutations = []
word_list = []
matches = []

#create word list
word_list = get_words_from_file()

#the letters to be used for permutations
letters = input('Enter letters:')

#create substring combinations 
substrings = return_substrings(letters)

#create permutations of the combinations
for sub in substrings:
    all_permutations.append(return_permutations(sub))
all_permutations = all_permutations
all_permutations = join_lists(all_permutations)

#match permutations to word list
matches = find_matches(all_permutations,word_list)
print(matches)
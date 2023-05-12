import pickle
text_dir = '/sylcmu.txt'


def beautify_cmu_entry(entry):

    # Pretty heuristically done but should work
    split_entry = entry.split('/#') # /# is the separator used

    # First section contains the word and its pronunciation

    # Two spaces to distinguish pronounciation from word
    word = split_entry[0].strip().split('  ')[0].strip() #word ends at first space
    pronounciation = split_entry[0].strip().split('  ')[-1].strip()

    syllab = split_entry[-1].split('#/')
    # Second entry is syllabification
    syllables = syllab[0].strip()

    # last entry is stress and weight
    stress = syllab[-1].strip().split(' ')[0][2:] # last index removes S:
    weight = syllab[-1].strip().split(' ')[1][2:] # last index removes W:

    return [word, pronounciation, syllables, stress, weight]


if __name__ == '__main__':

    with open(text_dir, 'r', errors='ignore') as f:

        entries = f.readlines()

    data = [','.join(beautify_cmu_entry(word)) + '\n' for word in entries]
    with open('/clean_sylcmu.txt', 'w') as out:

        out.writelines(data)

    dictionary = {d[0]: {
        'pronounciation': d[1],
        'syllables': d[2],
        'stress': d[3],
        'weight': d[4]
    } for d in data
    }
    with open('/sylcmu_dict.pickle', 'wb') as out_pickle:

        pickle.dump(dictionary, out_pickle)

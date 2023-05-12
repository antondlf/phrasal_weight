import os
import pandas as pd
import numpy as np


def query_weight(word_query, dictionary):

    query_entries = dictionary.loc[dictionary['word'] == word_query.upper()]

    if len(query_entries) > 0:

        return query_entries.iloc[0]['weight']

    else:

        word_part = word_query.split('-')
        concat_weight = str()
        for word in word_part:
            query_entries = dictionary.loc[dictionary['word'] == word.upper()]
            if len(query_entries) > 0:

                concat_weight += query_entries.iloc[0]['weight']

            else:

                 return np.nan


def query_stress(word_query, dictionary):

    query_entries = dictionary.loc[dictionary['word'] == word_query.upper()]

    if len(query_entries) > 0:

        return query_entries.iloc[0]['stress']

    else:

        word_part = word_query.split('-')
        concat_weight = str()
        for word in word_part:
            query_entries = dictionary.loc[dictionary['word'] == word.upper()]
            if len(query_entries) > 0:

                concat_weight += query_entries.iloc[0]['stress']

            else:

                return np.nan


def load_dictionary(path):

    return pd.read_csv(path, sep=',', names=['word', 'pronounciation', 'syllabification', 'stress', 'weight'])


def load_data(path):

    return pd.read_csv(path, sep=',')


def add_cols(data_path, dictionary_path):

    data = load_data(data_path)
    dictionary = load_dictionary(dictionary_path)

    data['stress_profil'] = data.word.map(lambda x: query_stress(x, dictionary))
    data['weight_profil'] = data.word.map(lambda x: query_weight(x, dictionary))

    data.to_csv(data_path)


if __name__ == '__main__':

    #project_path = './'
    data_path = 'students-2023.csv'
    dictionary_path = 'clean_sylcmu.txt'

    add_cols(data_path, dictionary_path)
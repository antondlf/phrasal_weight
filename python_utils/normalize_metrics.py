import string
import argparse

def read_text(path):

    with open(path, 'r') as f:

        text = f.read()

    return text.strip()


def filter_punctuation(text):

    return text.translate(str.maketrans('', '', string.punctuation)).replace('\n', ' ')


def tokenize(text):

    return [word for word in text.strip().split(' ') if word != '']


def save_lineated_text(text, num_words, save_dir, total_length=500):

    print(text)
    with open(save_dir, 'w') as out:

        for i in range(0, total_length, num_words):
            #print(text[i: i+num_words])
            try:
                print(' '.join(text[i:i+num_words]).strip()+'\n', i, i+num_words)
                out.write(' '.join(text[i:i+num_words])+'\n')

            except IndexError:

                out.write(' '.join(text[i:]) + '\n')


def main():

    parser = argparse.ArgumentParser(
        description='remove punctuations and lineate a text'
    )
    parser.add_argument(
        'path', type=str, help='path of text'
    )
    parser.add_argument(
        'save_path', type=str, help='path to save lineated text'
    )
    parser.add_argument(
        'num_words', type=int, help='number of words per line.'
    )

    args = parser.parse_args()

    text = read_text(args.path)
    print(text)
    save_lineated_text(
        tokenize(filter_punctuation(text)),
        args.num_words,
        args.save_path
    )


if __name__=='__main__':
    main()


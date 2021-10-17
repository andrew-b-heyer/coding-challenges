# Pieces cannot be counted more than once
# Assume only 2 pieces will ever make a word

def create_words(pieces):
    possible_words = []

    for i, piece_1 in enumerate(pieces):
        for n, piece_2 in enumerate(pieces):
            if i == n:
                continue
            else:
                possible_words.append([piece_1+piece_2, piece_1, piece_2])

    return possible_words


def find_matches(words, possible_words):
    for word in words:
        for possible_word in possible_words:

            whole_word = possible_word[0]
            piece_1 = possible_word[1]
            piece_2 = possible_word[2]

            if word == whole_word:
                print(piece_1 + " + " + piece_2 + " => " + whole_word)
                break

            else:
                print(whole_word + " != " + word)


if __name__ == '__main__':
    words = ["albums", "barely", "befoul", "convex",
             "hereby", "jigsaw", "tailor", "weaver"]

    pieces = ["al", "bums", "bar", "ely", "be", "foul",
              "con", "vex", "here", "by", "jig", "saw",
              "tail", "or", "we", "aver"]

    possible_words = create_words(pieces)
    find_matches(words, possible_words)

# create a list of integers which specify the length of each word in a certain sentence,
# but only if the word is not the word "the".


sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
word_lengths_using_list_comprehensions = []


if __name__ == "__main__":
################
# Normal way ###
################
    for word in words:
        if word != "the":
            word_lengths.append(len(word))
    print(words)
    print(word_lengths)

###############################
# Using List Comprehensions ###
###############################
    word_lengths_using_list_comprehensions = [len(word) for word in words if word != "the"]
    print(words)
    print(word_lengths_using_list_comprehensions)


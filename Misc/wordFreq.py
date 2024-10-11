from collections import defaultdict
def count_word_frequency(sentence):
    res = defaultdict(int)
    for i in sentence.split():
        if i in res:
            res[i] += 1
        else: 
            res[i] = 1
    return res

    pass

# sentence = "hello world hello"
sentence = "she sells sea shells on the sea shore"
count_word_frequency(sentence=sentence)

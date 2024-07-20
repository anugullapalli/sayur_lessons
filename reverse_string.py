def reverse_words(Sentence):
    #split words in whitespace
    words = Sentence.split(" ")

    #iterate list and reverse words using ::-1
    new_word_list = [word[::-1] for word in words]

    #jon the new list
    res_str = " ".join(new_word_list)
    return res_str

str1 = "My name is Anu"
print(reverse_words(str1))

word = "Anu"
new_word = [word[::-1] for letter in word]

b=[7,4,5,6]
print ("the revese list is ", b[::-1])

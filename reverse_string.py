def reverse_words(Sentence):
    #split words in whitespace
    words = Sentence.split(" ")

    #iterate list and reverse words using ::-1
    new_word_list = [word[::-1] for word in words]

    #jon the new list
    res_str = " ".join(new_word_list)
    print(res_str)

my_str="Hello SAYur stuDENTS!"
#reverse_words("Who are you")

#for word in my_str.split():
#    word = word.lower()


words=[word.lower() for word in my_str.split()]
print(words)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
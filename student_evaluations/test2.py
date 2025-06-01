# given an input string, count number of vowels

#create the list of vowels
#iterate through string
#each i , is it present in the list? 
# create variable counter initialize to 0
# if a vowel is encountered, increment by 1
# return number of vowels

vowels=['a','e','i','o','u']    # list of vowels

#get the input string
sentence=input("Enter the input string:")
sentence=sentence.lower()
print(sentence)
vowel_count = 0   #initialize vowel count to 0
whitespace_count = 0 #initialize to 0

for i in sentence:    #loop through the sentence
    if i in vowels:
        vowel_count+=1

print ("Vowel count for input string is", vowel_count)

for i in sentence:    #loop through the sentence
    if not(i.isalnum()):
        whitespace_count+=1

print("Non  alpha numeric count is ",whitespace_count)
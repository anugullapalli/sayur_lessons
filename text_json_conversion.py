
# Python program to convert text
# file to JSON
 
 
import json
 
 
# the file to be converted
filename = 'student_data.txt'
 
# resultant dictionary
dict1 = {}
 
# fields in the sample file 
fields =['name', 'gender', 'degree','id']



with open(filename,'r') as fh:
     

     
    for line in fh:
         
        # reading line by line from the text file
        description = list( line.strip().split(None, 4))
         
        # for output see below
        print(description) 
         
        # loop variable
        i = 0
        # intermediate dictionary
        dict2 = {}
        while i<len(fields)-1:
             
                # creating dictionary for each employee
                dict2[fields[i]]= description[i]
                i = i + 1
                 
        # appending the record of each employee to
        # the main dictionary
        print(dict2)
        print(description[3])
        dict1[description[3]]= dict2

 
 
# creating json file        
out_file = open("student_data.json", "w")
json.dump(dict1, out_file, indent = 3)
out_file.close()
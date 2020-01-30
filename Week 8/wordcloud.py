'''

Program to make a word cloud based on the frequency of words
in a text file. Common words (read from another file) will be 
ignored. 

'''
import string

#preparing file to be used in word cloud
with open("gettysburg.txt") as wordfile:
	wordfile = wordfile.read()
    
for i in string.punctuation:
    wordfile = wordfile.replace(i,"").lower()

wordfile = wordfile.split()

#creating the dictionary and populating it with frequencies of words
word_dict = {}

with open ("stopwords.txt") as stopfile:
    stopwords = stopfile.read().split()
    
for word in wordfile:
    if word in stopwords:
        continue
    else:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

#opening the file and adding in the html
with open("wordcloud.html", "w") as file:
    file.write("<!DOCTYPE html><html><head lang=\"en\"><meta charset=\"UTF-8\">\n\
                <title>Tag Cloud Generator</title></head><body>\n\
                <div style=\"text-align: center; vertical-align: middle;font-family: arial;\
                color: white; background-color:black;border:1px solid black\">\n")
    
    for word,size in word_dict.items():
        file.write("<span style=\"font-size:"+str(size*10)+"px\"> "+word+" </span>\n")
    
    file.write("</div></body></html>")
    
    

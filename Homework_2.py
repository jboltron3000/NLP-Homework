import re
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

#Went back and created a function that is 100% precise.
def missesMr(results): 
    regex1 = "(.*[Mr\.] .*)"
    regex2 = "(.*[Mrs\.] .*)"
    regex3 = "(.*[Ms\.] .*)"
    item = results
    if re.search(regex1, item):
        return True
    elif re.search(regex2, item):
        return True
    elif re.search(regex3, item):
        return True
    else:
        return False
            
def main():
    filename = open("HW2_InputFile.txt")
    ##Setting all the global variables I will be using
    myList = []
    wordList = []
    countList = []
    wordCount = 0
    sentenceCount = 0
    d = {}
    regex1 = "(\.|\?)"
    regex2 = "(\s)"
    regex3 = "(\,\s)"
    regex4 = "([\$\\\+\%\&\”\"\'\@\(\)\~\^\*\“\!\/\,]+)"
    regex5 = "(\-.+)"
    word = ""
    sentence = ""
    wordFreq = []
    #Processing the input from the file. 
    for line in filename:
        for words in line: 
            if re.search(regex1, words):
                if word == "Mr":
                    word += words
                elif word == "Mrs":
                    word += words
                elif word == "Ms":
                    word += words
                elif word == "Dr":
                    word += words
                else:
                    sentence += "."
                    word.lower()
                    myList.append(sentence)
                    wordList.append(word)
                    sentenceCount += 1
                    sentence = ""
                    word = ""
            elif re.search(regex2, words):
                if word.lower() in d:
                    word = word.lower()
                    d[str(word)] += 1
                    word = sentence + " "
                    wordList.append(word)
                    sentence += words
                    word = ""
                    wordCount += 1
                else:
                    word = word.lower()
                    d[str(word)] = 1
                    word = sentence + " "
                    wordList.append(word)
                    sentence += words
                    word = ""
                    wordCount += 1
            elif re.search(regex3, words):
                if word.lower() in d:
                    word = word.lower()
                    d[str(word)] += 1
                    word = sentence + " "
                    wordList.append(word)
                    sentence += words
                    word = ""
                    wordCount += 1
                else:
                    word = word.lower()
                    d[str(word)] = 1
                    word = sentence + " "
                    wordList.append(word)
                    sentence += words
                    word = ""
                    wordCount += 1
            elif re.search(regex4, words):
                sentence += words
            elif re.search(regex5, words):
                if word == "":
                    sentence += words
                else:
                    word += words
                    sentence += words
            else:
                if sentence == "":
                    sentence = words
                    word = words
                else:
                    word += words
                    sentence += words
    print(myList[1])
    print(wordCount)
    print(sentenceCount)
    for key in d:
        wordFreq.append(key)
        countList.append(d[key])
    print(countList)

    
main()
    
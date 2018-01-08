#!/usr/bin/python
#
# Project GitHub Exercises
# Created by Lokesh Madhu

import sys
import math

# Question 1:
#Write a program which will find all such numbers which are divisible by 7 but are not 
#a multiple of 5, between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.
#12/20/2017
def GitHubQ1(l1, l2):
    try:
        num1 = int(l1)
        num2 = int(l2)
    except ValueError:
        print ('Expecting integer values')
        sys.exit()
    numlist = []
    devnum = 7
    mulnum = 5
    #print(num1, num2)
    for i in range(num1, (num2 + 1)):
        #print(i)
        if (i % devnum) == 0:
            if (i % mulnum) != 0:
                numlist.append(i)
    return(numlist)

#Question 2:
#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program:
# 8
#Then, the output should be:
# 40320
#12/20/2017
def GitHubQ2(inum):
    try:
        num = int(inum)
    except ValueError:
        print ('Expecting integer values')
        sys.exit()
    
    fact = 1
    if num == 0 or num == 1:
        return(fact)
    else:
        for i in range(num):
            fact = num * GitHubQ2(num - 1)
    return(fact)

#Question 3:    
#With a given integral number n, write a program to generate a dictionary that 
#contains (i, i*i) such that is an integral number between 1 and n (both included). 
#and then the program should print the dictionary.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
#12/20/2017
def GitHubQ3(num):
    try:
        inum = int(num)
    except ValueError:
        print('Expecting integer value. Try again')
        sys.exit()
    if inum == 0:
        result = {0:0} 
        return(result)
    result = {}
    for i in range(1, inum+1):
        result[i] = i*i
    return(result)
    
#Question 4:
#Write a program that calculates and prints the value according to the given formula:
#Q = Square root of [(2 * C * D)/H]
#Following are the fixed values of C and H:
#C is 50. H is 30.
#D is the variable whose values should be input to your program in a comma-separated sequence.
#Example
#Let us assume the following comma separated input sequence is given to the program:
#100,150,180
#The output of the program should be:
#18,22,24
#12/20/2017
def GitHubQ4(dlist):
    c, h = 50, 30
    qlist = []
    for i in dlist:
        qlist.append(int(math.sqrt((2 * c * int(i))/h)))
    return (qlist)
    
#Question 5:
#Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
#The element value in the i-th row and j-th column of the array should be i*j.
#Note: i=0,1.., X-1; j=0,1,.., Y-1.
#Example
#Suppose the following inputs are given to the program:
#3,5
#Then, the output of the program should be:
#[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
#12/22/2017
def GitHubQ5(x, y):
    x = int(x)
    y = int(y)
    array = []
    # Using loop with comprehension method. 
    array = [[i*j for i in range(y)] for j in range(x)]
    #Using regular nested for loop method.
    #for i in range(x):
        #ielements = []
        #for j in range(y):
            #ielements.append(i*j)
        #array.append(ielements)   
    return(array)
#
#Question 6:
#Write a program that accepts a comma separated sequence of words as input and 
#prints the words in a comma-separated sequence after sorting them alphabetically.
#Suppose the following input is supplied to the program:
#without,hello,bag,world
#Then, the output should be:
#bag,hello,without,world
#
#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input.
#
def cmpwords(word1, word2):
    word1len = len(word1)
    word2len = len(word2)
    #print(word1, word2)
    if word1len <= word2len: wordloop = word1len
    else: wordloop = word2len    
    for k in range(wordloop):
        if word1[k] > word2[k]:            
            return(word2, word1)            
        elif word1[k] == word2[k]: continue
        else:
            return(word1, word2)
    if word1len <= word2len: return(word1, word2)
    else: return(word2, word1)
                    
def GitHubQ6(wordlist):
    wordlistlen = len(wordlist)
    if wordlistlen == 1: return(wordlist)
    for i in range(wordlistlen):
        for j in range(wordlistlen):    
            word1 = wordlist[i]
            word2 = wordlist[j]
            wordlist[j], wordlist[i] = cmpwords(word1, word2)                   
    return(wordlist)        
#



def main():
    Test = False    
    #Q1S
    #print(GitHubQ1(2000, 3200))
    #Q1E
    
    #Q2S
    #print('Enter a number to compute factorial! ->', end=' ')
    #num = input()
    #fact = GitHubQ2(num)
    #print(fact)
    #Q2E
    
    #Q3S
    #print('Enter a number: ->', end = ' ')
    #num = input()
    #dictresult = GitHubQ3(num)
    #print(dictresult)
    #Q3E
    
    #Q4S
    #print('Enter a sequence of \',\' seperated numbers ->', end=' ')
    #inlist = input()
    #inputlist = inlist.split(',')    
    #qlist = GitHubQ4(inputlist)
    #for i in qlist:
        #print('{},'.format(i),end='')
    #Q4E
    
    #Q5S
    #print('Enter a 2 dimensional array value for x and y (Eg: 3, 4) ->')
    #invalue = input()
    #value = invalue.replace(',', ' ').split()
    #if len(value) != 2:
        #print('Expecting 2 values. Try again.')
        #sys.exit()    
    #array = GitHubQ5(value[0], value[1])
    #print(array)
    #Q5E
    
    #Q6S
    listofwords = ['Lokesh', 'Avni', 'Arnav', 'Pavithra']
    print(listofwords)
    print(GitHubQ6(listofwords))
    if Test:
        print('abcd', 'abc', cmpwords('abcd', 'abc'))
        print('abc', 'abcd', cmpwords('abc', 'abcd'))
        print('abc', 'abc', cmpwords('abc', 'abc'))
        print('a', 'abc', cmpwords('a', 'abc'))
        print('abc', 'a', cmpwords('abc', 'a'))
        print('abcd', 'c', cmpwords('abcd', 'c'))
        print('cbcd', 'abcded', cmpwords('cbcd', 'abcded'))
    #Q6E
    
    
if __name__ == "__main__": main()
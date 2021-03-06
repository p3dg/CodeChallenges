__author__ = 'Peter Galvin'#2/16/2015
#The approach:
#rank of word is position in the alphabetized list of permutations
#first get word, alphabetize it.
#must get number of repeated letters and divide total permutations by the number of repeats factorial
#e.g. bookkeeper = 10!/2!/2!/3! = 151200 permutations because o and k are repeated twice, e thrice.
#
#We then go through a binary search of the list, looking at each 0th index letter in the string as we
#remove one letter from said index recursively and adjust the window of indices we're looking at.
# #return (long) rank

import sys, math, collections;

#get command line argument, becomes string we want to rank
yourString = sys.argv[1]
print "Analyzing rank of " + yourString + "..."

#Get the total number of permutations for your word
def getPerms(yourString):
    totalPerms = math.factorial(len(yourString))
    d = collections.defaultdict(int)
    for c in yourString:
        d[c] += 1

    for c in sorted(d, key=d.get, reverse=True):
        if(d[c]>1):
            totalPerms = totalPerms/math.factorial(d[c])

    return totalPerms

#end is the total number of permutations, or the length of the list
#of all combinations
end = getPerms(yourString)

#gets the first instance of the passed letter in the string
def getFirstIndexOf(string, letter):
    for i in range(0,len(string)):
        if string[i] == letter:
            return i

#gets the last instance of the passed letter in the string arg
def getLastIndexOf(string, letter):
    for i in reversed(range(len(string))):
        if string[i] == letter:
            return i

#Ranks string
#start is the last beginning position of our search
#end is the last ending of the chunk of our search
#We recursively cut down the word and search through the permutation space for its position!
def rankString(yourString, start, end):
   # print(start)
   # print(end)
    tempString = sorted(yourString)
    #print(tempString)
    range = end - start
   # print(range)
    if len(yourString) != 0:
        sections = range/len(tempString)
    if(len(tempString)<=0):
        return start +1
    else:
        letter = yourString[0]
        #print("looking at letter " + letter)
        first = getFirstIndexOf(tempString, letter)
        last = getLastIndexOf(tempString, letter)
        newStart = start + sections*first
        newEnd = start + sections*(last+1)

        #remove first letter to go through the search
        yourString = yourString[1:]

        return rankString(yourString, newStart, newEnd)



#Finally, let's kick it off!
print('The rank of your string, {0}, is... {1} '.format(yourString, rankString(yourString,0,end)))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
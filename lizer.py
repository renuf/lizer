import re

def counter(value, unit):
   #find all non-whitespace
   list = re.findall(value , unit)
   return len(list)

def wordCount(book):
  results = []
  in_file = open(book, "r")
  wordcount = 0
  uwordlist = []
  uwordcount = 0
  for line in in_file:
    wordcount = wordcount + counter("(\S)", line)
    #redl is the line split into a list to iter w/out chars
    redline = line.split()
    for entry in redline:
        uwordlist.append(entry)
  uwordlist = set(uwordlist)
  #count uniq words using length of list
  uwordcount = len(uwordlist)
  return [wordcount, uwordlist]
      
  return wordcount
  in_file.close()

def uwordcomp(s1, s2):
  #sets 1 and 2 are compared to see words in common
  #great and least are used to prevent length errors in iteration
  if len(s1) > len(s2):
    great = s1
    least = s2
  else:
    great = s2
    least = s1
  #initialize new set for words in common
  common = []
  for word in great:
    word = word.strip()
    if word in least and len(word) > 3:
      common.append(word)
  return(common)


def main():
  #Enter name of books
  book1 = input ("Enter name of first book: ")
  book2 = input ("Enter name of second book: ")

  #Enter names of authors
  author1 = input ("Enter last name of first author: ")
  author2 = input ("Enter last name of second author: ")
  #store total word counts from results
  res1 = wordCount(book1)
  res2 = wordCount(book2)
  wC1 = res1[0]
  wC2 = res2[0]
  #store all unique words
  uwords1 = res1[1]
  uwords2 = res2[1]
  #get len of unique words
  numUs1 = len(uwords1)
  numUs2 = len(uwords2)
  #commonW gives
  commonW = uwordcomp(uwords1, uwords2)
  
  print("")
  print(author1, "wordcount:", wC1, "uniqwords:", numUs1)
  print(author1, "the rate of unique word frequency is", (numUs1/wC1) * 100)
  print("")
  print(author2, "wordcount:", wC2, "uniqwords:", numUs2)
  print(author2, "unique word frequency is", (numUs2/wC2) * 100)
  print("")
  print("Unique words in common:", len(commonW))
  print("") 
main()

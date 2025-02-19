print("FIND THE LONGEST WORD")
words= input("input a sentence: ")
words = words.split() 
longest = " "
for word in words:
    if len(word) > len(longest):
        longest = word
print("The longest:", longest)
print("YEHEY")
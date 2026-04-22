inputSentence= input("Enter a sentence: ")
inputSentence = inputSentence.split()
inputSentence= list( map(lambda x : len(x),inputSentence ))
print(inputSentence)
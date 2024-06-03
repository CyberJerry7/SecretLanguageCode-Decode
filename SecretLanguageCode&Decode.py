# Developed by CyberJerry

print("\t\t>>> Code or Decode <<<\n\n")
codeOrDecode = input("Enter 1 to Code.\nEnter 2 to Decode.\nEnter here : ")

# if user presses keys other than 1,2
if codeOrDecode!='1' and codeOrDecode!='2': 
    while codeOrDecode!='1' and codeOrDecode!='2':
        print("\nThere are only two options...")
        codeOrDecode = input("Enter 1 to Code.\nEnter 2 to Decode.\nEnter here : ")

string = input("\nType your sentence here : ")

words = string.split(" ")

if codeOrDecode == "1":
    newWords = [] # Empty string
    for word in words:
        if len(word)>=3:
            randChars1 = "u093jweRQ3"
            randChars2 = "0w40MPVEW%"
            newString = randChars1+word[1:]+word[0]+randChars2
            newWords.append(newString)

        else:
            newWords.append(word[::-1])

    print("Code : "," ".join(newWords))

else: 
    newWords = [] # Empty string
    for word in words:
        if len(word)>=3:
            newString = word[10:-10]
            newString = newString[-1]+newString[:-1]
            newWords.append(newString)

        else: 
            newWords.append(word[::-1]) # reverse string

    print("Decode : "," ".join(newWords))        
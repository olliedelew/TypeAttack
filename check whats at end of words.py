lyst = []
with open("wordy - Copy.txt","r") as f:
    for line in f:
        words = f.readlines()
        print(words)
        for word in line.split():
           lyst.append(word)
#print(lyst)

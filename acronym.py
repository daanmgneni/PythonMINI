#pgm to print acroyms for a given word
word=input('Enter a word to get acronym ')

print(word[0].upper(),end=' ')#prints acronym for first word in upper case
for i in range(0,len(word)):
    if word[i]==' ' and word[i+1]!=' ' :
        print(word[i+1].upper(),end=' ')
    #prints characters followed by space


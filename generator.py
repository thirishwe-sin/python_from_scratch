words = ['apple', 'orange', 'juice', 'banana']
from random import randint

def randomSentenceGenerator(word):
    randomIndex = randint(0, len(words)-1)
    return f'{words[randomIndex]} {word}'

with open('./text.txt') as file:
    paragraph = file.read()
    wordLists = paragraph.split()
    sentenceList = list(map(randomSentenceGenerator,wordLists))
    paraCount = int(input('Paragraph count: '))
    
    for count in range(paraCount):
        with open('./generator.txt', 'a') as write_file:
            write_file.write(''.join(sentenceList) + '\n\n')
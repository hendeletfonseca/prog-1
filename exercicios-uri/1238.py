# https://www.beecrowd.com.br/judge/pt/problems/view/1238

qtdTestes = int(input())
for _ in range(qtdTestes):
    wordA, wordB = input().split()
    finalWord = ''
    if len(wordA) > len(wordB):
        for i in range(len(wordB)):
            finalWord += wordA[i]
            finalWord += wordB[i]
        for t in range(len(wordB), len(wordA)):
            finalWord += wordA[t]
    if len(wordB) > len(wordA):
        for i in range(len(wordA)):
            finalWord += wordA[i]
            finalWord += wordB[i]
        for t in range(len(wordA), len(wordB)):
            finalWord += wordB[t]
    if len(wordA) == len(wordB):
        for i in range(len(wordA)):
            finalWord += wordA[i]
            finalWord += wordB[i]
    print(finalWord)

import re

text = input()

#Word numbers
words = len(re.findall(r'\w+', text))

#Sentences number
sentences = text.count('.')
sentences += text.count('!')

#Letter numbers
i = 0
total = 0
letters = len(text)
while i < letters:
    if (text[i] != ' ') and (text[i] != ',') and (text[i] != "'") and (text[i] != '.') and (text[i] != '!'):
        total += 1
    if text[i] == "'":
        words -= 1
    i += 1

#grade
grade = 0.0588 * (total / words * 100) - 0.296 * (sentences / words * 100) - 15.8

#print (total)
#print (words)
#print (sentences)

print ('Grade ', round(grade))
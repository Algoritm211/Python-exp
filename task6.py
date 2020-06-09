from pprint import pprint

file = open('task6.txt', 'r', encoding='utf-8')

data = [i.rstrip() for i in file.readlines()]
file.close()
def sortByAlphabet(inputStr):
    return inputStr[0]

result = sorted(data, key=sortByAlphabet)
pprint(data)
pprint(result)

file = open('task6.txt', 'w', encoding='utf-8')
for i in data:
    file.write(i + '\n')


file.write('Отсортированный список:\n')
for i in result:
    file.write(i + '\n')

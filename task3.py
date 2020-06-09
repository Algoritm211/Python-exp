from pprint import pprint
file = open('task3.txt' , 'r')

count_str = 0

results = []
a = 1
for line in file.readlines():
    count_str += 1
    count = len(line) - 1
    count1 = len(line.split(' '))
    results.append({
    'Строка': a,
    'Символов в строке': count,
    'Слов в строке': count1
    }
    )
    a += 1

for elem in results:
    pprint(elem)
pprint('Всего строк: ' + str(count_str))

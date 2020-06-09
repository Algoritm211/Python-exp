file = open('task1.txt', 'r', encoding='utf-8')

result = [line.rstrip() for line in file.readlines()]

lowmark = []
count = 0
for elem in result:
    if int(elem[-1]) < 3:
        lowmark.append(elem)
    count += int(elem[-1])

print('Ученики, у который балл меньше 3:\n ', )
for i in lowmark:
    print(i)

print('Средний балл по классу: ' + str(count/len(result)))

file = open('task2.txt', 'w', encoding='utf-8')


while True:
    s = input()
    if s == '':
        break
    file.write(s+'\n')

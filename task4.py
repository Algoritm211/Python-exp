from pprint import pprint
fin = open('task4input.txt', 'r', encoding='utf-8')


children = [line.rstrip() for line in fin.readlines()]

children_s = [elem.strip(' лет') for elem in children]
children_sort = [elem.strip(' года') for elem in children_s]
children_sort.sort(key=lambda x: x[-1])

ml = children_sort[0]
st = children_sort[-1]
fout = open('task4output.txt' , 'w', encoding='utf-8')
fout.write('Самый младший - ' + ml + ' года\n')
fout.write('Cамый старший - ' + st + ' лет')
# fout.write('Самый младший - ' + )

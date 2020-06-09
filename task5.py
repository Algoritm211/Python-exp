from pprint import pprint
file = open('shop_1.txt', 'r', encoding='utf-8')

products = []
info = []

for i in file.readlines()[0::2]:
    products.append(i.rstrip())
file.close()
file = open('shop_1.txt', 'r', encoding='utf-8')
for i in file.readlines()[1::2]:
    info.append(i.rstrip().split())
file.close()

result = list(zip(products, info))
fout = open('task5.txt', 'w', encoding='utf-8')
fullprice = 0
for elem in result:
    price = float(elem[1][0]) * float(elem[1][1])
    fullprice += price
    text = 'Наименование товара: ' + elem[0] + ', кол-во единиц товара: '+ elem[1][0] +\
            ', cтоимость единицы товара: ' + elem[1][1] + ', общая стоимость: ' + str(price) +'\n'
    fout.write(text)

fout.write('Общая стоимость: ' + str(fullprice))

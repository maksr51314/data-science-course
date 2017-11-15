import csv

price_dic = {}

with open('goods_price.csv', 'rt') as goods_price:
    for el in csv.reader(goods_price):
        price_dic[el[0]] = int(el[1])

full_price_dic = {}

with open('goods_count.csv', 'rt') as goods_count:
    for el in csv.reader(goods_count):
        if el[0] in full_price_dic:
            full_price_dic[el[0]] += int(el[1])*price_dic[el[0]]
        else:
            full_price_dic[el[0]] = int(el[1])*price_dic[el[0]]

with open('goods_full_price.csv', 'wt') as goods_full_price:
    goods_writer = csv.writer(goods_full_price)
    for key, val in full_price_dic.items():
        goods_writer.writerow([key, val])
# with open('goods_count.csv', 'rt') as goods_count:


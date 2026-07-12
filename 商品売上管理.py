#商品売上管理
goods=[]
sales=[]
for g in range(5):
    good=input('購入された商品を入力してください>>')
    goods.append(good)
    sale=int(input(f'{good}による売上金額を入力してください>>'))
    sales.append(sale)
total_sales=sum(sales)
average_sales=sum(sales)/len(sales) #ここのsum(sales)は,total_salesでもいいかも？(9行目の代入より)
max_good=max(goods)
min_good=min(goods)
print(f'売上合計:{total_sales}円')
print(f'平均:{average_sales}円')
print(f'最高売上商品名:{max_good}')
print(f':最低売上商品名:{min_good}')
#在庫管理システム
def again():
    delete_again = input('続けて商品を削除しますか？「y」か「n」で答えてください>>')
    return delete_again=='y'

goods=[]
goods_number=0
for g in range(5):
    goods_number+=1
    goods_resistration=input(f'登録する{goods_number}つ目の商品名を入力してください>>')
    goods.append(goods_resistration)
print('登録された商品は以下の通りです。')
count=1
for d in range(5):
    display=''.join(goods[d])  #print(f'{count}.{goods[d]}')でもいいかもしれない？
    print(f'{count}.{display}')
    count+=1
while True:
    delete_goods=input('どの商品を削除しますか？')
    if delete_goods in goods:
        goods.remove(delete_goods)
        print(f'{delete_goods}を削除しました。')
        if again():
            continue
        else:
            break
    else:
        print('その商品はありません')
        if again():
            continue
        else:
            break
result='\n'.join(goods)
print(f'残っている商品の一覧は，\n{result}\nです。')
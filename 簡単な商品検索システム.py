#簡単な商品検索システム
def again():
    search_again=input('続けて商品を検索しますか？「y」か「n」で答えてください>>')
    return search_again=='y'

goods=[]
price=[]
for gp in range(5):  #毎回回数指定してるけど，回数を指定しないようにwhileのほうがいいのかな？
    reg_goods=input('登録する商品名を入力してください>>')  #「reg」は「registration」の略
    goods.append(reg_goods)
    reg_price=int(input(f'{reg_goods}の価格を入力してください>>'))
    price.append(reg_price)
print('登録された商品とその価格の一覧は以下の通りです。')
count=1
for dis in range(5):  #「dis」は「display」の略
    print(f'{count}.{goods[dis]}:{price[dis]}円')
    count+=1
information=dict(zip(goods,price))
while True:
    search=input('検索したい商品を入力してください>>')
    if search in information:
        search_price=information[search]
        print(f'{search}:{search_price}円')
        if again():
            continue
        else:
            print('ご利用ありがとうございました。')
            break
    else:
        print('その商品は登録されていません。')
        if again():
            continue
        else:
            print('ご利用ありがとうございました。')
            break
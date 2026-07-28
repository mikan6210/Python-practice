#飲み物アンケート集計
def reg_drinks():  #投票用の飲み物を登録する
    drinks=[]
    while True:
        drink=input('登録する飲み物を入力してください>>')
        drinks.append(drink)
        again=input('追加で飲み物を登録しますか？「y」か「n」で答えてください>>')
        if again=='y':
            continue
        else:
            print('登録を終了します')
            break
    return drinks

drinks=reg_drinks()  #3行目のリストの中身
dis_drinks=','.join(drinks)
print(f'登録された飲み物は，{dis_drinks}です。')  #reg_drinksの飲み物を全部表示
votes=[0]*len(drinks)   #ここは調べました
information=dict(zip(drinks,votes))
print('好きな飲み物についてのアンケートを実施しています。')
while True:
    like_drink=input('好きな飲み物を入力してください>>')
    if like_drink in information:
        print(f'{like_drink}に１票追加します')
        information[like_drink]+=1  #ここも調べました
        again=input('追加で投票を行いますか？「y」か「n」で答えてください>>')
        if again=='y':
            continue
        else:
            break
    else:
        print('その飲み物は登録されていません')
        again=input('追加で投票を行いますか？「y」か「n」で答えてください>>')
        if again=='y':
            continue
        else:
            break
for drinks,votes in information.items():
    print(f'{drinks}:{votes}票')
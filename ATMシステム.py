#ATMシステム
zandaka=int(input('現在の残高を入力してください>>'))
while True:
    nyuukin=1
    syukkin=2
    zandaka_check=3
    end=4
    print(f'{nyuukin}.入金')
    print(f'{syukkin}.出金')
    print(f'{zandaka_check}.残高確認')
    print(f'{end}.終了')
    select=(input('どの操作を行いますか？番号で入力してください>>'))
    if select=="1":
        nyuukin_kingaku=int(input('いくら入金しますか？>>'))
        zandaka+=nyuukin_kingaku
        print(f'{nyuukin_kingaku}円入金されたので，現在の残高は{zandaka}円です')
    elif select=="2":
        syukkin_kingaku=int(input('いくら出金しますか？>>'))
        zandaka-=syukkin_kingaku
        if zandaka<0:
            print('残高不足です')
            break
        else:
            print(f'{syukkin_kingaku}円出金されたので，現在の残高は{zandaka}円です')
    elif select=="3":
        print(f'あなたの現在の残高は{zandaka}円です')
    elif select=="4":
        print('ご利用ありがとうございました')
        break
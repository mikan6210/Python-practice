#ロッカー利用管理
def d_again():  #利用者の複数登録用
    again=input('利用者を再び登録しますか？「y」か「n」で答えてください>>')
    return again=='y'

def registration():  #登録用
    user_name=input('ロッカーの利用者名を入力してください>>')
    locker_num=int(input(f'{user_name}さんが利用するロッカー番号を答えてください>>'))
    return user_name,locker_num

print('スポーツジムのロッカー利用を管理します。')

def duplication_check():  #重複判定
    information=[]
    user_count=0
    while True:
        user_name,locker_num=registration()
        info=(user_name,locker_num)  #要素2つ→ディクショナリでもよかった？
        duplication=False
        for exist_user_name,exist_locker_num in information:
            if exist_locker_num==locker_num:
                print('そのロッカー番号はすでに登録されているため，登録できません。')
                duplication=True
                break
        if not duplication:
            print('そのロッカー番号を登録します。')
            user_count+=1
            information.append(info)
        if not d_again():
            print('登録を終了します。')
            break
    return information,user_count

information,user_count=duplication_check()
print('登録内容は以下の通りです。')
print(f'ロッカーの利用人数は，{user_count}人です。')
for user_name,locker_num in information:
    print(f'利用者名:{user_name}さん,ロッカー番号:{locker_num}番')
#映画館座席予約管理
def d_again():  #繰り返し用
    while True:
        again=input('追加で座席番号を登録しますか？「y」か「n」で答えてください>>')
        if again=='y':
            return True
        elif again=='n':
            return False
        else:
            print('「y」か「n」で入力してください')

def registration():  #登録用
    user_name=input('名前を入力してください>>')
    seat_number=input(f'{user_name}さんの座席番号を入力してください\n'
                      '例)A-1,B-5など>>')
    return user_name,seat_number

def duplication_check():  #重複確認用
    information=[]
    name_count=0
    while True:
        user_name,seat_number=registration()
        information_tuple=(user_name,seat_number)
        duplication=False
        for e_user_name,e_seat_number in information:
            if e_seat_number==seat_number:
                print('その座席は既に登録されているため登録できません')
                duplication=True
                break
        if not duplication:
            print('その座席番号を登録します')
            information.append(information_tuple)
            name_count+=1
        if d_again():
            continue
        else:
            break
    return information,name_count

print('映画館の座席予約を管理します。')
information,name_count=duplication_check()
print('登録内容は以下の通りです。')
print(f'予約人数は，{name_count}人です。')
for user_name,seat_number in information:
    print(f'利用者名:{user_name},座席番号:{seat_number}')
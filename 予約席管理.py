#予約席管理
def registration():  #情報の登録を行う
    d_information={}
    while True:
        reg_name=input('予約者の名前を入力してください>>')
        seat_num=int(input(f'{reg_name}さんの席番号を登録してください>>'))
        if seat_num in d_information.values():
            print('その席番号は登録されています')
            again=input('続けて席番号の登録を行いますか？「y」か「n」で答えてください>>')
            if again=='y':
                continue
            else:
                print('登録を終了します')
                break
        else:
            d_information[reg_name]=seat_num
            again=input('続けて席番号の登録を行いますか？「y」か「n」で答えてください>>')
            if again=='y':
                continue
            else:
                print('登録を終了します')
                break
    return d_information

information=registration()  #d_informationのこと
print('登録された情報は以下の通りです。')
for reg_name,seat_num in information.items():
    print(f'予約者名:{reg_name}さん,席番号:{seat_num}番')
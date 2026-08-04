#会議室予約システム
def d_again():  #繰り返し
    again=input('ほかの会議室を予約しますか？「y」か「n」で答えてください>>')
    return again=='y'

def information_registration():  #情報登録
    mr_name=input('予約したい会議室名を入力してください>>')  #mrはmeeting roomの略
    start_time=int(input('利用開始時間を入力してください>>'))
    end_time=int(input('利用終了時間を入力してください>>'))
    return mr_name,start_time,end_time

print('会議室の予約を管理します。')
reservations=[]
while True:
    mr_name,start_time,end_time=information_registration()
    reservation=(mr_name,start_time,end_time)
    duplication=False  #duplicationは重複
    for exist_mr_name,exist_start_time,exist_end_time in reservations:
        if mr_name==exist_mr_name:
            if start_time<exist_end_time and exist_end_time>start_time:  #重複しないための条件
                print('それは登録できません')
                duplication=True
                break
    if not duplication:
        print('登録します')
        reservations.append(reservation)
    if not d_again():
        break

from datetime import date
today=date.today()
print(f'本日{today}の会議室名と利用時間帯は以下の通りです。')
for mr,start,end in reservations:
    print(f'会議室名:{mr}会議室,利用時間:{start}時～{end}時')
#図書返却管理
def information_reg(m):  #情報の登録
    book_title=input('貸し出した本のタイトルを入力してください>>')
    lending_day=int(input('本の貸出日をで入力してください>>'))
    return_day=int(input('本の返却日を入力してください>>'))
    delta=return_day-lending_day
    if m in [1,3,5,7,8,10,12]:
        if delta<0:
            delta=(31-lending_day)+return_day
        else:
            delta=return_day-lending_day
    if m in [2,4,6,9,11]:  #うるう年の場合は？
        if delta<0:
            delta=(30-lending_day)+return_day
        else:
            delta=return_day-lending_day
    print(f'{book_title}を借りていた期間は{delta}日です。')
    return delta

from datetime import date
today=date.today()  #今日の日付
print(f'本日は{today}です。')
m=today.month  #今，何月か
rental_day=7
plus_money=100
print(f'本の無料貸し出し期間は{rental_day}日です。')
print(f'1日の延滞ごとに{plus_money}円が必要です。')
delta=information_reg(m) #delta,つまり貸出期間のこと

def cal_money(delta,rental_day):  #計算用,calはcalculation
    if delta<=rental_day:
        print('無料です。延滞料金は必要ありません')
    else:
        delay_day=delta-rental_day
        delay_money=delay_day*plus_money
        print(f'{delay_day}日遅れたので，延滞料金{delay_money}円をお支払いください')

cal_money(delta,rental_day)
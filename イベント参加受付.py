#イベント参加受付   
participants=[]
count=0
for r in range(5):
    registration=input('参加者の名前を登録してください>>')
    participants.append(registration)
print('受付終了')
while True:
    participant=input('参加する人の名前を入力してください>>')
    if participant in participants:
        print(f'{participant}さんは参加予定です')
        count+=1
        confirmation=input('追加で,参加状況の確認をしますか？「y」か「n」で答えてください>>')
        if confirmation=='y':
            continue 
        else:
            print('入力終了です')
            break
    elif not participant in participants:
        print(f'{participant}さんは参加登録されていません')    
        confirmation=input('追加で,参加状況の確認をしますか？「y」か「n」で答えてください>>')
        if confirmation=='y':
            continue 
        else:
            print('入力終了です')
            break
print(f'今回のイベントの参加人数は{count}人です')
#もし１回目と２回目の検索結果が同じでも人数は＋１人されてしまう
#例えば，１回目が「田中さん」，２回目も「田中さん」でも参加人数は１人なのに２人と表示されてしまう
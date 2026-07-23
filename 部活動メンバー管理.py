#部活動メンバー管理
print('部活動のメンバーを登録します。')
count=0
members=[]
while True:
    member=input('部活動のメンバーを入力してください>>')
    if member in members:
        print('その名前の人は登録されています。')
    else:
        members.append(member)
        count+=1
    again=input('続けてメンバーを入力しますか？「y」か「n」で答えてください>>')
    if again=='y':
        continue
    else:
        print('メンバーの登録を終了します。')
        break
print(f'{count}人のメンバーが登録されました。')
dis='\n'.join(members)   #「dis」は「display」の略
print(f'登録されたメンバーは，\n{dis}\nです。')
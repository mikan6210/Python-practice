#ポイントカード管理
def choices():
    count=1
    add_point=print(f'{count}.ポイント追加')
    count+=1
    use_point=print(f'{count}.ポイント使用')
    count+=1
    confirmination_point=print(f'{count}.ポイント確認')
    count+=1
    finish=print(f'{count}.終了')    #もう少し簡潔にしたい

point=int(input('現在のポイントを入力してください>>'))
print(f'あなたの現在のポイントは，{point}ポイントです。')
choices()
while True:
    choice=input('上記のいずれかを番号で入力してください>>')
    if choice=='1':
        add_points=int(input('ポイントをいくら追加しますか？>>'))
        point+=add_points
        print(f'{add_points}ポイント追加されたので，現在のポイントは，{point}です。')
        choices()
        continue
    elif choice=='2':
        uses_point=int(input('ポイントをいくら使用しますか？>>'))
        if uses_point>point:
            print('ポイントが足りません')
            continue
        else:
            point-=uses_point
            print(f'{uses_point}ポイント使用したので，現在のポイントは，{point}です。')
        choices()
        continue
    elif choice=='3':
        print(f'あなたの現在のポイントは，{point}ポイントです。')
        choices()
        continue
    else:
        print('ご利用ありがとうございました。')
        break
#ポイントがマイナスになってしまった時の状態が弱い
#不足したら-〇円というように表示され続けるから後続のものがやりづらさを感じる
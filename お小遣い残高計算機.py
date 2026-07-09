#お小遣い残高計算機
all_money=int(input('今月もらったお小遣いの金額を入力してください>>'))
print(f'あなたの手持ちの金額は{all_money}円です。')
for m in range(3):
  money=int(input(f'{m+1}回目の購入金額はいくらでしたか？>>'))
  all_money=all_money-money #所持金からどんどん減らしていく
  if all_money<0:
    print('お小遣いが足りません')
    break
  else:
    print(f'現在の金額は{all_money}円です')
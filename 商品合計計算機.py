#商品合計計算機
total=0
print(f'現在の購入金額は{total}円です')
tax=input('消費税を計算結果に含みますか？「y」か「n」で答えてください>>')
if tax=='y':
  for k in range(3):
    goods=input('商品の名前を入力してください>>')
    kingaku=int(input(f'{k+1}回目に購入した，{goods}の金額を入力してください>>'))
    kingaku=kingaku*1.1 #消費税を10%とする
    total+=kingaku
    print(f'現在の購入金額は{total}円です')
else:
  for k in range(3):
    goods=input('商品の名前を入力してください>>')
    kingaku=int(input(f'{k+1}回目に購入した，{goods}の金額を入力してください>>'))
    total+=kingaku
    print(f'現在の購入金額は{total}円です')
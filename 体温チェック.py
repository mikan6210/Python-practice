#体温チェック
body_temperature=float(input('体温を入力してください>>'))
if body_temperature>=37.5:
  print('熱があります，お家でゆっくり休んでください') #ユーザーが間違って整数で入力してしまった時はどうする？
else:
  print('問題ありません')
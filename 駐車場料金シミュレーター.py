#駐車場料金シミュレーター
print('この駐車場は1時間ごとに300円かかり,最大料金は1500円です。')
enter_time=int(input('駐車場の入庫時刻を整数で入力してください>>'))
exit_time=int(input('駐車場の出庫時刻を整数で入力してください>>'))
usage_time=exit_time-enter_time
if usage_time>=0:
    usage_time=exit_time-enter_time
else:
    usage_time=(24-enter_time)+exit_time
print(f'入庫時刻は{enter_time}時で，出庫時刻は{exit_time}時なので，')
print(f'駐車場の利用時間は，{usage_time}時間です。')
usage_hours=[]  #27行目，これをxとする
usage_fees=[]   #27行目，これをyとする
usage_hour=1
for uh in range(5):
    usage_hours.append(usage_hour)
    usage_hour+=1
for uf in range(5):           #一緒に書けなくはないかも？だけど分けて書いた
    usage_fee=300
    usage_fees.append(usage_fee)
prices=[]
for x,y in zip(usage_hours,usage_fees):      #28,29行目は調べました。
    prices.append(x*y)
#price = [x*y for x, y in zip(usage_hours, usage_fees)]のようにまとめてもいいかも？
if 1<=usage_time<=5:
    price=prices[usage_time-1]
else:
    price=1500
print(f'なので,お支払いする金額は{price}円です。')

#1時間300円ずつの加算，利用時間×300でできる→もう少し簡単にできるかも？
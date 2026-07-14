#家計簿システム
count=0
all_money=[]
print('5日分の支出を以下に入力してください')
for m in range(5):
    count+=1
    money=int(input(f'{count}日目の支出金額>>'))
    all_money.append(money)
total=sum(all_money)
average=total/len(all_money)
high=max(all_money)
low=min(all_money)
print(f'合計支出は{total}円です')
print(f'平均支出は{average}円です')
print(f'一番高い支出は{high}円です')
print(f'一番低い支出は{low}円です')
budget=int(input('予算>>'))
if total<=budget:
    print('予算内です')
else:
    print('予算オーバーです')
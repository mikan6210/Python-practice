#テスト成績管理
examinee=input('受験者の名前を入力してください>>')
print(f'{examinee}さんの成績を表示します')
japanese=int(input('国語の点数を入力してください>>'))
math=int(input('数学の点数を入力してください>>'))
society=int(input('社会の点数を入力してください>>'))
science=int(input('理科の点数を入力してください>>'))
english=int(input('英語の点数を入力してください>>')) #各教科の点数入力をもっと簡略化出来る？
scores=[japanese,math,society,science,english]
average=sum(scores)/len(scores)
print(f'あなたの平均点は{average}点です')
if average>=91 and average<=100: #もしくは，if 91<=average<=100:でもいい(他のところも)
  print('あなたはS評価です，おめでとう！')
elif average>=81 and average<=90:
  print('あなたはA評価です，頑張りましたね')
elif average>=71 and average<=80:
  print('あなたはB評価です，惜しかったです')
elif average>=61 and average<=70:
  print('あなたはC評価です，もう少し頑張ってください')
else:
  print('評価対象外です')
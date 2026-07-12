#成績管理システム
names=[]
scores=[]
for n in range(5):
    name=input("名前を入力してください>>")
    names.append(name)
    score=int(input('得点を入力してください>>'))
    scores.append(score)
dictionary=dict(zip(names,scores))
search=input('検索する名前>>')
if search in names:
    search_score=dictionary[search]
    print(f'{search}さんの得点は{search_score}点です')
else:
    print('見つかりません')
#図書貸出管理
books=[]
for b in range(5):
    book=input('登録したい本を入力してください>>')
    books.append(book)
rental=input('借りたい本>>')
if rental in books:
    print(f'{rental}を貸し出しました')
    books.remove(rental)
else:
    print('その本はありません')
result='\n'.join(books)
print(f'現在貸出できる本は，\n{result}\nです')
#レストラン注文管理
menu=[]
recipe_count=1
order_recipe=[]
for r in range(5):
    recipe=input(f'{recipe_count}つ目の料理名を登録してください>>')
    menu.append(recipe)
    recipe_count+=1
while True:
    order=input('注文する料理を入力してください>>')
    if order in menu:
        print(f'{order}の注文を受け付けました')
        menu.remove(order)
        order_recipe.append(order)
        add_order=input('追加で料理を注文しますか？「y」か「n」で答えてください>>')
        if add_order=='y':
            continue
        else:
            break
    else:
        print(f'{order}は当店にはございません')
        add_order=input('追加で料理を注文しますか？「y」か「n」で答えてください>>')
        if add_order=='y':
            continue
        else:
            break
result='\n'.join(order_recipe)
print(f'現在注文している料理は，\n{result}\nです')
possible_order='\n'.join(menu)
print(f'あと，\n{possible_order}\nを注文することができます')
#15~19行目と，22~26行目の内容が同じだから工夫できるかも？
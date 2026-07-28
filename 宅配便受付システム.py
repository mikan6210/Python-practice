#宅配便受付システム
def d_input():   #ここでは，情報の入力をする
    count=1      #input関数と被らないようにdefの頭文字dを最初につけた関数名にした:d_input
    rec_count=0    #recはreceptionの略
    names=[]
    weights=[]
    while True:
        name=(input('荷物を送る担当の名前を入力してください>>'))
        names.append(name)
        weight=(int(input(f'{name}さんが送る荷物の重さを入力してください(kg)>>')))
        weights.append(weight)
        print(f'{name}さんが今回荷物を送る担当です')
        print(f'{name}さんが送る荷物は{weight}kgです')
        rec_count+=1
        again=input('続けて荷物の配達担当を確認しますか？「y」か「n」で答えてください>>')
        if again=='y':
            count+=1
            continue
        else:
            break
    all_weight=sum(weights)
    return rec_count,names,all_weight  #タプルとしてこれらを返す

rec_count,names,all_weight=d_input()
print(f'受付件数は{rec_count}件です')
dis_names='\n'.join(names)
print(f'今回担当した人は,\n{dis_names}\nです')
print(f'荷物の総重量は{all_weight}kgです')
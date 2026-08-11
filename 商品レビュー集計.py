#商品レビュー集計
def d_again():  #繰り返し用
    while True:
        again=input('続けて商品をレビューしますか？「y」か「n」で答えてください>>')
        if again=='y':
            return True
        elif again=='n':
            return False
        else:
            print('「y」か「n」で答えてください')

def registration():  #登録用
    goods_name=input('レビューする商品名を入力してください>>')
    evaluation=True
    while evaluation:
        goods_evaluation=int(input(f'{goods_name}の評価を5段階評価してください。\n'
                                    '1が最低評価,5が最高評価です。>>'))
        if 1<=goods_evaluation<=5:
            break
        else:
            print('その評価はできません，入力し直してください。')
            continue
    vote_count=1
    return goods_name,goods_evaluation,vote_count

def d_deal_information(deal_information):  #データ集計用
    dict_deal_information={}
    for information_tuple,vote_count in deal_information.items():
        if information_tuple[0] in dict_deal_information:
            old_data=dict_deal_information[information_tuple[0]]  #(ポイント,票数)
            evaluation=information_tuple[1]
            add_point=evaluation*vote_count
            point=old_data[0]+add_point
            total_vote=old_data[1]+vote_count
            calc_tuple=(point,total_vote)
            dict_deal_information[information_tuple[0]]=calc_tuple
        else:
            evaluation=information_tuple[1]
            point=evaluation*vote_count
            calc_tuple=(point,vote_count)
            dict_deal_information[information_tuple[0]]=calc_tuple
    return dict_deal_information

def calc_average(calc_data):  #平均計算用
    average_information={}
    for goods_name,calc_tuple in calc_data.items():
        total_point=calc_tuple[0]
        total_vote=calc_tuple[1]
        average=total_point/total_vote
        average_information[goods_name]=average
    return average_information

def average_max_min(average_data):  #最高評価,最低評価用
    max_average=max(average_data.values())
    min_average=min(average_data.values())
    max_dict={}
    min_dict={}
    for goods_name,average in average_data.items():
        if average==max_average:
            max_dict[goods_name]=max_average
        if average==min_average:
            min_dict[goods_name]=min_average
    return max_dict,min_dict

print('入力された商品レビューを管理します。')
dict_information={}  #入力されたレビューの集計データ
while True:
    goods_name,goods_evaluation,vote_count=registration()
    information_tuple=(goods_name,goods_evaluation)
    if information_tuple in dict_information:
        dict_information[information_tuple]+=1
    else:
        dict_information[information_tuple]=vote_count
    if d_again():
        continue
    else:
        break
dict_deal_information=d_deal_information(dict_information)
average_information=calc_average(dict_deal_information)
max_dict,min_dict=average_max_min(average_information)
print('〈平均評価〉')
for goods_name,average in average_information.items():
    print(f'{goods_name}:{average}')
print('〈最高評価〉')
for goods_name,average in max_dict.items():
    print(f'{goods_name}:{average}')
print('〈最低評価〉')
for goods_name,average in min_dict.items():
    print(f'{goods_name}:{average}')
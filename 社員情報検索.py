#社員情報検索
employee_names=[]
department_names=[]
for ed in range(5):
    employee_name=input('社員の名前を入力してください>>')
    employee_names.append(employee_name)
    department_name=input(f'{employee_name}さんの部署名を入力してください>>')
    department_names.append(department_name)
#ほんとはここで社員名と部署名の対応一覧みたいなのを作りたかった
information=dict(zip(employee_names,department_names))
while True:
    search_emp=input('検索したい社員名を入力してください>>')
    if search_emp in information:
        search_dep=information[search_emp]
        print(f'{search_emp}さんは{search_dep}です。')
        add_search=input('追加で社員を検索しますか？「y」か「n」で答えてください>>')
        if add_search=='y':
            continue
        else:
            break
    else:
        print('その社員は登録されていません')
        add_search=input('追加で社員を検索しますか？「y」か「n」で答えてください>>')
        if add_search=='y':
            continue
        else:
            break
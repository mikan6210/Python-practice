#学生出席管理
def again():
    attend_again=input('続けて学生の出席を確認しますか？「y」か「n」で答えてください>>')
    return attend_again=='y'

students=[]
attend_students=[]
for s in range(5):
    student=input('登録する学生の名前を入力してください>>')
    students.append(student)
print('登録された学生の一覧は以下の通りです。')
count=1
for d in range(5):
    display=''.join(students[d])
    print(f'{count}人目:{display}さん')
    count+=1
while True:
    attend_student=input('出席した学生の名前を入力してください>>')
    if attend_student in students:
        students.remove(attend_student)
        attend_students.append(attend_student)
        print(f'{attend_student}さんの出席を受け付けました。')
        if again():
            continue
        else:
            break
    else:
        print(f'{attend_student}さんは登録されていません。')
        if again():
            continue
        else:
            break
print('本日の出席･欠席人数')
print(f'出席:{len(attend_students)}人')
print(f'欠席:{len(students)}人')
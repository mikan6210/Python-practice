#クラス成績分析
def d_again():  #繰り返し確認
    again=input('ほかの人の結果も管理しますか？「y」か「n」で答えてください>>')
    return again=='y'

def registration():  #情報の登録
    students=[]
    scores=[]
    print('クラスのテスト結果を管理します。')
    while True:
        student=input('生徒の名前を入力してください>>')
        students.append(student)
        score=int(input(f'{student}さんのテストの点数を入力してください>>'))
        scores.append(score)
        if d_again():
            continue
        else:
            print('登録を終了します。')
            break
    return students,scores

def display(students,scores):  #表示用
    total_score=sum(scores)
    student_number=len(scores)
    average_score=total_score/student_number  #23行目と24行目はいらないかも？この行でまとめてすれば
    max_score=max(scores)
    min_score=min(scores)
    dis_student='\n'.join(students)
    print(f'登録された生徒は，\n{dis_student}\nです')
    print(f'平均点は，{average_score}点です。')
    print(f'最高点は，{max_score}点です。')
    print(f'最低点は，{min_score}点です。')

students,scores=registration()
display(students,scores)
#名前が重複するとどうする？
#同じ名前の人もいるから許容？名前の重複は避けるべき？
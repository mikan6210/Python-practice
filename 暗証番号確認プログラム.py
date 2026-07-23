#暗証番号確認プログラム
reg=int(input('登録する暗証番号を入力してください>>'))  #registrationの略
print(f'登録された暗証番号は{reg}です。')
count=1
while count<=5:
    user_input=int(input('暗証番号を入力して下さい>>'))
    if user_input==reg:
        print('認証成功')
        break
    elif user_input!=reg and count<=4:
        print('暗証番号が違います。再入力してください。')
        count+=1
        continue
    elif user_input!=reg and count==5:
        print('利用できません')
        count+=1
        continue    #ここはbreakでもいい？→いい，むしろbreakのほうが良さそう
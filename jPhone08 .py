# jPhone Ver4 ホーム画面（メニュー選択）：分岐
title = 'jPhone Ver08'
line = '--------------------'
print(line)
print(title)
print(line)
value = 0
names = []
address = {}
# TODO
while (value !=99):
    print('【ホーム画面】')
    home_menu_item = '１．電卓\t\t２．連絡先\t\t９９.終了'
    print(home_menu_item)
    value = int(input('メニュー選択＞'))
    if value == 1:

        print('【電卓】')
        sum1 = int(input('数値１＞'))
        enzan = (input('演算子＞'))
        if enzan == 'bin':
            print(line)
            print(bin(sum1)[2:])
            print(line)
        elif enzan != 'bin':
            sum2 = int(input('数値２＞'))
            if enzan == '+':
                print(line)
                print(sum1 + sum2)
                print(line)
            elif enzan == '-':
                print(line)
                print(sum1 - sum2)
                print(line)
            elif enzan == '*':
                print(line)
                print(sum1 * sum2)
                print(line)
            elif enzan == '**':
                print(line)
                print(sum1 ** sum2)
                print(line)
            elif enzan == '/':
                print(line)
                print(sum1 / sum2)
                print(line)
            else:
                print(line)
                print('val=入力された演算子は無効です。')
                print(line)
        else:
            print(line)
            print('val=入力された演算子は無効です。')
            print(line)

    
    
    elif value == 2:
        print('【ホーム画面】')
        home_menu_item = '２１．新規連絡先\t\t２２．連絡先一覧\t\t２３.ソート（昇順）' 
        print(home_menu_item)
        value = int(input('メニュー選択＞'))
        # TODO
        if value == 21:
            
            
            print(len(names)+1,'件目')
            print(line)
            name1 = (input('姓（カナ）＞'))
            name2 = (input('名（カナ）＞'))
            phonenumber1 = (input('電話番号＞'))
            names.append(name1 + name2)
            address[names[-1]] = phonenumber1


        
        elif value == 22:
            print('【連絡先一覧】')
            
            for index in range(0,len(names)):
                print(index,names[index]) 
            phone_value = int(input('Ｎｏを入力＞'))
            if  0<=phone_value<len(names):
                print('{}さんの電話番号：{}' .format(names[phone_value],address[names[phone_value]]))
            else: 
                print('「範囲外の No が入力されました。」')
                
        elif value == 23:
            print('【ソート】')
            def bubble_sort(num):
                for i in range(len(num)):
                    for j in range(len(num) - 1 - i):
                        if num[j] > num[j + 1]:
                            num[j], num[j + 1] = num[j + 1], num[j]
                return num

            if __name__ == '__main__':
                import random
                num = (names)
            print(bubble_sort(num))
        else:
            print(line)
            print('！404 Not Found.！ お探しのページ番号は存在しませんでした。')
            print(line)
    elif value == 99:
        print(line)
        print('終了')
        print(line)      
    else:
        print(line)
        print('！404 Not Found.！ お探しのページ番号は存在しませんでした。')
        print(line)
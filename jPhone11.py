# jPhone Ver4 ホーム画面（メニュー選択）：分岐
title = 'jPhone Ver11'
line = '--------------------'
print(line)
print(title)
print(line)
value = 0
names = ['ジョウホウタロウ', 'ヤマダハナコ', 'アオキイチロウ']
address = {'ジョウホウタロウ': '090xxxxxxxx','ヤマダハナコ': '050xxxxxxxx','アオキイチロウ': '070xxxxxxxx'}
# TODO
while (value !=99):
    print('【ホーム画面】')
    home_menu_item = '１．電卓\t\t２．連絡先\t\t３．ゲーム\t\t９９.終了'
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
        home_menu_item = '２１．新規連絡先\t\t２２．連絡先一覧\n２３．ソート（昇順）\t\t２４．連絡先削除\n２５．連絡先検索\t\t２６．連絡先更新' 
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
            num = (names)
            def bubble_sort(num): #俺の嫌いなバブルソート：ただし、交換の必要のないところは省略する。
                change = True   #交換の余地ありと仮定
                
                for i in range(len(num)):
                    
                    if not change: #交換の余地なしとして繰り返し脱出
                        break
                    else:
                        print(i + 1,'回目')    
                    change = False
                    for j in range(len(num) - 1 - i):
                        
                        if num[j] > num[j + 1]:
                            num[j], num[j + 1] = num[j + 1], num[j]
                            change = True #交換の余地ありかも
                        print(num)
                return num

            print(bubble_sort(num))
        
        elif value == 24:
            print('【連絡先削除】')
            for index in range(0,len(names)):
                print(index,names[index]) 
            phone_value = int(input('Ｎｏを入力＞'))
            aa = (names[phone_value])
            bb = input(aa+'さんの情報を削除してもよいですか？(yes/no)＞')
            if  bb == 'yes':
                del ([names[phone_value]])
                print('削除しました')
            else: 
                print('削除を取り消しました。')    
        
        elif value == 25:
            print('【連絡先検索】') 
            index = -1
            i = 0
            phone_names = input('氏名を入力＞')
            
            found = False #処理状況管理（初期値はFalse）
            for i in range(len(names)):
                if names[i] == phone_names: #見つけたい値と一致したか？
                    index = address[names[i]]
                    print('{}さんの電話番号：{}' .format(phone_names,index))
                    found = True #見つかったことを処理状況としてセット
                    break
            
            if not found:
                print('「知らん名前が入力されました。」')
            
            

        
        elif value == 26:
            print('【連絡先更新】')
            
            for index in range(0,len(names)):
                print(index,names[index]) 
            phone_value = int(input('Ｎｏを入力＞'))
            if  0<=phone_value<len(names):
                print('{}さんの電話番号：{}' .format(names[phone_value],address[names[phone_value]]))
                new = (input('新しい電話番号＞'))
                del (address[names[phone_value]])
                address[names[phone_value]] = new
            else: 
                print('「範囲外の No が入力されました。」')
                
                
        else:
            print(line)
            print('！404 Not Found.！ お探しのページ番号は存在しませんでした。')
            print(line)
                    
    elif value == 3:
        print('【ゲーム】')
        game_item = '３１．ポイント照会\t\t３２．じゃんけん'
        print(game_item)
        game_value = int(input('メニュー選択＞'))
        if game_value == 31:     #まだ実装しない
            print('メンテンナンス中です。しばらくたってからもう一度お試しください。')
            
        elif game_value == 32:
            print('【じゃんけん】')
            print('じゃーんけーん・・・')
            
            import random
            list = ['グー','チョキ','パー'] #リストにじゃんけんの手を格納
            play = int(input('0:グー/1:チョキ/2:パー＞'))
            if play == 0:
                player = 'グー'
            elif play == 1:
                player = 'チョキ'
            elif play == 2:
                player = 'パー'
            
            com = random.choice(list)   #リストからランダムに選択させる
            
            if player == com:
                result_j = 'あいこ'
            elif player == 'グー':
                if com == 'チョキ':
                    result_j = '勝ち'
                elif com == 'パー':
                    result_j = '負け'
            elif player == 'チョキ':
                if com == 'パー':
                    result_j = '勝ち'
                elif com == 'グー':
                    result_j = '負け'
            elif player == 'パー':
                if com == 'グー':
                    result_j = '勝ち'
                elif com == 'チョキ':
                    result_j = '負け'
            
            print('COM：{}' .format(com))
            print('あなた：{}' .format(player))
            
            print(line)
            print(result_j)
            print(line)
            
        
    elif value == 99:
        print(line)
        print('終了')
        print(line)      
    else:
        print(line)
        print('！404 Not Found.！ お探しのページ番号は存在しませんでした。')
        print(line)
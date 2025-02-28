# jPhone Ver12 改 ... jPhone 12の改造ヴァージョン
title = 'jPhone Ver12 改'
line = '----------------------------------------------------------------------------------------------------'
print(line)
print(title)
print(line)
value = 0
names = ['ジョウホウタロウ', 'ヤマダハナコ', 'アオキイチロウ']
address = {'ジョウホウタロウ': '090xxxxxxxx','ヤマダハナコ': '050xxxxxxxx','アオキイチロウ': '070xxxxxxxx'}
point = 0
# TODO
while (value !=99):
    print('【ホーム画面】')
    home_menu_item = '１．電卓\t\t２．連絡先\t\t３．ゲーム\t\t９９.終了'
    print(home_menu_item)
    value = int(input('メニュー選択＞'))
    if value == 1:  #電卓

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
        if value == 21:  #連絡先追加機能
            
            
            print(len(names)+1,'件目')
            print(line)
            name1 = (input('姓（カナ）＞'))
            name2 = (input('名（カナ）＞'))
            phonenumber1 = (input('電話番号＞'))
            names.append(name1 + name2)
            address[names[-1]] = phonenumber1

        elif value == 22:  #連絡先一覧表示
            print('【連絡先一覧】')
            
            for index in range(0,len(names)):
                print(index,names[index]) 
            phone_value = int(input('Ｎｏを入力＞'))
            if  0<=phone_value<len(names):
                print('{}さんの電話番号：{}' .format(names[phone_value],address[names[phone_value]]))
            else: 
                print('「範囲外の No が入力されました。」')
                
        elif value == 23:  #昇順にソートする機能
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
        
        elif value == 24:  #連絡先を削除する機能
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
        
        elif value == 25:  #連絡先を検索する機能
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
            
        elif value == 26:  #連絡先を変更、更新する機能
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
        if game_value == 31:     #現在の獲得ポイントを表示
            print('【ポイント照会】')
            print('現在、{}ポイントです。' .format(point))
            
        elif game_value == 32:  #本田圭佑とじゃんけん勝負！
            result_j = 'abcd'
            point = 10
            while (result_j != '勝ち'):
                print('【じゃんけん】')
                print('ログインボーナス→10point')
                print('じゃーんけーん・・・')
                bomb = 'ポン！'
                
                import random
                list = ['グー','チョキ','パー'] #リストにじゃんけんの手を格納
                play = int(input('1:グー/2:チョキ/3:パー＞'))
                if play == 1:
                    player = 'グー'
                elif play == 2:
                    player = 'チョキ'
                elif play == 3:
                    player = 'パー'
                elif play == 10:
                    player = 'ダイナマイト'
                
                com = random.choice(list)   #リストからランダムに選択させる
                
                if player == com:
                    result_j = 'あいこ'
                    result_xy = ' '
                elif player == 'グー':
                    if com == 'チョキ':
                        result_j = '勝ち'
                    elif com == 'パー':
                        result_j = '負け'
                    result_xy = ' '
                elif player == 'チョキ':
                    if com == 'パー':
                        result_j = '勝ち'
                    elif com == 'グー':
                        result_j = '負け'
                    result_xy = ' '
                elif player == 'パー':
                    if com == 'グー':
                        result_j = '勝ち'
                    elif com == 'チョキ':
                        result_j = '負け'
                    result_xy = ' '
                elif player == 'ダイナマイト':
                    result_j = '勝ち'
                    result_xy = 'ほんだけいすけはばくしした'
                    bomb = 'ドーン！！！'
                
                print('COM：{}' .format(com))
                print('あなた：{}' .format(player))
                print('じゃーんけーん・・・{}' .format(bomb))
                if result_j == '勝ち':
                    if result_xy == 'ほんだけいすけはばくしした':
                        print(line)
                        print(result_xy)
                        print(line)
                        point += 800000000
                        print('8億ポイント獲得！')
                    elif result_xy == ' ':    
                        print(line)
                        print('やるやん。明日俺にリベンジさせて (結果:{})' .format(result_j))
                        print(line)
                        point += 10
                        print('10ポイント獲得！')
                        
                elif result_j == '負け':
                    import random
                    result_x = random.randint(1,3)
                    if result_x == 1:
                        print(line)
                        print('俺の勝ち！なんで負けたか明日までに考えておいてください。そしたら何かが見えてくるはずです。(結果:{})'.format(result_j))
                        print(line)
                        point = point - 10
                        print('10ポイント没収！')
                    elif result_x == 2:
                        print(line)
                        print('負けは次に繋がるチャンスです。ネバーギブアップ！ (結果:{})' .format(result_j))
                        print(line)   
                        point = point - 10
                        print('10ポイント没収！')
                    elif result_x == 3:
                        print(line)
                        print('たかがじゃんけん、そう思ってないですか？それやったら明日も俺が勝ちますよ。（結果:{})' .format(result_j))
                        print(line)
                        point = point - 10
                        print('10ポイント没収！')
                    else:
                        break
                elif result_j == 'あいこ':
                    print(line)
                    print(result_j)
                    print(line)
                    point = point - 5
                    print('5ポイント没収！')
                else:
                    break
        
        elif game_value == 1: #制作者しか知らない隠しコマンド
            
            import random

            energy = 500
            damage = 0
            enem_hp = random.randint(500000,1000001)
            print('まもののむれが現れた！：{}' .format(enem_hp))

            while damage >= 0:
                #なんかよくわからない戦いね
                print('【隠しゲーム～ドラゴンクエスチョン～】')
                command = int(input('１．パンチ,２．キック,３．必殺技,４．逃げる,５．最後の切り札＞'))    
                if command == 1: #ただのパンチ
                    damage = 100
                elif command == 2: #ただのキック
                    if energy > 0:
                        energy -= 100
                        damage = 200
                    else: #エネルギーが足りない時の処理だよ
                        print('エネルギーが足りねえ！！')
                        print('現在のエネルギー:{}'.format(energy))
                        continue
                elif command == 3: #必殺技だよ
                    if energy > 20:
                        energy -= 300
                        damage = 5000 
                    else:
                        print('エネルギーが足りねえ！！')
                        print('現在のエネルギー:{}'.format(energy))
                        continue
                elif command == 4: #~Escape~
                    print(line)
                    print('いやにげるんかい')
                    print(line)
                    break
                    
                elif command == 5: #最後の切り札だよ
                    print('～最後の切り札～')
                    energy -= 450
                    damage = 500000
                        
                elif command == 6: #選択肢にはない隠しコマンド
                    print('～人間には感じ取ることが出来ない音～')
                    print('？？「あぁ～水素の音ぉ～！」')
                    damage = 1000000000
                    print('まものはきもちよくなってそのまま永遠の眠りについた！')
                        
                elif command == 7: #選択肢にはない隠しコマンドアルファ
                    print('～ラッキー7～')
                    lucky = int(input('1(回復)か2(攻撃)を選んでね！攻撃量と回復量はランダムだよ！＞'))
                    import random
                    lucky_no = random.randint(500,10000)
                    if lucky == 1:
                        energy = energy + lucky_no
                        damage = 0
                        print('現在のエネルギー:{}'.format(energy))
                    elif lucky == 2:
                        damage = lucky_no
                    else:
                        print('もう一度入力してくれ！') 
                        
                elif command == 8:  #選択肢にはない隠しコマンド
                    print('～最終兵器～')
                    damage = 100000000
                    print('まもののむれはHCSの８階から飛び降りた！')
                    
                elif command == 846:  #選択肢にはない最強の隠しコマンド
                    print('～神様の攻撃～')
                    print('管理職の権限を行使してまもののむれを全員除籍させた！')
                    print('まもののむれはかなしいかおをして帰っていった')
                    print('この世のすべてを司る矢代の大御神にお賽銭500万円を納めた！')
                    break
                    
                elif command == 9:  # Bad End
                    print('～え？なんでここに警察が？～')
                    print('まもののむれは、「迷惑防止条例違反」でけんきょされた！')
                    print('まもののむれをたおした？')
                    break

                elif command == 132109:   #選択肢にはない隠しコマンド
                    print('？？「お医者さんカバン～」')
                    energy = energy + 100000000
                    damage = 0
                    print('現在のエネルギー:{}'.format(energy))
                else:
                    print('お気の毒ですが、ぼうけんしょ1は削除されました。')
                        
                    break
                        
                enem_hp -= damage
                if enem_hp < 0:
                    enem_hp = 0
                print('まもののむれに{}ダメージ与えた！残りHP{}' .format(damage,enem_hp))
            
                if enem_hp > 0:
                    continue
                else:
                    print('まもののむれをたおした！')
                    break
            
        elif game_value == 2: #制作者しか知らない隠しコマンドvol.2  岩見沢市（旧栗沢町）にある看板を表示するだけ
            print('------------------------------------------')
            print('|        たべたくなるほど、おいしい      |')
            print('|             栗沢のいちごは             |')
            print('|                栗沢一だ                |')     
            print('|            🍓         🍓               |')
            print('|                                        |')
            print('|栗沢町農業協同組合・栗沢町いちご生産組合|')
            print('------------------------------------------')
            print(' ')
            print('栗沢のいちごは栗沢一だとは、北海道岩見沢市の栗沢地区（旧栗沢町）に設置されている謎看板である。')
            print(' ')
            
        else:
            print('ほかの機能はまだメンテンナンス中です。しばらく経ってからやり直してください。')
            
    elif value == 99:
        print(line)
        print('終了')
        print(line)      
    else:
        print(line)
        print('！404 Not Found.！ お探しのページ番号は存在しませんでした。')
        print(line)
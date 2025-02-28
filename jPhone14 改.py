# jPhone Ver14 改 ... jPhone 14の改造ヴァージョン
title = 'jPhone14 改  jOS 14.9'
line = '----------------------------------------------------------------------------------------------------'
print(line)
print(title)
print(line)
value = 0
names = ['ジョウホウタロウ', 'ヤマダハナコ', 'アオキイチロウ']
address = {'ジョウホウタロウ': '090xxxxxxxx','ヤマダハナコ': '050xxxxxxxx','アオキイチロウ': '070xxxxxxxx'}
global point
point = 0
# TODO
global sum1
global enzan
global sum2


def calc_main():
        global sum1
        global enzan
        global sum2
        """計算機能
        計算に必要な情報を入力させ、calc を呼び
        出し、計算結果を表示する.
        """
        
        print('【電卓】')
        sum1 = int(input('数値１＞'))
        enzan = (input('演算子＞'))
        calc()
        
def calc():

        """計算処理
        引数で渡された値を演算子にしたがって計算し
        結果を返す.
        引数:
        sum1 (int): 計算対象の値.
        sum2 (int): 計算対象の値.
        enzan(str): 演算子.
        戻り値:
        int: 計算結果.
        """
        
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
            
        
            
        main()

        
def address_main():
        """連絡先機能
        連絡先機能のメニューを入力させ、入力さ
        れた番号に従って処理を振り分ける.「９９，
        戻る」が押されるまで連絡先機能の処理を繰り
        返す.
        """
        global value
        print('【ホーム画面】')
        home_menu_item = '２１．新規連絡先\t\t２２．連絡先一覧\n２３．ソート（昇順）\t\t２４．連絡先削除\n２５．連絡先検索\t\t２６．連絡先更新' 
        print(home_menu_item)
        value = int(input('メニュー選択＞'))
        if value == 21:
            address_append()
        elif value == 22:
            address_list()
        elif value == 23:
            address_sort()
        elif value == 24:
            address_remove()
        elif value == 25:
            address_search()
        elif value == 26:
            address_target()
        else:
            print('お探しのページは存在しません')
            main()
        # TODO
        
        
        global names 
        global address
        
def address_append():
            
            """新規連絡先の追加
            氏名と電話番号を入力させ、連絡先情報と
            して管理する.
            """
            print(len(names)+1,'件目')
            print(line)
            name1 = (input('姓（カナ）＞'))
            name2 = (input('名（カナ）＞'))
            phonenumber1 = (input('電話番号＞'))
            names.append(name1 + name2)
            address[names[-1]] = phonenumber1
            
            main()

def address_list():
            """連絡先の表示
            list_disp を呼び出し、氏名の一覧を表示
            する.address_target を呼び出し、個別処理対
            象の index を取得する.index がリストの範囲内
            であれば、処理対象の電話番号を表示す
            る.index がリストの範囲外であれば、エラーメ
            ッセージを表示する
            """
            
            print('【連絡先一覧】')
            
            for index in range(0,len(names)):
                print(index,names[index]) 
            phone_value = int(input('Ｎｏを入力＞'))
            if  0<=phone_value<len(names):
                print('{}さんの電話番号：{}' .format(names[phone_value],address[names[phone_value]]))
            else: 
                print('「範囲外の No が入力されました。」')
                
            main()
                
def address_sort():
            """連絡先のソート
            氏名の昇順に氏名のリストをソートする.
            """
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
            
            main()
        
def address_remove():
            """連絡先の削除
            list_disp を呼び出し、氏名の一覧を表
            示する.address_target を呼び出し、削除対
            象の index を入力させる.削除の警告メッセ
            ージを表示し、「yes」「no」を入力させる.
            「yes」が入力された場合、対象の連絡先を
            リストと辞書から削除する.「no」が入力さ
            れた場合は削除せず、その旨のメッセージ
            を表示する.
            """
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

            main()
        
def address_search():
            """連絡先の検索
            検索対象の氏名を入力させる.氏名がリス
            ト中に存在する場合は、連絡先を表示する.存
            在しなければ、エラーメッセージを表示する.
            """
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
            
            main()            
        
def address_target():
            """処理対象の連絡先入力
            処理対象とする連絡先の index を入力さ
            せ、処理対象の index を返す.
            戻り値:
            index: 処理対象の index.範囲外の
            index が入力された場合、「範囲外の No が入力されました。」 を返す.
            """
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
                
            main()                
                    
                    
def game_main():
        
        """ゲーム機能
        ゲーム機能のメニューを入力させ、入力さ
        れた番号に従って処理を振り分ける.「９９，
        戻る」が押されるまでゲーム機能の処理を繰り
        返す.
        """
        print('【ゲーム】')
        game_item = '３１．ポイント照会\t\t３２．じゃんけん\t\t３３．ホーム画面\t\t１．ドラゴンクエスチョン\t\t６．宝くじ'
        print(game_item)
        game_value = int(input('メニュー選択＞'))
        global point
        global n

        if game_value == 31:
            point_disp()
        elif game_value == 32:
            jyanken_main()
        elif game_value == 33:
            main()
        elif game_value == 1:
            command_1()
        elif game_value == 2:
            command_2()
        elif game_value == 3:
            command_3()
        elif game_value == 4:
            command_4()
        elif game_value == 5:
            command_5()
        elif game_value == 6:
            command_6()
        elif game_value == 7:
            command_7()
        else:
            main()
        
def point_disp():
    
        print('【ポイント照会】')
        print('現在、{}ポイントです。' .format(point))
        game_main()
                
def jyanken_main():   #じゃんけんゲーム
            global random
            global list
            global player
            global bomb
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
            else:
                print('ほんだけいすけ「そんな選択肢聞いたことありません。ペ〇シジャパンコ〇ラでも飲んで、頭爆発しましょう★」')
                point = point - 50
                print('ケイスケホンダに50ポイントとペプ〇ジ〇パン〇ーラ没収された！')
                main()
            jyanken_judge()
            
def jyanken_judge():
            global result_j
            global random
            global list
            global player
            global bomb
            global result_xy
            global com
            
            """じゃんけんの判定
            引数で渡されたユーザの手と COM の手を
            もとに、じゃんけんの勝敗を判定する.判定条
            件に一致しない場合（ユーザの手が範囲外の場
            合など）、エラーメッセージを表示する。
            引数:
            you (int): ユーザの手（0:グー/1:チョ
            キ/2:パー/10:ダイナマイト）.
            com (int): COM の手（0:グー/1:チョ
            キ/2:パー）.
            戻り値:
            result: 勝敗の結果
            （WIN/DRAW/LOSE/atomic bomb victim）. 
            """            
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
            point_update()

def point_update():
            global point            
            """ポイント更新
            勝敗に応じてポイントを更新する.今回獲
            得したポイント数を表示する.
            
            引数:
            result: 勝敗の結果（WIN/DRAW/LOSE）.
            """
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
                    main()
            elif result_j == 'あいこ':
                print(line)
                print(result_j)
                print(line)
                point = point - 5
                print('5ポイント没収！')
            game_main()
        
def command_1(): #リリースした隠しコマンド
            
            import random

            energy = 500
            damage = 0
            enem_hp = random.randint(500000,1000001)
            print('【隠しゲーム～ドラゴンクエスチョン～】')
            print('まもののむれが現れた！：{}' .format(enem_hp))

            while damage >= 0:
                #なんかよくわからない戦いね
                
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
                    print('まもののむれはHuman Control Schoolの８階から飛び降りた！')
                    
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
            game_main()
            
def command_2(): #制作者しか知らない隠しコマンドvol.2  岩見沢市（旧栗沢町）にある看板を表示するだけ
            global point
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
            print('隠し部屋を見つけたボーナスとして8億ポイントプレゼント！')
            point += 800000000
            game_main()
            
def command_3(): #制作者しか知らない隠しコマンドvol.3  北海道の高速道路をランダムで表示するだけ
            print('【北海道の高速道路をランダムで表示してE5道央道が出るまで終わらないよ★】')
            print('Enterを押すと始まるよ！')
            global space_only
            space_only = input(' ')
            iii = 0
            Avenue =['E5函館新道','E5道央自動車道','E5名寄美深道路','E5音威子府バイパス','E5豊富バイパス・幌富バイパス','E5A札樽自動車道','E5A後志自動車道','E5A黒松内新道','E38/E44/E61道東自動車道','E39旭川紋別自動車道','E44根室道路','E59函館江差自動車道','E60日高自動車道','E61十勝オホーツク自動車道','E62帯広広尾自動車道','E63深川留萌自動車道']
            while (iii != 1):
                import random
                iii = random.randint(0,15)
                print('----------------------')
                print(Avenue[iii])
                print('----------------------')
            print('お出かけの際は安全運転で！')
            game_main()
            
def command_4(): #制作者しか知らない隠しコマンドvol.4  ピンクの小粒（三遊亭）コーラック
            global point
            print('～ピンつまのコーナー～')
            
            print('（予備知識）ピンつまとは、三遊亭好楽（ピンク）の回答がつまらないというネットスラングである')
            
            print(' ,,ー----、')
            print(' || ▲ ▲ ｜')
            print(' 6 ￢u￢ |　')
            print(' ヽ　∀　ノ　 ＜今日の笑点も、俺様の答えでおまえらを笑い死にさせてやるよ。')
            print(' ／/Ｙ　|＼　')
            

            print('　　　　/　　　　/￣ /　　　　　　　　　　　　/ ')
            print('　　　 ＿＿＿＿/￣　＿＿/    /　　　　/￣￣　/ ')
            print('　　　/　　　　　　　　　 　/　　　＿/　    / ')
            print('　　 /　　　　　　　       /　　　　       / ')
            print('　＿＿＿＿＿/　　＿＿＿ ＿/　　　　　 　＿/    ')
            print(' ')
            print('隠し部屋を見つけたボーナスとして8億ポイントプレゼント！')
            point += 800000000
            game_main()
        
def command_5(): #制作者しか知らない隠しコマンドvol.5 よくわからないガチャ
            global space_only
            a = ['01 札幌','A13 岩見沢','A16 美唄','A20 砂川','A21 滝川','A24 深川','A28 旭川']
            # TODO
            print('Enterを押すと特別急行ライラックの停車駅がランダムで表示されるよ！')
            space_only = input(' ')
            import random
            result = random.choice(a)
            print('----------------------')
            print(result)    
            print('----------------------')
            game_main()
            
def command_6(): #リリースした隠しコマンドvol.6 ポイントを利用した宝くじ
            global space_only
            global point
            if point == 0:
                print('ほかのゲームでポイントを獲得してからもう一度お試しください')
            
            else:
                print('現在のポイント{}'.format(point))
                print('10ポイント使って宝くじができるよ！当選したくじによってはポイントが増えるよ！ Enterを押してね！')
                space_only = input(' ')
                import random as rand
                point = point - 10
                result = rand.randint(1,100)
                if result == 1:
                    print(line)
                    print('大当たり！！　100億ポイントプレゼント！')
                    print(line)
                    point = point + 10000000000
                        
                elif result <= 50:
                    print(line)
                    print('あたり！！　ヘルニアの私から5千万ポイントプレゼント！')
                    print(line)
                    point = point +  50000000
                    
                elif result <= 95:
                    print(line)
                    print('小当たり！　本当はポイントぶんどりたいけど、心優しい（笑）わたしから5万ポイントプレゼント！\nもしかしたら肘とかなおるかも？？')
                    print(line)
                    point = point +  50000
                else:
                    print(line)
                    print('おおはずれ！！')
                    print(line)
                    print('？？「山田君、全部持ってきなさい！！」')
                    print('ポイントをすべて没収された...')
                    
                    point = 1
            game_main()
        
def command_7(): #ジャパンワールドカップ in Python
            global point
            if point == 0:
                print('ほかのゲームでポイントを獲得してからもう一度お試しください')
                game_main()
            else:
                    import random
                    from tqdm import tqdm
                    from time import sleep
                    print('～競馬予想のコーナー～')  
                    umadic = {
                        "ギンシャリボーイ": 0,
                        "ピンクフェロモン": 1,
                        "チョクセンバンチョー": 2,
                        "ハイウッドリムジン": 3,
                        "バーニングビーフ": 4,
                        "サバンナストライプ": 5,
                        "ジラフ": 6,
                        "ハリボテエレジー": 7
                    }
                    print('出走馬:', umadic)

                    # ゲームループ
                    while True:
                        print('現在のポイント:', point)
                        
                        # ユーザーの予想入力
                        try:
                            s = int(input('どの馬が優勝するか予想してみましょう(左から、数字で入力してください)＞'))
                            if s not in umadic.values():
                                if s != 800:
                                    print("無効な選択肢です。もう一度入力してください。")
                                    continue
                        except ValueError:
                            print("数字を入力してください！")
                            continue
                        
                        # 賭けポイント入力
                        try:
                            q = int(input('何ポイント賭けますか？＞'))
                            if q <= 0 or q > point:
                                print("賭けポイントが無効です。もう一度入力してください。")
                                continue
                        except ValueError:
                            print("数字を入力してください！")
                            continue
                        
                        # ポイントを差し引く
                        point -= q
                        
                        #ハリボテエレジーの確定演出
                        if s == 800:     #隠しコマンドというかただのずる
                            u = list(umadic.keys())[7]
                            import random
                            nn = random.randint(50000,100000)
                            
                            
                            from tqdm import tqdm
                            from time import sleep
                                        
                            print('range(10)')                                                      #お気持ちで付けたプログレスバー
                            for i in tqdm(range(10), desc="proc1", postfix="range", ncols=80):
                                sleep(0.2)
                                pass

                            print("----------------------------------------------------")

                            print('range(10)')                                                      #お気持ちで付けたプログレスバー
                            print('「曲がれええええええええ!!」')
                            print('「ハリボテぇえええ！！」')
                            dics = {0: 'a', 1:'b', 2: 'c', 3:'d'}
                            for k, v in tqdm(dics.items(), desc="proc2", postfix="dict", ncols=80):
                                sleep(0.2)
                                pass
                                            
                            print("----------------------------------------------------")
                            print(u)                                                      #結果を表示
                            print("----------------------------------------------------")
                            s == u  #あたり
                            get_point = q * nn
                            point = point + get_point
                            print('{}ポイント獲得！'.format(get_point))
                            print('現在のポイント：{}' .format(point))
                            # ゲーム終了判定
                            finish = input('ゲームを終了しますか？(yes/no)＞').strip().lower()
                            if finish == 'yes':
                                print("ゲームを終了します。")
                                False
                                game_main()
                            else:
                                continue

                        # 勝ち馬をランダム決定
                        winning_horse = random.randint(0, 7)

                        # 配当倍率
                        if winning_horse == 7:  # ハリボテエレジー
                            payout_multiplier = random.randint(50000, 100000)
                        else:
                            payout_multiplier = random.randint(100, 10000)

                        # プログレスバー表示（お気持ち機能）
                        print("レーススタート！")
                        for _ in tqdm(range(10), desc="レース進行中", ncols=80):
                            sleep(0.2)
                            
                        print('range(10)')                                 #お気持ちで付けたプログレスバー
                        print('「曲がれええええええええ!!」')
                        print('「段ボールのはがれる音！！！」')
                        print('「ハリボテぇえええ！！」')
                        dics = {0: 'a', 1:'b', 2: 'c', 3:'d'}
                        for k, v in tqdm(dics.items(), desc="proc2", postfix="dict", ncols=80):
                            sleep(0.2)
                            pass

                        # 結果表示
                        print("----------------------------------------------------")
                        print("勝者は…", list(umadic.keys())[winning_horse])
                        print("----------------------------------------------------")

                        # 結果判定
                        if s == winning_horse:
                            winnings = q * payout_multiplier
                            point += winnings
                            print(f"おめでとうございます！{winnings}ポイント獲得！")
                        else:
                            print("残念！はずれです。")

                        # ゲーム終了判定
                        finish = input('ゲームを終了しますか？(yes/no)＞').strip().lower()
                        if finish == 'yes':
                            print("ゲームを終了します。")
                            False
                            game_main()

    
def info():
        print('')
        print('【jPhoneの取扱説明書】')
        print('ここにはたくさんの機能が詰まっているjOS13.6が内蔵されていますが、様々なページに隠しコマンドを仕組んでいます。')
        print('メニュー選択のところでいろいろ試して見てください。どうせ違ってもホームに戻るだけなのでなんの躊躇も要りません。')
        print('隠しコマンドをたくさん見つけられた人は明日いいことがあるかどうかわかんね')
        print('ただし、ホーム画面にはないです。')
        print('')
        main()
        

def get_weather(city, api_key):
    import requests
    # OpenWeatherMapのAPIエンドポイント
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # リクエストパラメータ
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",  # 温度を摂氏で取得
        "lang": "ja"       # 日本語でのレスポンス
    }
    
    try:
        # APIリクエストを送信
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # HTTPエラーがあれば例外を発生
        
        # レスポンスデータを取得
        weather_data = response.json()
        
        # 必要な情報を抽出
        city_name = weather_data["name"]
        temp = weather_data["main"]["temp"]
        weather = weather_data["weather"][0]["description"]
        
        # 天気情報を表示
        print(f"【{city_name}の天気予報】")
        print(f"現在の気温: {temp}°C")
        print(f"天候: {weather}")
        print(line)
    except requests.exceptions.RequestException as e:
        print(f"エラーが発生しました: {e}")
        print(line)
    except KeyError:
        print("天気情報の取得に失敗しました。")
        print(line)
    main()
    

# メイン実行部分
def weather():
    # 使用する都市名とAPIキーを指定
    print(line)
    print('【天気予報検索】')
    city_name = input("天気を知りたい都市名を入力してください: ")
    print(line)
    api_key ="d8940c5170364c7e0bd18b1c0ba3b3cf"# OpenWeatherMapのAPIキー
    
    get_weather(city_name, api_key)

    
def main():
    print('【ホーム画面】')
    home_menu_item = '１．電卓\t\t２．連絡先\t\t３．ゲーム\t\t４．取扱説明書\t\t５．天気予報\t\t９９.終了'
    print(home_menu_item)
    value = int(input('メニュー選択＞'))
    if value == 1:
        calc_main()
    elif value == 2:
        address_main()
    elif value == 3:
        game_main()
    elif value == 4:
        info()
    elif value == 5:
        weather()
    elif value == 99:
        print('シャットダウンしています')
        import sys
        sys.exit()
            
    # 実行制御
if __name__ == '__main__':
    main()
        
    
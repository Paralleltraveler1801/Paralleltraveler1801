title = 'jPhone Ver14  jOS 14.0.1'
import random
line = '--------------------'
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
        game_item = '３１．ポイント照会\t\t３２．じゃんけん'
        print(game_item)
        game_value = int(input('メニュー選択＞'))

        if game_value == 31:
            point_disp()
        elif game_value == 32:
            jyanken_main()
        else:
            main()
        
def point_disp():     #現在の獲得ポイントを表示
            
            print('【ポイント照会】')
            print('現在、{}ポイントです。' .format(point))
            main()
            
def jyanken_main():   #じゃんけんゲーム
            global random
            global list
            global player
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
            else:
                ('0~2で入力してください')
                main()
            jyanken_judge()
            
def jyanken_judge():
            global result_j
            
            """じゃんけんの判定
            引数で渡されたユーザの手と COM の手を
            もとに、じゃんけんの勝敗を判定する.判定条
            件に一致しない場合（ユーザの手が範囲外の場
            合など）、エラーメッセージを表示する。
            引数:
            you (int): ユーザの手（0:グー/1:チョ
            キ/2:パー）.
            com (int): COM の手（0:グー/1:チョ
            キ/2:パー）.
            戻り値:
            result: 勝敗の結果
            （WIN/DRAW/LOSE）. 
            """            
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
            point_update()

def point_update():
            global point            
            """ポイント更新
            勝敗に応じてポイントを更新する.今回獲
            得したポイント数を表示する.
            
            引数:
            result: 勝敗の結果（WIN/DRAW/LOSE）.
            """
            
            if result_j == '勝ち': #ポイントの配分
                point += 10
            elif result_j == 'あいこ':
                point += 5
            else:
                point += 0
            
            print(line)
            print(result_j) #結果
            print(line)
            
            print('{}ポイント獲得！' .format(point))
            
            main()

def main():
        print('【ホーム画面】')
        home_menu_item = '１．電卓\t\t２．連絡先\t\t３．ゲーム\t\t９９.終了'
        print(home_menu_item)
        value = int(input('メニュー選択＞'))
        if value == 1:
            calc_main()
        elif value == 2:
            address_main()
        elif value == 3:
            game_main()
        elif value == 99:
            print('シャットダウンしています')
            
    # 実行制御
if __name__ == '__main__':
    main()

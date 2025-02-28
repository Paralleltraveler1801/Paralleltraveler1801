smoto_point = 0
#TODO
print()
print("====開始====")
print()
print("遺憾ながらHCSの教員ですか？")
kyouin = str(input("はい->y,いいえ->n＞"))
if kyouin == "y":
    smoto_point = smoto_point + 1
    print()
    
    print("壁に頭を打ちつけますか？")
    kabe = str(input("はい->y,いいえ->n＞"))
    if kabe == "y" :
        smoto_point = smoto_point + 1
    print()
    
    print("どうでもいい話を永遠としますか？")
    hanasi = str(input("はい->y,いいえ->n＞"))
    if hanasi == "y" :
        smoto_point = smoto_point + 1
    print()
    
    print("授業中に寝ますか？")
    neru = str(input("はい->y,いいえ->n＞"))
    if neru == "y" :
        smoto_point = smoto_point + 1
    print()
    
    print("セクハラ発言をしてきますか？")
    sekuhara = str(input("はい->y,いいえ->n＞"))
    if sekuhara == "y" :
        smoto_point = smoto_point + 1
    print()
    
    print("HCS内でセクハラに関する苦情の件数がいちばん多いですか？")
    kuzyou = str(input("はい->y,いいえ->n＞"))
    if kuzyou == "y" :
        smoto_point = smoto_point + 1
    print()
    
    print("行事がある毎にチョコレートを渡してきますか？")
    kimoi = str(input("はい->y,いいえ->n＞"))
    if kimoi == "y" :
        smoto_point = smoto_point + 1
        print("気持ち悪いでですね。")
    print()
    
    print("その人から『Linax』を取ると、何も残りませんか？")
    linax = str(input("はい->y,いいえ->n＞"))
    if linax == "y" :
        smoto_point = smoto_point + 1
    print()
    
    print("話している最中に、会話に入ってきますか？")
    kaiwa = str(input("はい->y,いいえ->n＞"))
    if kaiwa == "y" :
        smoto_point = smoto_point + 1
    print()
    
    print("なぜ教員として居れるのか謎ですか？")
    kyouin = str(input("はい->y,いいえ->n＞"))
    if kyouin == "y" :
        smoto_point = smoto_point + 1
    print()
    
    if smoto_point >= 0 :
        print("====結果====")
        print("その人は、生徒に嫌われている『S本』という名の生命体の可能性があります。")
        print("S本である可能性{}％".format(smoto_point * 10))
        print()
else :
    print("その人は『S本』ではありません。")
    print("S本である可能性 0 ％")
    print()
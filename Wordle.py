import random

with open("word.txt") as f:#開檔案
    dict = f.read().splitlines()

ans = random.choice(dict)#隨機選擇一個英文字

# print(ans)

count = 5#玩家執行次數

print(ans)
for i in range(count):#進行遊戲回合
    guess = input("Type your guess word and the word must be a length of 5: ")#輸入長度為5的資料
    output = ""#輸出計算
    if len(guess)==5:#確保長度為5
        for i in range(5):#檢查每個英文字母
            # print(guess[i], ans[i])
            if(guess[i]==ans[i]):#是否相等
                output+="A"
            elif(guess[i] in ans):#是否存在
                output+="B"
            elif(guess[i] not in ans):#不存在
                output+="X"
        print("Your input is:", guess)
        print("The outpout is:", output)

        if(output=="AAAAA"):#如果答對就結束
            print("Congratulation!")
            break#答對你就可以不用繼續玩了


        count+=1#再玩一次
    else:#若長度非5，請再重新輸入
        guess = input("Type your guess word and the word must be a length of 5: ")#輸入長度為5的資料

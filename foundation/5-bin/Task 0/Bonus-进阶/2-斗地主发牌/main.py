from random import shuffle

def main() :
    cards = []

    for i in range(3, 11) :
        for j in range(0, 4) :
            cards.append((str(i), i))

    k = 11
    for i in ['J', 'Q', 'K', 'A', '2'] :
        for j in range(0, 4) :
            cards.append((i,k))
        k += 1

    #append()一次只能压入一个元素
    cards.append(("大王", 17))
    cards.append(("小王", 16))
    #extend(["大王", "小王"])一次可以加入多个元素
    #将列表中元素拆成单个元素，分别加入
    #cards.extend(["大王", "小王"])

    shuffle(cards)

    with open("Bonus-进阶/2-斗地主发牌/player1.txt", "w", encoding= "UTF-8") as file :
        player1_cards = sorted(cards[0:17], key = lambda x : x[1])
        for i in range(0, 17) :
            file.write(player1_cards[i][0])
            file.write(' ')
    with open("Bonus-进阶/2-斗地主发牌/player2.txt", "w", encoding= "UTF-8") as file :
        player2_cards = sorted(cards[17:34], key = lambda x : x[1])
        for i in range(0, 17) :
            file.write(player2_cards[i][0])
            file.write(' ')
    with open("Bonus-进阶/2-斗地主发牌/player3.txt", "w", encoding= "UTF-8") as file :
        player3_cards = sorted(cards[34:51], key = lambda x : x[1])
        for i in range(0, 17) :
            file.write(player3_cards[i][0])
            file.write(' ')
    with open("Bonus-进阶/2-斗地主发牌/others.txt", "w", encoding= "UTF-8") as file :
        others_cards = sorted(cards[51:54], key = lambda x : x[1])
        for i in range(0, 3) :
            file.write(others_cards[i][0])
            file.write(' ')

if __name__ == "__main__" :
    main()
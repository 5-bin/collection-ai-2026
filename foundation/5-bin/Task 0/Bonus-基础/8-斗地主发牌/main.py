from random import shuffle

def main() :
    cards = []

    for i in range(2, 11) :
        for j in range(0, 4) :
            cards.append(str(i))

    for i in ['J', 'Q', 'K', 'A'] :
        for j in range(0, 4) :
            cards.append(i)

    #append()一次只能压入一个元素
    cards.append("大王")
    cards.append("小王")
    #extend(["大王", "小王"])一次可以加入多个元素
    #将列表中元素拆成单个元素，分别加入
    #cards.extend(["大王", "小王"])

    shuffle(cards)

    with open("Bonus-基础/8-斗地主发牌/player1.txt", "w", encoding= "UTF-8") as file :
        for i in range(0, 17) :
            file.write(cards[i])
            file.write(' ')
    with open("Bonus-基础/8-斗地主发牌/player2.txt", "w", encoding= "UTF-8") as file :
            for i in range(17, 34) :
                file.write(cards[i])
                file.write(' ')
    with open("Bonus-基础/8-斗地主发牌/player3.txt", "w", encoding= "UTF-8") as file :
            for i in range(34, 51) :
                file.write(cards[i])
                file.write(' ')
    with open("Bonus-基础/8-斗地主发牌/others.txt", "w", encoding= "UTF-8") as file :
            for i in range(51, 54) :
                file.write(cards[i])
                file.write(' ')

if __name__ == "__main__" :
    main()
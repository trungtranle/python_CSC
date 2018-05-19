x = 1
name_1 = input('Nhập tên người chơi thứ nhất: ')
name_2 = input('Nhập tên người chơi thứ hai: ')
while x == 1:
    print('Bắt đầu chơi')

    choose_1 = input('%s nhập: scissors hoặc rock hoặc paper: ' % name_1)
    choose_2 = input('%s: scissors hoặc rock hoặc paper: ' % name_2)

    if choose_1 == "rock":
        if choose_2 == "rock":
            print("Tie")
        elif choose_2 == "paper":
            print("%s loses - %s wins" % (name_1, name_2))
        else:
            print('%s 1 wins - %s loses' % (name_1, name_2))

    if choose_1 == "paper":
        if choose_2 == "paper":
            print("Tie")
        elif choose_2 == "scissors":
            print("%s 1 loses - %s wins" % (name_1, name_2))
        else:
            print('%s 1 wins - %s loses' % (name_1, name_2))

    if choose_1 == "scissors":
        if choose_2 == "scissors":
            print("Tie")
        elif choose_2 == "rock":
            print("%s 1 loses - %s wins" % (name_1, name_2))
        else:
            print('%s 1 wins - %s loses' % (name_1, name_2))
    x = eval(input('Chơi tiếp = 1, ngừng >< 1: '))

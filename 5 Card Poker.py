total = 10000
import random
l = '2'
while l == '1' or l == '2':
    print('You are playing 5 Card Draw Poker')
    print(' ')
    print('1. Player chooses an amount of money to wager')
    print('2. Dealer deals the player 5 cards')
    print('3. Player chooses which cards he/she wants to keep and which he/she wants to switch out with new cards fromt the deck')
    print('4. Dealer switches the cards the player wants switched')
    print('5. The last 5 cards are assessed and winnings are awarded accordingly')
    print(' ')
    print('The odds for this game are as follows:')    
    print('Royal Flush................250:1 ')
    print('Straight Flush..............50:1 ')
    print('Four of a kind..............25:1 ')
    print('Full House...................8:1 ')
    print('Flush........................5:1 ')
    print('Straight.....................4:1 ')
    print('Three of a kind..............3:1 ')
    print('Two Pair.....................2:1 ')
    print('Pair of Jacks or Better......1:1')
    print(' ')
    print('Make sure of these things:')
    print(' ')
    print('1. Your wager does not exceed your total and is a whole number')
    print('2. When asked to choose a card to switch or keep, input the cooresponding number(1-5) found directly to the left of the card')
    print('3. Report any bugs that happen')
    print(' ')
    print('Have fun!!')
    print(' ')
    print('Your starting total is 10,000$')
    while total > 0:
        while l == '2':
            wage = input('please set wager amount --   ')
            l = '1'
        while wage.isnumeric() == False or int(wage) > total:
            print('That is not a valid wager amount, please try again')
            wage = input('please set wager amount --   ')
        wager = int(wage)
        deckscript = ['Ace of Spades', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', '7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades', 'Jack of Spades', 'Queen of Spades', 'King of Spades', 'Ace of Hearts', '2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts', '8 of Hearts', '9 of Hearts', '10 of Hearts', 'Jack of Hearts', 'Queen of Hearts', 'King of Hearts', 'Ace of Clubs', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs', '8 of Clubs', '9 of Clubs', '10 of Clubs', 'Jack of Clubs', 'Queen of Clubs', 'King of Clubs', 'Ace of Diamonds', '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', '7 of Diamonds', '8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds']
        decknumber = [11, 12, 13, 14, 15, 16, 17, 18, 19, 110, 111, 112, 113, 21, 22, 23, 24, 25, 26, 27, 28, 29, 210, 211, 212, 213, 31, 32, 33, 34, 35, 36, 37, 38, 39, 310, 311, 312, 313, 41, 42, 43, 44, 45, 46, 47, 48, 49, 410, 411, 412, 413]
        print(' ')
        print('Here are your cards:')
        pair = 0
        trio = 0
        straight = 0
        royalstraight = 0
        flush = 0
        there = 0
        dealt = random.sample(deckscript, 5)
        newdeckscript1 = list(set(deckscript) - set(dealt))
        a = dealt[0]
        b = dealt[1]
        c = dealt[2]
        d = dealt[3]
        e = dealt[4]
        print('1.', a)
        print('2.', b)
        print('3.', c)
        print('4.', d)
        print('5.', e)
        dealt1 = random.sample(newdeckscript1, 5)
        print(' ')
        x = input('How many cards do you wish to switch?--  ')
        while x != '0' and x != '1' and x != '2' and x != '3' and x != '4' and x != '5':
            print('That is not a valid input, please try again')
            x  = input('How many cards do you wish to switch?--  ')
        if x == '5':
            print(' ')
            print('Your final cards are:')
            f = dealt1[0]
            g = dealt1[1]
            h = dealt1[2]
            i = dealt1[3]
            j = dealt1[4]
            print('1.', f)
            print('2.', g)
            print('3.', h)
            print('4.', i)
            print('5.', j)
            dealtfinal = [f, g, h, i, j]
        if x == '4':
            y = input('Which card do you wish to keep?--  ')
            while y != '1' and y != '2' and y != '3' and y != '4' and y != '5':
                print('That is not a valid input, please try again')
                y  = input('Which card do you wish to keep?--  ')
            if y == '1':
                print(' ')
                print('Your final cards are:')
                f = dealt1[0]
                g = dealt1[1]
                h = dealt1[2]
                i = dealt1[3]
                print('1.', a)
                print('2.', f)
                print('3.', g)
                print('4.', h)
                print('5.', i)
                dealtfinal = [a, f, g, h, i]
            if y == '2':
                print(' ')
                print('Your final cards are:')
                f = dealt1[0]
                g = dealt1[1]
                h = dealt1[2]
                i = dealt1[3]
                print('1.', f)
                print('2.', b)
                print('3.', g)
                print('4.', h)
                print('5.', i)
                dealtfinal = [f, b, g, h, i]
            if y == '3':
                print(' ')
                print('Your final cards are:')
                f = dealt1[0]
                g = dealt1[1]
                h = dealt1[2]
                i = dealt1[3]
                print('1.', f)
                print('2.', g)
                print('3.', c)
                print('4.', h)
                print('5.', i)
                dealtfinal = [f, g, c, h, i]
            if y == '4':
                print(' ')
                print('Your final cards are:')
                f = dealt1[0]
                g = dealt1[1]
                h = dealt1[2]
                i = dealt1[3]
                print('1.', f)
                print('2.', g)
                print('3.', h)
                print('4.', d)
                print('5.', i)
                dealtfinal = [f, g, h, d, i]
            if y == '5':
                print(' ')
                print('Your final cards are:')
                f = dealt1[0]
                g = dealt1[1]
                h = dealt1[2]
                i = dealt1[3]
                print('1.', f)
                print('2.', g)
                print('3.', h)
                print('4.', i)
                print('5.', e)
                dealtfinal = [f, g, h, i, e]
        if x == '3':
            z0 = input('What is the first card you wish to keep?--  ')
            while z0 != '1' and z0 != '2' and z0 != '3' and z0 != '4':
                print('That is not a valid input, please try again')
                z0  = input('How many cards do you wish to keep?--  ')
            z1 = input('What is the second card you wish to keep?--  ')
            if z0 == '1':
                while z1 != '2' and z1 != '3' and z1 != '4' and z1 != '5':
                    print('That is not a valid input, please try again')
                    z1  = input('How many cards do you wish to keep?--  ')
            if z0 == '2':
                while z1 != '3' and z1 != '4' and z1 != '5':
                    print('That is not a valid input, please try again')
                    z1  = input('How many cards do you wish to keep?--  ')
            if z0 == '3':
                while z1 != '4' and z1 != '5':
                    print('That is not a valid input, please try again')
                    z1  = input('How many cards do you wish to keep?--  ')
            if z0 == '4':
                while z1 != '5':
                    print('That is not a valid input, please try again')
                    z1  = input('How many cards do you wish to keep?--  ')
            print(' ')
            print('Your final cards are:')
            if z0 == '1':
                if z1 == '2':
                    f = dealt1[0]
                    g = dealt1[1]
                    h = dealt1[2]
                    i = dealt1[3]
                    print('1.', a)
                    print('2.', b)
                    print('3.', g)
                    print('4.', h)
                    print('5.', i)
                    dealtfinal = [a, b, g, h, i]
                if z1 == '3':
                    f = dealt1[0]
                    g = dealt1[1]
                    h = dealt1[2]
                    i = dealt1[3]
                    print('1.', a)
                    print('2.', f)
                    print('3.', c)
                    print('4.', g)
                    print('5.', h)
                    dealtfinal = [a, f, c, g, h]
                if z1 == '4':
                    f = dealt1[0]
                    g = dealt1[1]
                    h = dealt1[2]
                    i = dealt1[3]
                    print('1.', a)
                    print('2.', f)
                    print('3.', g)
                    print('4.', d)
                    print('5.', h)
                    dealtfinal = [a, f, g, d,h]
                if z1 == '5':
                    f = dealt1[0]
                    g = dealt1[1]
                    h = dealt1[2]
                    i = dealt1[3]
                    print('1.', a)
                    print('2.', b)
                    print('3.', f)
                    print('4.', g)
                    print('5.', e)
                    dealtfinal = [a, b, f, g, e]
            if z0 == '2':
                if z1 == '3':
                    f = dealt1[0]
                    g = dealt1[1]
                    h = dealt1[2]
                    i = dealt1[3]
                    print('1.', f)
                    print('2.', b)
                    print('3.', c)
                    print('4.',g)
                    print('5.',h)
                    dealtfinal = [f, b, c, g, h]
                if z1 == '4':
                    f = dealt1[0]
                    g = dealt1[1]
                    h = dealt1[2]
                    i = dealt1[3]
                    print('1.', f)
                    print('2.', b)
                    print('3.', g)
                    print('4.', d)
                    print('5.',h)
                    dealtfinal = [f, b, g, d, h]
                if z1 == '5':
                    f = dealt1[0]
                    g = dealt1[1]
                    h = dealt1[2]
                    i = dealt1[3]
                    print('1.', f)
                    print('2.', b)
                    print('3.', g)
                    print('4.', h)
                    print('5.', e)
                    dealtfinal = [f, b, g, h, e]
            if z0 == '3':
                if z1 == '4':
                    f = dealt1[0]
                    g = dealt1[1]
                    h = dealt1[2]
                    i = dealt1[3]
                    print('1.', f)
                    print('2.', g)
                    print('3.', c)
                    print('4.', d)
                    print('5.', h)
                    dealtfinal = [f, g, c, d, h]
                if z1 == '5':
                    f = dealt1[0]
                    g = dealt1[1]
                    h = dealt1[2]
                    i = dealt1[3]
                    print('1.', f)
                    print('2.', g)
                    print('3.', c)
                    print('4.', h)
                    print('5.', e)
                    dealtfinal = [f, g, c, h, e]
            if z0 == '4':
                if z1 == '5':
                    f = dealt1[0]
                    g = dealt1[1]
                    h = dealt1[2]
                    i = dealt1[3]
                    print('1.', f)
                    print('2.', g)
                    print('3.', h)
                    print('4.', d)
                    print('5.', e)
                    dealtfinal = [f, g, h, d, e]
        if x == '2':
            z0 = input('What is the first card you wish to switch?--  ')
            while z0 != '1' and z0 != '2' and z0 != '3' and z0 != '4':
                print('That is not a valid input, please try again')
                z0  = input('How many cards do you wish to switch?--  ')
            z1 = input('What is the second card you wish to switch?--  ')
            if z0 == '1':
                while z1 != '2' and z1 != '3' and z1 != '4' and z1 != '5':
                    print('That is not a valid input, please try again')
                    z1  = input('How many cards do you wish to switch?--  ')
            if z0 == '2':
                while z1 != '3' and z1 != '4' and z1 != '5':
                    print('That is not a valid input, please try again')
                    z1  = input('How many cards do you wish to switch?--  ')
            if z0 == '3':
                while z1 != '4' and z1 != '5':
                    print('That is not a valid input, please try again')
                    z1  = input('How many cards do you wish to switch?--  ')
            if z0 == '4':
                while z1 != '5':
                    print('That is not a valid input, please try again')
                    z1  = input('How many cards do you wish to switch?--  ')
            print(' ')
            print('Your final cards are:')
            if z0 == '1':
                if z1 == '2':
                    f = dealt1[0]
                    g = dealt1[1]
                    h = dealt1[2]
                    i = dealt1[3]
                    print('1.', f)
                    print('2.', g)
                    print('3.', c)
                    print('4.', d)
                    print('5.', e)
                    dealtfinal = [f, g, c, d, e]
                if z1 == '3':
                    f = dealt1[0]
                    g = dealt1[1]
                    h = dealt1[2]
                    i = dealt1[3]
                    print('1.', f)
                    print('2.', b)
                    print('3.', g)
                    print('4.', d)
                    print('5.', e)
                    dealtfinal = [f, b, g, d, e]
                if z1 == '4':
                    f = dealt1[0]
                    g = dealt1[1]
                    h = dealt1[2]
                    i = dealt1[3]
                    print('1.', f)
                    print('2.', b)
                    print('3.', c)
                    print('4.', g)
                    print('5.', e)
                    dealtfinal = [f, b, c, g, e]
                if z1 == '5':
                    f = dealt1[0]
                    g = dealt1[1]
                    h = dealt1[2]
                    i = dealt1[3]
                    print('1.', f)
                    print('2.', b)
                    print('3.', c)
                    print('4.', d)
                    print('5.', g)
                    dealtfinal = [f, b, c, d, g]
            if z0 == '2':
                if z1 == '3':
                    f = dealt1[0]
                    g = dealt1[1]
                    h = dealt1[2]
                    i = dealt1[3]
                    print('1.', a)
                    print('2.', f)
                    print('3.', g)
                    print('4.', d)
                    print('5.', e)
                    dealtfinal = [a, f, g, d, e]
                if z1 == '4':
                    f = dealt1[0]
                    g = dealt1[1]
                    h = dealt1[2]
                    i = dealt1[3]
                    print('1.', a)
                    print('2.', f)
                    print('3.', c)
                    print('4.', g)
                    print('5.', e)
                    dealtfinal = [a, f, c, g, e]
                if z1 == '5':
                    f = dealt1[0]
                    g = dealt1[1]
                    h = dealt1[2]
                    i = dealt1[3]
                    print('1.', a)
                    print('2.', f)
                    print('3.', c)
                    print('4.', d)
                    print('5.', g)
                    dealtfinal = [a, b,f, d,g]
            if z0 == '3':
                if z1 == '4':
                    f = dealt1[0]
                    g = dealt1[1]
                    h = dealt1[2]
                    i = dealt1[3]
                    print('1.', a)
                    print('2.', b)
                    print('3.', f)
                    print('4.', g)
                    print('5.', e)
                    dealtfinal = [a, b,f, g, e]
                if z1 == '5':
                    f = dealt1[0]
                    g = dealt1[1]
                    h = dealt1[2]
                    i = dealt1[3]
                    print('1.', a)
                    print('2.', b)
                    print('3.', f)
                    print('4.', d)
                    print('5.', g)
                    dealtfinal = [a, b,f, d,g]
            if z0 == '4':
                if z1 == '5':
                    f = dealt1[0]
                    g = dealt1[1]
                    h = dealt1[2]
                    i = dealt1[3]
                    print('1.', a)
                    print('2.', b)
                    print('3.', c)
                    print('4.', f)
                    print('5.', g)
                    dealtfinal = [a, b, c, f, g]
        if x == '1':
            y = input('Which card do you wish to switch?--  ')
            while y != '1' and y != '2' and y != '3' and y != '4' and y != '5':
                print('That is not a valid input, please try again')
                y  = input('Which card do you wish to keep?--  ')
            if y == '1':
                print(' ')
                print('Your final cards are:')
                f = dealt1[0]
                g = dealt1[1]
                h = dealt1[2]
                i = dealt1[3]
                print('1.', f)
                print('2.', b)
                print('3.', c)
                print('4.', d)
                print('5.', e)
                dealtfinal = [f, b, c, d, e]
            if y == '2':
                print(' ')
                print('Your final cards are:')
                f = dealt1[0]
                g = dealt1[1]
                h = dealt1[2]
                i = dealt1[3]
                print('1.', a)
                print('2.', f)
                print('3.', c)
                print('4.', d)
                print('5.', e)
                dealtfinal = [a, f, c, d, e]
            if y == '3':
                print(' ')
                print('Your final cards are:')
                f = dealt1[0]
                g = dealt1[1]
                h = dealt1[2]
                i = dealt1[3]
                print('1.', a)
                print('2.', b)
                print('3.', f)
                print('4.', d)
                print('5.', e)
                dealtfinal = [a, b, f, d, e]
            if y == '4':
                print(' ')
                print('Your final cards are:')
                f = dealt1[0]
                g = dealt1[1]
                h = dealt1[2]
                i = dealt1[3]
                print('1.', a)
                print('2.', b)
                print('3.', c)
                print('4.', f)
                print('5.', e)
                dealtfinal = [a, b, c, f, e]
            if y == '5':
                print(' ')
                print('Your final cards are:')
                f = dealt1[0]
                g = dealt1[1]
                h = dealt1[2]
                i = dealt1[3]
                print('1.', a)
                print('2.', b)
                print('3.', c)
                print('4.', d)
                print('5.', f)
                dealtfinal = [a, b, c, d, f]
        if x == '0':
            print(' ')
            print('Your final cards are:')
            print('1.', a)
            print('2.', b)
            print('3.', c)
            print('4.', d)
            print('5.', e)
            dealtfinal = [a, b, c, d, e]
        print(' ')
        bd = [int('Ace of Spades' in list(dealtfinal)), int('Ace of Hearts' in list(dealtfinal)), int('Ace of Clubs' in list(dealtfinal)), int('Ace of Diamonds' in list(dealtfinal)), int('2 of Spades' in list(dealtfinal)), int('2 of Hearts' in list(dealtfinal)), int('2 of Clubs' in list(dealtfinal)), int('2 of Diamonds' in list(dealtfinal)), int('3 of Spades' in list(dealtfinal)), int('3 of Hearts' in list(dealtfinal)), int('3 of Clubs' in list(dealtfinal)), int('3 of Diamonds' in list(dealtfinal)), int('4 of Spades' in list(dealtfinal)), int('4 of Hearts' in list(dealtfinal)), int('4 of Clubs' in list(dealtfinal)), int('4 of Diamonds' in list(dealtfinal)), int('5 of Spades' in list(dealtfinal)), int('5 of Hearts' in list(dealtfinal)), int('5 of Clubs' in list(dealtfinal)), int('5 of Diamonds' in list(dealtfinal)), int('6 of Spades' in list(dealtfinal)), int('6 of Hearts' in list(dealtfinal)), int('6 of Clubs' in list(dealtfinal)), int('6 of Diamonds' in list(dealtfinal)), int('7 of Spades' in list(dealtfinal)), int('7 of Hearts' in list(dealtfinal)), int('7 of Clubs' in list(dealtfinal)), int('7 of Diamonds' in list(dealtfinal)), int('8 of Spades' in list(dealtfinal)), int('8 of Hearts' in list(dealtfinal)), int('8 of Clubs' in list(dealtfinal)), int('8 of Diamonds' in list(dealtfinal)), int('9 of Spades' in list(dealtfinal)), int('9 of Hearts' in list(dealtfinal)), int('9 of Clubs' in list(dealtfinal)), int('9 of Diamonds' in list(dealtfinal)), int('10 of Spades' in list(dealtfinal)), int('10 of Hearts' in list(dealtfinal)), int('10 of Clubs' in list(dealtfinal)), int('10 of Diamonds' in list(dealtfinal)), int('Jack of Spades' in list(dealtfinal)), int('Jack of Hearts' in list(dealtfinal)), int('Jack of Clubs' in list(dealtfinal)), int('Jack of Diamonds' in list(dealtfinal)), int('Queen of Spades' in list(dealtfinal)), int('Queen of Hearts' in list(dealtfinal)), int('Queen of Clubs' in list(dealtfinal)), int('Queen of Diamonds' in list(dealtfinal)), int('King of Spades' in list(dealtfinal)), int('King of Hearts' in list(dealtfinal)), int('King of Clubs' in list(dealtfinal)), int('King of Diamonds' in list(dealtfinal))]
        if (bd[0] + bd[1] + bd[2] + bd[3]) == (4) or (bd[4] + bd[5] + bd[6] + bd[7]) == (4) or (bd[8] + bd[9] + bd[10] + bd[11]) == (4) or (bd[12] + bd[13] + bd[14] + bd[15]) == (4) or (bd[16] + bd[17] + bd[18] + bd[19]) == (4) or (bd[20] + bd[21] + bd[22] + bd[23]) == (4) or (bd[24] + bd[25] + bd[26] + bd[27]) == (4) or (bd[28] + bd[29] + bd[30] + bd[31]) == (4) or (bd[32] + bd[33] + bd[34] + bd[35]) == (4) or (bd[36] + bd[37] + bd[38] + bd[39]) == (4) or (bd[40] + bd[41] + bd[42] + bd[43]) == (4) or (bd[44] + bd[45] + bd[46] + bd[47]) == (4) or (bd[48] + bd[49] + bd[50] + bd[51]) == (4):
            print('You got four of a kind!')
            total = total + (23 * wager)
        if  bd[0] + bd[4] + bd[8] + bd[12] + bd[16] + bd[20] + bd[24] + bd[28] + bd[32] + bd[36] + bd[40] + bd[44] + bd[48] == 5 or bd[1] + bd[5] + bd[9] + bd[13] + bd[17] + bd[21] + bd[25] + bd[29] + bd[33] + bd[37] + bd[41] + bd[45] + bd[49] == 5 or bd[2] + bd[6] + bd[10] + bd[14] + bd[18] + bd[22] + bd[26] + bd[30] + bd[34] + bd[38] + bd[42] + bd[46] + bd[50] == 5 or bd[3] + bd[7] + bd[11] + bd[15] + bd[19] + bd[23] + bd[27] + bd[31] + bd[35] + bd[39] + bd[43] + bd[47] + bd[51] == 5:
            flush = flush + 1
        if (bd[0] + bd[1] + bd[2] + bd[3]) == (1) and (bd[4] + bd[5] + bd[6] + bd[7]) == (1) and (bd[8] + bd[9] + bd[10] + bd[11]) == (1) and (bd[12] + bd[13] + bd[14] + bd[15]) == (1) and (bd[16] + bd[17] + bd[18] + bd[19]) == (1):
            straight = straight + 1
        if (bd[20] + bd[21] + bd[22] + bd[23]) == (1) and (bd[4] + bd[5] + bd[6] + bd[7]) == (1) and (bd[8] + bd[9] + bd[10] + bd[11]) == (1) and (bd[12] + bd[13] + bd[14] + bd[15]) == (1) and (bd[16] + bd[17] + bd[18] + bd[19]) == (1):
            straight = straight + 1
        if (bd[20] + bd[21] + bd[22] + bd[23]) == (1) and (bd[24] + bd[25] + bd[26] + bd[27]) == (1) and (bd[8] + bd[9] + bd[10] + bd[11]) == (1) and (bd[12] + bd[13] + bd[14] + bd[15]) == (1) and (bd[16] + bd[17] + bd[18] + bd[19]) == (1):
            straight = straight + 1
        if (bd[20] + bd[21] + bd[22] + bd[23]) == (1) and (bd[24] + bd[25] + bd[26] + bd[27]) == (1) and (bd[28] + bd[29] + bd[30] + bd[31]) == (1) and (bd[12] + bd[13] + bd[14] + bd[15]) == (1) and (bd[16] + bd[17] + bd[18] + bd[19]) == (1):
            straight = straight + 1
        if (bd[20] + bd[21] + bd[22] + bd[23]) == (1) and (bd[24] + bd[25] + bd[26] + bd[27]) == (1) and (bd[28] + bd[29] + bd[30] + bd[31]) == (1) and (bd[32] + bd[33] + bd[34] + bd[35]) == (1) and (bd[16] + bd[17] + bd[18] + bd[19]) == (1):
            straight = straight + 1
        if (bd[20] + bd[21] + bd[22] + bd[23]) == (1) and (bd[24] + bd[25] + bd[26] + bd[27]) == (1) and (bd[28] + bd[29] + bd[30] + bd[31]) == (1) and (bd[32] + bd[33] + bd[34] + bd[35]) == (1) and (bd[36] + bd[37] + bd[38] + bd[39]) == (1):
            straight = straight + 1
        if (bd[40] + bd[41] + bd[42] + bd[43]) == (1) and (bd[24] + bd[25] + bd[26] + bd[27]) == (1) and (bd[28] + bd[29] + bd[30] + bd[31]) == (1) and (bd[32] + bd[33] + bd[34] + bd[35]) == (1) and (bd[36] + bd[37] + bd[38] + bd[39]) == (1):
            straight = straight + 1
        if (bd[40] + bd[41] + bd[42] + bd[43]) == (1) and (bd[44] + bd[45] + bd[46] + bd[47]) == (1) and (bd[28] + bd[29] + bd[30] + bd[31]) == (1) and (bd[32] + bd[33] + bd[34] + bd[35]) == (1) and (bd[36] + bd[37] + bd[38] + bd[39]) == (1):
            straight = straight + 1
        if (bd[40] + bd[41] + bd[42] + bd[43]) == (1) and (bd[44] + bd[45] + bd[46] + bd[47]) == (1) and (bd[48] + bd[49] + bd[50] + bd[51]) == (1) and (bd[32] + bd[33] + bd[34] + bd[35]) == (1) and (bd[36] + bd[37] + bd[38] + bd[39]) == (1):
            straight = straight + 1
        if (bd[40] + bd[41] + bd[42] + bd[43]) == (1) and (bd[44] + bd[45] + bd[46] + bd[47]) == (1) and (bd[48] + bd[49] + bd[50] + bd[51]) == (1) and (bd[0] + bd[1] + bd[2] + bd[3]) == (1) and (bd[36] + bd[37] + bd[38] + bd[39]) == (1):
            royalstraight = royalstraight + 1
            straight = straight + 1
        if (bd[0] + bd[1] + bd[2] + bd[3]) == (3) or (bd[4] + bd[5] + bd[6] + bd[7]) == (3) or (bd[8] + bd[9] + bd[10] + bd[11]) == (3) or (bd[12] + bd[13] + bd[14] + bd[15]) == (3) or (bd[16] + bd[17] + bd[18] + bd[19]) == (3) or (bd[20] + bd[21] + bd[22] + bd[23]) == (3) or (bd[24] + bd[25] + bd[26] + bd[27]) == (3) or (bd[28] + bd[29] + bd[30] + bd[31]) == (3) or (bd[32] + bd[33] + bd[34] + bd[35]) == (3) or (bd[36] + bd[37] + bd[38] + bd[39]) == (3) or (bd[40] + bd[41] + bd[42] + bd[43]) == (3) or (bd[44] + bd[45] + bd[46] + bd[47]) == (3) or (bd[48] + bd[49] + bd[50] + bd[51]) == (3):
            trio = trio + 1
        if (bd[0] + bd[1] + bd[2] + bd[3]) == (2):
            pair = pair + 1
        if (bd[4] + bd[5] + bd[6] + bd[7]) == (2):
            pair = pair + 1
        if (bd[8] + bd[9] + bd[10] + bd[11]) == (2):
            pair = pair + 1
        if (bd[12] + bd[13] + bd[14] + bd[15]) == (2):
            pair = pair + 1
        if (bd[16] + bd[17] + bd[18] + bd[19]) == (2):
            pair = pair + 1
        if (bd[20] + bd[21] + bd[22] + bd[23]) == (2):
            pair = pair + 1
        if (bd[24] + bd[25] + bd[26] + bd[27]) == (2):
            pair = pair + 1
        if (bd[28] + bd[29] + bd[30] + bd[31]) == (2):
            pair = pair + 1
        if (bd[32] + bd[33] + bd[34] + bd[35]) == (2):
            pair = pair + 1
        if (bd[36] + bd[37] + bd[38] + bd[39]) == (2):
            pair = pair + 1
        if (bd[40] + bd[41] + bd[42] + bd[3]) == (2):
            pair = pair + 1
        if (bd[44] + bd[45] + bd[46] + bd[47]) == (2):
            pair = pair + 1
        if (bd[48] + bd[49] + bd[50] + bd[51]) == (2):
            pair = pair + 1
        if (bd[0] + bd[1] + bd[2] + bd[3]) == (2) or (bd[51] + bd[50] + bd[49] + bd[48])== (2) or (bd[44] + bd[45] + bd[46] + bd[47]) == (2) or (bd[43] + bd[42] + bd[41] + bd[40]) == (2):
           there = there + 1
        if trio == 1:
            if pair == 0:
                print('You got three of a kind!')
                total = total + (3 * wager)
            if pair == 1:
                print('You got a Full House!')
                total = total + 8 * wager
        if pair == 2:
                print('You got Two Pair!')
                total = total + 1 * wager
        if straight == 1:
            if flush == 0:
                print('You got a straight!!')
                total = total + (4 * wager)
            if flush == 1 and royalstraight == 0:
                print('You got a Straight Flush!!')
                total = total + (49 * wager)
            if royalstraight == 1 and flush == 1:
                print('Congratulations, you hit the jackpot with a Royal Flush!!')
                total = total + (249 * wager)
        if flush == 1 and straight == 0:
            print('You made a flush!!')
            total = total + (5 * wager)
        if (bd[0] + bd[1] + bd[2] + bd[3]) == (2) or (bd[51] + bd[50] + bd[49] + bd[48])== (2) or (bd[44] + bd[45] + bd[46] + bd[47]) == (2) or (bd[43] + bd[42] + bd[41] + bd[40]) == (2):
            if pair == 1:
                total = total
                print('You got a pair of Jacks or better!')
        else:
            total = total - wager
        print(' ')
        print('Your new total is:', total, '$')
        print(' ')
        l = input('If you want to continue with the same wager.....enter 1\nIf you want to change wager.....................enter 2\n')
        while l != '1' and l != '2':
            l = input('previous input not valid, please try again -- ')
            
print('Oh no! you lost all your money!')

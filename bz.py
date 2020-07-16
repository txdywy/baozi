import random

def game(init): 
    s = [random.randint(0,1) for i in range(6)]

    c4 = check(s[0], s[1], s[2])
    if c4 >= 0:
        if c4== s[3]:
            init+=1
        else:
            init-=1
    c5 = check(s[1], s[2], s[3])
    if c5 >= 0:
        if c5== s[4]:
            init+=6
        else:
            init-=6
    c6 = check(s[2], s[3], s[4])
    if c5 >= 0:
        if c5== s[5]:
            init+=21
        else:
            init-=21
    return init




def check(a, b, c, e=False):
    x = (a, b, c)

    if x in [(1,0,1), (0,1,0), (1,1,1), (0,0,0)]:
        if x in [(1,0,1), (0,1,0)]:
            return 1 if c else 0
        else:
            return 0 if c else 1
    if e:
        if x in [(0,0,0), (1,1,1)]:
            return 0 if c else 1
    return -1


def test():
    bg = 100
    s = [random.randint(0,1),random.randint(0,1),random.randint(0,1)]
    f = False
    w = [-1,-1,-1]
    z = ['p','p','p']
    t = [0,0,0]
    orig = None
    extra = False
    stop = False
    i=0
    while True:
        i+=1
        if len(s) > 10:
            break
        print("------------------------")
        print("第{}轮".format(i))
        print("本轮初始资金(没押注)${}".format(bg))
        print("游戏结果{}".format(s))
        print("预测情况{}".format(z))
        print("胜负情况{}".format(w))
        print("投注情况{}".format(t))
        s.append(random.randint(0,1))
        if f:
            if orig in [(0,0,0), (1,1,1)]:
                f = False
            if orig in [(1,0,1), (0,1,0)]:
                extra = True

        #if len(s) < 4:
        #    continue
        a, b, c, x = s[-4], s[-3], s[-2], s[-1]
        y = check(a,b,c, extra)
        extra = False
        if y >= 0:
            bet = 1
            if len(w)<3 :
                bet = 1
            else:
                if w[-1]==0 and w[-2]==0 and w[-3]==0:
                    orig = (s[-6], s[-5], s[-4])
                    s.append(random.randint(0,1))
                    s.append(random.randint(0,1))
                    w.append(-2)
                    z.append('p')
                    t.append(0)
                    w.append(-2)
                    z.append('p')
                    t.append(0)
                    f = True
                    continue
                elif w[-1]==0 and w[-2]==0:
                    bet = 21
                elif w[-1]==0:
                    bet = 6
            if y==s[-1]:
                bg+=bet
                w.append(1)
                z.append(y)
                t.append(bet)
            else:
                if bg >= bet:
                    bg-=bet
                else:
                    stop=True
                w.append(0)
                z.append(y)
                t.append(bet)
        else:
            w.append(-1)
            z.append('p')
            t.append(0)

        if bg>=300 or stop:
            print('----------')
            print(bg)
            print(len(s))
            print(len(w))
            return bg, len(s)
            break

win = []
fail = []
for i in range(1):
    b, l = test()
    if b >= 300:
        win.append(b)
    else:
        fail.append(b)
print("==========")
print("win:{} {}".format(len(win),sum(win)))
print("fail:{}".format(len(fail)))
    


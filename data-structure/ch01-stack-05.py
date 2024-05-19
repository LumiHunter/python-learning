def hanoi_tower(n, fr, tmp, to):
    if n == 1:
        print('원판 1: %s --> %s' % (fr, tmp))
    else:
        hanoi_tower(n-1, fr, to, tmp)
        print('원판 %d: %s --> %s' % (n, fr, to))
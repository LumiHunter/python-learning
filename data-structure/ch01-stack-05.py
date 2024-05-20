def hanoi_tower(n, fr, tmp, to):    # 원판 개수, 시작, 임시, 도착
    if n == 1:    # 재귀 구조의 멈춤 조건: 원판이 1개 남으면 바로 fr에서 to로.
        print('원판 1: %s --> %s' % (fr, to))
    else:
        hanoi_tower(n-1, fr, to, tmp)    # n-1개는 '어떻게든' to를 임시로 삼아 tep로 옮김
        print('원판 %d: %s --> %s' % (n, fr, to))    # n번째를 fr에서 to로
        hanoi_tower(n-1, tmp, fr, to)    # n-1을 다시 '어떻게든' fr을 임시로 삼아 to로 옮김
        
hanoi_tower(5, 'A', 'B', 'C')
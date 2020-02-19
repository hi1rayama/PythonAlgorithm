'''
ダブルハッシュ法：処理効率をよくするため,衝突が発生した場合に,別のハッシュ関数により求める方法.配列は素数でなければいけない
ハッシュ関数1 H(i): i mod (N-1) (N=要素数 )
ハッシュ関数2 DH(i):　i // (N-1) + 1 
'''

import sys
import math


def H(i):
    return i % (N-1)


def DH(i):
    return i//(N-1)+1


def DoubleHashing(mode):  # mode:0->入力 1->データの探索
    if(mode == 0):
        if(len(INPUT) > N):
            print('Error')
            sys.exit()
        for i in INPUT:
            x = i
            ha = H(x)
            while(hash_table[ha] is not None):
                dh = DH(x)
                if(ha+dh >= N):
                    ha = DH(ha+dh)
                else:
                    ha += dh
            hash_table[ha] = i
    elif(mode == 1):
        p = int(input('取り出すデータを入力：'))
        ha = H(p)
        cnt = 0
        while(hash_table[ha] != p):
            dh = DH(p)
            if(ha+dh >= N):
                ha = DH(ha+dh)
            else:
                ha += dh
            if(cnt == N-2):
                print("入力されたデータはありません")
                sys.exit()
            cnt += 1
        print('{0}は{1}番地に格納されていました'.format(p, ha))


N = int(input())

max_search = math.ceil(math.sqrt(N))
if(N > 3):
    for i in range(2, max_search):
        if N % i == 0:
            print('素数ではない')
            sys.exit()


INPUT = list(map(int, input().split()))  # 入力
hash_table = [None for i in range(N)]
DoubleHashing(0)
print(hash_table)
DoubleHashing(1)

'''
            結果
$ python3 DoubleHashing.py
11                   
11 3 32 4 50 34 19 39
[50, 11, 32, 3, 4, None, 39, None, 34, 19, None]
取り出すデータを入力：39
39は6番地に格納されていました
'''

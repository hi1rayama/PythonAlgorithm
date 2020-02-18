'''
線形探査法：衝突が発生した場合、すぐ次の要素番号の場所にデータを格納する方法
ハッシュ関数 H(i): i mod N (N=要素数)
'''

import sys
def H(i):
    return i%N

def LinearProbing(mode):#mode:0->入力 1->データの探索
    if(mode==0):
        if(len(INPUT) > N):
            print('Error')
            sys.exit()
        for i in INPUT:
            ha=H(i)
            while(hash_table[ha] is not None):
                if(ha==N-1):
                    ha=0
                else:
                    ha+=1
            hash_table[ha]=i
    elif(mode==1):
        p=int(input('取り出すデータを入力：'))
        ha=H(p)
        j=H(p)
        cnt=0
        while(hash_table[ha]!=p):
            if(ha==N-1):
                ha=0
            else:
                ha+=1
            if(cnt==N-1):
                print("入力されたデータはありません")
                sys.exit()
            cnt+=1
        print('{0}は{1}番地に格納されていました'.format(p,ha))




N=int(input())
INPUT = list(map(int, input().split()))  # 入力
hash_table=[None for i in range(N)]
LinearProbing(0)
print(hash_table)
LinearProbing(1)

'''
            結果
$ python3 LinearProbing.py
10
11 3 32 4 50 34 19 39
[50, 11, 32, 3, 4, 34, 39, None, None, 19]
取り出すデータを入力：11
11は1番地に格納されていました
'''
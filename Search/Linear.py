'''
線形探索：INPUT[0]から順にTと等しいかを調べ、等しくなったらその要素番号を出力する
計算量：O(n)

'''


def Linear_Search(N,INPUT,T):
    i=0
    while(i < N and T!=INPUT[i]):
        i+=1
    
    print('{0}は{1}番目にあります'.format(T,i+1))



N = int(input())
INPUT = list(map(int, input().split()))  # 入力
T=int(input())

Linear_Search(N,INPUT,T)


'''''''''''''''''''''''''''''''''
            結果
$ python3 Linear.py
8
28 14 15 29 27 23 13 30
23
23は6番目にあります

''''''''''''''''''''''''''''''''
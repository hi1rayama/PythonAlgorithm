'''
二分探索：昇順にならんでいる配列に対して半分、半分、半分．．．と絞り込む探索法
計算量：O(logn)

1. left = 0, right = N - 1とする(探索範囲をa[0]~a[N - 1]とする).
2. right − left > 1 となる間，3., 4. を繰り返す.
3. middle = (left + right) // 2 (切り捨て) とする.
4. x ≤ a[middle] ならば，right = middle とし，そうでなければ，left = middle とする.
5. right の値を出力する.
'''




def Binary_Search(N,INPUT,T):
    left=0
    right=N-1
    while(right - left > 1):
        middle=(left+right)//2
        if(T <= INPUT[middle]):
            right=middle
        else:
            left=middle
    print('{0}は{1}番目にあります'.format(T,right+1))





N = int(input())
INPUT = list(map(int, input().split()))  # 入力
T=int(input())
SORT=sorted(INPUT)
print(SORT)

Binary_Search(N,SORT,T)

'''
            結果
$ python3 Binary.py
8
28 14 15 29 27 23 13 30
23
ソート後：[13, 14, 15, 23, 27, 28, 29, 30]
23は4番目にあります

'''
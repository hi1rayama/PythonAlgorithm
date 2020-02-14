'''
単純選択法
1. 変数 i を最小要素を入れる配列番号として扱い，以下の操作を，i = 0~N - 2 について繰り返す.
2. INPUT_VALUE[i]~INPUT_VALUE[N - 1] の中から，最小要素 a[k] を探し，INPUT_VALUE[i] と入れ換える.

平均計算量：O(n^2)
最悪計算量：O(n^2)
内部ソート：○
安定ソート：×
'''

def selectionSort(N,INPUT_VALUE):
    print("ソート前：",INPUT_VALUE)
    try:
        for i in range(0,N):#ループ回数:N-1
            k=i #現在の最小値(範囲:INPUT_VALUE[i] ~ INPUT_VALUE[N-1])
            for j in range(i+1,N):#ループ回数:N-2
                if(INPUT_VALUE[k] > INPUT_VALUE[j]):
                    k=j #最小値の更新
    
            #入れ替え処理
            temp=INPUT_VALUE[i]
            INPUT_VALUE[i]=INPUT_VALUE[k]
            INPUT_VALUE[k]=temp
            print(i+1,"回目：",INPUT_VALUE)
        print("ソート後：",INPUT_VALUE)
    except:
        print("ERROR!!")

    



N=int(input())
INPUT = list(map(int, input().split())) #入力
selectionSort(N,INPUT)

'''''''''''''''''''''''''''''''''''''''''''''
                結果
$ python3 SelectionSort.py 
10    
1 2 3 10 5 9 8 5 7 6
ソート前： [1, 2, 3, 10, 5, 9, 8, 5, 7, 6]
1 回目： [1, 2, 3, 10, 5, 9, 8, 5, 7, 6]
2 回目： [1, 2, 3, 10, 5, 9, 8, 5, 7, 6]
3 回目： [1, 2, 3, 10, 5, 9, 8, 5, 7, 6]
4 回目： [1, 2, 3, 5, 10, 9, 8, 5, 7, 6]
5 回目： [1, 2, 3, 5, 5, 9, 8, 10, 7, 6]
6 回目： [1, 2, 3, 5, 5, 6, 8, 10, 7, 9]
7 回目： [1, 2, 3, 5, 5, 6, 7, 10, 8, 9]
8 回目： [1, 2, 3, 5, 5, 6, 7, 8, 10, 9]
9 回目： [1, 2, 3, 5, 5, 6, 7, 8, 9, 10]
10 回目： [1, 2, 3, 5, 5, 6, 7, 8, 9, 10]
ソート後： [1, 2, 3, 5, 5, 6, 7, 8, 9, 10]
'''''''''''''''''''''''''''''''''''''''''''''
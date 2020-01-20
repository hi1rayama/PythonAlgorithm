'''
単純選択法
1. 変数 i を最小要素を入れる配列番号として扱い，以下の操作を，i = 0~N - 2 について繰り返す.
2. INPUT_VALUE[i]~INPUT_VALUE[N - 1] の中から，最小要素 a[k] を探し，INPUT_VALUE[i] と入れ換える.
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
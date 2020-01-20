'''
単純挿入法
1. 変数 i を挿入する要素の配列番号として扱い，以下の操作を，i = 1 ~ N - 1 について繰り返す.
2. すでにソート済みの INPUT_VALUE[0]~INPUT_VALUE[i - 1] の中で，INPUT_VALUE[i] が入るべき位置 k を見つける (INPUT_VALUE[i] が最大の ときは k = i).
3. INPUT_VALUE~ INPUT_VALUE[i - 1] を 1 つ後ろにずらす (k = i のときは何もしない).
4.  INPUT_VALUE[i] の値を，空いた  INPUT_VALUE[k] に代入する.
'''

def insertionSort(N,INPUT_VALUE):
    print("ソート前：",INPUT_VALUE)
    try:
        for i in range(1,N):#ループ回数:N-1
            temp=INPUT_VALUE[i]
            for j in range(i,-1,-1):
                if(INPUT_VALUE[j-1] > temp):
                    INPUT_VALUE[j]=INPUT_VALUE[j-1]
                else:
                    break
            INPUT_VALUE[j]=temp
            print(i,"回目：",INPUT_VALUE)
        print("ソート後：",INPUT_VALUE)
    except:
        print("ERROR!!")

    



N=int(input())
INPUT = list(map(int, input().split())) #入力
insertionSort(N,INPUT)
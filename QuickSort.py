'''
クイックソート
1. i を先頭要素の番号，j を末尾要素の番号とする
2. 配列から任意の要素を取り出し，これを基準値 pivot とする
3. i > j となるまで 4.~7. を繰り返す
4. i を増加させていき，要素 INPUT_VALUEivot が見つかるまで配列を走査する
5. j を減少させていき，要素 INPUT_VALUE[j] <= pivot が見つかるまで配列を走査する
6. i < jかつINPUT_VALUE[i] != INPUT_VALUE[j]ならばINPUT_VALUE[i]とINPUT_VALUE[j]を交換し，iを1増加，jを1減少させて3.に戻る ここで，pivot として設定した要素自体も移動する可能性があることに注意します
7. i == jまたはINPUT_VALUE[i] == INPUT_VALUE[j]ならば，iを1増加，jを1減少させて3.に戻る

'''

def quickSort(INPUT_VALUE,start,end):
    I = start
    J = end
    pivot=INPUT_VALUE[int((I+J)/2)]

    while True:
        while (INPUT_VALUE[I] < pivot): #4
            I+=1   
        while (INPUT_VALUE[J] > pivot): #5
           J-=1
        
        if(I < J and INPUT_VALUE[I] != INPUT_VALUE[J]):#6
            INPUT_VALUE[I],INPUT_VALUE[J] = INPUT_VALUE[J],INPUT_VALUE[I]
            I=I+1
            J=J-1
        elif(I == J or INPUT_VALUE[I] == INPUT_VALUE[J]):#7
            I=I+1
            J=J-1
        if(I >= J):
            break
    #分割処理
    if(start < J):
        quickSort(INPUT_VALUE,start,J)
    if(end > I):
        quickSort(INPUT_VALUE,I,end)


N=int(input())
INPUT = list(map(int, input().split())) #入力
quickSort(INPUT,0,N-1)
print(INPUT)
'''''''''''''''''''''''''''''''''''''''''''''
                結果
$ python3 QuickSort.py 
10
6 9 12 7 15 23 2 10 4 20
[2, 4, 6, 7, 9, 10, 12, 15, 20, 23]
'''''''''''''''''''''''''''''''''''''''''''''
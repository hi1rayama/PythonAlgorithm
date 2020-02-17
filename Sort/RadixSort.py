'''
基数ソート(k=3桁の場合)
1. 10 個の容器(バケツ)を用意(a[0]~a[9])
2. k(3) 番目から 1 番目まで以下を繰り返し(最下位桁(1 の位)から最上位桁(3)まで)
3. 当該要素をキーとして，用意した容器でバケットソート

0~Aの整数値が対象の時
平均計算量：O(nlogA)
最悪計算量：O(nlogA)
内部ソート：×
安定ソート：○
'''

def radixSort(N, INPUT_VALUE):
    print("ソート前：", INPUT_VALUE)
    bucket = [[] for i in range(10)]
    bucket2 = [[] for i in range(10)]
    bucket3 = [[] for i in range(10)]
    result = []
    try:
        for value in INPUT_VALUE:
            R = value % 10
            if(R == 0):
                bucket[0].append(value)
            elif(R == 1):
                bucket[1].append(value)
            elif(R == 2):
                bucket[2].append(value)
            elif(R == 3):
                bucket[3].append(value)
            elif(R == 4):
                bucket[4].append(value)
            elif(R == 5):
                bucket[5].append(value)
            elif(R == 6):
                bucket[6].append(value)
            elif(R == 7):
                bucket[7].append(value)
            elif(R == 8):
                bucket[8].append(value)
            elif(R == 9):
                bucket[9].append(value)

        #関数化可能
        for value in bucket:
            for i in value:
                R = int((i % 100) / 10)
                if(R == 0):
                    bucket2[0].append(i)
                elif(R == 1):
                    bucket2[1].append(i)
                elif(R == 2):
                    bucket2[2].append(i)
                elif(R == 3):
                    bucket2[3].append(i)
                elif(R == 4):
                    bucket2[4].append(i)
                elif(R == 5):
                    bucket2[5].append(i)
                elif(R == 6):
                    bucket2[6].append(i)
                elif(R == 7):
                    bucket2[7].append(i)
                elif(R == 8):
                    bucket2[8].append(i)
                elif(R == 9):
                    bucket2[9].append(i)
        #関数化可能
        for value in bucket2:
            for i in value:
                R = int(i / 100)
                if(R == 0):
                    bucket3[0].append(i)                   
                elif(R == 1):
                    bucket3[1].append(i)                  
                elif(R == 2):
                    bucket3[2].append(i)
                elif(R == 3):
                    bucket3[3].append(i)
                elif(R == 4):
                    bucket3[4].append(i)
                elif(R == 5):
                    bucket3[5].append(i)
                elif(R == 6):
                    bucket3[6].append(i)
                elif(R == 7):
                    bucket3[7].append(i)
                elif(R == 8):
                    bucket3[8].append(i)
                elif(R == 9):
                    bucket3[9].append(i)

        for value in bucket3:
            result.extend(value)

        print("１桁目:", bucket)
        print("２桁目:", bucket2)
        print("３桁目:", bucket3)
        print("ソート後:", result)

    except:
        print("ERROR!")


N = int(input())
INPUT = list(map(int, input().split()))  # 入力
radixSort(N, INPUT)

'''''''''''''''''''''''''''''''''
            結果
$ python3 RadixSort.py 
9
374 889 309 397 987 473 346 607 881
ソート前： [374, 889, 309, 397, 987, 473, 346, 607, 881]
１桁目: [[], [881], [], [473], [374], [], [346], [397, 987, 607], [], [889, 309]]
２桁目: [[607, 309], [], [], [], [346], [], [], [473, 374], [881, 987, 889], [397]]
３桁目: [[], [], [], [309, 346, 374, 397], [473], [], [607], [], [881, 889], [987]]
ソート後: [309, 346, 374, 397, 473, 607, 881, 889, 987]
'''''''''''''''''''''''''''''''''

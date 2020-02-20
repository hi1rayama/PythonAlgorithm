'''
累積和：
'''


import sys

def CumulativeSum(N, S, M):
    CS_table = [0]
    max_value = 0
    number=0
    for i in range(N):
        CS_table.append(CS_table[i]+S[i])

    for i in range(N-M+1):
        tmp = CS_table[i+M] - CS_table[i]
        if(tmp > max_value):
            max_value = tmp
            number=i
    print('累積和テーブル:{}'.format(CS_table))
    print('最大値は{}で番地は[{}]~[{}]の合計'.format(max_value,number,number+M-1))


def main():
    print('要素数N個の配列Sの中から連続したM個の和の最大値を求める')
    N = int(input('N:'))
    INPUT = list(map(int, input('S:').split()))  # 入力
    M = int(input('M:'))
    if(N != len(INPUT) or N < M):
        print('入力エラー')
        sys.exit()
    
    print('配列S:{}'.format(INPUT))
    CumulativeSum(N, INPUT, M)


main()

'''
            結果
$ python3 CumulativeSum.py 
要素数N個の配列Sの中から連続したM個の和の最大値を求める
N:3 
S:1 2 3
M:2
配列S:[1, 2, 3]
累積和テーブル:[0, 1, 3, 6]
最大値は5で番地は[1]~[2]の合計
'''
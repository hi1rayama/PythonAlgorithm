'''
深さ優先探索：グラフ探索に使えるアルゴリズムの1つ.FIFO(スタック)のデータ構造を使用する方法と再帰関数を利用する方法がある.
            隣接しているノードの中で未探索なノードが有る限り、とにかく進めるだけ進み深くノードを探索する.
            隣接したノードが全て探索済みになったらまだ探索していない隣接ノードが存在するノードまで戻ってから
            その隣接ノードを探索する.

1. 探索
        a) 現在探索しているノードの隣接ノードの中から未探索ノードを探し、探索を進める
        b) 隣接ノードに未探索ノードが見つからなかったら「2.経路の後退」に進む

2. 経路の後退
        未探索の隣接ノードが残っているノードを発見するまで、通過してきた経路を戻る

3. 探索の繰り返し及び終了条件
        手順1.,2.を再帰的に繰り返す. 再帰を使用するため、最終的には始点に戻ってくる.
        始点に戻ったことが確認されると処理が終了する
'''

##########################################グラフ探索を行う準備##########################################
# ノード
class Node:
    def __init__(self):
        self.start_node = None
        self.end_node = None


NODES = 9  # ノードの数
START = 0  # 探索開始ノード
edge_cnt = 0  # 木を構成するエッジとして登録されたエッジのカウンタ
df_flag = [0 for i in range(NODES)]  # 探索状況[0:未探索, 1:探索済み] 初期値：0
TREE = [Node() for i in range(NODES - 1)]  # 探索木

lis = [[0, 1], [0, 3], [1, 2], [1, 3], [1, 4], [2, 5],
               [3, 6], [3, 7], [4, 5], [5, 7], [5, 8], [6, 7], [7, 8]]  # エッジ(隣接リスト)

matrix = [[0 for i in range(NODES)] for i in range(NODES)]  # エッジ(隣接行列)
for edge in lis:
    i, j = edge[0], edge[1]
    matrix[i][j] = 1
    matrix[j][i] = 1

##########################################main関数##########################################


def main():
    print("------------隣接行列------------")
    for m in matrix:
        print(m)
    df_search(START)
    # 結果を表示する
    print("探索木")
    for node in TREE:
        print("({0},{1}) ".format(node.start_node, node.end_node))

##########################################深さ優先探索を行う関数##########################################


def df_search(nd):
    global edge_cnt
    n = 0
    df_flag[nd] = 1  # ノードndを探索済みにする

    while(n < NODES):  # 探索するノードnを小さい順から確認していく
        if(matrix[nd][n] == 1 and df_flag[n] == 0):  # 隣接しているノードでまだ探索していない場合
            TREE[edge_cnt].start_node = nd #探索木に出発点を登録
            TREE[edge_cnt].end_node = n #探索木に到着点を登録
            edge_cnt += 1
            df_search(n)
        n += 1


# 実行
main()

'''''''''''''''''''''''''''''''''
            結果
------------隣接行列------------
[0, 1, 0, 1, 0, 0, 0, 0, 0]
[1, 0, 1, 1, 1, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 1, 0, 0, 0]
[1, 1, 0, 0, 0, 0, 1, 1, 0]
[0, 1, 0, 0, 0, 1, 0, 0, 0]
[0, 0, 1, 0, 1, 0, 0, 1, 1]
[0, 0, 0, 1, 0, 0, 0, 1, 0]
[0, 0, 0, 1, 0, 1, 1, 0, 1]
[0, 0, 0, 0, 0, 1, 0, 1, 0]
探索木
(0,1) 
(1,2) 
(2,5) 
(5,4) 
(5,7) 
(7,3) 
(3,6) 
(7,8) 
'''''''''''''''''''''''''''''''''
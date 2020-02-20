'''
素朴な文字列照合(逐次探索)：テキストに沿って、単語を1文字ずつずらしながら、単語がテキストに出現するかを調べる
                あまり効率は良くない
'''

import sys
def NaiveMaching(T,W):
    for i in range(len(T)-len(W)):
        if (T[i:len(W)+i]==W[0:len(W)]):
            print('{}はTEXTの{}番目から{}番目までにある'.format(W,i,i+len(W)-1))
            sys.exit()
    print('{}はTEXTの{}番目から{}番目までにある'.format(W,len(T)-len(W),len(T)-1))

def main():
    TEXT=input('TEXT:')
    WORD=input('SEATCH WORD:')
    NaiveMaching(TEXT,WORD)
main()

'''
    結果
$ python3 NaiveMaching.py
TEXT:algorithm
SEATCH WORD:go
goはTEXTの2番目から4番目までにある
'''
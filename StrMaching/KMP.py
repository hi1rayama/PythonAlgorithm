
import sys

def KMPMaching(T, W,Table):
    i = 0
    j = 0
    while(i + j < len((T))):
        if(T[i+j] == W[j]):
            j = j+1
            if(j == len(W)):
                return i
        else:
            i = i+j-Table[j]
            if(j > 0):
                j = Table[j]
    return len(T)


def MakePatternMatchingTable(W,Table):
    print(Table)
    Table[0] = -1
    for j in range(len(W)):
        k = j-1
        while (k > 0 and equal(W, j, k) == False):
            k = k-1
        Table[j] = k


def equal(w, j, k):
    for i in range(k):
        if(w[i] != w[j-k+i]):
            return False

    return True


def main():
    TEXT = input('TEXT:')
    WORD = input('SEATCH WORD:')
    Table=[0 for i in range(len(WORD))]
    MakePatternMatchingTable(WORD,Table)
    print(Table)
    ans=KMPMaching(TEXT,WORD,Table)
    print(ans)


main()

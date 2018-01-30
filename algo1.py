'''
Created on Jan 23, 2018

@author: fiihagan30
'''
'''
Created on Jan 23, 2018

@author: ehagan
'''
#
mySorted = []

L = [0, 2, -1]


def mymergeSort(L):
    def getSplit(mylist):
        return int(int(len(mylist)) / 2)
    #L = [0, 2, -1]
    startSize = getSplit(L)
    A = sorted(L[:startSize[0]])
    B = sorted(L[startSize[0]:])
    i = 0
    j = 0
    C = []
    for k in range(int(len(L))):
        if i == int(len(A)):
            C.extend(B[j:])
            break
        if j == int(len(B)):
            C.extend(A[i:])
            break
        if A[i] < B[j]:
            if A[i] in C:
                C.insert(C.index(A[i]), A[i])
            else:
                C.append(A[i])
            i += 1
        elif A[i] > B[j]:
            if B[j] in C:
                C.insert(C.index(B[j]), B[j])
            else:
                C.append(B[j])
            j += 1
        elif A[i] == B[j]:
            C.append(A[i])
            C.append(B[j])
            j += 1
            i += 1
    return C

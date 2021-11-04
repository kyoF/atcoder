import sys
def main():
    input = stdin.readline
    H,W = map(int, input().split())
    A = [tuple(map(int, input().split())) for _ in range(H)]
    R = [sum(A[i][j] for i in range(H)) for j in range(W)]
    ans = [ [ R[i] + C[j] - A[i][j] for j in range(W) ] for i in range(H) ]
    for a in ans:
        print(*a)
        
if __name__ == '__main__':
    main()
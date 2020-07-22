def get_survival_number(N, m):
    if N == 1:
        return 0
    """ temp = get_survival_number(N-1,m)+m%N
    if temp<=N:
        return temp
    else:
        return temp%N """
    return (get_survival_number(N-1,m)+m%N)%N

def main():
    print(get_survival_number(2,9))

if __name__ == "__main__":
    main()


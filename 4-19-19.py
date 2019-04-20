def tower_of_hanoi(n):

    def toh_recur(n, start, end, aux):
        if n == 1:
            print("Move " + start + " to " + end)
            return
        toh_recur(n - 1, start, aux, end)
        print("Move " + start + " to " + end)
        toh_recur(n - 1, aux, end, start)

    toh_recur(n, '1', '3', '2')

tower_of_hanoi(3)
import sys


def main():
    cases = int(sys.stdin.readline())

    for case in range(cases):
        lines = int(sys.stdin.readline())

        # create 2 empty list, init_list, final_list
        ini_list = []
        fin_list = []

        for line in range(lines):
            x = sys.stdin.readline().rstrip('\n')
            ini_list.append(x)

        for line in range(lines):
            x = sys.stdin.readline().rstrip('\n')
            fin_list.append(x)

        ini_list_ind = lines - 1
        fin_list_ind = lines - 1

        while ini_list_ind >= 0 and fin_list_ind >= 0:
            if fin_list_ind >= 0 and fin_list[fin_list_ind] != ini_list[ini_list_ind]:
                ini_list_ind -= 1
            else:
                ini_list_ind -= 1
                fin_list_ind -= 1

        while fin_list_ind >= 0:
            print(fin_list[fin_list_ind])
            fin_list_ind -= 1

        print()

if __name__ == '__main__':
    main()

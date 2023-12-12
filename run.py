def show_board(hit, miss):
    print("---- Player Board ----")
    print(" 0 1 2 3 4 5 6 ")
    for x in range(7):
        row = ""
        for y in range(7):
            if place in hit:
                ch = " X " 
            elif place in miss:
                ch = " O "
            else:
                ch = " * "
            row += ch
            place += 1
            print(x," ",row)

def show_compboard(hit, miss): 
    print("---- Computer Board ---- ")
    print(" 0 1 2 3 4 5 6 ")
        for x in range(7):
            row = ""
            for y in range(7):
                if place in hit:
                    ch = " X " 
                elif place in miss:
                    ch = " O "
                else:
                    ch = " * "
                row += ch
                place += 1
                print(x," ",row)
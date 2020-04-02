for i in range(2):
	print("    |    |    ")
	print("______________")
print("    |    |    ")
poslst = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
y = 0
for i in range(9) :
    o = input("Enter your position: ")
    if poslst[int(o)-1] == "X" or poslst[int(o)-1] == "O" or int(o) < 1 or int(o) >= 9 or int(o)%1 != 0 or o == "" :
        print("You tried to cheat. You lose your turn.")
        continue
        # i starts from 0 -8
    if i%2 != 0:
        poslst[int(o)-1] = "O"
    else :
        poslst[int(o)-1] = "X"
    print(" ", poslst[0], "  | ", poslst[1], "  | ", poslst[2], "   ")
    print("___________________")
    print(" ", poslst[3], "  | ", poslst[4], "  | ", poslst[5], "   ")
    print("___________________")
    print(" ", poslst[6], "  | ", poslst[7], "  | ", poslst[8], "   ")
    if poslst[0] == poslst[1] == poslst[2] == "X" or poslst[0] == poslst[1] == poslst[2] == "O" :
         print(poslst[0], "is the winner")
         break
    elif poslst[0] == poslst[3] == poslst[6] == "X" or poslst[0] == poslst[3] == poslst[6] == "O" :
        print(poslst[0], "is the winner")
        y = y + 1
        break
    elif poslst[0] == poslst[4] == poslst[8] == "X" or poslst[0] == poslst[3] == poslst[6] == "O":
        print(poslst[0], "is the winner")
        y = y + 1
        break
    elif poslst[1] == poslst[4] == poslst[7] == "X" or poslst[0] == poslst[3] == poslst[6] == "O":
        print(poslst[1], "is the winner")
        y = y + 1
        break
    elif poslst[2] == poslst[2] == poslst[6] == "X" or poslst[0] == poslst[3] == poslst[6] == "O":
        print(poslst[2], "is the winner")
        y = y + 1
        break
    elif poslst[2] == poslst[5] == poslst[8] == "X" or poslst[0] == poslst[3] == poslst[6] == "O":
        print(poslst[2], "is the winner")
        y = y + 1
        break
    elif poslst[3] == poslst[4] == poslst[5] == "X" or poslst[0] == poslst[3] == poslst[6] == "O":
        print(poslst[3], "is the winner")
        y = y + 1
        break
    elif poslst[6] == poslst[7] == poslst[8] == "X" or poslst[0] == poslst[3] == poslst[6] == "O":
        print(poslst[6], "is the winner")
        y = y + 1
        break
if y != 1 :
    print("It's a draw")

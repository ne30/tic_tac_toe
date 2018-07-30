def check(i,j,s):
    r = 0
    for k in range(i):
        if j[k] == j[i]:
            r = 1
            break
    if r:
        print("You already entered that please re-enter")
        j[i] = int(input("Enter for "+s+"\n"))
        return check(i,j,s)
def fun(a,s):
    return (a[0]==a[3]==a[6]==s) or (a[1]==a[4]==a[7]==s) or(a[2]==a[5]==a[8]==s) or (a[0]==a[1]==a[2]==s) or (a[3]==a[4]==a[5]==s) or (a[6]==a[7]==a[8]==s) or (a[0]==a[4]==a[8]==s) or (a[2]==a[4]==a[6]==s)
def print_box(a,b):
    print("\n"*7)
    print(b[6],"|", b[7],"|",b[8])
    print("---------")
    print(b[3],"|",b[4],"|",b[5])
    print("---------")
    print(b[0],"|",b[1],"|",b[2])

    print("\n"*7)
    print(a[6]+" | "+ a[7] +" | "+a[8])
    print("---------")
    print(a[3]+" | "+ a[4] +" | "+a[5])
    print("---------")
    print(a[0]+" | "+ a[1] +" | "+a[2])
catch = 'y'
while catch == 'y':
    r = 0
    q = 0
    a = [" "]*9
    j = [0 for i in range(9)]
    b = [(i+1) for i in range(9)]
    print_box(a,b)
    for i in range(5):
        if i%2 == 0:
            j[i] = int(input("Enter for x\n"))
            check(i,j,'x')
            b[j[i]-1] = "_"
            a[j[i]-1] = 'x'
            print_box(a,b)
        else:
            j[i] = int(input("Enter for o\n"))
            check(i,j,'o')
            b[j[i]-1]="_"
            a[j[i]-1] = 'o'
            print_box(a,b)
    if fun(a,"x"):
        r=1
        print('Player1 has won the game')
    elif fun(a,"o"):
        r=1
        print("this one")
        print("Player2 has won the game")
    else:
        i = 5
        while i<9:
            if i%2 == 0:
                j[i] = int(input("Enter for x\n"))
                check(i,j,'x')
                a[j[i]-1] = 'x'
                b[j[i]-1]="_"
                print_box(a,b)
                i = i+1
                if fun(a,"x"):
                    print("Player1 has won the game")
                    break
            else:
                j[i] = int(input("Enter for o\n"))
                check(i,j,'o')
                a[j[i]-1] = 'o'
                b[j[i]-1]="_"
                i = i+1
                print_box(a,b)
                if fun(a,"o"):
                    q = 1
                    print("Player2 has won the game")
                    break
        if fun(a,"x") and r!=1:
            print("Player1 has won the game")
        elif fun(a,"o") and q!=1:
            print("Player2 has won the game")
        if (fun(a,"x")==fun(a,"o")):
            print("The match was draw")
    print("Do you want to play again ?y/n")
    catch = input().lower()

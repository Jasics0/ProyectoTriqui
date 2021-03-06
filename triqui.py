import speech_recognition as sr

r = sr.Recognizer()
game_board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
winner = ""



def num(sound):
    arr=["uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve"];
    try:
        int(sound)
        if int(sound)<=9 and int(sound)>=1:
            return sound
        else:
            return "Diga un número entre el 1 y el 9"    
    except ValueError:

        for i in range(9):
            if arr[i]==sound:
                return (i+1)
        return "No se encontró el numero"


def hear():
    with sr.Microphone() as source:
        print('Diga el número de la casilla : ')
        audio = r.listen(source)
 
        try:
            text = r.recognize_google(audio,language="es-MX")
            return num(text)
        except:
            return "No se entendió el número"

def show():
    for i in range(3):
        for j in range(3):
            print("\t", game_board[i][j], end=" ")
        print()
    print("\n")


def checkV():
    count = 0
    figure = ""
    j = 0
    global winner
    for i in range(3):

        if game_board[0][i] != "-":
            figure = game_board[0][i]
        else:
            j = 3

        for j in range(3):
            if game_board[j][i] == figure:
                count += 1
            else:
                j = 3
        j = 0
        if count == 3:
            winner = figure
            return True
        else:
            count = 0
    return False


def checkH():
    count = 0
    figure = ""
    j = 0
    for i in range(3):
        global winner
        if game_board[i][0] != "-":
            figure = game_board[i][0]
        else:
            j = 3

        for j in range(3):
            if game_board[i][j] == figure:
                count += 1
            else:
                j = 3
        j = 0
        if count == 3:
            winner = figure
            return True
        else:
            count = 0
    return False


def checkD():
    global winner
    if(game_board[0][0] != "-" and game_board[0][0] == game_board[1][1] and game_board[1][1] == game_board[2][2]):
        winner = game_board[0][0]
        return True
    elif(game_board[0][2] != "-" and game_board[0][2] == game_board[1][1] and game_board[1][1] == game_board[2][0]):
        winner = game_board[0][2]
        return True
    else:
        return False


def win():
    for i in range(3):
        if(i == 1):
            if(checkV()):
                return True
        elif(i == 2):
            if(checkH()):
                return True
        else:
            if(checkD()):
                return True
    return False


def write(player):
    global game_board
    k = 0
    validate = False
    while(not validate):
        num = hear()
        try:
            a = int(num)
            for i in range(3):
                if(validate):
                    break
                for j in range(3):
                    if(k == (a-1) and game_board[i][j] == "-"):
                        validate = True
                        if(player == 0):
                            game_board[i][j] = "x"
                        else:
                            game_board[i][j] = "o"
                        break
                    k += 1

            if(not validate):
                k = 0
                print("Esa casilla ya está ocupada.\n")

        except ValueError:
            print(num)


def play():
    i = 0
    while(not win()):
        print("\n")
        show()
        if(i == 0):
            print("Turno de la x")
            write(i)
            i = 1
        else:
            print("Turno de la o")
            write(i)
            i = 0


if __name__ == '__main__':
    play()
    show()
    print("El ganador es: "+winner)

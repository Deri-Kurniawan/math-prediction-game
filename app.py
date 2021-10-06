import random


def question1():
    print("TODO : Enter a number in the range 1 to 10000")
    answer = int(input("pilih angka > "))
    if(answer < 1 or answer > 10000):
        print("Error : Please input a number on range")
        return question1()
    else:
        return answer


def question2(answer):
    randomNumber = random.randrange(1, 100)
    print("TODO : Multiply the number you choose by the number (", randomNumber, ")")
    input("Enter to continue...")
    return answer * randomNumber


def question3(answer, answerTemp):
    print("TODO : Add the number you chose at the beginning with the result of the multiplication earlier")
    input("Enter to continue...")
    return answer + answerTemp


def question4(answer, answerTemp):
    print("TODO : Then the result is divided by the number you chose at the beginning")
    input("Enter to continue...")
    return int(answer / answerTemp)


def start():
    print("\n")
    print("AUTHOR : DERI KURNIAWAN")
    print("GITHUB : https://github.com/Deri-Kurniawan")
    print("\n")

    print("===========================START=============================")
    answer = question1()
    answerTemp = answer
    print("=============================================================")
    print("==========================================")
    print("INFO : The number you choose : ", answerTemp)
    print("==========================================")
    answer = question2(answer)
    print("=============================================================")
    print("==========================================")
    print("INFO : The number you choose : ", answerTemp)
    print("==========================================")
    answer = question3(answer, answerTemp)
    print("=============================================================")
    print("==========================================")
    print("INFO : The number you choose : ", answerTemp)
    print("==========================================")
    answer = question4(answer, answerTemp)
    print("=============================================================")
    print("I know that you are now thinking of numbers ", answer)
    print("=============================================================")
    print("If your answer is not the same, then try repeating your math calculations")
    print("=============================================================")


start()
repeat = True
while(repeat == True):
    question = input("Play again? [y/n]> ")
    if(question == 'y'):
        start()

    elif(question == 'n'):
        print("=============================================================")
        print("Thanks For Playing!")
        print("============================END==============================")
        repeat = False
        break

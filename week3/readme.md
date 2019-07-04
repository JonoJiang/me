int(x) defines a variable as a number

while True:
        guessedNumber = input(message)
        print("You guessed {},".format(guessedNumber),)
        try:
            guessedNumber = int(guessedNumber)
            print("Thankyou")
            return guessedNumber
        except Exception as e:
            print("that is not a number")
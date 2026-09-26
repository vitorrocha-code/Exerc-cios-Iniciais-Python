for contador in range(1,100):
    contador += 1
    if contador % 3 == 0 and contador % 5 == 0:
        print("FizzBuzz")
    elif contador % 3 == 0:
        print("Fizz")
    elif contador % 5 == 0:
        print("Buzz")
    else:
        print(contador)
numbers = list(range(1,16))

def fizzbuzz():
    for i in numbers:
        if i % 3 == 0 and i % 5 ==0:
            print('fizzbuzz')
        elif i % 5 == 0:
            print('buzz')
        elif i % 3 == 0:
            print('fizz')
        else:
            print(i)
    return fizzbuzz

fizzbuzz()





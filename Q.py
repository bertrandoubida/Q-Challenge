"""
def fizzbuzz(n)

n = 15
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz

"""
numbers = list(range(1,16))

def fizzbuzz():
    for i in numbers:
        if i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        elif i % 15 == 0:
            print('fizzbuzz')
        else:
            print(i)
    return fizzbuzz

print(fizzbuzz)





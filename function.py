def jane():
    print("Hello there, Welcome to function session class")
# calling a function
jane()
jane()

def add():
    num=int(input("enter first number"))
    num2=int(input("enter second number"))
    print(f"sum of {num} and {num2} is {num+num2}")

def check_is_odd_even():
    nambari=int(input("weka nambari"))
    if nambari %2==0:
        print(f"{nambari} is even")
    else:
        print(f"{nambari} is odd")

add()
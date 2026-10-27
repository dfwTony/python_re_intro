# if else

name = input("Please enter your name: ")

age = int(input("What is your age?"))


if age == 18:
    print(f"welcome {name}, You are 18 years old")
elif age > 18:
    print(f"welcome {name}, You are an adult")

else:
    print(f"welcome {name}, You are a child")
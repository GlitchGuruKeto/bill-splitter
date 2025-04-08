import random

print("Enter the number of friends joining (including you):")
num = int(input())

if num <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friends = {}
    for _ in range(num):
        name = input()
        friends[name] = 0

    print("Enter the total bill value:")
    bill = float(input())

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    use_lucky = input()

    if use_lucky == "Yes":
        lucky = random.choice(list(friends.keys()))
        print(f"{lucky} is the lucky one!")
        if num > 1:
            split_value = round(bill / (num - 1), 2)
            for name in friends:
                friends[name] = 0 if name == lucky else split_value
        else:
            # Just in case there's only one person, avoid division by zero
            friends[lucky] = round(bill, 2)
    else:
        print("No one is going to be lucky")
        split_value = round(bill / num, 2)
        for name in friends:
            friends[name] = split_value

    print(friends)

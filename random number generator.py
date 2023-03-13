import random
random_number=random.randint(1,10)
ans=0
while ans!=random_number:
    ans=int(input("enter number"))
    if ans>random_number:
        print("too big")
    elif ans<random_number:
        print("too small")
print(f"your guess{random_number} is correct")

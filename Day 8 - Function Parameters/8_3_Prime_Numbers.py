# Function that checks if the input number passed to it is a prime number
def prime_checker(number):
    if number > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(number/2)+1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (number % i) == 0:
                print("It's not a prime number.")
                break
        else:
            print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)

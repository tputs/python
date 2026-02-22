def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True



def main():
    number = int(input('Enter a number: '))
    print(is_prime(number))
    


if __name__ == "__main__":
    main()
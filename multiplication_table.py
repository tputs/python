def multiplication_table(n):
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            print(f"{x * y:>4}", end=" ")
        print()


def main():
    number = int(input("Enter a number: "))
    multiplication_table(number)


if __name__ == "__main__":
    main()

def calculate_square(n):
    return n * n

if __name__ == "__main__":
    n = int(input("Please enter a positive integer: "))
    result = calculate_square(n)
    print("The square of", n, "is:", result)
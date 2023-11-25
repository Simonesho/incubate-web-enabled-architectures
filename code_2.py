def main():
    main()


import random
    data = generate_random_data()

if __name__ == "__main__":
    for item in data:
        print(f"Random Number: {item}")

    return data
def generate_random_data():
    data = [random.randint(1, 100) for _ in range(10)]

def main():

    print (generate_squared_list(5))

def generate_squared_list(X):
    return [i ** 2 for i in range(1, X + 1)]


if __name__ == '__main__':
    main()


def main():

    number = int(input('Enter value: '))

    while(number < 0 or number > 100):
        number = int(input('Enter value: '))

    print(number)

    ########################################
    # Do not delete the return statement
    ########################################
    return number


if __name__ == '__main__':
    main()

def main():
    a = 0
    b = 5

    #ゼロ割が発生したときにはzero divisionを表示
    try:
        print(a//b)
        print(b//a)
    except ZeroDivisionError:
        print('zero division')

if __name__ == '__main__':
    main()
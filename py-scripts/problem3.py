def main():
    #リスト作成
    list = [1,2,3,4,5]

    #添え字が偶数番の要素だけ出力
    for i in range(len(list)):
        if i % 2 == 0:
            print(list[i])

if __name__ == "__main__":
    main()
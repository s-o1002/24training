def main():
    #1~31までの整数を要素とするリスト
    list1 = list(range(1,32))
    #1~12までの整数を要素とするリスト
    list2 = list(range(1,13))
    #共通する要素の数をカウントする変数
    count = 0

    #list1の要素とlist2の要素を比較
    for value1 in list1:
        for value2 in list2:
            #list1の要素とlist2の要素の下一桁が一致している場合
            if value1 % 10 == value2 % 10:
                count += 1

    #共通する要素の数を出力
    print(count)

if __name__ == '__main__':
    main()
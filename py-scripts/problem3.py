def print_even_index(val):
    #引数がリストでない場合はエラーを出力
    if not isinstance(val, list):
        raise TypeError("引数はリスト型である必要があります")

    #添え字が偶数番の要素だけ出力
    for i in range(len(val)):
        if i % 2 == 0:
            print(val[i])

if __name__ == "__main__":
    print_even_index([1, 2, 3, 4, 5])
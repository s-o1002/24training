def make_tuple(list):
    #リストの長さが2以上でない場合はIndexErrorを発生させる
    if len(list) < 2:
        raise IndexError("IndexError")

    #リストの先頭と末尾をタプルとして格納
    tuple = (list[0],list[-1])

    #タプルの表示
    print(tuple)

if __name__ == "__main__":
    #リスト作成
    list = [1,2,3,4,5]
    make_tuple(list)
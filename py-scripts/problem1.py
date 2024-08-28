#先頭を0番目としてリストxに対してy番目とy+1番目の間にzを挿入して表示する関数
def insert_value(x, y, z):
    # yがリストの範囲内にあることを確認
    if 0 <= y < len(x):
        x.insert(y+1, z)
    else:
        raise IndexError("IndexError")
    print(x)

if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    y = 0
    z = 100
    insert_value(x, y, z)
def print_slice(string, x, y):
    #strが文字列でない場合、エラーを表示する
    if not isinstance(string, str):
        raise ValueError('not a string')

    #x,yが整数でない場合、エラーを表示する
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError('not an integer')

    #xが0未満、yが文字列の長さ以上の場合、エラーを表示する
    if x < 0 or y >= len(string):
        raise ValueError('out of range')

    #先頭を0番目とし、strのx番目からy番目を取り出して表示する
    print(string[x:y+1])

if __name__ == '__main__':
    print_slice('training', 1, 4)
def add_dict(dictionary, *kwargs):
    #辞書でない場合はエラーを返す
    if not isinstance(dictionary, dict):
        raise TypeError('not a dict')

    #辞書に存在すれば追加せず、存在しなければ-1で追加する
    for key in kwargs:
        dictionary[key] = dictionary.get(key, -1)

    #辞書の表示
    print(dictionary)

if __name__ == '__main__':
    add_dict({'apple': 10, 'grape': 20, 'orange': 30}, 'apple', 'pineapple')
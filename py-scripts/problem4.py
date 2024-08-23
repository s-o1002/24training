def main():
    #辞書の作成
    d = {'apple':10, 'grape':20, 'orange':30}

    #'apple'というキーが存在しなければ-1を'apple'の値として追加
    d['apple'] = d.get('apple', -1)

    #'pineapple'というキーが存在しなければ-1を'pineapple'の値として追加
    d['pineapple'] = d.get('pineapple', -1)

    #辞書の表示
    print(d)

if __name__ == '__main__':
    main()
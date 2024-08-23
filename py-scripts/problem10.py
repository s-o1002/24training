def main():
    dic = {'two':324, 'four':830, 'three':493, 'one':172, 'five':1024}

    #値でソート
    dic_sorted = sorted(dic.items(), key=lambda x:x[1])

    #キーのみをリストに格納
    keys = [x[0] for x in dic_sorted]

    #キーの表示
    print(keys)

if __name__ == '__main__':
    main()
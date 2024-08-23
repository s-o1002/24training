def main():
      li = [{'a': 6, 'b': 7, 'c': 6},
            {'a': 4, 'b': 2, 'c': 3},
            {'a': 1, 'b': 5, 'c': 8}]

      #bの値で降順にソート
      li.sort(key=lambda x: x['b'], reverse=True)

      #リストの表示
      print(li)

if __name__ == '__main__':
    main()
# 24新卒スペシャルレッスン
9月からの業務に備えた基礎学習を進めているリポジトリ  
Pythonを実行できるDocker環境を作成することができ、  
練習問題10問分のスクリプトとそのテストコードが実行できる。

## セットアップ～テスト実施まで
### プロジェクトのクローン
まず、このリポジトリをローカル環境へクローンする
```
> git clone https://github.com/s-o1002/24training.git
```
### Dockerコンテナの起動
クローン後、プロジェクトディレクトリへ遷移する
```
> cd 24training
```

24trainingディレクトリで以下のコマンドを実行し、Dockerのイメージをビルド
```
24training> docker build -t my_python_env .
```

以下のコマンドを実行し、Dockerコンテナを起動してbashを開きます
```
> docker run -it --name my_python_container my_python_env bash
```
### スクリプトの実行
起動後は練習問題のスクリプトが格納されているディレクトリ「/work/python」が開かれるので、  
ここで以下のようにスクリプトを実行できる(以下は練習問題1)
```
/work/python# python problem1.py
```
以下のように表示されれば成功
```
[1, 100, 2, 3, 4, 5]
```
### テストの実行
そのまま「/work/python」ディレクトリで以下のコマンドでテストを実行できる(以下は練習問題1)
```
/work/python# coverage run -m unittest discover -s ../tests -p "test_problem1.py" -v
```

実行したテストのカバレッジ率は以下のコマンドで確認できる
```
coverage report
```

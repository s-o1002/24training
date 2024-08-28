# 24新卒スペシャルレッスン
9月からの業務に備えた基礎学習を進めているリポジトリ  
Pythonを実行できるDocker環境を作成することができ、  
練習問題10問分のスクリプトとそのテストコードが実行できる。

## セットアップ～テスト実施まで
### プロジェクトのクローン
まず、このリポジトリをローカル環境へクローンします
```
> git clone https://github.com/s-o1002/24training.git
```
### Dockerコンテナの起動
クローン後、プロジェクトディレクトリへ遷移します
```
> cd 24training
```

24trainingディレクトリで以下のコマンドを実行し、Dockerのイメージをビルドします
```
24training> docker build -t my_python_env .
```

以下のコマンドを実行し、Dockerコンテナを起動してbashを開きます
```
> docker run -it --name my_python_container my_python_env bash
```
### スクリプトの実行
起動後は練習問題のスクリプトが格納されているディレクトリ「/work/python」が開かれるので、  
ここで以下のようにスクリプトを実行できます(以下は練習問題1)
```
/work/python# python problem1.py
```
以下のように表示されれば成功
```
[1, 100, 2, 3, 4, 5]
```
  
ECRを操作するスクリプトを実行する場合はディレクトリ「/work/aws」に移動して
aws configureコマンドでキーの設定をします
```
/work/python# cd ../aws  
/work/aws# aws configure  
```
アクセスキー,シークレットキー,リージョン,出力結果の形式の設定を行ってください  
設定を行った後に実行ができるようになります(以下はECRリポジトリの作成)
```
/work/aws# python createEcrRepository.py
```
既に作成などがされていなければ、"24-training-ecr-repository"が作成され以下のように表示されます  
```
リポジトリ「24-training-ecr-repository」を作成しました
```
### テストの実行
「/work/python」ディレクトリで以下のコマンドでテストを実行できる(以下は練習問題1)
```
/work/python# coverage run -m unittest discover -s ../tests -p "test_problem1.py" -v
```

実行したテストのカバレッジ率は以下のコマンドで確認できます
```
coverage report
```
  
AWSのテストも同じように実行ができます
「/work/aws」ディレクトリで以下のようなコマンドでテストを実行できます
```
/work/aws# coverage run -m unittest discover -s ../tests/aws
```
上記のコマンドだと全てのテストが実行されます

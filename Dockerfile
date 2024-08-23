# ベースイメージの指定
FROM python:3.8-slim

#ライブラリのインストール
RUN pip install --no-cache-dir boto3 moto coverage

#作業ディレクトリの作成
RUN mkdir -p /work

#Pythonスクリプトを配置するためのディレクトリの作成
RUN mkdir -p /work/python

#作業ディレクトリを指定
WORKDIR /work/python

COPY py-scripts/ .

COPY tests/ ../tests
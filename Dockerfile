# ベースイメージの指定
FROM python:3.8-slim

#ライブラリのインストール
RUN pip install --no-cache-dir boto3 moto coverage pytest

RUN apt-get update && apt-get install -y unzip curl

#AWS CLIのインストール
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install

#作業ディレクトリの作成
RUN mkdir -p /work

#Pythonスクリプトを配置するためのディレクトリの作成
RUN mkdir -p /work/python

#作業ディレクトリを指定
WORKDIR /work/python

COPY py-scripts/ .

COPY tests/ ../tests

COPY aws/ ../aws
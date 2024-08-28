import unittest
from moto import mock_aws
import boto3
from botocore.exceptions import ClientError
from createEcrRepository import create_repository
import sys
from io import StringIO
from unittest.mock import MagicMock, patch

class TestCreateRepository(unittest.TestCase):
    # 標準出力のリダイレクト
    def setUp(self):
        self.io = StringIO()
        sys.stdout = self.io

    # 標準出力のリダイレクト解除
    def tearDown(self):
        sys.stdout = sys.__stdout__

    # create_repository関数が正常にリポジトリを作成することを確認
    @mock_aws
    def test_create_repository_success(self):
        # create_repository関数でリポジトリを作成する
        repository_name = '24-training-ecr-repository'
        repository = create_repository(repository_name)
        
        # describe_repositoriesでリポジトリリストを取得
        client = boto3.client('ecr', region_name='ap-northeast-1')
        response = client.describe_repositories(repositoryNames=[repository_name])

        # 検証
        self.assertEqual(len(response['repositories']), 1)
        self.assertEqual(response['repositories'][0]['repositoryName'], repository_name)
        self.assertEqual(self.io.getvalue().strip(), f"リポジトリ「{repository_name}」を作成しました")

    # 既に存在するリポジトリ名でcreate_repository関数を呼び出すと"既に同じ名前のリポジトリが存在します。"と表示されることを確認
    @mock_aws
    def test_create_repository_same_name(self):
        # モックECRクライアントを作成
        client = boto3.client('ecr', region_name='ap-northeast-1')
        
        # モックリポジトリを作成
        repository_name = '24-training-ecr-repository'
        client.create_repository(repositoryName=repository_name)

        # create_repository関数を呼び出す
        create_repository(repository_name)
        self.assertIn("既に同じ名前のリポジトリが存在します。", self.io.getvalue().strip())

    # create_repository関数でリポジトリ作成時にエラーが発生した場合、"エラーが発生しました。"と表示されることを確認
    @patch('boto3.Session.client')
    def test_create_repository_error(self,mock_client):
        mock_ecr_client = MagicMock()
        mock_client.return_value = mock_ecr_client

        # ClientError を発生させる
        mock_ecr_client.create_repository.side_effect = ClientError(
            {'Error': {'Code': 'ClientError', 'Message': 'An error occurred'}}, 
            'CreateRepository'
        )

        # create_repository関数を呼び出す
        create_repository('24-training-ecr-repository')

        self.assertIn("エラーが発生しました。", self.io.getvalue().strip())

if __name__ == '__main__':
    unittest.main()
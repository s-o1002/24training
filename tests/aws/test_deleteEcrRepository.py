import unittest
from moto import mock_aws
import boto3
from botocore.exceptions import ClientError
from deleteEcrRepository import delete_repository
import sys
from io import StringIO
from unittest.mock import MagicMock, patch

class TestDeleteRepository(unittest.TestCase):
    # 標準出力のリダイレクト
    def setUp(self):
        self.io = StringIO()
        sys.stdout = self.io

    # 標準出力のリダイレクト解除
    def tearDown(self):
        sys.stdout = sys.__stdout__

    # delete_repository関数が正常にリポジトリを削除することを確認
    @mock_aws
    def test_delete_repository_success(self):
        # モックECRクライアントを作成
        client = boto3.client('ecr', region_name='ap-northeast-1')
        
        # モックリポジトリを作成
        repository_name = '24-training-ecr-repository'
        client.create_repository(repositoryName=repository_name)
        
        # delete_repository関数を呼び出す
        response = delete_repository(repository_name)
        
        # 検証
        self.assertEqual(self.io.getvalue().strip(), f"リポジトリ「{repository_name}」を削除しました")
        
        # 指定したリポジトリが削除されたことを確認
        with self.assertRaises(client.exceptions.RepositoryNotFoundException):
            client.describe_repositories(repositoryNames=[repository_name])

    # delete_repository関数がリポジトリが存在しない場合にリポジトリ名「{repository_name}」が見つかりませんと出力することを確認
    @mock_aws
    def test_delete_repository_failure(self):
        # delete_repository関数を呼び出す
        repository_name = 'non-existent-repository'
        response = delete_repository(repository_name)

        # 検証
        self.assertEqual(self.io.getvalue().strip(), f"リポジトリ名「{repository_name}」が見つかりません")

        # リポジトリが存在しないことを確認
        client = boto3.client('ecr', region_name='ap-northeast-1')
        with self.assertRaises(ClientError) as e:
            client.describe_repositories(repositoryNames=[repository_name])

    # delete_repository関数でリポジトリ削除時にエラーが発生した場合、"リポジトリの削除に失敗しました"と表示されることを確認
    @patch('boto3.Session.client')
    def test_delete_repository_error(self,mock_client):
        mock_ecr_client = MagicMock()
        mock_client.return_value = mock_ecr_client

        # ClientError を発生させる
        mock_ecr_client.delete_repository.side_effect = ClientError(
            {'Error': {'Code': 'ClientError', 'Message': 'An error occurred'}}, 
            'CreateRepository'
        )
        # 削除対象のリポジトリを作成
        client = boto3.client('ecr', region_name='ap-northeast-1')
        client.create_repository(repositoryName='24-training-ecr-repository')

        # delete_repository関数を呼び出す
        repository_name = '24-training-ecr-repository'
        response = delete_repository(repository_name)

        # 検証
        self.assertEqual(self.io.getvalue().strip(), "リポジトリの削除に失敗しました")

if __name__ == '__main__':
    unittest.main()
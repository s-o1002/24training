import sys
from io import StringIO
import unittest
from unittest.mock import MagicMock, patch
import boto3
from botocore.exceptions import ClientError
from moto import mock_aws
from listEcrRepositories import list_repositories
import pytest

class TestListRepositories(unittest.TestCase):
    # 標準出力のリダイレクト
    def setUp(self):
        self.io = StringIO()
        sys.stdout = self.io

    # 標準出力のリダイレクト解除
    def tearDown(self):
        sys.stdout = sys.__stdout__

    # list_repositories関数が正常にリポジトリをリストすることを確認
    @mock_aws
    def test_list_repositories_success(self):
        # モックECRクライアントを作成
        client = boto3.client('ecr', region_name='ap-northeast-1')
        
        # モックリポジトリを作成
        client.create_repository(repositoryName='repo1')
        client.create_repository(repositoryName='repo2')
        
        # 関数を呼び出す
        list_repositories()
        
        # 検証
        self.assertEqual(self.io.getvalue().strip(), 'repo1\nrepo2')

    # リポジトリが存在しない場合
    @mock_aws
    def test_list_repositories_failure(self):
        # モックECRクライアントを作成
        client = boto3.client('ecr', region_name='ap-northeast-1')
        
        # 関数を呼び出す
        list_repositories()
        
        # 検証
        self.assertEqual(self.io.getvalue().strip(), 'リポジトリが見つかりませんでした。')

    @patch('boto3.Session.client')
    def test_list_repositories_client_error(self, mock_client):
        mock_ecr_client = MagicMock()
        mock_client.return_value = mock_ecr_client
        
        # ClientError を発生させる
        mock_ecr_client.describe_repositories.side_effect = ClientError(
            {'Error': {'Code': 'ClientError', 'Message': 'An error occurred'}}, 
            'DescribeRepositories'
        )

        # 関数を呼び出す
        list_repositories()
        
        # 検証
        self.assertEqual(self.io.getvalue().strip(), 'エラーが発生しました。')

if __name__ == '__main__':
    unittest.main()
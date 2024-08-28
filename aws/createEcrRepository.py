import boto3
from botocore.exceptions import ClientError

def create_repository(repository_name):
    try:
        session = boto3.Session(profile_name='default')

        ecr_client = session.client('ecr', region_name='ap-northeast-1')
        
        response = ecr_client.create_repository(
            repositoryName=repository_name
        )
        print(f"リポジトリ「{repository_name}」を作成しました")
    except ClientError as e:
        # 既に同じ名前のリポジトリが存在する場合
        if e.response['Error']['Code'] == 'RepositoryAlreadyExistsException':
            print("既に同じ名前のリポジトリが存在します。")
        else:
            # その他のエラー
            print("エラーが発生しました。")

if __name__ == '__main__':
    repository_name = '24-training-ecr-repository'
    create_repository(repository_name)
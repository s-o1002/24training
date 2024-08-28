import boto3
from botocore.exceptions import ClientError

def delete_repository(repository_name):
    try:
        session = boto3.Session(profile_name='default')

        ecr_client = session.client('ecr', region_name='ap-northeast-1')

        response = ecr_client.delete_repository(
            repositoryName=repository_name,
            force=True
        )
        print(f"リポジトリ「{repository_name}」を削除しました")
    except ClientError as e:
        if e.response['Error']['Code'] == 'RepositoryNotFoundException':
            print(f"リポジトリ名「{repository_name}」が見つかりません")
        else:
            print("リポジトリの削除に失敗しました")

if __name__ == '__main__':
    repository_name = '24-training-ecr-repository'
    delete_repository(repository_name)

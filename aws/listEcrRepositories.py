import boto3
from botocore.exceptions import ClientError


def list_repositories():
    try:
        session = boto3.Session(profile_name='default')

        ecr_client = session.client('ecr', region_name='ap-northeast-1')

        response = ecr_client.describe_repositories()
        repositories = response['repositories']

        if repositories:
            for repo in repositories:
                print(repo['repositoryName'])
        else:
            print("リポジトリが見つかりませんでした。")
    except ClientError as e:
        print("エラーが発生しました。")

if __name__ == '__main__':
    list_repositories()

import boto3

client = boto3.client('apigateway')


def entry():
    create_api()
    print("OK...")


def create_api():
    response = client.import_rest_api(
        body=open('routine_api.yaml', 'r').read(),
        parameters={
            'endpointConfigurationTypes': 'REGIONAL'
        }
    )
    print(response)


if __name__ == '__main__':
    entry()

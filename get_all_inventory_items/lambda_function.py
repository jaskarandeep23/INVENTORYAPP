import json
 
import boto3
 
 
def lambda_handler(event, context):

    dynamo_client = boto3.client("dynamodb")

    table_name = "Inventory"
 
    try:

        response = dynamo_client.scan(TableName=table_name)

        items = response["Items"]
 
        return {

            "statusCode": 200,

            "body": json.dumps(items),

        }

    except Exception as e:

        print(e)

        return {

            "statusCode": 500,

            "body": json.dumps(str(e)),

        }
 
 # trigger deployment
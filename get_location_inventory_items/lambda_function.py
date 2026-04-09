import json
import boto3

def lambda_handler(event, context):

    dynamo_client = boto3.client("dynamodb")

    table_name = "Inventory"
 
    if "pathParameters" not in event or "id" not in event["pathParameters"]:

        return {

            "statusCode": 400,

            "body": json.dumps("Missing 'id' path parameter"),

        }
 
    location_id = event["pathParameters"]["id"]
 
    try:

        response = dynamo_client.scan(TableName=table_name)

        items = response["Items"]
 
        filtered_items = []
 
        for item in items:

            if "location_id" in item and item["location_id"]["N"] == location_id:

                filtered_items.append(item)
 
        return {

            "statusCode": 200,

            "body": json.dumps(filtered_items),

        }
 
    except Exception as e:

        print(e)

        return {

            "statusCode": 500,

            "body": json.dumps(str(e)),

        }
 
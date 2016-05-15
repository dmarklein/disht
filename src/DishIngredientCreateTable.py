from __future__ import print_function # Python 2/3 compatibility
import boto3
#import uuid

dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="http://dynamodb.us-east-1.amazonaws.com")

# <DishIngredient>
# -dishIngredientId
# -name
# -dishId
# -quantity
# -quanitytUnits

table = dynamodb.create_table(
    TableName='DishIngredient',
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'name',
            'KeyType': 'RANGE'  #sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'name',
            'AttributeType': 'S'
        }

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
    # TODO: secondary index for dishId??
)

print("Table status:", table.table_status)

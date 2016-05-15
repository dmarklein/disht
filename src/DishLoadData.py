from __future__ import print_function # Python 2/3 compatibility
import boto3
import uuid as uuid

dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="http://dynamodb.us-east-1.amazonaws.com")

# <Dish>
# -id
# -name
# -description
# -restaurantLocationId
# -price
# -categoryId
# -nutrition info?

table = dynamodb.Table('Dish')

table.put_item(
   Item={
       'id': str(uuid.uuid4()),
       'name': "burrito bowl",
       'description': "rice, beans, chicken, guacamole, salsa, cheese, n stuff",
       'price': "6.50",
       'restaurantLocationId': str(uuid.uuid4()),
       'categoryId': str(uuid.uuid4())
    }
)

table.put_item(
   Item={
       'id': str(uuid.uuid4()),
       'name': "sweet tea",
       'description': "water, tea, sugar!",
       'price': "1.00",
       'restaurantLocationId': str(uuid.uuid4()),
       'categoryId': str(uuid.uuid4())
    }
)

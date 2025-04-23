import boto3
from helper_functions import deserialize_item
import pandas as pd

client = boto3.client("dynamodb")

# get single item by partition and sort key
item = client.get_item(
    TableName="MediaProducts",
    Key={
        "product_id": {"S": "BOOK001"},
        "category": {"S": "BOOK"}
    }
)
print(deserialize_item(item["Item"]))

# get all items by partition key
items = client.query(
    TableName="MediaProducts",
    KeyConditionExpression="product_id = :pid",
    ExpressionAttributeValues={
        ":pid": {"S": "BOOK001"}
    }
)

# get all items by a specific filter
items = client.scan(
    TableName="MediaProducts",
    FilterExpression="category = :cat",
    ExpressionAttributeValues={
        ":cat": {"S": "BOOK"}
    }

)

# return as pandas dataframe
items = [deserialize_item(item) for item in items["Items"]]
df = pd.DataFrame(items)
print(df)
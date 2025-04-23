import boto3

client = boto3.client("dynamodb")
print("Before create:", client.list_tables())

key_schema = [
    {
        "AttributeName": "product_id",
        "KeyType": "HASH"
    },
    {
        "AttributeName": "category",
        "KeyType": "RANGE"
    }
]

attr_defs = [
    {
        "AttributeName": "product_id",
        "AttributeType": "S"
    },
    {
        "AttributeName": "category",
        "AttributeType": "S"
    }
]

client.create_table(
    TableName="MediaProducts",
    KeySchema=key_schema,
    AttributeDefinitions=attr_defs,
    TableClass="STANDARD",
    BillingMode="PAY_PER_REQUEST"
)

print("After create:", client.list_tables())

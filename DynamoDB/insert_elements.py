import boto3
import csv

from helper_functions import reformat_dict


counts = {}

client = boto3.client("dynamodb")

with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cat = row["category"]
        if cat not in counts:
            counts[cat] = 1
        else:
            counts[cat] += 1
        row["product_id"] = row["category"] + str(counts[cat]).zfill(3)
        # print(reformat_dict(row))

        respones = client.put_item(
            TableName="MediaProducts",
            Item=reformat_dict(row)  # alternative to custom function is to use serialize_item from from boto3.dynamodb.types import TypeSerializer
        )
        
        print(respones)
        
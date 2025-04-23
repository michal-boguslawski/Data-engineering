from boto3.dynamodb.types import TypeDeserializer


deserializer = TypeDeserializer()

def deserialize_item(item):
    return {k: deserializer.deserialize(v) for k, v in item.items()}

def get_type(value):
    try:
        float(value)
        return {"N": value}
    except ValueError:
        return {"S": value}

def reformat_dict(dict_):
    return {key: get_type(value) for key, value in dict_.items()}
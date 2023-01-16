import logging

import boto3
import botocore

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
aws_access_key_id = "dummy-access-key"
aws_secret_access_key = "dummy-secret-key"
dynamo_db = boto3.client(
    "dynamodb",
    endpoint_url="http://localhost:8000",
    region_name="us-west-2",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
)
TABLE_NAME = "Passengers"


# Temporary, in the future will provision the table and dynamodb instance in Terraform
def create_table():
    """Creates dynamodb table if table doesn't already exist"""
    # Describe table, if it exists catch error and log that table already exists
    try:
        dynamo_db.describe_table(TableName=TABLE_NAME)
        return f"Table:{TABLE_NAME} already exists"
    # Create table Passengers, should only run if table doesn't exists
    except dynamo_db.exceptions.ResourceNotFoundException:
        response = dynamo_db.create_table(
            TableName=TABLE_NAME,
            KeySchema=[{"AttributeName": "passenger_id", "KeyType": "HASH"}],
            AttributeDefinitions=[
                {"AttributeName": "passenger_id", "AttributeType": "N"},
            ],
            ProvisionedThroughput={
                "ReadCapacityUnits": 5,
                "WriteCapacityUnits": 5,
            },
        )
        return response


def delete_table():
    """Deletes dynamodb table if it exists"""
    try:
        dynamo_db.delete_table(TableName=TABLE_NAME)
        return ("Table %s deleted", TABLE_NAME)
    except botocore.exceptions.ClientError as error:
        return error


def get_passengers():
    """Gets all passengers from dynamodb table"""
    try:
        response = dynamo_db.scan(TableName=TABLE_NAME)
    except botocore.exceptions.ClientError as error:
        return error
    return response["Items"]


def add_passenger(new_passenger, passenger_id):
    try:
        dynamo_db.put_item(
            TableName=TABLE_NAME,
            Item={
                "passenger_id": {"N": str(passenger_id)},
                "Survived": {"N": str(new_passenger["Survived"])},
                "Pclass": {"N": str(new_passenger["Pclass"])},
                "passenger_name": {"S": new_passenger["passenger_name"]},
                "Sex": {"S": new_passenger["Sex"]},
                "Age": {"N": str(new_passenger["Age"])},
                "SibSp": {"N": str(new_passenger["SibSp"])},
                "Parch": {"N": str(new_passenger["Parch"])},
                "Ticket": {"S": new_passenger["Ticket"]},
                "Fare": {"N": str(new_passenger["Fare"])},
                "Cabin": {"S": new_passenger["Cabin"]},
                "Embarked": {"S": new_passenger["Embarked"]},
            },
        )
    except botocore.exceptions.ClientError as error:
        return error
    return dynamo_db.get_item(TableName=TABLE_NAME, Key={"passenger_id": {"N": "2"}})


def get_passenger(passenger_id: int):
    try:
        response = dynamo_db.get_item(
            TableName=TABLE_NAME,
            Key={"passenger_id": {"N": passenger_id}},
        )
    except botocore.exceptions.ClientError as error:
        raise error
    return response


def update_passenger(new_passenger, passenger_id):

    # Initializes update and expression attribute values
    expression_attribute_values = {}
    update_expression = "SET "
    # iterates through passenger to update attribute values and update expression
    for key, value in new_passenger.items():
        print(type(value))
        print(isinstance(value, str))
        if key != "PassengerId":
            if str(value) is not None:
                update_expression += f"{key} = :{key}, "
                if isinstance(value, int):
                    print("value is an int")
                    expression_attribute_values[f":{key}"] = {"N": f"{value}"}
                elif isinstance(value, str):
                    print("value is a str")
                    expression_attribute_values[f":{key}"] = {"S": f"{value}"}
    update_expression = update_expression[:-2]  # removes last comma and space
    try:
        response = dynamo_db.update_item(
            TableName=TABLE_NAME,
            Key={"passenger_id": {"N": f"{passenger_id}"}},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
        )
    except botocore.exceptions.ClientError as error:
        return error
    return response


def delete_passenger(passenger_id):
    try:
        response = dynamo_db.delete_item(
            TableName=TABLE_NAME,
            Key={"passenger_id": {"N": f"{passenger_id}"}},
        )
    except botocore.exceptions.ClientError as error:
        return error
    return response

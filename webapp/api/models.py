from dataclasses import dataclass, field
from uuid import uuid4
import os

import marshmallow_dataclass
from boto3 import resource
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

REGION_NAME = 'ap-southeast-1'
DB_URL = os.getenv('DB_URL')
print(DB_URL)
ddb = resource('dynamodb',
               endpoint_url=DB_URL,
               aws_access_key_id="anything",
               aws_secret_access_key="anything",
               region_name=REGION_NAME)


@dataclass
class DynamoObj:
    id: str

    table = None

    def delete(self):
        return self.delete_by_id(self.id)

    def to_dict(self):
        return self.get_schema().dump(self)

    @classmethod
    def get_schema(cls):
        return marshmallow_dataclass.class_schema(cls)()

    @classmethod
    def build(cls, item_dict):
        """
        Return: if the item_dict has no id attribute, create new db item (meaning new record)
        """
        if 'id' not in item_dict or not item_dict['id']:
            item_dict['id'] = str(uuid4()).replace('-', '')
        return cls.get_schema().load(item_dict)

    def put(self):
        try:
            response = self.table.put_item(Item=self.to_dict())
        except ClientError as err:
            raise err
        else:
            return response

    @classmethod
    def get_by_id(cls, id):
        response = cls.table.get_item(Key={'id': id})
        return cls.build(response['Item'])

    @classmethod
    def delete_by_id(cls, id):
        response = cls.table.delete_item(Key={'id': id})
        return response

    @classmethod
    def list_all(cls):
        response = cls.table.scan()
        items = response['Items']
        while 'LastEvaluatedKey' in response:
            response = cls.table.scan(
                ExclusiveStartKey=response['LastEvaluatedKey'])
            items += response['Items']
        return items


@dataclass
class Patient(DynamoObj):
    citizen_id: str
    patient_id: str
    first_name: str
    last_name: str
    nick_name: str
    first_name_eng: str
    last_name_eng: str
    nick_name_eng: str
    birth_date: str
    phone_number: str
    gender: str
    email: str
    info: str
    checking_in: str = field(default='out')

    table = ddb.Table('patients')

    def check_in(self):
        self.checking_in = 'in'
        self.put()

    def check_out(self):
        self.checking_in = 'out'
        self.put()

    @classmethod
    def get_by_checking_in(cls, status):
        return cls.table.query(
            IndexName='NameCheckinIndex',
            KeyConditionExpression=Key('checking_in').eq(status)
        )['Items']

    @classmethod
    def list(cls, request):
        limit = 10
        filter_text = ''
        ex_start = {'id': request.args['id'], 'first_name': request.args['first_name'],
                    'checking_in': request.args['checking_in']}

        kwargs = {
            'IndexName': 'NameCheckinIndex',
            'KeyConditionExpression': Key('checking_in').eq('out'),
            'Limit': limit,
        }
        if request.args['id']:
            kwargs['ExclusiveStartKey'] = ex_start
        if filter_text:
            kwargs['KeyConditionExpression'] = Key('checking_in').eq(
                'out') & Key('first_name').begins_with(filter_text)

        response = cls.table.query(**kwargs)
        result = {'patients': response['Items'],
                  'pre_last_key': ex_start}
        if 'LastEvaluatedKey' in response:
            result['last_key'] = response['LastEvaluatedKey']
        else:
            result['last_key'] = {
                'id': '', 'first_name': '', 'checking_in': ''}
        return result

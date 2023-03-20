import boto3
from botocore.exceptions import ClientError


ddb = boto3.resource('dynamodb',
                     endpoint_url='http://dynamo:8000',
                     aws_access_key_id="anything",
                     aws_secret_access_key="anything",
                     region_name="ap-southeast-1")


def sync_patients():

    patients = [
        {
            "birth_date": "2499-04-13T00:00:00Z",
            "checking_in": "out",
            "citizen_id": "",
            "email": "5 \u0e21.7 \u0e15.\u0e1a\u0e49\u0e32\u0e19\u0e41\u0e1e \u0e2d.\u0e04\u0e39\u0e40\u0e21\u0e37\u0e2d\u0e07 \u0e08.\u0e1a\u0e38\u0e23\u0e35\u0e23\u0e31\u0e21\u0e22\u0e4c",
            "first_name": "\u0e17\u0e2d\u0e07\u0e43\u0e1a",
            "first_name_eng": "Thongbai",
            "gender": "F",
            "id": "4898604f6c30e8f79118b337ba066547",
            "info": "\u0e04\u0e27\u0e32\u0e21\u0e14\u0e31\u0e19",
            "last_name": "\u0e2a\u0e34\u0e21\u0e07\u0e32\u0e21",
            "last_name_eng": "Simngam",
            "nick_name": "\u0e43\u0e1a",
            "nick_name_eng": "Bai",
            "patient_id": "690259",
            "phone_number": "082-2111828"
        },
        {
            "birth_date": "2524-07-23T00:00:00Z",
            "checking_in": "out",
            "citizen_id": "3310100735004",
            "email": "651 \u0e21.26 \u0e15.\u0e28\u0e34\u0e25\u0e32 \u0e2d.\u0e40\u0e21\u0e37\u0e2d\u0e07 \u0e08.\u0e02\u0e2d\u0e19\u0e41\u0e01\u0e48\u0e19",
            "first_name": "\u0e2a\u0e38\u0e27\u0e25\u0e35",
            "first_name_eng": "Suwalee",
            "gender": "F",
            "id": "cf7ce614d1413f67518db89f9b020b65",
            "info": "",
            "last_name": "\u0e0a\u0e31\u0e22\u0e21\u0e30\u0e40\u0e23\u0e34\u0e07 ",
            "last_name_eng": "Chaimaraeng",
            "nick_name": "",
            "nick_name_eng": "",
            "patient_id": "692718",
            "phone_number": "088-5718524"
        },
        {
            "birth_date": "2529-01-10T00:00:00Z",
            "checking_in": "out",
            "citizen_id": "1319900059510",
            "email": "127/2 \u0e16.\u0e18\u0e32\u0e19\u0e35 \u0e15.\u0e43\u0e19\u0e40\u0e21\u0e37\u0e2d\u0e07 \u0e2d.\u0e40\u0e21\u0e37\u0e2d\u0e07\u0e1a\u0e38\u0e23\u0e35\u0e23\u0e31\u0e21\u0e22\u0e4c \u0e08.\u0e1a\u0e38\u0e23\u0e35\u0e23\u0e31\u0e21\u0e22\u0e4c",
            "first_name": "\u0e28\u0e38\u0e20\u0e0a\u0e31\u0e22",
            "first_name_eng": "Suphachai",
            "gender": "M",
            "id": "4898604f6c30e8f79118b337ba4258a3",
            "info": "",
            "last_name": "\u0e40\u0e25\u0e32\u0e2b\u0e1a\u0e38\u0e15\u0e23",
            "last_name_eng": "Laohabut",
            "nick_name": "\u0e0b\u0e34\u0e1e",
            "nick_name_eng": "Sepp",
            "patient_id": "690723",
            "phone_number": "091-0122094"
        },
        {
            "birth_date": "19 07 2543",
            "checking_in": "out",
            "citizen_id": "1100703059839",
            "email": "8 \u0e21.16 \u0e15.\u0e0a\u0e48\u0e2d\u0e07\u0e41\u0e21\u0e27 \u0e2d.\u0e25\u0e33\u0e17\u0e30\u0e40\u0e21\u0e22\u0e0a\u0e31\u0e22 \u0e08.\u0e19\u0e04\u0e23\u0e23\u0e32\u0e0a\u0e2a\u0e35\u0e21\u0e32",
            "first_name": "\u0e08\u0e34\u0e23\u0e32\u0e20\u0e23\u0e13\u0e4c",
            "first_name_eng": "Jiraporn",
            "gender": "F",
            "id": "ba0c8e5cfd020602b72720f8bb6e0da4",
            "info": "",
            "last_name": "\u0e1e\u0e25\u0e1e\u0e31\u0e19\u0e18\u0e4c",
            "last_name_eng": "Phonphan",
            "nick_name": "",
            "nick_name_eng": "",
            "patient_id": "692428",
            "phone_number": "063-2108197"
        },
        {
            "birth_date": "2534-09-22T00:00:00Z",
            "checking_in": "out",
            "citizen_id": "1410300088391",
            "email": "4 \u0e21.8 \u0e15.\u0e01\u0e38\u0e14\u0e2b\u0e21\u0e32\u0e01\u0e44\u0e1f \u0e2d.\u0e2b\u0e19\u0e2d\u0e07\u0e27\u0e31\u0e27\u0e0b\u0e2d \u0e08.\u0e2d\u0e38\u0e14\u0e23\u0e18\u0e32\u0e19\u0e35",
            "first_name": "\u0e28\u0e34\u0e23\u0e34\u0e19\u0e20\u0e32",
            "first_name_eng": "Sirinapha",
            "gender": "F",
            "id": "4898604f6c30e8f79118b337ba5d98f0",
            "info": "",
            "last_name": "\u0e2d\u0e23\u0e38\u0e13\u0e13\u0e32",
            "last_name_eng": "Aruna",
            "nick_name": "\u0e40\u0e01\u0e4b",
            "nick_name_eng": "Ke",
            "patient_id": "010011",
            "phone_number": "093-3297130"
        },
        {
            "birth_date": "2550-07-08T00:00:00Z",
            "checking_in": "out",
            "citizen_id": "",
            "email": "",
            "first_name": "\u0e21\u0e38\u0e17\u0e34\u0e15\u0e32",
            "first_name_eng": "",
            "gender": "F",
            "id": "434f48adf668bb728c89f0f4d4134276",
            "info": "",
            "last_name": "\u0e21\u0e2b\u0e32\u0e27\u0e2a\u0e38",
            "last_name_eng": "",
            "nick_name": "",
            "nick_name_eng": "",
            "patient_id": "691206",
            "phone_number": "063-4566165"
        }]

    patient_table = ddb.Table('patients')

    with patient_table.batch_writer() as batch:
        for patient in patients:
            try:
                batch.put_item(Item=patient)
            except ClientError as err:
                print(
                    "Couldn't put an itme to the tables. Here's why: %s: %s",
                    err.response['Error']['Code'], err.response['Error']['Message'])
                raise


sync_patients()

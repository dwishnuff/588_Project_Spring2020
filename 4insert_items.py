import boto3

# boto3 is the AWS SDK library for Python.
# The "resources" interface allow for a higher-level abstraction than the low-level client interface.
# More details here: http://boto3.readthedocs.io/en/latest/guide/resources.html
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('FreewayData')


# The BatchWriteItem API allows us to write multiple items to a table in one request.
with table.batch_writer() as batch:

    batch.put_item(Item={"Location": "Johnson Cr NB", "Length": "1.89", "Date": "2011-09-15", "Time": "8:55:00", "Volume": "5", "Speed": "53", "DetectorId":"1353"})
    batch.put_item(Item={"Location": "Johnson Cr NB", "Length": "1.89", "Date": "2011-09-15", "Time": "8:55:20", "Volume": "3", "Speed": "75", "DetectorId":"1353"})
    batch.put_item(Item={"Location": "Johnson Cr NB", "Length": "1.89", "Date": "2011-09-15", "Time": "8:55:40", "Volume": "7", "Speed": "58", "DetectorId":"1353"})

    batch.put_item(Item={"Location": "Johnson Cr NB", "Length": "1.89", "Date": "2011-09-15", "Time": "8:56:00", "Volume": "6", "Speed": "57", "DetectorId":"1353"})
    batch.put_item(Item={"Location": "Johnson Cr NB", "Length": "1.89", "Date": "2011-09-15", "Time": "8:56:20", "Volume": "6", "Speed": "75", "DetectorId":"1353"})
    batch.put_item(Item={"Location": "Johnson Cr NB", "Length": "1.89", "Date": "2011-09-15", "Time": "8:56:40", "Volume": "11", "Speed": "61", "DetectorId":"1353"})

    batch.put_item(Item={"Location": "Johnson Cr NB", "Length": "1.89", "Date": "2011-09-15", "Time": "8:55:00", "Volume": "7", "Speed": "65", "DetectorId":"1354"})
    batch.put_item(Item={"Location": "Johnson Cr NB", "Length": "1.89", "Date": "2011-09-15", "Time": "8:55:20", "Volume": "10", "Speed": "60", "DetectorId":"1354"})
    batch.put_item(Item={"Location": "Johnson Cr NB", "Length": "1.89", "Date": "2011-09-15", "Time": "8:55:40", "Volume": "7", "Speed": "53", "DetectorId":"1354"})

    batch.put_item(Item={"Location": "Johnson Cr NB", "Length": "1.89", "Date": "2011-09-15", "Time": "8:56:00", "Volume": "9", "Speed": "53", "DetectorId":"1354"})
    batch.put_item(Item={"Location": "Johnson Cr NB", "Length": "1.89", "Date": "2011-09-15", "Time": "8:56:20", "Volume": "6", "Speed": "57", "DetectorId":"1354"})
    batch.put_item(Item={"Location": "Johnson Cr NB", "Length": "1.89", "Date": "2011-09-15", "Time": "8:56:40", "Volume": "8", "Speed": "47", "DetectorId":"1354"})

    batch.put_item(Item={"Location": "Johnson Cr NB", "Length": "1.89", "Date": "2011-09-15", "Time": "8:55:00", "Volume": "4", "Speed": "59", "DetectorId":"1355"})
    batch.put_item(Item={"Location": "Johnson Cr NB", "Length": "1.89", "Date": "2011-09-15", "Time": "8:55:20", "Volume": "5", "Speed": "62", "DetectorId":"1355"})
    batch.put_item(Item={"Location": "Johnson Cr NB", "Length": "1.89", "Date": "2011-09-15", "Time": "8:55:40", "Volume": "5", "Speed": "65", "DetectorId":"1355"})

    batch.put_item(Item={"Location": "Johnson Cr NB", "Length": "1.89", "Date": "2011-09-15", "Time": "8:56:00", "Volume": "7", "Speed": "60", "DetectorId":"1355"})
    batch.put_item(Item={"Location": "Johnson Cr NB", "Length": "1.89", "Date": "2011-09-15", "Time": "8:56:20", "Volume": "4", "Speed": "67", "DetectorId":"1355"})
    batch.put_item(Item={"Location": "Johnson Cr NB", "Length": "1.89", "Date": "2011-09-15", "Time": "8:56:40", "Volume": "4", "Speed": "49", "DetectorId":"1355"})

    batch.put_item(Item={"Location": "Foster NB", "Length": "1.6", "Date": "2011-09-15", "Time": "8:55:00", "Volume": "8", "Speed": "24", "DetectorId":"1361"})
    batch.put_item(Item={"Location": "Foster NB", "Length": "1.6", "Date": "2011-09-15", "Time": "8:55:20", "Volume": "13", "Speed": "32", "DetectorId":"1361"})
    batch.put_item(Item={"Location": "Foster NB", "Length": "1.6", "Date": "2011-09-15", "Time": "8:55:40", "Volume": "10", "Speed": "24", "DetectorId":"1361"})

    batch.put_item(Item={"Location": "Foster NB", "Length": "1.6", "Date": "2011-09-15", "Time": "8:56:00", "Volume": "9", "Speed": "15", "DetectorId":"1361"})
    batch.put_item(Item={"Location": "Foster NB", "Length": "1.6", "Date": "2011-09-15", "Time": "8:56:20", "Volume": "8", "Speed": "19", "DetectorId":"1361"})
    batch.put_item(Item={"Location": "Foster NB", "Length": "1.6", "Date": "2011-09-15", "Time": "8:56:40", "Volume": "10", "Speed": "26", "DetectorId":"1361"})

print("items added to table")
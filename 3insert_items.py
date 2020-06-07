import boto3

# boto3 is the AWS SDK library for Python.
# The "resources" interface allow for a higher-level abstraction than the low-level client interface.
# More details here: http://boto3.readthedocs.io/en/latest/guide/resources.html
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('FreewayData')


# The BatchWriteItem API allows us to write multiple items to a table in one request.
with table.batch_writer() as batch:

    batch.put_item(Item={"Location": "Sunnyside NB", "Length": "0.94", "Date": "2011-09-15", "Time": "8:55:00", "Volume": "6", "Speed": "67", "DetectorId":"1345"})

    batch.put_item(Item={"Location": "Sunnyside NB", "Length": "0.94", "Date": "2011-09-15", "Time": "8:55:20", "Volume": "9", "Speed": "71","DetectorId":"1345"})

    batch.put_item(Item={"Location": "Sunnyside NB", "Length": "0.94", "Date": "2011-09-15", "Time": "8:55:40", "Volume": "5", "Speed": "79","DetectorId":"1345"})

    batch.put_item(Item={"Location": "Sunnyside NB", "Length": "0.94", "Date": "2011-09-15", "Time": "8:56:00", "Volume": "7", "Speed": "53", "DetectorId":"1345"})

    batch.put_item(Item={"Location": "Sunnyside NB", "Length": "0.94", "Date": "2011-09-15", "Time": "8:56:20", "Volume": "6", "Speed": "71", "DetectorId":"1345"})

    batch.put_item(Item={"Location": "Sunnyside NB", "Length": "0.94", "Date": "2011-09-15", "Time": "8:56:40", "Volume": "7", "Speed": "60", "DetectorId":"1345"})

    batch.put_item(Item={"Location": "Sunnyside NB", "Length": "0.94", "Date": "2011-09-15", "Time": "8:55:00", "Volume": "8", "Speed": "71", "DetectorId":"1346"})

    batch.put_item(Item={"Location": "Sunnyside NB", "Length": "0.94", "Date": "2011-09-15", "Time": "8:55:20", "Volume": "10", "Speed": "49", "DetectorId":"1346"})

    batch.put_item(Item={"Location": "Sunnyside NB", "Length": "0.94", "Date": "2011-09-15", "Time": "8:55:40", "Volume": "7", "Speed": "53", "DetectorId":"1346"})

    batch.put_item(Item={"Location": "Sunnyside NB", "Length": "0.94", "Date": "2011-09-15", "Time": "8:56:00", "Volume": "11", "Speed": "54", "DetectorId":"1346"})

    batch.put_item(Item={"Location": "Sunnyside NB", "Length": "0.94", "Date": "2011-09-15", "Time": "8:56:20", "Volume": "7", "Speed": "67", "DetectorId":"1346"})

    batch.put_item(Item={"Location": "Sunnyside NB", "Length": "0.94", "Date": "2011-09-15", "Time": "8:56:40", "Volume": "6", "Speed": "67", "DetectorId":"1346"})

    batch.put_item(Item={"Location": "Sunnyside NB", "Length": "0.94", "Date": "2011-09-15", "Time": "8:55:00", "Volume": "5", "Speed": "69", "DetectorId":"1347"})

    batch.put_item(Item={"Location": "Sunnyside NB", "Length": "0.94", "Date": "2011-09-15", "Time": "8:55:20", "Volume": "3", "Speed": "51", "DetectorId":"1347"})

    batch.put_item(Item={"Location": "Sunnyside NB", "Length": "0.94", "Date": "2011-09-15", "Time": "8:55:40", "Volume": "5", "Speed": "65", "DetectorId":"1347"})

    batch.put_item(Item={"Location": "Sunnyside NB", "Length": "0.94", "Date": "2011-09-15", "Time": "8:56:00", "Volume": "5", "Speed": "57", "DetectorId":"1347"})

    batch.put_item(Item={"Location": "Sunnyside NB", "Length": "0.94", "Date": "2011-09-15", "Time": "8:56:20", "Volume": "3", "Speed": "67", "DetectorId":"1347"})

    batch.put_item(Item={"Location": "Sunnyside NB", "Length": "0.94", "Date": "2011-09-15", "Time": "8:56:40", "Volume": "6", "Speed": "61", "DetectorId":"1347"})

    batch.put_item(Item={"Location": "Sunnyside NB", "Length": "0.94", "Date": "2011-09-15", "Time": "8:55:00", "Volume": "3", "Speed": "58", "DetectorId":"1348"})

    batch.put_item(Item={"Location": "Sunnyside NB", "Length": "0.94", "Date": "2011-09-15", "Time": "8:55:20", "Volume": "1", "Speed": "85", "DetectorId":"1348"})

    batch.put_item(Item={"Location": "Sunnyside NB", "Length": "0.94", "Date": "2011-09-15", "Time": "8:55:40", "Volume": "2", "Speed": "77", "DetectorId":"1348"})

    batch.put_item(Item={"Location": "Sunnyside NB", "Length": "0.94", "Date": "2011-09-15", "Time": "8:56:00", "Volume": "4", "Speed": "70", "DetectorId":"1348"})

    batch.put_item(Item={"Location": "Sunnyside NB", "Length": "0.94", "Date": "2011-09-15", "Time": "8:56:20", "Volume": "1", "Speed": "62", "DetectorId":"1348"})

    batch.put_item(Item={"Location": "Sunnyside NB", "Length": "0.94", "Date": "2011-09-15", "Time": "8:56:40", "Volume": "1", "Speed": "68", "DetectorId":"1348"})

print("batch items added")

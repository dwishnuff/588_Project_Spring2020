import boto3

# boto3 is the AWS SDK library for Python.
# The "resources" interface allow for a higher-level abstraction than the low-level client interface.
# More details here: http://boto3.readthedocs.io/en/latest/guide/resources.html
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('FreewayData')


# The BatchWriteItem API allows us to write multiple items to a table in one request.
with table.batch_writer() as batch:
    """"
    batch.put_item(Item={"Location": "Sunnyside NB", "Length": "0.94",
        "DayInfo": { "Date": "2011-09-15", "Time": {{"TimeStamp": "8:55", "Volume": "6", "Speed": "67"},{"TimeStamp": "8:55", "Volume": "9", "Speed": "71"},{"TimeStamp": "8:55", "Volume": "5", "Speed": "79" },{"TimeStamp": "8:56", "Volume": "7", "Speed": "53"}}}})
    """
    batch.put_item(Item={"Location": "Sunnyside NB", "Length": "0.94",
                         "DayInfo": {"Date": "2011-09-15", "Time": {"TimeStamp": "8:55", "Volume": "6", "Speed": "67"},
                                                                    }})


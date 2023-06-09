# AWS ptython Boto3

## The tutorial
- https://aws.amazon.com/developers/getting-started/python/

## Study of the s3_sample.py example


output:
```
>>> bucket_name = 'python-sdk-sample-{}'.format(uuid.uuid4())
>>> bucket_name
'python-sdk-sample-60fbf1a4-d87e-44a0-b16f-87bb61876575'
>>> print('Creating new bucket with name: {}'.format(bucket_name))
Creating new bucket with name: python-sdk-sample-60fbf1a4-d87e-44a0-b16f-87bb61876575
>>> s3client.create_bucket(Bucket=bucket_name)
{u'Location': '/python-sdk-sample-60fbf1a4-d87e-44a0-b16f-87bb61876575', 'ResponseMetadata': {'HTTPStatusCode': 200, 'RetryAttempts': 0, 'HostId': 'NCVmZkj8SXKTyrRGE4VwwbBE25DAzlOBRpz8V/GDxKDd8q6Ho2XSFUSQSAXZqohwNyu95F/Wplo=', 'RequestId': 'AD345B3F6D397693', 'HTTPHeaders': {'content-length': '0', 'x-amz-id-2': 'NCVmZkj8SXKTyrRGE4VwwbBE25DAzlOBRpz8V/GDxKDd8q6Ho2XSFUSQSAXZqohwNyu95F/Wplo=', 'server': 'AmazonS3', 'x-amz-request-id': 'AD345B3F6D397693', 'location': '/python-sdk-sample-60fbf1a4-d87e-44a0-b16f-87bb61876575', 'date': 'Sun, 05 Apr 2020 20:39:19 GMT'}}}
>>>

>>> list_buckets_resp['Buckets']
[{u'CreationDate': datetime.datetime(2020, 4, 5, 20, 39, 19, tzinfo=tzutc()), u'Name': 'python-sdk-sample-60fbf1a4-d87e-44a0-b16f-87bb61876575'}]
>>> list_buckets_resp['Owner']
{u'DisplayName': 'mayel.espino', u'ID': 'ea319f8845bb99eba5c99db35be083e24a2b2f646e3c8a28e8bd4b68b4c49d36'}


>>> list_buckets_resp['Owner']['DisplayName']
'mayel.espino'

>>> print('Uploading some data to {} with key: {}'.format(
...     bucket_name, object_key))
Uploading some data to python-sdk-sample-60fbf1a4-d87e-44a0-b16f-87bb61876575 with key: python_sample_key.txt


>>> s3client.put_object(Bucket=bucket_name, Key=object_key, Body=b'Hello World!')
{u'ETag': '"ed076287532e86365e841e92bfc50d8c"', 'ResponseMetadata': {'HTTPStatusCode': 200, 'RetryAttempts': 0, 'HostId': 'bx9naQX6/DDZefdWSigePGF9e9UsIemNpkFliEPf/U/Tdd+/juHUklDCSQlzAYD9PsaSQt1EM3g=', 'RequestId': 'A5DB613D40CAB1E0', 'HTTPHeaders': {'content-length': '0', 'x-amz-id-2': 'bx9naQX6/DDZefdWSigePGF9e9UsIemNpkFliEPf/U/Tdd+/juHUklDCSQlzAYD9PsaSQt1EM3g=', 'server': 'AmazonS3', 'x-amz-request-id': 'A5DB613D40CAB1E0', 'etag': '"ed076287532e86365e841e92bfc50d8c"', 'date': 'Sun, 05 Apr 2020 21:15:46 GMT'}}}
>>>

>>> url = s3client.generate_presigned_url(
...     'get_object', {'Bucket': bucket_name, 'Key': object_key})
>>>
>>> url
u'https://python-sdk-sample-60fbf1a4-d87e-44a0-b16f-87bb61876575.s3.amazonaws.com/python_sample_key.txt?AWSAccessKeyId=AKIAYVOYMTHS66DCH2CK&Expires=1586125142&Signature=pcrkk4nVhiVE%2FQw1cshDFMnoNG0%3D'


>>> s3resource = boto3.resource('s3')
>>>
>>> s3resource
s3.ServiceResource()
>>>

>>> bucket = s3resource.Bucket(bucket_name)
>>>
>>> bucket
s3.Bucket(name='python-sdk-sample-60fbf1a4-d87e-44a0-b16f-87bb61876575')


>>> object_key
'python_sample_key.txt'
>>>
>>> obj = bucket.Object(object_key)
>>>
>>> obj
s3.Object(bucket_name='python-sdk-sample-60fbf1a4-d87e-44a0-b16f-87bb61876575', key='python_sample_key.txt')
>>>

>>>
>>> print('Bucket name: {}'.format(bucket.name))
Bucket name: python-sdk-sample-60fbf1a4-d87e-44a0-b16f-87bb61876575
>>> print('Object key: {}'.format(obj.key))
Object key: python_sample_key.txt
>>> print('Object content length: {}'.format(obj.content_length))
Object content length: 12
>>> print('Object body: {}'.format(obj.get()['Body'].read()))
Object body: Hello World!
>>> print('Object last modified: {}'.format(obj.last_modified))
Object last modified: 2020-04-05 21:15:46+00:00
>>>

>>> delete_responses = bucket.objects.delete()
>>> delete_responses
[{u'Deleted': [{u'Key': 'python_sample_key.txt'}], 'ResponseMetadata': {'HTTPStatusCode': 200, 'RetryAttempts': 0, 'HostId': 'B7OXjvw5/2o+9Qvfc20Ms/aJqeWeoaXxhdQQ3NJHbr22Ep5uxafjpYHmgT4Wh99RyGU2uEG1+Uw=', 'RequestId': '2EE39948A1F08A82', 'HTTPHeaders': {'x-amz-id-2': 'B7OXjvw5/2o+9Qvfc20Ms/aJqeWeoaXxhdQQ3NJHbr22Ep5uxafjpYHmgT4Wh99RyGU2uEG1+Uw=', 'server': 'AmazonS3', 'transfer-encoding': 'chunked', 'connection': 'close', 'x-amz-request-id': '2EE39948A1F08A82', 'date': 'Sun, 05 Apr 2020 21:25:43 GMT', 'content-type': 'application/xml'}}}]


>>> for delete_response in delete_responses:
...     for deleted in delete_response['Deleted']:
...         print('\t Deleted: {}'.format(deleted['Key']))
...
	 Deleted: python_sample_key.txt
>>>

>>> bucket.delete()
{'ResponseMetadata': {'HTTPStatusCode': 204, 'RetryAttempts': 0, 'HostId': 'qXySYJH75zCw3BvsaWEZHWCE6yblbPSV1vXtUU7uT19i8ysvJXLSlO60GDADv6unOU6FYuVL6Us=', 'RequestId': '7417E43B4C66A51A', 'HTTPHeaders': {'x-amz-id-2': 'qXySYJH75zCw3BvsaWEZHWCE6yblbPSV1vXtUU7uT19i8ysvJXLSlO60GDADv6unOU6FYuVL6Us=', 'date': 'Sun, 05 Apr 2020 21:28:01 GMT', 'x-amz-request-id': '7417E43B4C66A51A', 'server': 'AmazonS3'}}}
>>>

```

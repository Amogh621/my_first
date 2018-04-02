import json
from pprint import pprint

bucket = json.load(open('data.json'))['Records'][0]['s3']['bucket']['name']

etag = json.load(open('data.json'))['Records'][0]['s3']['object']['eTag']

pprint("name of the bucket:"+bucket)

pprint("eTag"+etag)

            




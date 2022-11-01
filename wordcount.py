import boto3
s3_client = boto3.client('s3')

mock_event = {
    "Records": [{
        "s3": {
            "bucket": {
                "name": "example-bucket",
            },
            "object": {
                "key": "test%2Fkey",
                "size": 1024,
            }
        }
    }]
}

def get_bucket_name(event):
    return event["Records"][0]['s3']['bucket']['name']

def get_object_name(event):
    return event["Records"][0]['s3']['object']['key']

def get_object_size(event):
    return event["Records"][0]['s3']['object']['size']

def wordcount(filedata):
    words = filedata.split()
    num_words = len(words)
    return num_words

def lambda_handler(event, context):
    print(f"Bucket: {get_bucket_name(event)}")
    print(f"Filename: {get_object_name(event)}")
    print(f"File Size: {get_object_size(event)}")
    file_name = get_object_name(event)
    fixed_file_name = file_name.replace('/', '-')
    bucket_name = get_bucket_name(event)
    download_path = f"/tmp/{fixed_file_name}"
    s3_client.download_file(bucket_name, file_name, download_path)
    with open(download_path, encoding="utf8") as f:
        filedata = f.read()
        num_words = wordcount(filedata)
        print(num_words)
    return f"The word count in the file {download_path} is {num_words}."

"""if __name__ == "__main__":
    test = wordcount("HelloWorld Accurate COunt")
    print(test)

    with open("book.txt", encoding="utf8") as f:
        filedata = f.read()
        num_words = wordcount(filedata)
        print(num_words)
"""
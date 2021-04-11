import boto3
import config

client = boto3.client('rekognition',
        aws_access_key_id = config.aws_access_key_id,
        aws_secret_access_key = config.aws_secret_access_key,
        region_name=config.region_name
    )

def eyes_are_closed(bin_img):
   
    response = client.detect_faces(
        Image={
            'Bytes': bin_img
        },
        Attributes=[
            'ALL',
        ]
    )
    if len(response['FaceDetails'])<=0:
      return False
    firstFace = response['FaceDetails'][0] #only looks at the first face
    return not firstFace['EyesOpen']['Value']

with open("eyes_open.jpg", "rb") as image:
  f = image.read()
print(eyes_are_closed(f))

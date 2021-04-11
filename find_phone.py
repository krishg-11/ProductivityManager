import boto3
import config

client=boto3.client('rekognition',
                      aws_access_key_id=config.aws_access_key_id,
                      aws_secret_access_key=config.aws_secret_access_key,
                      region_name=config.region_name)
                      
def find_phone(bin_img):
  response = client.detect_labels(Image={'Bytes': bin_img}, MaxLabels=10)

  for label in response['Labels']:
    #print ("Label: " + label['Name'])
    if("PHONE" in label['Name'].upper()): 
      return True
    #print("------------------------------------------------------------")
      # print ("Confidence: " + str(label['Confidence']))
      # print ("Instances:")
      # for instance in label['Instances']:
      #     print ("  Bounding box")
      #     print ("    Top: " + str(instance['BoundingBox']['Top']))
      #     print ("    Left: " + str(instance['BoundingBox']['Left']))
      #     print ("    Width: " +  str(instance['BoundingBox']['Width']))
      #     print ("    Height: " +  str(instance['BoundingBox']['Height']))
      #     print ("  Confidence: " + str(instance['Confidence']))

  return False

# with open("phon.JPG", "rb") as image:
#   f = image.read()
# print(find_phone(f))


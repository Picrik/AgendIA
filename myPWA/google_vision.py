import json

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision

    import io
    from google.oauth2.service_account import Credentials
    with open(r'myPWA\google_api_key\hackathon-triplea-key.json') as f:
        info = json.load(f)

    vision_credentials = Credentials.from_service_account_info(info)
    client = vision.ImageAnnotatorClient(credentials=vision_credentials)

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')


    full_text = texts[0].description.replace('\n',' ')

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return full_text


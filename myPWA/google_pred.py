import json
from PIL import Image
from google.cloud import automl
from google.oauth2.service_account import Credentials
from .crop_img import crop_img_elmts
from .google_vision import detect_text
from os import remove

with open(r'myPWA\google_api_key\hackathon-triplea-key.json') as f:
    info = json.load(f)


class VisionConnection:

    def __init__(self, info):
        vision_credentials = Credentials.from_service_account_info(info)

        # TODO(developer): Uncomment and set the following variables
        self.project_id = "hackathon-triplea"
        self.ocr_model_id = "IOD1463786427127955456"
        # file_path = r"img/System-Of-A-Down-Affiche-Tour-2011-06-Juin-Paris-Bercy.jpg"
        self.file_path = r"img/unnamed.jpg"
        self.params = {"score_threshold": "0.8"}
        self.prediction_client = automl.PredictionServiceClient(credentials=vision_credentials)

        # Get the full path of the model.
        self.model_full_id = automl.AutoMlClient.model_path(
            self.project_id, "us-central1", self.ocr_model_id
        )

    def load_image(self, file_path):
        # Read the file.
        with open(file_path, "rb") as content_file:
            content = content_file.read()
            image = automl.Image(image_bytes=content)
            self.payload = automl.ExamplePayload(image=image)

    def vision_request(self):
        request = automl.PredictRequest(
            name=self.model_full_id,
            payload=self.payload,
            params=self.params
        )
        return self.prediction_client.predict(request=request)


def text_extractor(response, file_path):
    image = Image.open(file_path)
    dict_rez = dict()

    for result in response.payload:
        n = 0
        print("Predicted class name: {}".format(result.display_name))
        print("Predicted class score: {}".format(result.image_object_detection.bounding_box))
        test = str(result.image_object_detection.bounding_box).replace('\n', '').replace('x', '"x"').replace('y',
                                                                                                             ',"y"').replace(
            'normalized_vertices', '').split('}')
        test = [i + '}' for i in test]
        test.pop(2)
        coord1 = json.loads(test[0])
        coord2 = json.loads(test[1])
        tag = ("topic", "date")[result.annotation_spec_id == '8917728695053975552']

        name_fic_elem = crop_img_elmts(coord1, coord2, image, tag, n, file_path.split(sep='\\')[::-1][0])

        ocr_result = detect_text(name_fic_elem)
        remove(name_fic_elem)
        dict_rez[tag] = dict_rez.get(tag, "") + " " + ocr_result
        n += 1

    return dict_rez


def process_photo(file_path):
    connection = VisionConnection(info)
    connection.load_image(file_path)
    response = connection.vision_request()
    res = text_extractor(response, file_path)
    print(res)
    return res

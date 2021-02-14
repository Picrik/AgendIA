import cv2
import numpy as np
from pyzbar.pyzbar import decode
import re
import webbrowser

def get_data():
    print("Hello world 3")

def scan_qr():
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    while True:
        sucess, img = cap.read()
        for barcode in decode(img):
            myData= barcode.data.decode('utf-8')
            print(myData)
            regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
            url = re.findall(regex, myData)
            if url != "" and regex != "":
                if input("Voulez-vous ouvrir le lien de l'évènement ? ") == "Oui":  #Bouton pour répondre sur l'apps
                    webbrowser.open(url[0][0])  # Go to example.com
                    print("url", url[0][0])
                    cv2.waitKey(0)
                    break
                else:
                    break
            pts = np.array([barcode.polygon], np.int32)
            pts = pts.reshape(-1, 1, 2)
            cv2.polylines(img, [pts], True,(255,0,255), 5)
            pts2 = barcode.rect
            cv2.putText(img, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,255), 2)
        cv2.imshow('Result',img)
        cv2.waitKey(1)
    cv2.destroyAllWindows()

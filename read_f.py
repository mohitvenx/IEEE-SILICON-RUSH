import cv2
import pytesseract
import pandas as pd
from PIL import Image
import pytesseract
def read(img_path):
        img = Image.open(img_path)
        ocr_result = pytesseract.image_to_string(img)
        a = print(ocr_result)
        with open(r"./test_10.docx",'w') as f:
                print(ocr_result,file=f)
        with open(r"./test_10.csv.xls",'w') as f:
                print(ocr_result,file=f)
        ##  print(ocr_result, file=f)
        result = {'final': a}
        a = pd.read_csv("./test_10.docx")
        a.to_html("./Table10.html")
        b = a.to_html()
        return a,b


#/Users/nitishvirupakshareddy/PycharmProjects/OpencvPython/Resources/IEEE-SILICON-RUSH/test_7.docx

from csv import reader
import matplotlib.pyplot as plt
import cv2
import easyocr
from pylab import rcParams
rcParams['figure.figsize']= 8,16

reader = easyocr.Reader(['en'])
from PIL import Image
bounds = reader.readtext("D:\\IEEE-SILICON-RUSH\\labrep2_hack_crop.png")
with open(r"D:\\IEEE-SILICON-RUSH\\bounds.docx", 'w') as f:
    print(bounds, file=f)


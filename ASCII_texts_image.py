from PIL import Image, ImageDraw, ImageFont
import cv2 
import math
import numpy as np
import imutils
chars = "`.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"#[::-1]
# chars = "#Wo- "[::-1]
charArray = list(chars)
charLength = len(charArray)
interval = charLength/256

scaleFactor = 0.09

oneCharWidth = 10
oneCharHeight = 18

def getChar(inputInt):
    return charArray[math.floor(inputInt*interval)]

# text_file = open("Output.txt", "w")
cap = cv2.VideoCapture(1)
try:
    while True:
            ret,im = cap.read(0)
            # im = cv2.cvtColor(im , cv2.COLOR_BGR2GRAY)
            im = imutils.resize(im,width=500,height=300)
            im = Image.fromarray(im).convert('RGB')
            
            fnt = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)
            
            width, height = im.size
            im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), Image.NEAREST)
            width, height = im.size
            pix = im.load()
            
            outputImage = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color = (0, 0, 0))
            d = ImageDraw.Draw(outputImage)
            
            for i in range(height):
                for j in range(width):
                    r, g, b = pix[j, i]
                    h = int((r+g+b)/3)
                    pix[j, i] = h
                    # text_file.write(getChar(h))
                    d.text((j*oneCharWidth, i*oneCharHeight), getChar(h), font = fnt, fill = (r, g, b))
            
                # text_file.write('\n')
            
            # outputImage.save('output.png')
            img = np.array(outputImage)
            cv2.imshow("frame",img)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
except:
    print("What")
cap.release()
cv2.destroyAllWindows()
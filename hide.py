import sys
import numpy as np
import cv2

class Hide:
    def __init__(self):
        pass

    def readFile(self, fileName):
        with open(fileName, "r+") as f:
            fileString = f.read()
            f.close
        return fileString

    def getBinarySet(self, num):
        binaryNumber = bin(num)
        setBits = binaryNumber[2:]
        return setBits
        
    def validateMsgImg(self, msg, imgDimension): #verify the size of msg and img
        imgSize = imgDimension * 3 #Each pixel storage 3 bytes (RGB values)
        countAllBinary = 0
        for c in msg:
            binarySet = self.getBinarySet(ord(c))
            countAllBinary = countAllBinary + len(binarySet)
        return countAllBinary < imgSize
        
    def replaceMultiple(self, text, listString, newString):
        for s in listString:
            text = text.replace(s, newString)
        return text
            
    def showImg(self, img):
        cv2.imshow('imag', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def saveImage(self, name, img):
        cv2.imwrite('./imageResult/'+ name,img)

    def steganography(self, msgFile, imgFile):
        img = cv2.imread(imgFile)
        msg = self.readFile(msgFile)
        msg = self.replaceMultiple(msg, ["\n", "\t"], "")
        binarySetMsg_ = ""
        for c in msg:
            binaryOfChar = self.getBinarySet(ord(c)).zfill(8)
            binarySetMsg_ = binarySetMsg_ + binaryOfChar
        binarySetMsg_ = binarySetMsg_ + "00000011"
        if not(self.validateMsgImg(msg, img.size)):
            print("Impossível ocultar mensagem. \nVerifique o tamanho da mensagem e da imagem!")
        else:
            self.toHide(binarySetMsg_, img)
            self.showImg(img)
            self.saveImage(imgFile, img)

    def toHide(self, binaryMsg, img):
        rows, columns, channels = img.shape
        countBit = 0
        stop = False
        for r in range(rows):
            for c in range(columns):
                for channel in range(channels):
                    if countBit == len(binaryMsg):
                        stop = True
                        break
                    currentValue = img[r][c][channel]
                    binaryCurrentValue = self.getBinarySet(currentValue)
                    binaryNewValue = binaryCurrentValue[:-1] 
                    binaryNewValue = binaryNewValue + binaryMsg[countBit] #Chang the last bit to the next bit from message
                    countBit = countBit + 1
                    newValue = int(binaryNewValue, 2) #Convert binary to decimal
                    img.itemset((r, c, channel), newValue)
                if stop:
                    break
            if stop:
                break

def main():
    textFile = sys.argv[1]
    imgFile = sys.argv[2]
    steg = Hide()
    steg.steganography(textFile, imgFile)

if __name__ == '__main__':
    main()
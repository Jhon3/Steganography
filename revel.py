import sys
import cv2

class Revel:
    def __init__(self):
        pass

    def saveFile(self, msg):
            with open('./textResult/result.txt', 'w') as f:
                f.write(msg)
                f.close

    def getMsg(self, binarySet):
        msg = ""
        bytes_ = [binarySet[i:i+8] for i in range(0, len(binarySet), 8)]
        for b in bytes_:
            codeascii = int(b, 2)
            msg = msg + str(chr(codeascii))
        return  msg
    
    def getBinarySet(self, num):
        binaryNumber = bin(num)
        setBits = binaryNumber[2:]
        return setBits

    def discover(self, imgFile):
        img =  cv2.imread(imgFile)
        rows, columns, channels = img.shape
        bitSetMsg = ""
        binaryChar = ""
        stop = False
        
        for r in range(rows):
            for c in range(columns):
                for channel in range(channels):
                    currentValue = img[r][c][channel]
                    binaryCurrentValue = self.getBinarySet(currentValue)
                    binaryChar = binaryChar + binaryCurrentValue[-1]
                    if (len(binaryChar) == 8):
                        if(binaryChar == "00000011"):
                            stop = True
                        else:
                            bitSetMsg = bitSetMsg + binaryChar
                            binaryChar = ""
                if stop:
                    break
            if stop:
                break
        originalMsg = self.getMsg(bitSetMsg)
        print(originalMsg)
        self.saveFile(originalMsg)
    
def main():
    imgFile = sys.argv[1]
    #hide_ = sys.argv[2].lower() == 'true'
    steg = Revel()
    steg.discover(imgFile)

if __name__ == '__main__':
    main()
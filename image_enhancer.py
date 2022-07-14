# Your imports here
import os
import cv2
import numpy as np
from PIL import ImageOps, Image




class ImageEnhancer:
    def __init__(self):
        self.count1 = 1
        self.count2 = 1

    def ChangeCOLOR(self,image):   

        alpha = 1.85 # Contrast control (1.0-3.0)
        beta = 0 # Brightness control (0-100)
        manual_result = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

        # text
        cv2.putText(manual_result,'after', (17,28), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, lineType=cv2.LINE_AA)
        cv2.putText(image,'before', (17,28), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, lineType=cv2.LINE_AA)

        # Stacking the original image with the enhanced image (before/after)
        result = np.hstack((image, manual_result))

        return result, manual_result


    def readIMG(self,path,show=True,SingResults=False):
        #1.read image
        Path = f"./data/{path}"
        self.image = cv2.imread(Path)

        #2.change color
        result, single_result = self.ChangeCOLOR(self.image)

        #3.make folder to save results
        if not os.path.exists('Results'):
            os.mkdir('Results')
        if not os.path.exists('Single-Results-Gray'):
            os.mkdir('Single-Results-Gray')

        #4.save image
        if SingResults:
            #save for gray image
            cv2.imwrite(os.path.join('Single-Results-Gray',f'Single_img_Gray_{self.count1}.jpg'), single_result)

        #5.show image
        if show:
            # save for RGB image
            cv2.imwrite(os.path.join('Results',f'Images_{self.count1}.jpg'), result)   
            cv2.imshow("Result", result)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        self.count1 += 1

class ImageEnhancerGray(ImageEnhancer):
    def __init__(self):
        self.count1 = 1
        self.count2 = 1   

    def readIMG_Gray(self,path):
        self.readIMG(path,show=False,SingResults=True)

        single_img = Image.open(f'./Single-Results-Gray/Single_img_Gray_{self.count2}.jpg')     

        single_img = ImageOps.autocontrast(single_img, cutoff=40)
        result = np.hstack((self.image,single_img))     
        result = cv2.resize(result, (0,0), fx=0.9, fy=0.9)
        
        cv2.imwrite(os.path.join('Results',f'Gray_images_{self.count2}.jpg'), result)     
        self.count2 += 1

        cv2.imshow("Result", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()









    '''
    Image operations for rgb images
    Methods:
        - Read image
        - Change Brightness/Contrast/Color
        - Show image
        - Save image
    '''
    '''
    ImageEnhancer methods and properties + Auto-contrast for gray images
    Method:
        - Pillow Auto-contrast
    '''
   

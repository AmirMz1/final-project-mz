from image_enhancer import ImageEnhancer
from image_enhancer import ImageEnhancerGray
import pandas as pd
import shutil

ImageEnhancer = ImageEnhancer()
ImageEnhancerGray = ImageEnhancerGray()


df = pd.read_csv('./data/info.csv')
print(df,'\n\n')

for index, row in df.iterrows():
    if row['img_mode'] == 'rgb':
        ImageEnhancer.readIMG(row['filename'])
    else: # so is gray
        ImageEnhancerGray.readIMG_Gray(row['filename']) 

shutil.rmtree('./Single-Results-Gray') # Remove Single-Result folder, it's for gray image - not useful
print('Result saved successfully..!')



# Your imports here


# Read info file (csv or xlsx) # doen *
# Read images # done *
# Check image mode from info file # done *

# if mode=='rgb'  --> Use ImageEnhancer class to change brightness/contrast # done *
# if mode=='gray' --> Use ImageEnhancerGray class to auto contrast # done *
# Show images and results side by side (before/after) # done *
# Save results in a separate folder (results) # done *

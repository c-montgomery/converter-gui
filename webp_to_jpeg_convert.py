from PIL import Image
import os
from tkinter import *

im = os.listdir('C:\\Users\\craym\\Pictures')
for item in im:
	try:
		if str(item).endswith('.webp'):
			filename = item[:-5]
			
			im_final =Image.open('C:\\Users\\craym\\Pictures\\' + item)
			
			im_final.save('C:\\Users\\craym\\Pictures\\Wallpapers\\' + filename + '.jpg', format = 'PNG')
	except OSError:
		print('error')
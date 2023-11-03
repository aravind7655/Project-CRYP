from PIL import Image
import os
#image = Image.open('demo_image.jpg')

#image = Image.open('Columnaris/1.jpg')
#new_image = image.resize((400, 400))
#new_image.save('train/Columnaris/1.jpg')

#print(image.size) # Output: (1920, 1280)
#print(new_image.size) # Output: (400, 400)


f = './input-leaf/Virus/'
for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    img = img.resize((600,600))
    #new_image.save('train/Columnaris/1.jpg')
    img.save(f_img)
    #print(f_img.size) # Output: (400, 400)

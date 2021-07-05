from PIL import Image, ImageFilter

img = Image.open('./pikachu.jpg')
blurf_img=img.filter(ImageFilter.BLUR)
blurf_img.save('blur.png','png')

sharpf_img=img.filter(ImageFilter.SHARPEN)
sharpf_img.save('sharp.png','png')

smoothf_img=img.filter(ImageFilter.SMOOTH)
smoothf_img.save('smooth.png','png')

img = Image.open('./pikachu.jpg')
c_img=img.convert('L')
c_img.save('grey.png','png')

resize=img.resize((300,300))
resize.save('resize.png','png')

rs=(100,100,400,400)
crp=img.crop(rs)
crp.save('crop.png','png')
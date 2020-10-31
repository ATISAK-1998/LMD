from PIL import Image

im = input("กรุณาใส่รายการที่คุณต้องการ : ")

def ss_p(im):
    if im == str("1"):

        image1 = Image.open(r"C:\Users\A_ATISAK\Desktop\Python for Project\Image\logo_1.png")
        #image1.show()
        out = image1.resize((300, 300))
        out.show()

    elif im == str("2"):

        image2 = Image.open(r"C:\Users\A_ATISAK\Desktop\Python for Project\Image\logo_2.png.png")
        image2.show()

x=ss_p(im)

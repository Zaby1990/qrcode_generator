import qrcode
from PIL import Image


def make_plain_qrcode(text, pic_type="png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # 30% errors can be corrected
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    if pic_type == "png":
        pic = qr.make_image(
            back_color=(255, 255, 255),  # background-color
            fill_color=(0, 0, 0),       # frontcolor
        )
    elif pic_type == "svg":
        pass
    else:
        pass

    return pic


def combine_pictures(foreground, background):
    width_back, height_back = background.size
    width_fore, height_fore = int(width_back / 2), int(height_back / 2)
    size_fore = width_fore, height_fore
    im.thumbnail(size_fore, Image.ANTIALIAS)
    # offset_x = int(max((size_fore[0] - im.size[0]) / 2, 0))
    # offset_y = int(max((size_fore[1] - im.size[1]) / 2, 0))
    # offset_tuple = (offset_x, offset_y) #pack x and y into a tuple
    # new_im = Image.new(mode='RGBA', size=size_fore, color=(255, 255, 255, 0))
    
    new_im.paste(im, offset_tuple,im)

    pos_fore = int(width_back / 2) - int(width_fore / 2) + \
        10, int(height_back / 2) - int(height_fore / 2) + 10

    pic = plainqr.paste(im, pos_fore, im)
    return pic

if __name__ == "__main__":
    url = "https://www.sk-oelsnitz.de/"
    plainqr = make_plain_qrcode(url)
    img = "../nur Sperk.png"
    im = Image.open(img)
    combine_pictures(im, plainqr)

    plainqr.show()

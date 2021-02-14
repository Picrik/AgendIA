from PIL import Image
from os import remove

def get_photo_elem(pt1, pt2, image):
    width, height = image.size
    left = pt1['x'] * width
    top = pt1['y'] * height
    right = pt2['x'] * width
    bottom = pt2['y'] * height
    area_contain_photo = image.crop([left, top, right, bottom])
    return area_contain_photo

def crop_img_elmts(coord1, coord2, image, tag, n, name):
    img_t_cook = get_photo_elem(coord1, coord2, image)
    name_fic_elem = r"tmp_upload/elem_" + tag + "_" + str(n) + "_" + str(
        image.size) + "_" + name
    img_t_cook.save(name_fic_elem)

    return name_fic_elem


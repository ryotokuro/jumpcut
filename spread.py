from PIL import Image

def spread(r, l, type):
    RPAGE_PATH = 'output/' + r + '.' + type
    LPAGE_PATH = 'output/' + l + '.' + type
    imR = Image.open(RPAGE_PATH)
    imL = Image.open(LPAGE_PATH)

    (PAGE_WIDTH, PAGE_HEIGHT) = (imR.size[0], imR.size[1])

    new_im = Image.new('RGB', (PAGE_WIDTH*2, PAGE_HEIGHT))
    new_im.paste(imL)
    new_im.paste(imR, (PAGE_WIDTH, 0, PAGE_WIDTH*2, PAGE_HEIGHT))

    new_im.save('output/spread.' + type)
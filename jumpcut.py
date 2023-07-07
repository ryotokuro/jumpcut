# Import required libraries
from PIL import Image
import glob

def jumpcut(filename, type):
    # Set input path
    PATH = 'input/' + filename + '.' + type

    # Get dimensions
    TOTAL_WIDTH = TOTAL_HEIGHT = 0
    with Image.open(PATH) as im:
        (TOTAL_WIDTH, TOTAL_HEIGHT) = (im.size[0], im.size[1])

    (COL_WIDTH, ROW_HEIGHT) = (200, 296)

    for col in range(4):
        # Set crop coordinates
        (left, right) = (COL_WIDTH*col, COL_WIDTH*col + COL_WIDTH)
        (upper, lower) = (0, ROW_HEIGHT)

        for row in range(4):
            # Open original scrambled image
            im = Image.open(PATH)

            # Crop image
            snippet = im.crop((left, upper, right, lower))

            # Save to output path
            path = 'transform/(' + str(col) + ',' + str(row) + ').' + type
            snippet.save(path)

            # Shift crop window down
            upper = lower
            lower = ROW_HEIGHT*(row+2)

    # Open all segments and store in list
    image_list = []
    for file in glob.glob('transform/*.' + type):
        im = Image.open(file)
        image_list.append(im)

    # Define new image canvas
    new_im = Image.new('RGB', (TOTAL_WIDTH, TOTAL_HEIGHT))

    # Paste segments to form new image
    x_offset = y_offset = 0
    i = 1
    for row in range(1, 5):
        for col in range(1, 5):
            im = image_list[i-1]
            new_im.paste(im, (x_offset, y_offset))

            # If a factor of 4, shift to next row
            if i % 4 == 0:
                x_offset = 0
                y_offset += 296
            else:    
                x_offset += im.size[0]

            i += 1

    # Add end-pieces
    with Image.open(PATH) as im:
        MERGED_WIDTH = COL_WIDTH*4
        MERGED_HEIGHT = ROW_HEIGHT*4

        # Append right section
        section = (MERGED_WIDTH, 0, TOTAL_WIDTH, TOTAL_HEIGHT)
        right_slice = im.crop(section)
        new_im.paste(right_slice, section)

        # Append bottom section
        section = (0, MERGED_HEIGHT, MERGED_WIDTH, TOTAL_HEIGHT)
        bottom_slice = im.crop(section)
        new_im.paste(bottom_slice, section)

    # Save to output folder
    new_im.save('output/' + filename + '.' + type)
import sys
import argparse
from yolo import YOLO, detect_video
from PIL import Image
import pdb

def detect_img(yolo):
    while True:
        img = input('Input image filename:')
        try:
            image = Image.open(img)
        except:
            print('Open Error! Try again!')
            continue
        else:
            r_image = yolo.detect_image(image)
            r_image.show()
    yolo.close_session()

FLAGS = None

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--model_path', type=str,
        help='path to model weight file, default ' + YOLO.get_defaults("model_path"),
		default='model_data/trained_weights_final.h5'
    )
    FLAGS = parser.parse_args()
    detect_img(YOLO(**vars(FLAGS)))

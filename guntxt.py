import cv2
import numpy as np
import os
def parse_txt_annotation(ann_dir, img_dir):
    all_insts = []
    labels = {'gun': 0}

    for ann in sorted(os.listdir(ann_dir)):
        img = {'object':[]}

        with open(ann_dir + ann, 'r') as f:
            img['filename'] = img_dir + ann[:-4] + ".jpg"
            image = cv2.imread(img['filename'], cv2.IMREAD_UNCHANGED)
            img['width'] = image.shape[1]
            img['height'] = image.shape[0]

            try:
                n = int(f.readline())
            except Exception:
                # No gun, just record image attribute
                all_insts.append(img)
            else:
                # Has gun(s), record image attribute and bounding boxes
                for _ in range(n):
                    xmin, ymin, xmax, ymax = map(int, f.readline().split(' '))
                    obj = {
                        "xmin": xmin,
                        "ymin": ymin,
                        "xmax": xmax,
                        "ymax": ymax,
                        "name": "gun"
                    }
                    labels['gun'] += 1
                    img['object'].append(obj)
                all_insts.append(img)
    
    return all_insts, labels
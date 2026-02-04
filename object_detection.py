#!/usr/bin/env python


from typing import List

class CocoBoundingBox(object):
    """A bounding box for an object in the COCO format.

    Arguments:
        cls: int
            The object's class
        conf: float
            The confidence in the object's class (between 0 and 1)
        x_min: int
            The bounding box's lowest x-coordinate
        y_min: int
            The bounding box's lowest y-coordinate
        width: int
            The bounding box's width in pixels
        height: int
            The bounding box's height in pixels
    """

    def __init__(self,
                 cls: int,
                 conf: float,
                 x_min: int,
                 y_min: int,
                 width: int,
                 height: int):
        self.cls = cls
        self.conf = conf
        self.x_min = x_min
        self.y_min = y_min
        self.width = width
        self.height = height


def coco2yolo(bbox: CocoBoundingBox, img_w: int, img_h: int) -> List[float]:
    """Take a CocoBoundingBox object and return an array of bounding box
    coordinates in the YOLO format.

    Arguments:
        bbox: CocoBoundingBox
            Input bounding box
        img_w: int
            Image width in pixels
        img_h: int
            Image height in pixels
        
    Returns:
        List[float]: Yolo bounding box in the format
        [center x, center y, width, height], where all values are given as
        fractions of the total width or height of the image
    """
    x_cntr = (bbox.x_min + bbox.width / 2) / img_w
    y_cntr = (bbox.y_min + bbox.height / 2) / img_h
    width = bbox.width / img_w
    height = bbox.height / img_h
    return [x_cntr, y_cntr, width, height]

def iou(bbox1: CocoBoundingBox, bbox2: CocoBoundingBox) -> float:
    """Calculate the intersect over union (IoU) between two bounding boxes.
    
    Arguments:
        bbox1: CocoBoundingBox
            Bounding Box 1
        bbox2: CocoBoundingBox
            Bounding Box 2

    Returns:
        Float: IoU between bbox1 and bbox2
    """
    x_overlap = min(
        max(bbox1.x_min + bbox1.width - bbox2.x_min, 0),
        max(bbox2.x_min + bbox2.width - bbox1.x_min, 0))
    y_overlap = min(
        max(bbox1.y_min + bbox1.height - bbox2.y_min, 0),
        max(bbox2.y_min + bbox2.height - bbox1.y_min, 0))
    union = x_overlap * y_overlap
    if union == 0:
        return 0
    intersect = bbox1.width * bbox1.height + bbox2.width * bbox2.height - union
    return intersect / union


def nms(bboxes: List[CocoBoundingBox], thresh: float) -> List[CocoBoundingBox]:
    """Perform non-maximum suppression on a list of bounding boxes.  I.e.,
    overlapping bounding boxes will be discarded.
    
    Arguments:
        bboxes: List[CocoBoundingBox]
            List of bounding boxes to perform non-maximum suppression on
        thresh: float
            IoU threshold for dropping duplicate boxes
    
    Returns:
        List[CocoBoundingBox]: List of non-suppressed bounding boxes
    """
    bboxes.sort(key=lambda x: x.conf)
    filtered = []
    while len(bboxes) > 0:
        filtered.append(bboxes.pop())
        remaining = []
        for bbox in enumerate(bboxes):
            if iou(bbox, filtered[-1]) < thresh:
                remaining.append(bbox)
        bboxes = remaining
    return filtered


def mean_average_precision(predicted: List[List[CocoBoundingBox]],
                           ground_truth: List[List[CocoBoundingBox]],
                           thresh: float) -> float:
        """Return the mean average precision of a set of predicted bounding
        boxes on a list of images against a set of ground truth bounding boxes
        on the same list of images.
        
        Arguments:
            predicted: List[List[CocoBoundingBox]]
                List of lists of detected bounding boxes where each element in
                the outer list corresponds to the predicted detections on a
                unique image
            ground_truth: List[List[CocoBoundingBox]]
                List of lists of detected bounding boxes where each element in
                the outer list corresponds to the ground truth detections on a
                unique image
            thresh: float
                IoU threshold for detection

        Returns:
            float: the mean average precision of the predicted bounding boxes,
            i.e., the #true positives / (#true positives + #false positives)
            averaged across all confidence thresholds at a given IoU and across
            all classes in the dataset
        """
        gt_cls = {}
        for idx, img in enumerate(ground_truth):
            for bbox in img:
                if bbox.cls not in gt_cls:
                    gt_cls[bbox.cls] = [[]] * (idx + 1)
                gt_cls[bbox.cls][idx].append(bbox)
        
        wtd_avg_prec = []
        for cls in gt_cls:
            conf_ts = set([c for c in i.conf for i in predicted])
            prec = []
            for conf in conf_ts:
                tp = 0
                fp = 0
                for img, gt in zip(predicted, cls):
                    for pred_bbox in img:
                        if pred_bbox.conf >= conf and pred_bbox.cls == cls:
                            match = False
                            for gt_bbox in gt:
                                if iou(gt_bbox, pred_bbox) >= thresh:
                                    match = True
                                    break
                            tp += match
                            fp += not match
                prec.append(tp / (tp + fp))
            cls_weight = sum([len(bxs) for bxs in gt_cls[cls]]) / \
                sum([sum([len(bxs) for bxs in gt_cls[c]]) for c in gt_cls])
            wtd_avg_prec.append( cls_weight * sum(prec) / len(prec))
        return sum(wtd_avg_prec)


if __name__ == '__main__':
    bbox = CocoBoundingBox(1, 0.8, 100, 200, 300, 400)

    # Problem 1:
    # Write a function that takes a bounding box object in the COCO bounding
    # box format and returns an array in the YOLO bounding box format, i.e.,
    # a list in the format [center x, center y, width, height] where all
    # values are given as fractions of the total width or height of the image.
    print('Problem #1:\n{}'.format(coco2yolo(bbox, 640, 480)))

    # Problem 2:
    # Write a function that calculates the intersect over union (IoU) for two
    # bounding boxes.
    print('Problem #2:\n{}'.format())

    # Problem 3:
    # Write a function that calculates that performs non-maximum supression
    # on a list of bounding boxes.
    print('Problem #3:\n{}'.format())

    # Problem 4:
    # Write a function that calculates mean average precision on a list of
    # proposed bounding boxes and their ground truths.
    print('Problem #4:\n{}'.format())
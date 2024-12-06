import os 
from tqdm import tqdm 
import urllib
import zipfile
import shutil
import csv
import subprocess 
from collections import defaultdict
import cv2
import json
import detectron2
from detectron2.utils.logger import setup_logger
import numpy as np
import cv2
import random
import os 
import json
import matplotlib.pyplot as plt

from detectron2 import model_zoo
from detectron2.engine import DefaultTrainer, DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer, ColorMode
from detectro2.data import DatasetCatalog, MetadataCatalog
from detectron2.data.datasets import register_coco_instances
from detectron2.evaluation import COCOEvaluator, inference_on_dataset
from detectron2.data import build_detection_test_loader







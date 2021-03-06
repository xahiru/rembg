import argparse
import glob
import io
import os
from distutils.util import strtobool
from PIL import Image
import filetype
from skimage import transform
from tqdm import tqdm

from .multiprocessing import parallel_greenscreen
from .u2net.detect import predict
from .bg import remove, remove_many
from itertools import islice, chain
import moviepy.editor as mpy
import numpy as np
import cv2
import ffmpeg
import cv2
import subprocess as sp

if __name__ == '__main__':
    parallel_greenscreen("C:\\Users\\tim\\Videos\\test\\tim_scarfe-1608643016102.mp4", 
                worker_nodes = 3, 
                cpu_batchsize = 100, 
                gpu_batchsize = 5)


# %%'

import numpy as np
import pandas as pd

from openpyxl.utils import column_index_from_string

# %%'

import polars as pl

# %%'

import dask.dataframe as dd

from dask.diagnostics import ProgressBar

from dask.distributed import Client
from dask.distributed import get_task_stream

# %%'

from scipy import signal as ss   
from scipy.optimize import curve_fit

import scipy.cluster.hierarchy as sch
from scipy.cluster.hierarchy import dendrogram

from scipy.io import savemat
from scipy.io import loadmat

import scipy.interpolate as IPL
from scipy.interpolate import griddata

# %%'

# geometric mean & standard deviation.
from scipy.stats import gmean
from scipy.stats import gstd

from scipy.stats import wilcoxon   # Wilcoxon signed-rank test.
from scipy.stats import spearmanr
from scipy.stats import mannwhitneyu
from scipy.stats import kruskal   #  Kruskal-Wallis H-test for independent samples.      # as kw
from scipy.stats import friedmanchisquare
from scipy.stats import normaltest as norm

# %%'

# adjusting p-values to account for multiple comparisons ( example : Bonferroni).
from statsmodels.stats.multitest import multipletests 
import statsmodels.formula.api as smf
import statsmodels.api as sm

import pingouin as pg 

# %%'
# %%'

import matplotlib.pyplot as plt
%matplotlib qt

# to make a legend for the overlapped gray band of normal ranges.
import matplotlib.patches as mpatches

from matplotlib.gridspec import GridSpec

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.lines import Line2D
from matplotlib.colors import LogNorm

# %%'

import seaborn as sns

from statannotations.Annotator import Annotator

# %%'

import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as pyo

# %%'

import cv2
        # import opencv  as cv2
            # ModuleNotFoundError: No module named 'opencv'1
from PIL import Image

# I didn't use it
# import open3d as o3d

# %%'

# The underlying dataframe values remain full‑precision (typically 64‑bit floating point).
    # Only the string representation shown in the notebook or console is formatted to 6 decimals.
    # Any calculations you perform still use the original high‑precision numbers.
pd.set_option('display.float_format', lambda x: '%.6f' % x)
pd.set_option('display.max_columns', None)

# sns.set(font_scale=1.75)   #  this makes the default seaborn : gray background with grids.

# sns.set_style("white")
# sns.set(style="whitegrid", font_scale=1.75)

# font_scale : I made it 3 for statistical plots.
sns.set(style="ticks", font_scale=2)  # matplotlib style : only the fontsize is changed.

# %%'

np.set_printoptions(suppress=True)

# %%'
############

# these 2 modules are not present in env_11 environment.

from open_ephys.analysis import Session

from PyPDF2 import PdfFileMerger, PdfFileReader


import adaptivekde as opt
    # opt
    # Out[39]: <module 'adaptivekde' from '/home/azare/anaconda3/envs/env_2/lib/python3.10/site-packages/adaptivekde/__init__.py'>

################
#

# %%'
###################

import spikeinterface as si  
import spikeinterface.extractors as se
import spikeinterface.sorters as sst    
import spikeinterface.widgets as sw
import spikeinterface.exporters as exp

from spikeinterface.preprocessing import (bandpass_filter, common_reference)
import spikeinterface.preprocessing as prep 
import spikeinterface.postprocessing as post


import spikeinterface.qualitymetrics as qm
from spikeinterface.qualitymetrics import compute_quality_metrics

# note : this is part of the spikeinterface[full] installation.
# no need to install it separately !!
from probeinterface import Probe, get_probe
from probeinterface import read_probeinterface
from probeinterface import write_probeinterface
from probeinterface.plotting import plot_probe , plot_probe_group


##############

import spikeinterface.curation as cur

from spikeinterface.sortingcomponents.peak_detection import detect_peaks
from spikeinterface.sortingcomponents.peak_localization import localize_peaks
from spikeinterface.sortingcomponents.motion_estimation import estimate_motion
from spikeinterface.sortingcomponents.motion_correction import CorrectMotionRecording

#################

import pickle
import copy

# %%'

# import hyperspy.api as hs

#
#from math import pi
#
#import sounddevice as sd
#

# %%'

from sklearn.pipeline import make_pipeline as mpl

from sklearn.preprocessing import StandardScaler , PowerTransformer
stsc = StandardScaler() 

from sklearn.metrics import r2_score , silhouette_score

from sklearn.model_selection import GridSearchCV , KFold

from sklearn.preprocessing import PolynomialFeatures    #  as pf
from sklearn.linear_model import LinearRegression       #  as LR

from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans

# %%' built-in modules (written in C)

import os
import sys
import subprocess

from pathlib import Path
import re      # regular expression
import collections
import string
import json

import math
import itertools

# %%'

# progress bar
from tqdm import tqdm
tqdm.pandas()  # Enable tqdm for pandas operations

# %%'

# not used
    # from threading import Lock
    # lock = Lock()

from joblib import Parallel, delayed

# %%'

import torch

# %%'



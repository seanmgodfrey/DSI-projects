import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import cPickle
from cuisinify import cuisinify
import seaborn as sns
from IPython.display import Image
from IPython.core.display import HTML
import spacy
import os
from spacy.en import English
from matplotlib import gridspec
from matplotlib import cm
from sklearn.cross_validation import KFold, cross_val_score, train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier, \
    ExtraTreesClassifier, ExtraTreesRegressor
from sklearn.ensemble import AdaBoostRegressor, BaggingRegressor, GradientBoostingRegressor
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler
from sklearn.metrics import confusion_matrix, recall_score, precision_score, accuracy_score, \
    roc_auc_score, roc_curve
from sklearn.metrics import classification_report
import matplotlib.patheffects as path_effects
from sklearn.grid_search import GridSearchCV, RandomizedSearchCV
from scipy.stats import randint
import time
from operator import itemgetter

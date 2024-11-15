import matplotlib.pyplot as plt
import os 
import time
from typing import Iterable
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim 
import torch.nn.functional as F
from torchvision import datasets, transforms
from torch.optim import lr_scheduler

def get_data():
    return train_loader, test_loader

@dataclass 
class SystemConfiguration:

@dataclass 
class TrainingConfiguration:

def setup_system():

def train():
    return epoch_loss, epoch_acc

def validate():
    return test_loss, accuracy

def main():
    return model, epoch_train_loss, epoch_train_acc, epoch_test_loss, epoch_test_acc

def get_optimizer_and_scheduler():
    return optimizer, scheduler

def plot_loss_accuracy():
    return 

class SmallModel():
    def __init__():
        super.__init__()
        self._body = nn.Sequential()
        self._head = nn.Sequential()
    def forward():
        return x 

class MediumModel():
    def __init__():
        super.__init__()
        if batch_norm:
            self._body = nn.Sequential()
        else:
            self._body = nn.Sequential()
        self._head = nn.Sequential()
    def forward():
        return x 



          






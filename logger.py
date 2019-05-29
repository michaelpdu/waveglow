import random
import torch
from tensorboardX import SummaryWriter
from plotting_utils import plot_alignment_to_numpy, plot_spectrogram_to_numpy
from plotting_utils import plot_gate_outputs_to_numpy

class WaveglowLogger(SummaryWriter):
    def __init__(self, logdir):
        super(WaveglowLogger, self).__init__(logdir)

    def log_training(self, reduced_loss, duration, iteration):
            self.add_scalar("training.loss", reduced_loss, iteration)
            self.add_scalar("duration", duration, iteration)

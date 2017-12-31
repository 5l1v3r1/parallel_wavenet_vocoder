# coding: utf-8
import torch
from torch import nn


def wavenet(layers=12,
            stacks=2,
            channels=64,
            cin_channels=None,
            gin_channels=None,
            dropout=1 - 0.95,
            kernel_size=3,
            ):
    from wavenet_vocoder import WaveNet

    model = WaveNet(layers=layers, stacks=stacks,
                    channels=channels, dropout=dropout,
                    kernel_size=kernel_size,
                    cin_channels=cin_channels, gin_channels=gin_channels)

    return model

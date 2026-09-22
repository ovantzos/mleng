import torch
import torch.nn as nn
from torch.nn import Sequential, Identity
import torch.nn.functional as fnn
import numpy as np

device = 'cuda' if torch.cuda.is_available() else 'mps' if torch.mps.is_available() else 'cpu'

class Additive(Sequential):
    def forward(self, input):
        return sum(L(input) for L in self)
    
def ResBlock(C, stride=1):
    ksize, pad = 3,1
    Cin, Cout = C,stride*C
    if stride==1:
        skip_connection = Identity()
    else:
        skip_connection = Sequential(
            nn.Conv2d(Cin,Cout, kernel_size=1, bias=False, stride=stride),
            nn.BatchNorm2d(Cout),
        )
    return Sequential(
        Additive(
            skip_connection,
            Sequential(
                nn.Conv2d(Cin,Cout,ksize, padding=pad, bias=False, stride=stride),
                nn.BatchNorm2d(Cout),
                nn.ReLU(),
                nn.Conv2d(Cout,Cout,ksize, padding=pad, bias=False, stride=1),
                nn.BatchNorm2d(Cout),
            ),
        ),
        nn.ReLU()
    )

def ResNet18():
    return Sequential(
        # conv1
        nn.Conv2d(3,64, kernel_size=7, stride=2, padding=3, bias=False),
        nn.BatchNorm2d(64),
        nn.ReLU(),

        # conv2_x
        nn.MaxPool2d(kernel_size=3, stride=2, padding=1),
        ResBlock(64),
        ResBlock(64),

        # conv3_x
        ResBlock(64, stride=2),
        ResBlock(128),

        # conv4_x
        ResBlock(128, stride=2),
        ResBlock(256),

        # conv5_x
        ResBlock(256, stride=2),
        ResBlock(512),

        # global avg_pool
        nn.AdaptiveAvgPool2d((1,1)),
        nn.Flatten(),

        # fc+softmax
        nn.Linear(512,1000),
        nn.Softmax(dim=1)
    )


def ResNet18_CIFAR():
    return Sequential(
        # conv1
        nn.Conv2d(3,64, kernel_size=1, bias=False),
        nn.BatchNorm2d(64),
        nn.ReLU(),

        # conv2_x
        ResBlock(64),
        ResBlock(64),

        # conv3_x
        ResBlock(64, stride=2),
        ResBlock(128),

        # conv4_x
        ResBlock(128, stride=2),
        ResBlock(256),

        # conv5_x
        ResBlock(256, stride=2),
        ResBlock(512),

        # global avg_pool
        nn.AdaptiveAvgPool2d((1,1)),
        nn.Flatten(),

        # fc+softmax
        nn.Linear(512,10),
        nn.Softmax(dim=1)
    )

if __name__=='__main__':
    print(f"Running on {device}")

    B,H,W,C = 1,224,224,3
    im = torch.tensor(np.ones((B,C,H,W)),dtype=torch.float32).to(device)
    model = ResNet18().to(device)
    print(f"ResNet18: {im.shape}->{model(im).shape}")

    B,H,W,C = 1,32,32,3
    im = torch.tensor(np.ones((B,C,H,W)),dtype=torch.float32).to(device)
    model = ResNet18_CIFAR().to(device)
    print(f"ResNet18_CIFAR: {im.shape}->{model(im).shape}")
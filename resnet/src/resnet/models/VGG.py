import torch
import torch.nn as nn
import torch.nn.functional as fnn
import numpy as np

device = 'cuda' if torch.cuda.is_available() else 'mps' if torch.mps.is_available() else 'cpu'

def ConvBlock(c_in, c_out, k_size, no_layers):
    return nn.Sequential(
        nn.Conv2d(c_in,c_out, k_size, padding='same'),
        *[nn.Conv2d(c_out,c_out, k_size, padding='same') for _ in range(no_layers-1)],
        nn.AvgPool2d(2)
    )

def VGG(c_in, conv_layers, lin_layers, ksize=3):
    L, ci = [], c_in
    # Convolutional Blocks
    for c,n_layers in conv_layers:
        L.append(ConvBlock(ci,c,ksize,n_layers))
        ci=c
    # Global Average Pooling
    L.append(nn.Sequential(
        nn.AdaptiveAvgPool2d((1,1)),
        nn.Flatten(),
    ))
    # FC Layers
    for c in lin_layers:
        L.append(nn.Linear(ci,c))
        ci=c
    return nn.Sequential(*L)

def VGG19(Cin):
    return VGG(Cin, 
               conv_layers=[(64,2),(128,2),(256,4),(512,4),(512,4)], 
               lin_layers=[4096,4096,1000])

if __name__=='__main__':
    B,H,W,C = 1,224,224,3
    im = torch.tensor(np.ones((B,C,H,W)),dtype=torch.float32)
    model = VGG19(C)
    print(f"{im.shape}->{model(im).shape}")
import torch
import torch.nn as nn


class NeuralNet(nn.Module):
    def __init__(self,inner_dim,hidden_dim,outer_dim):
        super(NeuralNet, self).__init__()
        self.l1=nn.Linear(inner_dim,hidden_dim)
        self.l2=nn.Linear(hidden_dim,hidden_dim)
        self.l3=nn.Linear(hidden_dim,outer_dim)
        self.relu=nn.ReLU()

    def forward(self,val):
        out=self.l1(val)
        out=self.relu(out)
        out=self.l2(out)
        out=self.relu(out)
        out=self.l3(out)

        return out

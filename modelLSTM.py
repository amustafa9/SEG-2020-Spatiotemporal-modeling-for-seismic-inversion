import torch.nn as nn

class LSTM(nn.Module):
    def __init__(self):
        super(LSTM, self).__init__()
        self.lstm = nn.LSTM(input_size=1, hidden_size=20)
        self.linear = nn.Linear(20, 1)
        
    def forward(self, x):
        """x must have shape (seq_len, batch, input_size) and output must 
        have shape (batch, seq_len, 1)"""
        
        a1, _ = self.lstm(x)
        out = self.linear(a1)
        
        return out.transpose(0,1) # bring batch to first dimension


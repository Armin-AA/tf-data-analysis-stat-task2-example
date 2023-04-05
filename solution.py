import pandas as pd
import numpy as np

from scipy.stats import norm

chat_id = 98268891

def solution(p: float, x: np.array) -> tuple:
    alpha_1 = (1 - p) / 2
    alpha_2 = (1 + p) / 2
    a1, a2 = pow(alpha_1, 1 / (x.size)), pow(alpha_2, 1 / (x.size))
  
    return (x.max() - 0.035) / a2 + 0.035, \
           (x.max() - 0.035) / a1 + 0.035

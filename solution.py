import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 98268891 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    df = len(x) - 1
    var = np.var(x, ddof=1)
    lower = chi2.ppf(alpha / 2, df)
    upper = chi2.ppf(1 - alpha / 2, df)
    var1 = df * var / upper
    var2 = df * var / lower
    return np.sqrt((var1 * 12)) + 0.035, np.sqrt((var2 * 12)) + 0.035

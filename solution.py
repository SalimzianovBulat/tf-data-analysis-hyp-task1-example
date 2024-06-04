import pandas as pd
import numpy as np


chat_id = 469801461 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    import scipy.stats as sps
    alpha = 0.03
    x_mean, y_mean = x_success / x_cnt, y_success / y_cnt
    x_variance, y_variance = x_mean * (1 - x_mean) / x_cnt, y_mean * (1 - y_mean) / y_cnt
    z = sps.norm.ppf(1-alpha)
    return y_mean - x_mean > np.sqrt(x_variance + y_variance) * z

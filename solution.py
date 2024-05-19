import pandas as pd
import numpy as np


chat_id = 469801461 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    import scipy.stats as sps
    alpha = 0.03

    first = np.concatenate((np.ones(x_success), np.zeros(x_cnt - x_success)))

    second = np.concatenate((np.ones(y_success), np.zeros(y_cnt - y_success)))
    return sps.ttest_ind(first, second)[1] <= alpha

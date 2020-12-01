import numpy as np
from scipy import sparse

sparse_matrix = sparse.load_npz('E:\\Web_lab\\exp1\\output\\tf_idf_matrix.npz')

print(sparse_matrix.toarray())


def tf_idf_normalize():
    normalize_matrix = np.zeros((N, N_item))
    for col in range(N):  # 计算归一化矩阵
        sum_2 = math.sqrt(np.sum(tf_idf_matrix[:, col] ** 2))
        normalize_matrix[:, col] = tf_idf_matrix[:, col] / sum_2
    return normalize_matrix

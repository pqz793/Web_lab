import numpy as np
import nltk
import re
from scipy import sparse
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

porter_stemmer = PorterStemmer()

path0 = "E:\Web_lab\exp1\\"  # 基础目录
N = 1000
word_list = []

def compare(input_word_vec, tf_idf_col_vec):
    return

#计算查询词或词组的向量，不用作归一化（归一化后，在最后比较时只是因子不同）
def cal_input_query(query_str):
    vec = np.zeros(1000)
    query_list = query_str.split()
    for word in query_list:
        w = porter_stemmer.stem(word)  # 词根化处理
        if w in word_list:
            vec[word_list.index(w)] = 1
    return vec

def main():
    path_npz = path0 + "output\\tf_idf_matrix.npz"
    path_query = path0 + "input\\semantic_search.txt"
    path_inverted_table = path0 + "output\\inverted_table.txt"
    sparse_matrix = sparse.load_npz(path_npz)
    tf_idf_matrix = sparse_matrix.todense()
    # print(tf_idf_matrix)

    file_query = open(path_query)
    iter_f = iter(file_query)
    query = []  #存放输入的查询词或词组
    for line in iter_f:  # 遍历文件，按行遍历，读取文本，每个文本对应一个字符串
        line = re.sub(r'\n.*$', "", line)
        #w = porter_stemmer.stem(line)  # 词根化处理
        query.append(line)
    file_query.close()

    file_inverted_table = open(path_inverted_table)
    iter_f = iter(file_inverted_table)
    for line in iter_f:
        line = re.sub(r'\n.*$', "", line)
        word_list.append(line.split()[0])
    file_inverted_table.close()
    #print(query)
    #print(word_list)
    #print(len(word_list))
    for word in query:
        vec = cal_input_query(word)
        compare(vec, )



if __name__ == "__main__":
    main()

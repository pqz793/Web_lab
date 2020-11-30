import os
import nltk
import re
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
porter_stemmer = PorterStemmer()
stop_words_table = stopwords.words('english')
for w in ['!', ',', '.', '?', ':', '<', '>','@','[',']','(',')','-']:
    stop_words_table.append(w)
# print(stop_words_table)


path = "E:\Web_lab\exp1\data_temp1\maildir"  # 文件夹目录
files_maildir = os.listdir(path)  # 得到文件夹下的所有文件名称
s = []
i = 1

def filter(line):
    line = re.sub(r'Message-ID.*$', "", line)
    line = re.sub(r'Date.*$', "", line)
    line = re.sub(r'From.*$', "", line)
    line = re.sub(r'To.*$', "", line)
    line = re.sub(r'Mime-Version.*$', "", line)
    line = re.sub(r'Content.*$', "", line)
    line = re.sub(r'X.*$', "", line)
    line = re.sub(r'\t.*$', "", line)
    #line = re.sub(r'[^\s]', "", line)
    return line


def build_invert_list(path):
    f = open(path)
    iter_f = iter(f)  # 创建迭代器
    str = ""
    for line in iter_f:  # 遍历文件，按行遍历，读取文本，每个文本对应一个字符串
        line = filter(line)
        str = str + line
    text = nltk.word_tokenize(str)  # 分词
    # print(text)
    s_temp = []
    for word in text:
        w = porter_stemmer.stem(word)  # 词根化处理
        if w not in stop_words_table:
            s_temp.append(w)
    s.append(s_temp)
    print(s_temp)
    print('\n')


for file_person in files_maildir:  # 遍历第一层文件夹maildir
    path1 = path + "\\" + file_person
    diff_doc = os.listdir(path1)
    for doc in diff_doc:       # 遍历第二层文件夹
        path2 = path1 + "\\" + doc
        if not os.path.isdir(path2):
            build_invert_list(path2)
            continue
        diff_file = os.listdir(path2)
        for file in diff_file:  # 遍历当前文件夹中的每个文件
            path3 = path2 + "\\" + file
            build_invert_list(path3)
            #print(str + '\n')
            # s.append(str) #每个文件的文本存到list中

            # print(s)  # 打印结果

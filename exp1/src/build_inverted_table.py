import os
import nltk
import re
import operator
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

porter_stemmer = PorterStemmer()
stop_words_table = stopwords.words('english')  # 创建英文默认倒排表
file_No = {}
inverted_table = {}
i = 0
path0 = "E:\Web_lab\exp1\\"  # 基础目录


def build_stop_words_table():
    # print(stop_words_table)
    # 扩展英文倒排表
    for w in ['!', ',', '.', '?', ':', '<', '>', '@', '[', ']', '(', ')', '-']:
        stop_words_table.append(w)


# 利用正则表达式过滤除了主题和正文之外的部分
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

#根据word更新倒排表
def add_inverted_table(word):
    if word not in inverted_table:
        temp = []
        temp.append(i)
        inverted_table[word] = temp
    else:
        if i not in inverted_table[word]:
            inverted_table[word].append(i)


#根据传入的path处理对应的文件，包含预处理和建立倒排表
def build_invert_list(path):
    global i
    file_No[path] = i  # 建立字典：key = path， value = 第几次被读到

    f = open(path)
    iter_f = iter(f)
    str = ""
    for line in iter_f:  # 遍历文件，按行遍历，读取文本，每个文本对应一个字符串
        line = filter(line)  # 只读取主题和正文
        str = str + line

    f.close()
    text = nltk.word_tokenize(str)  # 分词
    # print(text)
    #s_temp = []
    for word in text:
        w = porter_stemmer.stem(word)  # 词根化处理
        if w not in stop_words_table:  # 去停用词处理
            add_inverted_table(w)
            # s_temp.append(w)
    # s.append(s_temp)
    # print(s_temp)
    # print('\n')
    i = i + 1



def file_read():
    path = path0 + "data_temp1\maildir" #数据集目录
    files_maildir = os.listdir(path)  # 得到文件夹下的所有文件名称
    for file_person in files_maildir:  # 遍历第一层文件夹maildir
        path1 = path + "\\" + file_person
        diff_doc = os.listdir(path1)
        for doc in diff_doc:       # 遍历第二层文件夹
            path2 = path1 + "\\" + doc
            if not os.path.isdir(path2):  # 注意，该层目录中也可能有文件
                build_invert_list(path2)
                continue
            diff_file = os.listdir(path2)
            for file in diff_file:  # 遍历当前文件夹中的每个文件
                path3 = path2 + "\\" + file
                build_invert_list(path3)


def write_1000_inverted_table():
    list1 = sorted(inverted_table.items(), key=lambda item: len(item[1]), reverse=True)
    path_inverted_table = path0 + "output/inverted_table.txt"
    file_inverted_table = open(path_inverted_table, 'w+')
    for j in range(20): #后续改为1000
        file_inverted_table.write(list1[j][0] + ' : ' + str(list1[j][1]) + '\n')
    file_inverted_table.close()


def main():
    build_stop_words_table()
    file_read()
    write_1000_inverted_table()


if __name__ == "__main__":
    main()

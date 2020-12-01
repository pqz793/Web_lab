def AND(p1,p2):
    #对两个倒排表求交
    answer=[]
    len1=len(p1)
    len2=len(p2)
    i1=0
    i2=0
    while i1<len1 and i2<len2:
        if p1[i1]==p2[i2]:
            answer.append(p1[i1])
        elif int(p1[i1])<int(p2[i2]):
            i1=i1+1
        else:
            i2=i2+1
    return answer

def OR(p1,p2):
    #对两个倒排表求并，注意去重
    temp=p1+p2
    answer = list(set(temp))
    answer.sort(key=temp.index)
    return answer


def handle_query(query):
    #参数为bool查询字符串query
    #返回对应的文档序号列表
    querylist=query.split(" ")
    len=len(querylist)
    return exp(querylist)

'''
表达式：由单独的"项"或者"项"与"OR"运算符连接形成；
项：由单独的"因子"或"因子"和&运算符连接而成；
因子：可以是单独的V或F，也可以是用括号括起来的"表达式"。
'''

def exp(querylist):#读入一个表达式并返回其结果文档列表
    global i
    result=item(querylist)
    while(querylist[i]=="OR"):
        i=i+1
        result=OR(result,item(querylist))
    return result


def item(querylist):
    global i
    result=factor(querylist)
    while(querylist[i]=="AND"):
        i=i+1
        result=AND(result,factor(querylist))
    return result


def factor(querylist):
    global i
    if querylist[i]=="(":
        i=i+1
        return exp(querylist,i)
        i=i+1
    elif querylist[i]=="NOT":
        return notExp(querylist,i)
    else:
        return L[querylist[i]]

def notExp(querylist,L):
    i=i+1
    if querylist[i]=="(":
        i=i+1
        return exp(querylist)
        i=i+1
    elif querylist[i]=="NOT":
        return notExp(querylist,i+1)
    else:
        l=list(range(517403))
        for elem in L[querylist[i]]:
            l.remove(elem)



if __name__ == "__main__":
    i=0
    inverted_table={}
    with open("./output/inverted_table.txt") as file:
        for line in file.readlines():
            line = line.strip('\n').split(" ")
            word=line[0]
            del line[0]#去掉开头的词项以及冒号
            del line[1]
            inverted_table[word]=line

    with open("bool_query.txt") as file:
        for line in file.readlines():
            line = line.strip('\n')
            doc_list=handle_query(line)
            print(doc_list)


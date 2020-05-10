'''
-----------------------------------伪机器学习----------------------------------------

                                                                                    '''
import pickle

#加密学习

def ectlearn (inword,word):#参数:（inword = 汉字，word = 带声调的汉语拼音）

    pinyin_dict = open('dict\\pinyin_dict.pkl','rb') #只读模式打开二进制文件pickle（一个字典）

    pinyin_note = pickle.load(pinyin_dict) #转化二进制文件存入pinyin_note变量

    pinyin_note[inword] = word #新增键和值

    pinyin_dict.close() #关闭pickle

    pinyin_dict = open('dict\\pinyin_dict.pkl','wb') #写入模式打开pickle

    pickle.dump(pinyin_note,pinyin_dict) #添加后的字典转二进制写入

    pinyin_dict.close() #关闭pickle



#解密学习

def learn (inword,word):#参数:（inword = 汉字，word = 带声调的汉语拼音）
 
    pinyin_dict = open('dict\\pinyin_dict.pkl','rb') #只读模式打开二进制文件pickle（一个字典）
    
    pinyin_note = pickle.load(pinyin_dict) #转化二进制文件存入pinyin_note变量
    
    if word in  pinyin_note: #添加键和值
        
        pinyin_note[word]+=[inword]

    else:
        pinyin_note[word] = []
        pinyin_note[word]+=[inword]

    pinyin_dict.close() #关闭pickle

    pinyin_dict = open('dict\\pinyin_dict.pkl','wb') #写入模式打开pickle

    pickle.dump(pinyin_note,pinyin_dict) #添加后的字典转二进制写入

    pinyin_dict.close() #关闭pickle

    ectlearn (inword,word) #调用加密学习函数

    vl = str(pinyin_note[word].index(inword)) #汉字在字典中拼音键值列表中的索引值存入vl

    num = ''

    for i in vl: # str 索引值不一定是一个字符，但字典中只有对应的一个字符的值
        
        num += pinyin_note[i]

    return num #返回汉字在字典中拼音键值列表中的索引值

#测试

if __name__ == '__main__':

    inword = input('输入汉字：')

    word = input('输入带声调拼音：')

    print(learn (inword,word))

    pinyin_dict = open('dict\\pinyin_dict.pkl','rb')

    pinyin_note = pickle.load(pinyin_dict)

    pinyin_dict.close()

    print(pinyin_note)

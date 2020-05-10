'''
----------------------------------解密---------------------------------------
                                                                                '''

import pickle
import re
import Lock as L

def unlockf(word):#密文->数字

    m_ndict = open('dict\\m_n_dict.pkl','rb')

    m_nwbook = pickle.load(m_ndict)

    m_ndict.close()

    word = m_nwbook[word]

    return word


def unlocks(word):#数字->错位后的字母

    n_wdict = open('dict\\n_w_dict.pkl','rb')

    n_wwbook = pickle.load(n_wdict)

    n_wdict.close()

    word = n_wwbook[word]

    return word


def unlockt(word):#字母错误还原

    rdict = open('dict\\rw_dict.pkl','rb')

    rwbook = pickle.load(rdict)

    rdict.close()

    word = rwbook[word]

    return word


def unlockfo(word,num):#还原成原文

    pdict = open('dict\\pinyin_dict.pkl','rb')

    pwbook = pickle.load(pdict)

    pdict.close()

    word = pwbook[word][num]

    return word


def unlock(words):


    pdict = open('dict\\pinyin_dict.pkl','rb')

    pwbook = pickle.load(pdict)

    pdict.close()

    bwords = ''

    for word in words:

        bwords += unlockf(word)

    words = ''

    bwords = re.findall(r'.{2}', bwords)

    for word in bwords:

        words += unlocks(word)

    bwords = ''

    for word in words:

        bwords += unlockt(word)

    words = ''

    bwords = bwords.split(' ')

    bwords.pop()

    for word in bwords:

        bword = word.split('|')

        num = ''

        word = bword[0]

        for i in bword[1]:

            num += pwbook[i]

        num = int(num)

        words += unlockfo(word,num)

    return words


if __name__ == '__main__': #测试

    while True:

        words = input('输入：')

        if unlock(words) == '':

            print('这玩意儿不是我加密的')

        else:

             print(unlock(words))

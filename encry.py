'''
----------------------------------加密函数---------------------------------------
                                                                                '''
import pickle
import ml
import pinyin

def lock_upf(word):#文字转拼音（字母）

    pdict = open('dict\\pinyin_dict.pkl','rb')

    pwbook = pickle.load(pdict)

    pdict.close()

    if word in pwbook :#有的之间用

        num = pwbook[str(pwbook[pwbook[word]].index(word))]

        word = pwbook[word] + '|'+ num + ' '

    else :#没有的存进去

        word_pin = pinyin.trans(word)

        num = ml.learn(word,word_pin)

        word = word_pin + '|' +num + ' '

    return word


def lock_ups(word):#字母错乱顺序

    ddict = open('dict\\dw_dict.pkl','rb')

    dwbook = pickle.load(ddict)

    ddict.close()

    if word in dwbook:
    
        word = dwbook[word]

    else:

        rdict = open('dict\\rw_dict.pkl','rb')

        rwbook = pickle.load(rdict)

        rdict.close()

        rdict = open('dict\\rw_dict.pkl','wb')

        rwbook[word] = word

        pickle.dump(rwbook,rdict)

        rdict.close()

        ddict = open('dict\\dw_dict.pkl','wb')

        dwbook[word] = word

        pickle.dump(dwbook,ddict)

        ddict.close()

    return word


def lock_upt(word):#字母->数字

    w_ndict = open('dict\\w_n_dict.pkl','rb')

    w_nwbook = pickle.load(w_ndict)

    w_ndict.close()

    if word in w_nwbook:

        word = w_nwbook[word]

        return word

    else:

        n_wdict = open('dict\\n_w_dict.pkl','rb')

        n_wwbook = pickle.load(n_wdict)

        n_wdict.close()

        n_wdict = open('dict\\n_w_dict.pkl','wb')

        n_wwbook['?'+word] = word

        pickle.dump(n_wwbook,n_wdict)

        n_wdict.close()

        w_ndict = open('dict\\w_n_dict.pkl','wb')

        w_nwbook[word] = '?'+word

        pickle.dump(w_nwbook,w_ndict)

        w_ndict.close()

        return '?'+word


def lock_upfo(word):#数字->密文

    n_mdict = open('dict\\n_m_dict.pkl','rb')

    n_mwbook = pickle.load(n_mdict)

    n_mdict.close()

    if word in n_mwbook:
    
        word = n_mwbook[word]

    else:

        m_ndict = open('dict\\m_n_dict.pkl','rb')

        m_nwbook = pickle.load(m_ndict)

        m_ndict.close()

        m_ndict = open('dict\\m_n_dict.pkl','wb')

        m_nwbook[word] = word

        pickle.dump(m_nwbook,m_ndict)

        m_ndict.close()

        n_mdict = open('dict\\n_m_dict.pkl','wb')

        n_mwbook[word] = word

        pickle.dump(n_mwbook,n_mdict)

        n_mdict.close()

    return word


def lock_up(words):#循环上面的步骤

    bwords = ''

    for word in words:

        bwords += lock_upf(word)

    words = ''

    for word in bwords:

        words += lock_ups(word)

    bwords = ''

    for word in words:

        bwords += lock_upt(word)

    words = ''

    for word in bwords:

        words += lock_upfo(word)

    return words


if __name__ == '__main__': #测试

    while True:

        words = input('输入：')

        print(lock_up(words))

import pickle
a=open('dw_dict.pkl','rb')
b=pickle.load(a)
print(b)
a.close()

a=open('rw_dict.pkl','rb')
b=pickle.load(a)
print(b)
a.close()

a=open('w_n_dict.pkl','rb')
b=pickle.load(a)
print(b)
a.close()

a=open('n_w_dict.pkl','rb')
b=pickle.load(a)
print(b)
a.close()

a=open('n_m_dict.pkl','rb')
b=pickle.load(a)
print(b)
a.close()

a=open('m_n_dict.pkl','rb')
b=pickle.load(a)
print(b)
a.close()

a=open('pinyin_dict.pkl','rb')
b=pickle.load(a)
print(b)
a.close()

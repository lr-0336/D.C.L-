'''
------------------------------随机打乱字典---------------------------------------
                                                                                '''

import pickle
import random

def test():#打开根字典，检测效验值是否等于0
    rootpkl = open ('dict\\root_dict.pkl','rb')
    validation = pickle.load(rootpkl)
    rootpkl.close()
    if validation[0] == 0:
        upset()
        return 1
    else:
        return 0
    
def upset():#进行随机打乱，将效验值改为1

    rootpkl = open ('dict\\root_dict.pkl','rb')

    dw = {}

    rw = {}

    rootdict = pickle.load(rootpkl)

    rootpkl.close()

    order = random.sample(range(1, 89),88)

    for i in range(0,88):

        dw[rootdict[i+1]] = rootdict[order[i]]

    for key, val in dw.items():

        rw[val] = key

    rootdict[0] = 1

    rootpkl = open ('dict\\root_dict.pkl','wb')

    dwpkl = open('dict\\dw_dict.pkl','wb')

    rwpkl = open('dict\\rw_dict.pkl','wb')

    pickle.dump(rootdict,rootpkl)

    pickle.dump(dw,dwpkl)

    pickle.dump(rw,rwpkl)

    rootpkl.close()

    dwpkl.close()

    rwpkl.close()

    

if __name__ == '__main__': #测试

    upset()

    

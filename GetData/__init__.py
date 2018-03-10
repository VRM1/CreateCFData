import json
import numpy as np
from collections import defaultdict
# ok
def GetUserNItems(name,subset_num=None):

    lukup = {'music':'Musical_Instruments','clothing':'Men_Clothing','movies':'Movies',\
             'electronics':'Electronics','books':'Books'}
    uniq_itms = set()
    subs_usr_itm = defaultdict(list)
    t_itm_list = []
    with open('dataset/'+lukup[name]+'_Useritems.json') as fp:
        usr_itm = json.load(fp)

    for usr in usr_itm:
        itms = set(usr_itm[usr].strip().split(','))
        # convert the value  as set for O(1) search
        usr_itm[usr] = itms
        t_itm_list.append(len(itms))

    med_itms = np.average(t_itm_list)
    print '# users:{} average number of items selected by user is:{}'.format(len(usr_itm),med_itms)
    print 'removing all users who purchased less than:{} items'.format(med_itms+2)
    usrs = usr_itm.keys()
    # filter users who have less than average number of items
    for u in usrs:
        if len(usr_itm[u]) < med_itms+2:
            usr_itm.pop(u)
    print 'number of users after filtration is:{}'.format(len(usr_itm))
    for u in usr_itm:
            uniq_itms.update(usr_itm[u])
    print '# users:{}, # items:{}'.format(len(usr_itm),len(uniq_itms))
    return (usr_itm,uniq_itms)

if __name__ == '__main__':
    GetUserNItems()

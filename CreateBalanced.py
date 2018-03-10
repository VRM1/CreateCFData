# this program creates a balanced dataset
import random
import multiprocessing
from tqdm import tqdm
from GetData import GetUserNItems
from collections import defaultdict
import numpy
numpy.random.seed(10)
# Options are: music,clothing,movies, electronics,books
name = 'movies'
data = GetUserNItems(name)
usr_itm,uniq_itms = data[0],data[1]

def drawNegatives(u):
    t_posit_samples = len(usr_itm[u])
    neg_samples = uniq_itms - usr_itm[u]
    negs = random.sample(neg_samples,t_posit_samples)
    # collect all the positive values
    posit = [(i,1) for i in usr_itm[u]]
    # collect all the negative values
    negtivs = [(i,0) for i in negs]
    return (u,posit+negtivs)

def makeBalanced():

    balanced_data = defaultdict(list)
    num_workers = multiprocessing.cpu_count()
    p = multiprocessing.Pool(num_workers)
    print 'total unique items:{}'.format(len(uniq_itms))
    # start negative sampling ok
    usrs = usr_itm.keys()
    for res in tqdm(p.imap(drawNegatives, iter(usrs)), total=len(usrs)):
        usr = res[0]
        itms = res[1]
        balanced_data[usr] = itms

    # write to output
    with open(name+'_balanced.csv','w') as fp:
        fp.write('user,item,label\n')
        for u in balanced_data:
            itms = balanced_data[u]
            for itm in itms:
                fp.write(u+',')
                fp.write(itm[0]+','+str(itm[1])+'\n')


if __name__ == '__main__':
    makeBalanced()


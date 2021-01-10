import numpy as np
temp = np.array([float(i) for i in input().split(',')])
n_samples,n_features = np.array([int(i) for i in input().split(',')])
data = np.array (temp).reshape(n_samples,n_features)
means = np.mean(data,axis=0)
data = (data - np.mean(data)) / np.std(data)
cov = np.cov(data,rowvar=False)
eigvalue,eigvec = np.linalg.eig(cov)
eig_pairs = [(np.abs(eigvalue[i]), eigvec[:,i]) for i in range(n_features)]
eig_pairs.sort(reverse=True)
val,pmt = eig_pairs[0]

flag = "+"
if pmt[1] < 0:
    flag = ""
print("第1主成分=%.5f*(x1-%.2f)"%(pmt[0],means[0])+ flag+"%.5f*(x2-%.2f)"%(pmt[1],means[1]))
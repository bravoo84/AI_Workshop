
#--This algo is based on Support vector Machine--#
#--Import libs from anaconda...rather create conda env--#
#--for plotting numbers 0-9 on a graph--#

import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn import svm #(svm=support Vector machine)

alg=svm.SVC(gamma=1,C=1000)

digits=datasets.load_digits()

xtrain,ytrain=digits.data[:100],digits.target[:100]

alg.fit(xtrain,ytrain)

#-- change values in image and data indices--#

plt.imshow(digits.images[9],cmap=plt.cm.gray_r,interpolation="nearest")
print(alg.predict(digits.data[9]))
plt.show()

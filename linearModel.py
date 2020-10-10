import numpy as np
from sklearn import linear_model as lm
from sklearn.metrics import mean_squared_error as mse, r2_score as r2
from sklearn.model_selection import cross_val_score as cvs

# trainTestname = '../dataset/debug.csv'
# testTestname = '../dataset/debug.csv'

trainFilename = '../dataset/dota2Train.csv'
testFilename = '../dataset/dota2Train.csv'

numpyArr = np.loadtxt(trainFilename, delimiter=",")
yTrain, XTrain = np.hsplit(numpyArr, [1])

print("ytrain: ",yTrain)
print("xtrain: ", XTrain)

numpyArr = np.loadtxt(testFilename, delimiter=",")
yTest, xTest = np.hsplit(numpyArr, [1])

mean = np.mean(yTrain)
var = np.var(yTrain)

lr = lm.LogisticRegression(max_iter=1000)
scores = cvs(lr, XTrain, yTrain, cv=10)
lr.fit(XTrain, yTrain.values.ravel())
predictions = lr.predict(xTest)
# with open('linearClassResults.txt', 'w') as o:
# 	o.write('Data metrics:' + '\n')
# 	o.write('Mean: ' + str(mean) + '\n')
# 	o.write('Var: ' + str(var) + '\n')
# 	o.write('Cross Val Scores:' + '\n')
# 	o.write(str(scores) + '\n')
# 	o.write('Mean squared error: ' + '\n')
# 	o.write(str(mse(yTest, predictions)))

import joblib

filename = 'dota2.h5'
joblib.dump(lr, filename)
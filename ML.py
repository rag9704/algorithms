import pandas as pd
import quandl
import math,datetime
import numpy as np
from sklearn import preprocessing,cross_validation,svm
from sklearn.linear_model import LinearRegression
from matplotlib import style
import matplotlib.pyplot as plt
import pickle



style.use('ggplot')

df = quandl.get('WIKI/GOOGL')
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
df['HL_pct']=(df ['Adj. High']- df['Adj. Low'])*100/df['Adj. Low']
df['pct']=(df ['Adj. Close']- df['Adj. Open'])*100/df['Adj. Open']
df = df[['Adj. Close','HL_pct','pct','Adj. Volume']]#features
forecast_col='Adj. Close'

df.fillna(-99999,inplace=True)
forecast_out= int(math.ceil(0.01*len(df)))#predict next 10% time of data
print(forecast_out)
df['label']=df[forecast_col].shift(-forecast_out)


X = np.array(df.drop(['label'],1))

X= preprocessing.scale(X)
X_lately=X[-forecast_out:]
X=X[:-forecast_out:]


df.dropna(inplace=True)
y= np.array(df['label'])


X_train , X_test , y_train , y_test= cross_validation.train_test_split(X,y,test_size=.2)
clf=LinearRegression(n_jobs=-1)
clf.fit(X_train,y_train)
with open('linearregression..pickel','wb') as f:
    pickle.dump(clf,f)
pickle_in=open('linearregression..pickel','rb')
clf=pickle.load(pickle_in)

accuracy=clf.score(X_test,y_test)
#print(accuracy)
#predict
forecast_set=clf.predict(X_lately)
print(forecast_set,accuracy,forecast_out)
df['forecast']=np.nan
last_date=df.iloc[-1].name
last_unix=last_date.timestamp()
one_day=86400
next_unix=last_unix + one_day

for i in forecast_set:
    next_date=datetime.datetime.fromtimestamp(next_unix)
    next_unix+=one_day
    df.loc[next_date]=[np.nan for _ in range(len(df.columns)-1)] + [i]
print(df.tail())
df['Adj. Close'].plot()

df['forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()






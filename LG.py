import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
adv_df=pd.read_csv('advertisement.csv')
print(adv_df.head())
x=adv_df[['TV']]
y=adv_df['Sales']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=42)
x_train_reshape=x_train.values.reshape(-1,1)
x_test_reshape=x_test.values.reshape(-1,1)
y_train_reshape=y_train.values.reshape(-1,1)
y_test_reshape=y_test.values.reshape(-1,1)
lin=LinearRegression()
lin.fit(x_train_reshape,y_train_reshape)
print("slope:",lin.coef_)
print("intercept:",lin.intercept_)
defsales_predicted(amount):
return 7.12+0.0556*amount
sale_prd=sales_predicted(50)
sale=round(sale_prd*1000)
print("sales:",sale)

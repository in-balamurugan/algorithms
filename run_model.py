from algo.model import LinearRegression

r=LinearRegression(x_test=[1,1,1], x_train=[2,2,2],
        y_train=[3,None,3],y_test=[4,None,4],metric='logloss')
print(f'Updated values for y_train and y_test {r.y_train} and {r.y_test}\n')

y_predict=r.predict(x_predict=[5,5,5])
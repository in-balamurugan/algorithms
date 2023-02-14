from typing import List

def nulls_with_average(func):
    def wrapper(*args):
        print(*args)
        null_replaced_args = []
        for l in args:
            if(isinstance(l, list)):
                avg = int(sum(x for x in l if x is not None) / len([(x) for x in l if x is not None]))
                updated_list = [avg if x is None else x for x in l]
                null_replaced_args.append(updated_list)
            else:
                null_replaced_args.append(l)
        
        return func(*null_replaced_args)
    return wrapper

class Model:

    @nulls_with_average
    def __init__(self, x_test: List[int], x_train: List[int],y_train: List[int],y_test: List[int]):
        self.x_test = x_test
        self.x_train = x_train
        self.y_train = y_train
        self.y_test = y_test
        print(f'\nInitiating Model......\n')

class Regression(Model):
    def __init__(self, x_test:List[int], x_train:List[int],y_train:List[int],y_test:List[int],metric: str):
        Model.__init__(self,x_test, x_train,y_train,y_test)
        self.metric=metric
        print(f'Metric Set......\n')
        


class LinearRegression(Regression):
    def __init__(self, x_test, x_train,y_train,y_test,metric):
        Regression.__init__(self,x_test, x_train,y_train,y_test,metric)
        


    def predict(self,x_predict:List[int]) ->  List[int]:
        print(f'Predicting through Linear Regression......\n')
        return [6,6,6]


import os
from data.util import get_data

PATH = os.path.join(os.getcwd(), 'data\\data_orders.csv')

data = get_data(PATH)

print(data)
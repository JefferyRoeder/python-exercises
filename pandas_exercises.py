import pandas as pd
import numpy as np
from pydataset import data
import env

mpg = data('mpg')
mpg.head(2)

#1.a
mpg.head(2)
mpg['total_mpg'] = (mpg['cty'] + mpg['hwy'])/2
mpg.head(2)
mpg.groupby('manufacturer').total_mpg.agg('mean').sort_values(ascending = False).head(1)

#1.b
len(mpg[['manufacturer']].groupby('manufacturer').agg('count'))

#1.c

len(mpg[['model']].groupby('model').agg('count'))


#1.d
mpg['automatic_trans'] = mpg['trans'].str.contains('auto')
mpg.head(3)

mpg[['automatic_trans','model']].groupby('automatic_trans').agg('count')

#2 

pd.merge(users,roles,left_on='role_id',right_on='id',how='left')

pd.merge(users,roles,left_on='role_id',right_on='id',how='inner')

#3.a

# def get_db_url():
#     user = input("Username: ")
#     password = input("Password: ")
#     host = input("Host: ")
#     database = input("Database: ")
#     url = f'mysql+pymysql://{user}:{password}@{host}/{database}'
#     return url

def get_db_url():
    user = env.user
    password = env.password
    host = env.host
    database = input("Database: ")
    url = f'mysql+pymysql://{user}:{password}@{host}/{database}'
    return url

url = get_db_url()

#3.b,c,d,e

employees = pd.read_sql('SELECT * FROM employees',url)

titles = pd.read_sql('SELECT * FROM titles',url)
#3.f,g
pd.merge(employees,titles,left_on='emp_no',right_on='emp_no',how='left')

employees_titles.groupby('title').emp_no.agg('count')
#3.h
employees_titles.groupby('title').from_date.agg('max')

#3.i
departments_all = pd.merge(dept_emp,departments,left_on='dept_no',right_on='dept_no',how='left')

employees_all = pd.merge(departments_all,employees_titles,left_on='emp_no',right_on='emp_no')

employees_all.head()

#crosstab of titles by dept

pd.crosstab(employees_all.dept_name,employees_all.title,margins=True)

#4. chipotle db

orders = pd.read_sql("""SELECT * FROM orders""",url)

orders['price'] = orders['price'].str.replace('$','').astype(float)

orders.groupby('item_name').item_name.agg('count').sort_values(ascending=False).head(3)

orders.groupby('item_name').price.agg('sum').sort_values(ascending=False).head(3)
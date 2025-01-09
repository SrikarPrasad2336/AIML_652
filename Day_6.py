#Generator

def square(i):
    #0,1,2,3,4,5,6,7,8,9
    for i in range(i):
        i=i+2
        yield i
        #return n
square(10)
for i in square(10):
    print(i)

# using lambda function with 2 variables
def add(x,y):
    return x+y
res=add(10,20)
print(res)
result=lambda x,y:x*y
print(result(10,20))

# using lambda function with 3 variables
def add(x,y,z):
    return x+y+z
res=add(10,20,200)
print(res)
result=lambda x,y,z:x*y*z
print(result(10,20,200))

#Decorator
def sample(func):
    def wrapper(item):
        item=item.upper()
        return func(item)#call the wrapped function with modified value
    return wrapper

@sample
def process(item):
    return item

result=process #testing the function
print(result("hello"))

#decorator using upper case
def sample(func):
    def wrapper(item):
        item=item.upper()
        return func(item)#call the wrapped function with modified value
    return wrapper

@sample
def process(item):
    return item

result=process #testing the function
print(result("MALLA REDDY UNIVERSITY"))

#decorator using lower case
def sample(func):
    def wrapper(item):
        item=item.upper()
        return func(item)#call the wrapped function with modified value
    return wrapper

@sample
def process(item):
    return item

result=process #testing the function
print(result("MallA reDDy UNiveRSitY"))

#Dataframe with Dictionary
import pandas as pd
screen_time=[1,2,5,6]
stu_name=["aa","bb","cc","dd"]
id=[2,5,1,6]
dict1={"screen_time":screen_time,"stu_name":stu_name,"id":id}
print(dict1)
df=pd.DataFrame(dict1)
print(df)

#Dataframe with Dictionary by using head tag
import pandas as pd
screen_time=[1,2,5,6,45,23,65,56,12,78,]
stu_name=["aa","bb","cc","dd","ee","ff","gg","hh","ii","jj"]
id=[5,1,6,2,4,6,8,2,8,9]
dict1={"screen_time":screen_time,"stu_name":stu_name,"id":id}
print(dict1)
df=pd.DataFrame(dict1)
df.head(3)
print(df)

#Dataframe with Dictionary by using tail tag
import pandas as pd
screen_time=[1,2,5,6,45,23,65,56,12,78,]
stu_name=["aa","bb","cc","dd","ee","ff","gg","hh","ii","jj"]
id=[5,1,6,2,4,6,8,2,8,9]
dict1={"screen_time":screen_time,"stu_name":stu_name,"id":id}
print(dict1)
df=pd.DataFrame(dict1)
df.tail(3)
#print(df)

#create a dataframes product id,product name,discount percentage by using list and dictionaries create 20 rows from that get first 10 rows and last ten rows
import pandas as pd

product_names = [656,652,642,640,641,643,714,674,666,646,699,607,600,719,637,638,657,655,673,633]
discount_percentages = [12,24,43,11,65,67,32,75,76,78,12,78,34,56,26,54,75,12,67,88]
product_ids = [1,11,2,12,3,13,4,14,5,15,6,16,7,17,8,18,9,19,10,20]

data = {
    'Product ID': product_ids,
    'Product Name': product_names,
    'Discount Percentage': discount_percentages
}

df = pd.DataFrame(data)

first_10_rows = df.head(10)
last_10_rows = df.tail(10)

print("First 10 Rows:",first_10_rows)
print("\nLast 10 Rows:",last_10_rows)
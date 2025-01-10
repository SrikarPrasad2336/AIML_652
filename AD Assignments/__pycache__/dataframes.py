import pandas as pd
student_name=["ram","mani","shannu","skar","karthik","asad"]
stu_id=[641,642,640,652,666,643]
rank=[20,14,34,32,42,41]
dict={"student_name":student_name,"stu_id":stu_id,"rank":rank}
df=pd.DataFrame(dict)
print(df)
import pandas as pd
data={
    'student':["aryan","tansihq","doraemon","nobita","dekisugi"],
    'rank':[1,4,3,5,2],
    'marks':[95,70,80,60,90]
}
df=pd.DataFrame(data,index=['student 1 ','student 2 ','student 3 ','student 4 ','student 5 '])
print(f"student marks \n{df}")
print(f"here is the value of particular\n{df.loc['student 5 ','student']}")
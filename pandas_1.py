import pandas as pd
data ={'student':['aryan','yash','mayank','gay','imroz'],
        'marks':[90,80,79,67,57],
        'rank':[1,2,3,4,5]}
df=pd.DataFrame(data,index=[ 'student 1','student 2','student 3','student 4','student 5'])
print(df) 

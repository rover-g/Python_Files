import pandas as pd 


sch_input = input('Please enter the path : ')
atnd_input = input('Please enter the path : ')

def sch_data():
    sch = pd.read_csv(sch_input)
    sch.columns = sch.columns.str.replace(" ", "_")
    sch = sch[['Assigned_To','End']]
    sch.sort_values(by = ['Assigned_To','End'], inplace = True ,ascending = [1,0])
    sch.drop_duplicates(subset = ["Assigned_To"], inplace = True)
    return sch

def atnd_data():
    atnd = pd.read_csv(atnd_input)
    atnd.columns = atnd.columns.str.replace(" ", "_")
    atnd = atnd[['Assigned_To','End_Date']]
    atnd = atnd.rename({'End_Date':'End'}, axis = 1)
    atnd.sort_values(by = ['Assigned_To','End'], inplace = True ,ascending = [1,0])
    atnd.drop_duplicates(subset = ["Assigned_To"], inplace = True)
    return atnd

def idle_list():
    idle_data = pd.concat([sch_data(),atnd_data()], axis = 0)
    idle_data.sort_values(by = ['Assigned_To','End'], inplace = True ,ascending = [1,0])
    idle_data.drop_duplicates(subset = ["Assigned_To"], inplace = True)
    return idle_data 

#print(idle_list())
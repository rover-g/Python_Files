import pandas as pd 
import numpy as np
from pathlib import Path
from datetime import datetime
import pandas.io.formats.excel
from pandas.tseries.offsets import DateOffset, BDay

sch_input = input('Please enter the path : ')
atnd_input = input('Please enter the path : ')

def sch_data(): # reads and modifies the scheduled artist data
    sch = pd.read_csv(sch_input)
    sch.columns = sch.columns.str.replace(" ", "_")
    sch = sch[['Assigned_To','End']]
    sch.sort_values(by = ['Assigned_To','End'], inplace = True ,ascending = [1,0])
    sch.drop_duplicates(subset = ["Assigned_To"], inplace = True)
    return sch

def atnd_data(): # reads and modifies the absence data of the artists
    atnd = pd.read_csv(atnd_input)
    atnd.columns = atnd.columns.str.replace(" ", "_")
    atnd = atnd[['Assigned_To','End_Date']]
    atnd = atnd.rename({'End_Date':'End'}, axis = 1)
    atnd.sort_values(by = ['Assigned_To','End'], inplace = True ,ascending = [1,0])
    atnd.drop_duplicates(subset = ["Assigned_To"], inplace = True)
    return atnd

def idle_list(): # concats both the sheet and gives the final output as desired
    idle_data = pd.concat([sch_data(),atnd_data()], axis = 0)
    idle_data.sort_values(by = ['Assigned_To','End'], inplace = True ,ascending = [1,0])
    idle_data.drop_duplicates(subset = ["Assigned_To"], inplace = True)
    idle_data['End'] = pd.to_datetime(idle_data['End'])
    idle_data['Free_from'] = idle_data['End'] + BDay()
    idle_data = (idle_data[['Assigned_To', 'Free_from']])
    idle_data.sort_values(by = ['Free_from'], inplace = True , ascending = True)
    idle_data = idle_data.reset_index()
    idle_data.index = np.arange(1,len(idle_data)+1)
    idle_data = (idle_data[['Assigned_To', 'Free_from']])
    path = Path(r'C:\Users\rahul\Documents\DNEG_Works\Idle_list\New_Idle_Artist_List.xlsx')
    datestring = datetime.now().strftime('%Y-%m-%d')
    exportpath = path.parent/f'{path.stem}-{datestring}{path.suffix}'
    writer = pd.ExcelWriter(exportpath,engine='xlsxwriter',datetime_format='mmm d yyyy')
    idle_data.to_excel(writer, sheet_name = 'Idle_list')
    output = writer.save()
    print('Sucessfully Exported')
    return output

idle_list()
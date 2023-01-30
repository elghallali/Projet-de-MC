# pip install -r requirements.txt
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import glob
import os
import re

# Create Analyse class
class Analyse:

    # Constructor Method
    def __init__(self,location):
        self.__location = location
        self.__excel_files = glob.glob(self.__location+'\\*.xlsx')
        self.__indices_list = ['MASI', 'MSI20']


    # Creation the necessary folders
    def __createNewDirectories(self):
        new_folders = ['Data','images']
        os.chdir(self.__location)
        for i in new_folders:
            if not os.path.exists(self.__location+'\\'+i):
                os.makedirs(i)
            if i == 'images':
                path = self.__location + '\\'+ i
                os.chdir(path)
                for j in self.__indices_list:
                    if not os.path.exists(path+'\\'+j):
                        os.makedirs(j)

    # Ratio Method
    def __ratio(self, dataFrame, indice):
        df = pd.DataFrame()
        dataFrame_list = list(dataFrame.columns)
        df['Date'] = pd.to_datetime(dataFrame['Date'], format='%d/%m/%Y')
        for i in range(3,len(dataFrame_list)):
            df[dataFrame_list[i]] = dataFrame[dataFrame_list[i]] / dataFrame[indice]
        new_data = df.iloc[:,1:].apply(np.mean)
        new_data_index = list(new_data.index)
        new_row = ['Moyenne des ratio']
        for i in new_data_index:
            new_row.append(new_data[i])
        df.loc[255] = new_row
        df.to_excel(f'{self.__location}\\Data\\Ratio{indice}.xlsx', index = False)

    # Correlation Method for creating Excel table
    def __correlation(self, dataFrame, indice):
        df = pd.DataFrame()
        dataFrame_list = list(dataFrame.columns)
        df[indice] = dataFrame[indice]
        for i in range(3, len(dataFrame_list)):
            df[dataFrame_list[i]] = dataFrame[dataFrame_list[i]]
        df_corr = df.corr()
        sns.heatmap(df_corr, cmap='RdBu', center=0, vmin=-1, vmax=1)
        plt.savefig(f'{self.__location}\\images\\Correlation{indice}.png')
        plt.clf()
        df_corr.to_excel(f'{self.__location}\\Data\\Correlation{indice}.xlsx')

    # Correlation Images Method
    def __correlationImage(self, dataFrame, indice):
        dataFrame_list = list(dataFrame.columns)
        for i in range(3, len(dataFrame_list)):
            sns.set()
            sns.regplot(x=dataFrame[indice], y=dataFrame[dataFrame_list[i]], data=dataFrame )
            plt.savefig(f'{self.__location}\\images\\{indice}\\Corr{indice}{dataFrame_list[i]}.png')
            plt.clf()

    # Create Excel files and Images
    def create_files(self):
        self.__createNewDirectories()
        for file in self.__excel_files:
            df = pd.read_excel(file, date_parser='%d/%m/%Y')
            for indice in self.__indices_list:
                self.__ratio(df, indice)
                self.__correlationImage(df, indice)
                self.__correlation(df, indice)

# Create Location path and a list of indexes
def createLocation():
    locationInput = input('Enter files location : ')
    location = locationInput.replace('\\', '\\\\')
    df = pd.read_excel('./MC_DATA_2022.xlsx', date_parser='%d/%m/%Y')
    df.to_excel(f'{location}\\DATA.xlsx', index = False)
    return location





location= createLocation()
analyse1 = Analyse(location)
analyse1.create_files()








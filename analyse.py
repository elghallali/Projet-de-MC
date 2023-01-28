# python pip install pandas
import pandas as pd

# python pip install seaborn
import seaborn as sns

# python pip install matplotlib
import matplotlib.pyplot as plt

# python pip install numpy
import numpy as np
import glob
import os
import re

# Create Analyse class
class Analyse:

    def __init__(self,location, tab):
        self.location = location
        self.excel_files = glob.glob(location+'\\*.xlsx')
        self.indices_list = tab

    # Creation the necessary folders
    def createNewDirectories(self):
        new_folders = ['Data','images']
        os.chdir(self.location)
        for i in new_folders:
            if not os.path.exists(self.location+'\\'+i):
                os.makedirs(i)
            if i == 'images':
                path = location + '\\'+ i
                os.chdir(path)
                for j in self.indices_list:
                    if not os.path.exists(path+'\\'+j):
                        os.makedirs(j)

    # Ratio Method
    def ratio(self, dataFrame, indice):
        df = pd.DataFrame()
        dataFrame_list = list(dataFrame.columns)
        df['Date'] = pd.to_datetime(dataFrame['Date'], format='%d/%m/%Y')
        for i in range(3,len(dataFrame_list)):
            df[dataFrame_list[i]+' / ' + indice] = dataFrame[dataFrame_list[i]] / dataFrame[indice]
        new_data = df.iloc[:,1:].apply(np.mean)
        new_data_index = list(new_data.index)
        new_row = ['Moyenne des ratio']
        for i in new_data_index:
            new_row.append(new_data[i])
        df.loc[255] = new_row
        df.to_excel(f'{self.location}\\Data\\Ratio{indice}.xlsx', index = False)

    # Correlation Method for creating Excel table
    def correlation(self, dataFrame):
        df = pd.DataFrame()
        dataFrame_list = list(dataFrame.columns)
        for i in range(1, len(dataFrame_list)):
            df[dataFrame_list[i]] = dataFrame[dataFrame_list[i]]
        df_corr = df.corr()
        sns.heatmap(df_corr, cmap='RdBu', center=0, vmin=-1, vmax=1)
        plt.savefig(f'{self.location}\\images\\Correlation.png')
        df_corr.to_excel(f'{self.location}\\Data\\Correlation.xlsx')

    # Correlation Images Method
    def correlationImage(self, dataFrame, indice):
        dataFrame_list = list(dataFrame.columns)
        for i in range(3, len(dataFrame_list)):
            sns.set()
            sns.regplot(x=dataFrame[indice], y=dataFrame[dataFrame_list[i]], data=dataFrame )
            plt.savefig(f'{self.location}\\images\\{indice}\\Corr{indice}{dataFrame_list[i]}.png')
            plt.clf()

    # Create Excel files and Images
    def create_files(self):
        for file in self.excel_files:
            df = pd.read_excel(file, date_parser='%d/%m/%Y')
            for indice in self.indices_list:
                self.ratio(df, indice)
                self.correlationImage(df, indice)
            self.correlation(df)

# Create Location path and a list of indexes
def createLocation():
    locationInput = input('Enter files location : ')
    location = locationInput.replace('\\', '\\\\')
    num = int(input('Enter the number of indexes : '))
    tab = []
    for i in range(num):
        indice = input('Enter Index : ')
        tab.append(indice.upper())
    return location,tab

# Create default dataset
def createDataSet(location):
    test = input("Entrer Oui/Yes : si vous necessites une dataset par default et Non/No : sinon : ")
    test = test.lower()
    if test in ['yes', 'oui', 'si']:
        df = pd.read_excel('./MC_DATA_2022.xlsx', date_parser='%d/%m/%Y')
        df.to_excel(f'{location}\\DATA.xlsx', index = False)


location, tab = createLocation()
createDataSet(location)
analyse1 = Analyse(location, tab)
analyse1.createNewDirectories()
analyse1.create_files()








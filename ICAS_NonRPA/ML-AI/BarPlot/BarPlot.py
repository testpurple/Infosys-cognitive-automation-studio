'''
Copyright 2020 Infosys Ltd.
Use of this source code is governed by Apache 2.0 license that can be found in the LICENSE file or at 
https://opensource.org/licenses/Apache-2.0 .
'''
import pandas as pd
import plotly.io as pio
import matplotlib.pyplot as plt
import seaborn as sns
from abstract_bot import Bot
import json

class BarPlot(Bot):


    def bot_init(self):
        pass

    def execute(self, executionContext):
        try:
            file_path = executionContext['csv_path']
            outputfile_path = executionContext['outputfile_path']
            x_axis = executionContext['x_axis']
            y_axis = executionContext['y_axis']
            Title = executionContext['Title']
            
    
            data = pd.read_csv(file_path,sep=',',encoding="latin-1")
            
            
            sns.barplot(x=x_axis, y=y_axis, data=data)
            plt.xticks(rotation=45)
            plt.title(Title)
            #plt.show()

            
            plt.savefig(outputfile_path+"barplot_png",dpi=200)
            return {"status":"success"}
        
        except Exception as e:
            return {'Exception' : str(e)}

if __name__ == "__main__":
    context = {}
    bot_obj = BarPlot()

    # context = {'csv_path':'D:\\Bot_Factory\\testedbots\\dummymedalssheet.csv', "x_axis":"Country","y_axis":"Gold", 
    #             "Title":"Count of medals CountryWise",
    #             'outputfile_path':'D:\\Bot_Factory\\usecases\\'}
    
    context = {'csv_path':'', "x_axis":"","y_axis":"", 
                "Title":"",
                'outputfile_path':''}
    

    bot_obj.bot_init()
    output = bot_obj.execute(context)
    print(output)
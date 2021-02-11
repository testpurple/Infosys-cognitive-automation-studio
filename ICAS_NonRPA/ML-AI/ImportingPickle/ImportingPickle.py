'''
Copyright 2020 Infosys Ltd.
Use of this source code is governed by Apache 2.0 license that can be found in the LICENSE file or at 
https://opensource.org/licenses/Apache-2.0 .
'''
import os
import traceback
import sys
import pickle
from abstract_bot import Bot

# -- bot for Loading the Pickle File from given directory  --
class ImportingPickle(Bot):


    def bot_init(self):
        pass

    def execute(self, executionContext):
        try:
            file_path = executionContext['pickle_file_path']
            file_name = executionContext['pickle_name']

           # open a file, where you stored the pickled data
            file = open(file_path +'/'+ file_name , 'rb')

            # dump information to that file
            data = pickle.load(file)

            # close the file
            file.close()

            return {'pickle output':data}
        except:
          exc_type, exc_value, exc_traceback = sys.exc_info()
          formatted_lines = traceback.format_exc().splitlines()
          return {'Error' : formatted_lines[-1]} 

if __name__ == "__main__":
    context = {}
    bot_obj = ImportingPickle()

    context = {'pickle_file_path':'','pickle_name':''}

    bot_obj.bot_init()
    output = bot_obj.execute(context)
    print(output)
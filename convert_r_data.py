import os
import pandas as pd
import rpy2.robjects as robjects
import pandas.rpy.common as com


def convert_datafiles(datasets_folder):
    '''convert .RData files to .csv files and clean up'''
    for root, dirs, files in os.walk(datasets_folder):
        for name in files:
            if name.endswith('.RData'):
                name_ = os.path.splitext(name)[0]
                name_path = os.path.join(datasets_folder, name_)
                # creat sub-directory
                if not os.path.exists(name_path):
                    os.makedirs(name_path)
                file_path = os.path.join(root, name)
                robj = robjects.r.load(file_path)
                # check out subfiles in the data frame
                for var in robj:
                    myRData = com.load_data(var)
                    # convert to DataFrame
                    if not isinstance(myRData, pd.DataFrame):
                        myRData = pd.DataFrame(myRData)
                    var_path = os.path.join(datasets_folder,name_,var+'.csv')
                    myRData.to_csv(var_path)
                # clean up old data
                os.remove(os.path.join(datasets_folder, name)) 

    print("Success!")

if __name__ == "__main__":
	convert_datafiles('data/')

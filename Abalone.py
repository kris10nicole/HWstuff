def main2(): 
    data_index='http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data' 
    abalone=pd.read_csv(data_index,header=None,names=['sex','length','diameter','height','whole weight','shucked weight','viscera weight','shell weight','rings']) 
    title=abalone.head(0) 
      
    for i in range(0,len(title.columns)): 
        if type(abalone.ix[1,i])==numpy.float64: 
            histogram_outlier(abalone.ix[:,i],title.columns[i]) 

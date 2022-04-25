def loadData():
    data = pd.read_csv('NHANES_combined.csv.gz', header=0, compression='gzip', low_memory=False, engine='c')
    return data
 
def main():
    data = loadData()
    

if __name__ == '__main__':
    main()
from joblib import Parallel, delayed
        
def sample(tag):
    for i in range(1000):
        for j in range(1000):
            print('{} processing'.format(tag))

if __name__=="__main__":
    tags = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
    result = Parallel(n_jobs=-1)([delayed(sample)(tag) for tag in tags]) # check system monitor or htop while execution

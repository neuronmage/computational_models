import ipyparallel as ipp

def howdy(label):
    pd = pandas 
    message = "Howdy, World!"
    file = "{0}.txt".format(label)
    df = pd.DataFrame()
    if os.path.exists(file):
        message = "Sup, World!"
    with open(file, "w") as f:
        f.writelines(message)

with ipp.Cluster(n=4) as rc: ## 4 cores (starts and connects to the local cluster)
    with rc[:].sync_imports():
        import os
        import pandas as pd
        from scipy import stats

    e_all = rc[:] ## getting whatever cores we allow (ideally, p-cores)
    sync_res = e_all.map_sync(howdy, ("H1", "H2", "H3", "H4")) ## using map_sync() means we won't accidently cut off a Ss while iterating



'''import os

path="notebooks/research.ipynb"

dir,file=os.path.split(path)

os.makedirs(dir)

with open(path,"w") as f:
    pass
# test.py file added'''

from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData
 
custdataobj=CustomData()
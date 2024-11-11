# Market_cap_prediction

## Introduction  

This is a information program designed for investors and stock traders. It has 5 functions:  
1. show company profile information  
2. show key financial numbers  
3. get financial reports of selected company
4. do visualization of income and cost of companies  
5. predict the market cap of companies and give recommended valuation based on AI models  

## Dependence
pandas, numpy, joblib, yfinance, matplotlib, os, seaborn  
if no, please download this modules using pip


## Model Explanation
The prediction model is based on Random Forest with RMSE around 1 billion.  
As for the train set, considering that companies with extremely high market cap are not usually having accordingly amazing financial data. For this model which aim is to make reasonable prediction using financial data, these over-valued companies are not conductive for model performance. Therefore, these companies are deleted from the train set as outliers. And the range of market in trainset is 10 billion. So the 1 billion error is acceptable. More often, it is hard to predict the marketcap of company, because the factors are extremely complicated. But this model could give investors a relatively helpful reference.


## Demo
Firstly, change the dir
```bash
cd ./project_folder  
```

Call python3 to run program
```bash
python3 app.py
```
## Initialize the environment

Clone the source code from remote through your preferred protocol.

```bash
# through HTTP
git clone https://github.com/Ivanhandsome777/Market_cap_prediction.git
```



Initialize the Conda env.

```bash
# first time setup
conda env create -f environment.yml
# or update
conda env update -f environment.yml
```

### Activate the Conda environment

```bash
conda activate yjlhandsome
```

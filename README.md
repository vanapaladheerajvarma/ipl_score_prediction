# IPL SCORE PREDICTION

![Python 3.6](https://img.shields.io/badge/Python-3.6-brightgreen.svg) ![Numpy](https://img.shields.io/badge/Library-Numpy-red.svg) ![Pandas](https://img.shields.io/badge/Library-Pandas-yellow.svg) ![Matplotlib](https://img.shields.io/badge/Library-Matplotlib-blue.svg) ![scikit-learnn](https://img.shields.io/badge/Library-Scikit_Learn-pink.svg) ![Flask](https://img.shields.io/badge/Library-Flask-orange.svg)

Predicting The Score of IPL Teams With the Necessary Parameters 


## Understanding Requirement

Here we need to Bulid Machine Learning model such that our model will predict the score of Batting Team or First Innings Score  


 ## Data Agoisition && Data Preparation
 
 **Data Agoisition**
 
 First we need Data to Our Model To Train.Here Fortunately Our[`DataSet`](https://www.kaggle.com/dineshchandthakur/ipl-dataset) is Present in Kaggle
 
 **IPL DATSET Consists of all the matches(per bowl) which are played between 2013-2018**
 
 **Data Prepration**
 
 Here in our Dataset 
 
 
 Number of Data Points=76014
 
 Number of Features =11
 
 Number of Missing Values=0
 
 Number of Duplicates=0
 
 **FEATURES**
 
 |__FEATURES__|__Description__|__Type__|
 |-|-|-|
|__mid__|__Every Unique Match has Unique Mid__|__Int__|
|__date__|__Date of Match__|__Date __|
|__venue__|__Venue of Match__|__Categorical Data__|
|__bat_team__|__Batting Team of Match__|__Categorical Data__|
|__bowl_team__|__Bowling Team of Match__|__Categorical Data__|
|__runs__|__Runs Scored until the Present Ball of Over__|__Int__|
|__wickets__|__Wickets Lost on the Present Ball of Ove __|__Int(<=10)__|
|__overs__|__Present Ball of Over__|__Float(0.1-19.6)__|
|__runs_last_5__|__Runs Scored in Last Five Overs Until Present Ball of Over __|__Int__|
|__wickets_last_5__|__Wickets Lost in Last Five Overs Until Present Ball of Over __|__Int(<=10) __|
|__total__|__Total Runs Scored in the Match__|__Float(0.1-19.6) __|
 
 
 -mid = Every Unique Match has Unique Mid  (Int)
 
 -date = Date of Match  (Date)
 
 -venue= Venue of Match (Categorical Data)
 
 -bat_team=Batting Team of Match (Categorical Data)
 
 -bowl_team = Bowling Team of Match (Categorical Data)
 
 -runs  = Runs Scored on the Present Ball of Over (Int)
 -wickets	=Wickets Lost on the Present Ball of Over
 -overs = Present Ball of Over
 -runs_last_5 = Runs Scored in Last Five Overs Until Present Ball of Over
 -wickets_last_5=Wickets Lost in Last Five Overs Until Present Ball of Over
 -total =Total Runs Score until Prsent Ball of Over
 
 Here among all the Features 
 
 
 
 
 
 ## Exploratory Data Analysis
 
 Here we want to mainly Analyse Two Things
 
 1)**Number of Games Played in Each Venue**
 
 2)**Number of Games Played by Each Team**
 
 ## Modeling
 
  
 
 ## Modeling

 
  ## Evaluation

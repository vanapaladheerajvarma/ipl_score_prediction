# IPL SCORE PREDICTION

Predicting The Score of IPL Teams With the Necessary Parameters 


## Understanding Requirement

Here we need to Bulid Machine Learning model such that given the Venue or Stadium where the Game is Played between Two Teams and also the we need runs,wickets,overs,

runs_last_5	and wickets_last_5 as an input features to the model.So that this model will predict the **TOTAL** Score of the given Batting Team 


 ## Data Agoisition && Data Preparation
 
 Fortunately all the Dat
 
 
 
 ## Exploratory Data Analysis
 
 Here we want to mainly Analyse Two Things
 
 1)**Number of Games Played in Each Venue**
 
 2)**Number of Games Played by Each Team**
 
 ## Modeling
 
  Here main point is it is Character data and Sequence of data is very important.so it is a Time series Problem
  
  i.e for Character data we prefer Neural Netorks {ANN,CNN,Simple RNN,LSTM(Char RNN) etc}
  
  also Sequence of data is very important and length of input is not same {Simple RNN,LSTM(Char RNN) etc}
        
  and also there will be both long and short term dependencies {LSTM(Char RNN)}
        
  So we are using LSTM called Char RNN
  
  ### Char-RNN
  
  * In Char-RNN  if input is c(i) means the output is c(i+1) and this c(i+1) is again input to RNN and output is c(i+2) and it goes on
  
  * Many to Many RNN of same Length.so it has one o/p corresponding to each input
  
  * It may have more than one hidden Layer
 
 ## Modeling

 
  ## Evaluation

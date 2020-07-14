# ipl_score_prediction

# Music-Generation 

Generating new Music using Deep Learning.Here we need to create a Deep Learning Model which can generate "New Music" 


## Understanding Requirement

Here we need to build a Deep Learning Model so that  it can find patterns in the music that humans and should generate 'New Music" with

these types of patterns.

In a nutshell Music is a sequence of musical components/events



 ## Data Agoisition 
 
 Generally music is represented in many formats like sheet-music,abc-notation,MIDI,mp3 files Etc.we can take any type of notation and
 
 create our model.so I am taking abc notation for generation of model.
 
### ABC NOTATION

It consists of 2 parts

* 'Meta Data'

* 'Music'{sequence of characters where character represen music}

so we are downloading dataset in abc notation
 
 
 ## Data Preparation
 
 Here all are characters so we converting each of character to unique number. 
 
 
 
 ## Exploratory Data Analysis
 
 No need of EDA
 
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

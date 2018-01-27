# Named-Entity-Recognition-with-Bidirectional-LSTM-CNNs
  A keras implementation of Bidirectional-LSTM_CNNs for Named-Entity-Recoganition. The original paper can be found at https://arxiv.org/abs/1511.08308

The implementation differs from the original paper in the following ways :
  1) lexicons are not considered
  2) Bucketing is used to speed up the training

# Result 
  The model produces a test F1_score of 90.9 % with 70 epochs. The results produced in the paper for the given architecture is 91.14
  Architecture(BILSTM-CNN with emb + caps)
  
 # Netork Model in paper
 ![alt text](https://raw.githubusercontent.com/kamalkraj/Named-Entity-Recognition-with-Bidirectional-LSTM-CNNs/master/model_on_paper.png)
 
 # Network Model Constructed Using Keras
 ![alt text](https://raw.githubusercontent.com/kamalkraj/Named-Entity-Recognition-with-Bidirectional-LSTM-CNNs/master/model.png)
 
 
 
 
 
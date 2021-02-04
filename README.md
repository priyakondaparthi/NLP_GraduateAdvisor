# NLP_GraduateAdvisor
AI based Graduate adviser using NLP for University 


##Introduction

Natural Language processing(NLP) the ability of machines to understand and interpret human language. 
Sentiment Analysis, Next Sentence Prediction and Question Answering(QA) are the popular applications of NLP. 
The prominence of Question Answering systems is growing in customer centric businesses where customer service is  the focus.  
The success of QA systems is due to the introduction of state-of-the-art BERT(Bidirectional Encoder Representations from Transformers) [1] language model  and SQuAd (Stanford Question Answering Dataset) [2] .  BERT is trained on Wikipedia text and interprets each word in relation to sentence context with human level accuracy.

The project aims  to develop an automated Question Answering system that acts as a graduate advisor and responds to students’ queries.  In contrast to traditional QA systems the project  proposes a novel approach  where users query the system without entering the input context. The final deliverable of project is a web application with an interface that allows students to enter question, select category and view the predicted model response. The dataset for the project is collected with the help of graduate advisors and FAQs section of department website. The project uses BERT  finetuned on SQuAD as baseline  model.   The project employs Jaccard similarity score as the performance metric .



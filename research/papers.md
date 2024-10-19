# Text-to-speech








# Intent extraction
1. paper: Approaches to Text classification ( https://dl.acm.org/doi/pdf/10.1145/3439726),  file:///C:/Users/gichu/Downloads/text%20classificatoion.pdf
    
    - Classical machine learning models typically follow a two-step procedure:
        - Extact hand-crafted features from documents.
        - Use a classifier to make predictions based on these features.
        - Popular hand-crafted features include Bag of Words (BoW) and classification algorithms like Naïve Bayes, SVM, HMM, gradient boosting trees, and random forests.
        - *LIMITATIONS* : 
            - reliance on the hand-crafted features requires tedious feature engineering and analysis to obtain good performance.
            - strong dependence on domain knowledge
            - cannot take full advantage of large amounts of training data, because the features (or feature templates) are pre-defined.


## Intent Classification
1. Paper: https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7463729
    - l method exploits a hybrid feature representation created by combining top-down processing using knowledge-guided patterns with bottom-up processing using a bag-of-tokens model

2. https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8910417
    - In order to classify intents of customers, a dialogue system needs to analyze the incoming messages. The messages are called utterances, or acts-of-speech
    - BoW-NB (Bag of Words with Naive Bayes): Baseline model using word counts (Bag of Words) representation.
        - Ignores word order and uses only unigrams due to lack of bi-gram counts. *this means cant keep track of context, or phrases, but avoids data sparsity as due to infreq bigram counts*
        - Steps:
            - Remove stop words.
            - Apply lemmatization. (reduce to root)

    - Naive Bayes (NB) is efficient during training since it passes through data once.
    - Assumptions:
        - Conditional independence (words are independent given the class).
        - Positional independence (word position doesn't matter).
        - Limitation: Cannot handle unseen words.

    - CBoW-SVM (Continuous Bag of Words with Support Vector Machine):
    - Uses word embeddings (Word2Vec, GloVe, FastText) to create continuous representations of words.
    - Embeddings help the model capture meaning from unseen but similar words.
    - Like BoW, CBoW loses word order information.
    - CBoW creates fixed-size input vectors, independent of utterance length or vocabulary size, which is beneficial for SVM.
    - Two variations considered: Sum of embedding vectors., Average of embedding vectors.

    - suggests hierachichal classification:  During testing, classification begins at the root node, with each classifier's output guiding the selection of the next classifier, continuing until a leaf node is predicted as the final class.

3. Paper : https://arxiv.org/pdf/1903.08268

   *Title: Simple, Fast, Accurate Intent Classification and Slot Labeling for
Goal-Oriented Dialogue System*






### Techniques
1. Paper: https://ieeexplore.ieee.org/abstract/document/8950616
    - BAG OF WORDS:
        - feature representation: Represents a document as a vector of word occurrences for the specified text,
        - Codebook Generation : One of the simple and easy techniques in BoW is applying K-means clustering on all the vectors. There is a center for each cluster, and the codewords will be defined as those centers, and the size of the codebook will be equal to the number of the clusters


2. SLOT Labelling


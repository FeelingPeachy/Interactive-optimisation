# bridge optimisation using evolutionary algorithms and audio interfaces

## Plan
Main components of the project may be:

- Encoding/ representation
- actual bridge render + physics simulation
- fitness function + EA implementation
- voice interface:
    - speech to text
    - text to instruction set


### neccesary simplifications
- considering the bridge in 2D
- simplyfing the physics model, only considering forces like strain, compression, etc...
- inital modelling done with static loads, after which point can experiment with dynamic loads
- similar in essence to bridge poly builder, with two static points on each end, connected by dynamic beams....
- first performing single objective optimisation, to be extended to multi-objective after which

Objectives (may include):
- maximising load distribution
- maximising the load that can be carried before failure
- minimising cost: wheather that is reducing num of beams/ considering diffferent materials with different properties
- ...

### Encoding/ representation of the bridge
- graph representation possible: representing joints as nodes and beams as edges

### actual bridge render + physics simulation
- plan is to use c# with unity


### Evolutionary algorithms


#### fitness function


### voice interface:
---

#### speech-to-text
open source text-to-speech: Project DeepSpeech - 
https://github.com/mozilla/DeepSpeech?utm_source=newsletter&utm_medium=email&utm_campaign=sep29&ref=assemblyai.com

more exghaustive list of open source models: https://www.assemblyai.com/blog/the-top-free-speech-to-text-apis-and-open-source-engines/

#### text to instruction set

- *limited dataset for training could be an isssue, maybe using pretrained models may help*
- given user input how can we determine how to change the state of the system to reflect input and guide the search 
- given that we are likely mapping to a small subset of instructions, constrain speech and use simple text classifcation as opposed to intent extraction, entity extraction, slot filling ... action mapping ....

    1. Intent Extraction 

    Paper: https://dl.acm.org/doi/pdf/10.1145/3366423.3380268

        - goes beyond this limited framework of treat this as a classification task, where each user words is assigned a single intent from a predefined set of categories.
          discovering one or more generic intents from text, even if those intents were not encountered during training
        - Proposes OPINE (OPen INtent Extraction), a domain-agnostic model using:
        - BiLSTM with CRF for sequence tagging of intents.
        - Multi-head self-attention to capture dependencies between distant words.
        - aims to formulate a sequence tagging task over three tags: Action, Object, and None. user intent then consists of a matching pair of an Action phrase and an Object phrase

    Paper: https://arxiv.org/pdf/1902.10909




    paper: Approaches to Text classification ( https://dl.acm.org/doi/pdf/10.1145/3439726)
        
        - Approaches to automatic text classification can be categorized into:
        - Rule-based methods: Utilize pre-defined rules and require deep domain knowledge.
        - Machine learning-based methods: Learn classifications from data using pre-labeled examples.
        - Classical machine learning models typically follow a two-step procedure:
            - Extact hand-crafted features from documents.
            - Use a classifier to make predictions based on these features.
            - Popular hand-crafted features include Bag of Words (BoW) and classification algorithms like Naïve Bayes, SVM, HMM, gradient boosting trees, and random forests.
        
        *Limitations (Tedious feature engineering.)*




### Bridges + physics
----
Defintions:

https://www.ncdot.gov/initiatives-policies/Transportation/bridges/historic-bridges/bridge-types/Pages/truss.aspx#:~:text=%E2%80%8BTruss%20bridges%20are%20characterized,a%20combination%20of%20the%20materials.

https://www.tn.gov/tdot/structures-/historic-bridges/what-is-a-truss-bridge.html

https://aretestructures.com/what-types-of-truss-bridges-are-there-which-to-select/
- constrain to truss Bridges
    - ​Truss bridges are characterized by the joining of numerous relatively small structural members into a series of interconnected triangles.



The joints method determine forces at the truss joints or nodes using FBD’s. The general assumptions to apply this method are:

    (a). All truss elements are considered rigid, they never bend.

    (b). A force applied to the truss structure will only produce compression or tension on the elements.

    (c). Tension - compression forces’ directions are parallel to the elements.

    (d). Any force on a truss element is transmitted to its ends.

    (e). A truss structure in equilibrium means that every joint or node is at equilibrium.

    (f). Once determined the value of a tension or compression force at one of the ends of an element, the complementary force at the other end of the element will be equal but in opposite direction. (equilibrium condition).



- optimistaion of truss brigde example: https://link.springer.com/article/10.3103/S1052618817010149



## where might the interactive element of the EA come about?
- Setting Aspiration levels (desired values for objective functions) and reservation levels (minimum acceptable values) serve as reference points in fitness assessment, allowing the DM to operate within a familiar framework
https://ieeexplore.ieee.org/abstract/document/4282030?casa_token=_PJpCUvIAhgAAAAA:TBMG_COXNNt7ORy9VEH6x2-n-3TRaJM5ETOLjczPwQb6555lJqnGT_g1BQk0_qlf8rEEirthWA

- Enable users to select, mutate, or recombine designs
- enable users to modify rates of mutation/selection
- enable the selection of a set of candidate solutions, or rank them also and give weightings
- local optimisatoins where we can isolate a region in which we choose where to optimise
#Deep Learning Engineer questions

Pick three of these questions, including at least one marked [Code].

* Given different train/test accuracy curves, describe what is going on and how to address it (overfitting, learning rate too high, etc.)


* What is the difference between object classification and detection? How do any related architectures often differ to accomplish these tasks?
  
  
* How do you deal with severely unbalanced data? In what situations might this occur?
https://machinelearningmastery.com/tactics-to-combat-imbalanced-classes-in-your-machine-learning-dataset/
https://towardsdatascience.com/methods-for-dealing-with-imbalanced-data-5b761be45a18


https://forums.fast.ai/t/images-normalization/4058/5   normalize  the image is anothe idea to 

    Putting the data on the same scale (Scaling)
    Balancing the data around a point (Centering)


* How do you reduce overfitting in a neural network? What is regularization, and how does it impact overfitting?
dropout/pooling is only one of the regularization methods

https://machinelearningmastery.com/introduction-to-regularization-to-reduce-overfitting-and-improve-generalization-error/

    Underfitting can easily be addressed by increasing the capacity of the network, but overfitting requires the use of specialized techniques.
    Regularization methods like weight decay provide an easy way to control overfitting for large neural network models.
    A modern recommendation for regularization is to use early stopping with dropout and a weight constraint.

Below is a list of five of the most common additional regularization methods.

    Activity Regularization: Penalize the model during training base on the magnitude of the activations.
    Weight Constraint: Constrain the magnitude of weights to be within a range or below a limit.
    Dropout: Probabilistically remove inputs during training.
    Noise: Add statistical noise to inputs during training.
    Early Stopping: Monitor model performance on a validation set and stop training when performance degrades.

https://machinelearningmastery.com/weight-regularization-to-reduce-overfitting-of-deep-learning-models/

* Say you have collected camera data from a mobile robot in which you would like to denote various objects of multiple classes with bounding boxes. How would you go about annotating these objects in your dataset? How would your answer change if instead of bounding boxes, you used semantic segmentation? What about instance segmentation?
What 
???
* Say you have collected 3D data from a mobile robot in which you would like to denote various objects of multiple classes with bounding boxes. How would you go about annotating these objects in your dataset?
???

* Given a dataset of images or 3D data over time, what do you need to consider in creating training and validation data? How would you create your test set to test a related trained network?
split the training dataset to 60/20/20 or 70/15/15 or 80/10/10, validation data is a good way to monitor the training result. We as machine learning engineers use this data to fine-tune the model hyperparameters.
Validation set may impact training data indirectly as validation set is like a standard. We try to find the model fit these dataset best, although model does not learn directly from it.
1. test set should contain all the categories/classes of the prediction. 
2. Make sure all the data in test set not in train data. Because test set is used to evaluate a final model.
https://towardsdatascience.com/train-validation-and-test-sets-72cb40cba9e7


* Explain the concepts behind Deep Reinforcement Learning, and how you would implement such a technique toward Motion Planning. How would you determine the reward functions to use? Would your implementation generalize well towards new, previously unseen environments?
* Have you deployed any models you have trained and tested into any production systems, or otherwise used on hardware
  outside of the same computer you trained the network on, such as an embedded system? What additional steps did you take to implement the model, and what type of testing did you perform to ensure appropriate performance?
  
* **[Code]** Explain a recent deep learning research paper you read and how it improved upon existing methods. What were its strengths and weaknesses? Code a mock-up of the network used in this paper in your desired deep learning
   library.
* **[Code]** Explain the ResNet neural network architecture. What were some of the key insights of this architecture
  compared to previous approaches, and why do they result in improvements in performance? Code an example of how to use residual layers in your desired deep learning library.
* **[Code]** Explain the GoogLeNet/Inception neural network architecture. What were some of the key insights of this
  architecture compared to previous approaches, and why do they result in improvements in performance? Code an example of how to use inception layers in your desired deep learning library.
* **[Code]** Explain the MobileNet neural network architecture. What were some of the key insights of this architecture
  compared to previous approaches, and why do they result in improvements in speed performance? Code an example of how to implement MobileNet in your desired deep learning library, and compare it to layers in other neural networks, noting why inference speed is improved.
* Describe behavioral cloning. How would you go about gathering quality data for this?
* What is dropout, and what is it used for? Let’s say we have a dropout layer with 50% drop probability. How would you
  scale the inputs/outputs between train and inference time? What if the drop probability is 75%?
* Explain why a convolutional neural network typically performs better on image-related tasks that a fully-connected
  network.
* **[Code]** Why do vanilla convolutional neural networks (just convolutions followed by pooling layers, out into fully -connected layers) often struggle in determining where in an image an object resides, and how have more recent methods improved in this area?
* Explain how backpropagation works.
* **[Code]** Given a dataset of your choosing, code a neural network in a deep learning library of your choice to train a
  model to do some type of inference over the data. Include any pre-processing steps. Explain why you chose the type of inference you did, as well as what you could apply your trained model to do.

Relevant Nanodegree Projects

If you put these on your resume, make sure you know your code and the topic in-depth before the interview!

    Self-Driving Car Engineer - Traffic Sign Classification, Behavioral Cloning and Semantic Segmentation, along with any deep learning-based approaches you may have used on other computer vision projects
    Robotics Software Engineer - Follow Me, Pick and Place with Deep Learning

For bonus points (both in getting the interview and for use in your interview), use the skills you learned in the above projects toward a novel solution to another problem in this area!

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import urllib.request

import numpy as np
import tensorflow as tf

TRAINING = "Training/training.csv"
TEST = "Test/test.csv"

training_set = tf.contrib.learn.datasets.base.load_csv_with_header(
      filename=TRAINING,
      target_dtype=np.int,
      features_dtype=np.float32)
	  
test_set = tf.contrib.learn.datasets.base.load_csv_with_header(
      filename=TEST,
      target_dtype=np.int,
      features_dtype=np.float32)

feature_columns = [tf.contrib.layers.real_valued_column("", dimension=4)]

  
  
classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,
                                              hidden_units=[10, 20, 10],
                                              n_classes=3,
                                              model_dir="/tmp/testing_model")
											  
def training():
  
  def get_train_inputs():
    x = tf.constant(training_set.data)
    y = tf.constant(training_set.target)

    return x, y

  
  classifier.fit(input_fn=get_train_inputs, steps=2000)
  print("Successfully training, you can go to /tmp/testing model to see the training data")
  
  
def evaluate():
  training()
  def get_test_inputs():
    x = tf.constant(test_set.data)
    y = tf.constant(test_set.target)

    return x, y

	
  accuracy_score = classifier.evaluate(input_fn=get_test_inputs,
                                       steps=1)["accuracy"]

  print("\nTest Accuracy: {0:f}\n".format(accuracy_score))

def prediction():
  x1 = input('Enter a x1: ')
  y1 = input('Enter a y1: ')  
  x2 = input('Enter a x2: ')
  y2 = input('Enter a y2: ') 
  
  def testing_line_1():
    return np.array(
      [[x1, y1, x2, y2]], dtype=np.float32)


  def check_line(result):
    if result == [0]:
      return "left to right"
    elif result == [1]:
      return "right to left"
	  
	  
	  
  predictions_1 = list(classifier.predict(input_fn=testing_line_1))
  print (30 * "-" , "RESULT" , 30 * "-")
  print(
      "Result from line 1 :    {}\n"
      .format(check_line(predictions_1)))
	  
  print (67 * "-")  
      
def print_menu():    
    print (30 * "-" , "MENU" , 30 * "-")
    print ("1. Training")
    print ("2. Evaluate")
    print ("3. Prediction !! Make sure u have run menu 1 and 2 at least once !!")
    print ("4. Exit")
    print (67 * "-")
  
loop=True      
  
while loop:        
    print_menu()   
    choice = input("Enter your choice [1-5]: ")
     
    if choice== "1":     
        training()
    elif choice== "2":
        evaluate()
    elif choice== "3":
        prediction()
    elif choice== "4":
        print ("Menu 4 has been selected")
        print ("Exit from the application")
        loop = False
    else:
        print("Wrong option selection. Enter any key to try again..")
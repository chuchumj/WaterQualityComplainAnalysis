# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Minst
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
#from tqdm import trange
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
print("\n Training image data:{}".format(mnist.train.images.shape))
print("\n Validation image data:{}".format(mnist.validation.images.shape))
print("\n Testing image data:{}".format(mnist.test.images.shape))
print("\n Test labels data:{}".format(mnist.test.labels.shape))
num_labels = np.sum(mnist.test.labels, axis = 0, dtype = np.int)
print("\n label distribution: {}".format(list(zip( range(10),num_labels ))))
image = np.reshape(mnist.train.images[1, : ], [28,28])
plt.imshow(image , cmap="gray")

x = tf.placeholder([None, 784], dtype =tf.float32)
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.matmul(x,W)+b
py = tf.nn.softmax(y)



y_ = tf.placeholder([None,10] )
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_*tf.log(py), reduction_indices = [1]))  
train_step = tf.train.GradientDescentOptimizer(0.05).minimize(cross_entropy)


#CREATING NEW SESSION
sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step,feed_dict = {x: batch_xs,y:batch_ys} )
correct_prediction = tf.equal(tf.argmax(py,1), tf.argmax(ylabel,1)) 
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print("test accuracy:{0}".format(sess.run(accuracy, feed_dict={x:mnist.test.images ,ylabel: mnist.test.labels})))

    

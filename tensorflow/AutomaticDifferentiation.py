# Loading necessary libraries
import tensorflow as tf
import numpy as np

'''x = tf.constant([2.0])
with tf.GradientTape(persistent=False, watch_accessed_variables=True) as grad:
  f = x ** 2

# Print gradient output
print('The gradient df/dx where f=(x^2):\n', grad.gradient(f, x))
'''

x = tf.constant([2.0])
x = tf.Variable(x)

with tf.GradientTape(persistent=False, watch_accessed_variables=True) as grad:
  f = x ** 2

# Print gradient output
print('The gradient df/dx where f=(x^2):\n', grad.gradient(f, x))









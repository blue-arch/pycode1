# Import necessary libraries
import tensorflow as tf
import numpy as np

'''tensor = tf.constant(0)
print("Print constant tensor {} of rank {}".format(tensor, tf.rank(tensor)))
print("Show full tensor:", tensor)'''

# NOTE: We use .numpy() to transform tf.tensor to numpy
tensor = tf.constant([1,2,3])
print("Tensor:", tensor)
print("Rank:", tf.rank(tensor).numpy())
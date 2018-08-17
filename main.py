# MENYELESAIKAN PERSAMAAN
# a = (b+c)∗(c+2)
# b = 2.0
# c = 1.0

import tensorflow as tf
import waktuproses

# first, create a TensorFlow constant
const = tf.constant(2.0, name="const")

# create TensorFlow variables
b = tf.Variable(2.0, name='b')
c = tf.Variable(1.0, name='c')

# now create some operations
d = tf.add(b, c, name='d')  # d = b + c
e = tf.add(c, const, name='e')  # e = c + 2
a = tf.multiply(d, e, name='a')  # a = d * e

# setup the variable initialisation
init_op = tf.global_variables_initializer()

# start the session
with tf.Session() as sess:
    # initialise the variables
    sess.run(init_op)
    # compute the output of the graph
    a_out = sess.run(a)
    print("Variable a is {}".format(a_out))
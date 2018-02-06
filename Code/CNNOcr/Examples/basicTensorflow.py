import tensorflow as tf

x = tf.Variable(3,name="x")
y = tf.Variable(4,name="y")

f = x*x*y + y + 2
init = tf.global_variables_initializer()
sess=tf.InteractiveSession()
init.run()
result = f.eval()
print(result)
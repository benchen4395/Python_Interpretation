# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 13:58:24 2017

@author: benchen4395
"""

'''
tf.shape(a)和a.get_shape()比较:
    
相同点：都可以得到tensor(a)的尺寸
不同点：tf.shape()中a 数据的类型可以是tensor, list, array
        a.get_shape()中a的数据类型只能是tensor,且返回的是一个元组（tuple）
'''
import tensorflow as tf
import numpy as np

x=tf.constant([[1,2,3],[4,5,6]])       # x是一个张量+
# 这里注意：直接输出x为：print(x) = Tensor("Const_1:0", shape=(2, 3), dtype=int32)
# 输出x的类型为： print(type(x)) = <class 'tensorflow.python.framework.ops.Tensor'>
y=[[1,2,3],[4,5,6]]                    # y是一个列表，而不是一个数组 type(y)=list
z=np.arange(24).reshape([2,3,4])       # z是一个numpy数组。type(z) = <class 'numpy.ndarray'>

sess=tf.Session()  
# tf.shape()
x_shape=tf.shape(x)                    #  x_shape 是一个tensor,当使用了tf.shape时，与 y_shape同类型
y_shape=tf.shape(y)                    #  <tf.Tensor 'Shape_2:0' shape=(2,) dtype=int32>  
z_shape=tf.shape(z)                    #  <tf.Tensor 'Shape_5:0' shape=(3,) dtype=int32>  
print(sess.run(x_shape))              # 结果:[2 3]  
print(sess.run(y_shape))              # 结果:[2 3]  
print(sess.run(z_shape))              # 结果:[2 3 4]  
  
#a.get_shape()  
x_shape=x.get_shape()  # 返回的是TensorShape([Dimension(2), Dimension(3)]),不能使用 sess.run() 因为返回的不是tensor 或string,而是元组
print(x_shape)   # 返回(2, 3)
x_shape=x.get_shape().as_list()  # 可以使用 as_list()得到具体的尺寸，x_shape=[2 3]  
print(x_shape)   # 返回[2, 3]
y_shape=y.get_shape()  # AttributeError: 'list' object has no attribute 'get_shape'  
z_shape=z.get_shape()  # AttributeError: 'numpy.ndarray' object has no attribute 'get_shape'  

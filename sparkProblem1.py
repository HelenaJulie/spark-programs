# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 19:55:00 2019

@author: helen
"""


import findspark

findspark.init()
import json
import pyspark
from pyspark import SparkConf, SparkContext

conf = SparkConf()
conf.setMaster("spark://169.254.124.97:7077")
conf.setAppName("Output")
sc = SparkContext(conf = conf)

reviewdata=sc.textFile(r'C:\Users\helen\Desktop\sparkhomework\review.data')
def cmp(i):
 x = json.loads(i)
 if(100 < len(x["reviewText"].split())):
  return True
 else:
  return False

compare = reviewdata.filter(cmp)
x = compare.groupBy(lambda i: json.loads(i)['overall'])

combine = x.map(lambda i: [j for j in i[1]])

combine.saveAsTextFile(r"C:\Users\helen\Desktop\sparkhomework\Outputreview")
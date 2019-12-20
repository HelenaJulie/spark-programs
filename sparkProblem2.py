# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 20:39:16 2019

@author: helen
"""

import findspark

findspark.init()
import json
import pyspark
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

import pyspark.sql.functions as f


conf = SparkConf()
conf.setMaster("spark://169.254.124.97:7077")
conf.setAppName("pypy")
sc = SparkContext(conf = conf)
    
sqlContext = SQLContext(sc)

metadata = sqlContext.read.json(r"C:\Users\helen\Desktop\sparkhomework\meta.data")
reviewdata = sqlContext.read.json(r"C:\Users\helen\Desktop\sparkhomework\review.data")

x=reviewdata.join(metadata, reviewdata.asin == metadata.asin).select(reviewdata["*"],metadata["categories"])



musicreviews=x.filter(x.categories=="Music")
musicreviews = musicreviews.withColumn('wordCount', f.size(f.split(f.col('reviewText'), ' ')))

musicreviews.groupBy().avg('wordcount').collect()
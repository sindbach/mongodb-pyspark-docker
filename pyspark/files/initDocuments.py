
''' Load the content of times.json and load into the database to initiate data '''
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
import sys
import json
from bson import json_util

def project(doc):
    j = json.loads(doc, object_hook=json_util.object_hook)                              
    return {"doc": str(j["doc"]), "myid": j["myid"], "timestamp": j["timestamp"]}

sparkConf = SparkConf().setMaster("local").setAppName("MongoSparkConnectorTour").set("spark.app.id", "MongoSparkConnectorTour")
#If executed via pyspark, sc is already instantiated
sc = SparkContext(conf=sparkConf)
sqlContext = SQLContext(sc)
dfi = sqlContext.read.format("com.mongodb.spark.sql.DefaultSource")\
                    .option("spark.mongodb.input.uri", "mongodb://mongodb:27017/spark.times")\
                    .load()

if (dfi.count()<1) :
    times = sc.textFile("times.json")
    converted = times.map(project)
    dfo = sqlContext.createDataFrame(converted)
    dfo.write.format("com.mongodb.spark.sql")\
            .option("spark.mongodb.output.uri", "mongodb://mongodb:27017/spark.times")\
            .save()
    print("Documents inserted.")
else :
    print("Database 'spark' collection 'times' is not empty. Maybe you've loaded a data into the collection previously ? skipping process. ")

sys.exit(0)
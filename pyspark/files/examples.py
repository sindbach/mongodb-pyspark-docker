
import sys
from pyspark.sql import SQLContext
from pyspark import SparkContext, SparkConf

sparkConf = SparkConf().setMaster("local").setAppName("MongoSparkConnectorTour").set("spark.app.id", "MongoSparkConnectorTour")

#If executed via pyspark, sc is already instantiated
sc = SparkContext(conf=sparkConf)
sqlContext = SQLContext(sc)

# create and load dataframe from MongoDB URI
df = sqlContext.read.format("com.mongodb.spark.sql.DefaultSource")\
                    .option("spark.mongodb.input.uri", "mongodb://mongodb:27017/spark.times")\
                    .load()

# print data frame schema
df.printSchema()

# convert dataframe to rdd 
rdd = df.rdd 
rdd.first()

# Filter by Integer and by String
df.filter(df["myid"] < 2).show()
df.filter(df["doc"] == "V ").show()

# DataFrames SQL example 
df.registerTempTable("temporary")
sqlResult = sqlContext.sql("SELECT myid, doc, timestamp FROM temporary WHERE myid > 6 AND doc='V '")
sqlResult.show()

# Save out the filtered DataFrame result
sqlResult.write.format("com.mongodb.spark.sql.DefaultSource")\
        .option("spark.mongodb.output.uri", "mongodb://mongodb:27017/spark.output")\
        .mode("overwrite")\
        .save()

# Read it back in to confirm 
df = sqlContext.read.format("com.mongodb.spark.sql.DefaultSource")\
                    .option("spark.mongodb.input.uri", "mongodb://mongodb:27017/spark.output")\
                    .load()
df.show()

print("Done")
sys.exit(0)
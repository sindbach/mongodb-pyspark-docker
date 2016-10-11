# Docker for MongoDB and Apache Spark (Python)

An example of docker-compose to set up a single [Apache Spark](http://spark.apache.org/) node connecting to [MongoDB](https://www.mongodb.com/) via [MongoDB Spark Connector](https://github.com/mongodb/mongo-spark)

For the Scala equivalent example see [mongodb-spark-docker](https://github.com/sindbach/mongodb-spark-docker).

** For demo purposes only **

#### Environment : 

* Ubuntu v16.04
* Apache Spark v2.0.1
* MongoDB Spark Connector v2.0.0-rc0
* MongoDB v3.2.x
* Python v2.7.x

### Starting up 

You can start by running command : 

```
docker-compose run pyspark bash
```

Which would run the spark node and the mongodb node, and provides you with bash shell for the pyspark. 

From the spark instance, you could reach the MongoDB instance using `mongodb` hostname. 

You can find a small dataset example in `/home/ubuntu/times.json` which you can load using [initDocuments.py](pyspark/files/initDocuments.py) :

```
pyspark --packages org.mongodb.spark:mongo-spark-connector_${SCALA_VERSION}:${MONGO_SPARK_VERSION} ./initDocuments.py
```


For example, please see [examples.py](pyspark/files/examples.py) load dataframes and write back to mongodb. This file will also be available inside of the pyspark container in `/home/ubuntu/examples.py`

Run the `pyspark` by executing: 

```sh
pyspark --packages org.mongodb.spark:mongo-spark-connector_${SCALA_VERSION}:${MONGO_SPARK_VERSION}
```

To set session wide option you can also specify: 

```
pyspark --conf "spark.mongodb.input.uri=mongodb://mongodb:27017/spark.times" --conf "spark.mongodb.output.uri=mongodb://mongodb/spark.output" --packages org.mongodb.spark:mongo-spark-connector_${SCALA_VERSION}:${MONGO_SPARK_VERSION} 
```

You can also append `<file.py>` to execute a python file via spark-submit. For example: 

```sh
spark-submit --packages org.mongodb.spark:mongo-spark-connector_${SCALA_VERSION}:${MONGO_SPARK_VERSION} ./examples.py 
```

### More Information. 

See related article:

* [MongoDB Spark Connector](https://docs.mongodb.com/spark-connector/)

* [MongoDB Course M233: Getting Started with Spark and MongoDB](https://university.mongodb.com/courses/M233/about)



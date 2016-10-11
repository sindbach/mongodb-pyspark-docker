
# set data : You can run use initDocuments.scala to import using Spark itself.
spark-submit --packages org.mongodb.spark:mongo-spark-connector_${SCALA_VERSION}:${MONGO_SPARK_VERSION} ./initDocuments.py

# Run spark-shell 
pyspark --conf "spark.mongodb.input.uri=mongodb://mongodb:27017/spark.times" --conf "spark.mongodb.output.uri=mongodb://mongodb/spark.output" --packages org.mongodb.spark:mongo-spark-connector_${SCALA_VERSION}:${MONGO_SPARK_VERSION}

# Or you can run python file through the shell by specifying `<file.py>`. For example to run `examples.py`: 
spark-submit --packages org.mongodb.spark:mongo-spark-connector_${SCALA_VERSION}:${MONGO_SPARK_VERSION} ./examples.py


# start 1 master/worker
${SPARK_HOME}/sbin/start-master.sh
${SPARK_HOME}/sbin/start-slave.sh spark://spark:7077

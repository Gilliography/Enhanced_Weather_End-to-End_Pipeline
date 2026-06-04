from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder \
    .appName("WeatherStreaming") \
    .getOrCreate()

schema = StructType([
    StructField("time", StringType()),
    StructField("temperature_2m", DoubleType()),
    StructField("relative_humidity_2m", DoubleType()),
    StructField("pressure_msl", DoubleType()),
    StructField("rainfall", DoubleType())
])

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "weather-events") \
    .option("startingOffsets", "latest") \
    .load()

weather_df = df.selectExpr("CAST(value AS STRING)")

query = weather_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
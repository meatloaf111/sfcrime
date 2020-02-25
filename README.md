# sfcrime
SF Crime Project Files

# Step 3 Answers
### How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

### What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?

I added following conf.

        .config("spark.streaming.kafka.maxRatePerPartition","100") \
        .config("spark.executor.memory","2g") \
        .config("spark.default.parallelism","2") \

This led to increase "inputRowsPerSecond" from 5.866 to 7.88

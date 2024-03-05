from pyspark.sql import SparkSession

# Define the path to the Wikiticker data
data_path = "s3://batch-processing-bucket/source-folder/wikiticker-2015-09-12-sampled.json"

# Specify the output path in S3
output_path = "s3://batch-processing-bucket/data-output/filtered"

def main():
    # Initialize a Spark session
    spark = SparkSession.builder.appName('FilterWikitickerData').getOrCreate()
    
    # Load the data into a DataFrame
    df = spark.read.json(data_path)
    
    # Apply filters to the DataFrame
    filtered_df = df.filter((df.cityName == "London") & (df.delta > 20))
    
    # Print the total count of records after filtering
    count = filtered_df.count()
    print(f"Total count of records after filtering: {count}")
    
    # Print the first 5 rows of the filtered DataFrame
    print("First 5 rows of the filtered data:")
    filtered_df.show(5)
    
    # Print the schema of the filtered DataFrame
    print("Schema of the filtered data:")
    filtered_df.printSchema()
    
    # Write the filtered data to S3 (in parquet format)
    filtered_df.write.mode('overwrite').parquet(output_path)
    
    print("Filtered data has been written to S3 successfully")

if __name__ == "__main__":
    main()

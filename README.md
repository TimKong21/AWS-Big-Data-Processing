# AWS Big Data Processing

## Overview

This project demonstrates the process of big data analysis using AWS services, focusing on filtering and analyzing the [Wikiticker dataset](https://github.com/apache/druid/blob/master/examples/quickstart/tutorial/wikiticker-2015-09-12-sampled.json.gz). Utilizing technologies such as Amazon EMR, S3, Glue, and Athena, it showcases an end-to-end pipeline from data processing with Spark to data storage, cataloging, and querying.

<p align="center">
  <img src="https://projex.gumlet.io/aws-project-for-batch-processing-with-pyspark-on-aws-emr/images/image_651651421652557979282.png?w=1242&dpr=1.0" alt="Intro image" width="80%"/>
</p>

## Project Structure

```bash
AWS Big Data Processing
├── Code/
│   └── filter.py                               # Spark job script for processing the dataset
├── Data/
│   ├── datatypes.json                          # Schema definition for AWS Glue catalog table
│   └── wikiticker-2015-09-12-sampled.json      # Sampled Wikiticker dataset for analysis
└── Project Documentation.pdf                   # Detailed project documentation
```

## Getting Started

### Prerequisites

- AWS account with access to EMR, S3, Glue, and Athena services.
- AWS CLI installed and configured.

### Setup and Execution

1. **Prepare the Data**: Upload the `wikiticker-2015-09-12-sampled.json` file to your S3 bucket.

2. **Launch an EMR Cluster**: Refer to the `Project Documentation.pdf` for detailed instructions on setting up the EMR cluster.

3. **Run the Spark Job**:
   - SSH into the EMR master node.

   - Use `vi` to create and edit `filter.py` directly on the node:
     ```bash
     vi filter.py
     ```

   - Insert the Spark script content into `filter.py`. Exit and save the file by typing `:wq!`.

   - Execute the script using Spark-submit:
     ```bash
     spark-submit filter.py
     ```
     
4. **Catalog the Data**: Use the provided `datatypes.json` to create a schema in AWS Glue for the filtered dataset.

5. **Query with Athena**: Following the setup in Glue, use Athena to execute queries against your data.

### Cleaning Up

Ensure to terminate the EMR cluster and delete any unused resources in S3 to avoid unnecessary charges.

## Further Information

For detailed instructions, configuration options, and best practices, refer to the `Project Documentation.pdf` included in this repository.

## References

The following resources provide foundational lab exercises that inspired the tasks and structure of this project:

- **[Spark Job for Filtering and Processing Wikiticker Data](https://www.projectpro.io/hands-on-labs/spark-job-for-filtering-data)**: Details the tasks in developing a Spark job for data filtering, similar to the approach taken in this project.
- **[Create Glue Catalog Table and Query Data in AWS Athena](https://www.projectpro.io/hands-on-labs/aws-glue-catalog-table-example)**:  Details the process of creating a Glue catalog table and using Athena for querying, as implemented in the workflow of this project.
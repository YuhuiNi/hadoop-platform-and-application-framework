1.How can you create an RDD? Mark all that apply

- Reading from a local file available both on the driver and on the workers
- Reading from HDFS
- Apply a transformation to an existing RDD

2.How does Spark make RDDs resilient in case a partition is lost?

- Tracks the history of each partition and reruns what is needed to restore it

3.Which of the following sentences about flatMap and map are true?

- flatMap accepts a function that returns multiple elements, those elements are then flattened out into a continuous RDD.
- map transforms elements with a 1 to 1 relationship, 1 input - 1 output

4.Check all wide transformations

- Repartition, even if it triggers a shuffle, can improve performance of your pipeline by balancing the data distribution after a heavy filtering operation




1.Check all true statements about the Directed Acyclic Graph Scheduler

- The DAG is managed by the cluster manager
- A DAG is used to track dependencies of each partition of each RDD

2.Why is building a DAG necessary in Spark but not in MapReduce?

- Because MapReduce always has the same type of workflow, Spark needs to accommodate diverse workflows.

3.What are the differences between an action and a transformation? Mark all that apply

- A transformation is from worker nodes to worker nodes, an action between worker nodes and the Driver (or a data source like HDFS)
- A transformation is lazy, an action instead executes immediately.

4.Generally, which are good stages to mark a RDD for caching in memory?

- The first RDD, just after reading from disk, so we avoid reading from disk again.
- At the start of an iterative algorithm.

5.What are good cases for using a broadcast variable? Mark all that apply

- Copy a small/medium sized RDD for a join
- Copy a large lookup table to all worker nodes
- Copy a large configuration dictionary to all worker nodes

6.We would like to count the number of invalid entries in this example dataset:

```
invalid = sc.accumulator(0)
d = sc.parallelize(["3", "23", "S", "99", "TT"]).foreach(count_invalid)
```

What would be a good implementation of the count_invalid function?

```
def count_invalid(element):
    try:
        int(element)
    except:
        invalid.add(1)
```




 
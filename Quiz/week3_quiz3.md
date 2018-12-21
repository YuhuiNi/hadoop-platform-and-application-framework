1.Name the configuration file which holds HDFS tuning parameters

- hdfs-site.xml

2.Name the parameter that controls the replication factor in HDFS:

- dfs.replication

3.Check answers that apply when replication is lowered

- HDFS is less robust
- less likely make data local to more workers
- more space


4.Check answers that apply when NameNode fails to receive heartbeat from a DataNode

- DataNode is marked dead
- No new I/O is sent to particular DataNode that missed heartbeat check
- Blocks below replication factor are re-replicated on other DataNodes

5.How is data corruption mitigated in HDFS

- checksums are computed on file creation and stored in HDFS namespace for verification when data is retrieved.
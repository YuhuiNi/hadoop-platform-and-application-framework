1.Which of these kinds of data motivated the Map/Reduce framework?

- Large number of internet documents that need to be indexed for searching by words

2.What is the organizing data structure for map/reduce programs?

- A list of identification keys and some value associated with that identifier

3.In map/reduce framework, which of these logistics does Map/Reduce do with the map function?

- Distribute map to cluster nodes, run map on the data partitions at the same time

4.Map/Reduce performs a ‘shuffle’ and grouping. That means it...

- Shuffles <key,value> pairs into different partitions according to the key value, and sorts within the partitions by key.

5.In the word count example, what is the key?

- The word itself.

6.Streaming map/reduce allows mappers and reducers to be written in what languages:

- All of the above

7.The assignment asked you to run with 2 reducers. When you use 2 reducers instead of 1 reducer, what is the difference in global sort order?

- With 1 reducer, but not 2 reducers, the word counts are in global sort order by word.





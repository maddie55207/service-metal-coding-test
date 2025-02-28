---- Database Design ----

For this portion of the test, I used the following product:
https://www.pvcfittingsonline.com/4004-012ab-1-1-4-schedule-40-pvc-pipe-5-ft-section.html#

I've included screenshots of the schema and indices of each table in MySQL as well as a diagram to more easily visualize how the tables connect to one another. 

I designed four tables in order to render the product: product_categories, products, products_questions, and product_reviews. Each of these tables has a uuid as a primary key to serve as an internal id, as well as a friendly identifier, or slug, that can be used as a url parameter for each product. I also utilized foreign keys to reference data from other tables where necessary. Finally, in addition to their primary keys automatically serving as indices, I also created indexes in each table for the slug field (as this value will likely be frequently used to query the table) as well as indexes on any foreign key columns in order to optimize JOIN queries.

---- API Interaction ----

While the provided JSONPlaceholder url only contains 200 entries, I decided to sort by most recent upon retrieval in the event that more were added at any point. Since JSONPlaceholder, as stated in the documentation, does not actually update on the server, I made sure to rely on checking the status codes to ensure that each operation was successful.

---- Algorithms ----

I initially approached this problem using a multi-loop implementation before deciding that recursion would offer a cleaner solution. I've also provided two sample input files: permutations_input.txt, which is a replication of the example provided in the instructions, and permutations_input2.txt, which consists of strings meant to test the cases of different lengths and the ordering of digits/uppercase/lowercase.





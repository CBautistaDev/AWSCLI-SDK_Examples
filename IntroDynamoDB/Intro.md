# Lab Overview
Amazon DynamoDB is a fast and flexible NoSQL database service for all applications that need consistent, single-digit millisecond latency at any scale. It is a fully managed database and supports both document and key-value data models. Its flexible data model and reliable performance make it a great fit for mobile, web, gaming, ad-tech, IoT, and many other applications.

In this lab, you will create a table in Amazon DynamoDB to store information about a music library. You will then query the music library and, finally, delete the DynamoDB table.

# Topics covered
In this lab, you will:

Create an Amazon DynamoDB table
Enter data into an Amazon DynamoDB table
Query an Amazon DynamoDB table
Delete an Amazon DynamoDB table


# Task 1: Create a New Table
In this task, you will create a new table in DynamoDB named Music. Each table requires a Primary Key that is used to partition data across DynamoDB servers. A table can also have a Sort Key. The combination of Primary Key and Sort Key uniquely identifies each item in a DynamoDB table.

In the AWS Management Console, click Services, then click DynamoDB.

Click Create table.

For Table name, type: 
Music

For Primary key, type 
Artist
 and leave String selected.

Select  Add sort key, then in the new field type 
Song
 and leave String selected.

Your table will use default settings for indexes and provisioned capacity.

Click Create.
The table will be created in less than a minute.

# Task 2: Add Data
In this task, you will add data to the Music table. A table is a collection of data on a particular topic.

Each table contains multiple items. An item is a group of attributes that is uniquely identifiable among all of the other items. Items in DynamoDB are similar in many ways to rows in other database systems. In DynamoDB, there is no limit to the number of items you can store in a table.

Each item is composed of one or more attributes. An attribute is a fundamental data element, something that does not need to be broken down any further. For example, an item in a Music table contains attributes such as Song and Artist. Attributes in DynamoDB are similar columns in other database systems, but each item (row) can have different attributes (columns).

When you write an item to a DynamoDB table, only the Primary Key and Sort Key (if used) are required. Other than these fields, the table does not require a schema. This means that you can add attributes to one item that may be different to the attributes on other items.

Click the Items tab, then click Create item.
 If the table is still being created, refresh the web page to display the Items tab.

For Artist String, type: 
Pink Floyd

For Song String, type: 
Money

These are the only required attributes, but you will now add additional attributes.

To create an additional attribute, click the plus sign  to the left of Song, then click Append.
Append

In the drop-down list, select String.
A new attribute row will be added.

For the new attribute, enter:
In FIELD, type: 
Album
In VALUE, type: 
The Dark Side of the Moon
Add another new attribute by clicking the plus sign  to the left Album, then click Append.

In the drop-down list select Number.

A new number attribute will be added.

For the new attribute, enter:
In FIELD, type: 
Year
In VALUE, type: 
1973
Click Save to store the new Item with its four attributes.
The item will appear in the console.

Now create a second Item, using these attributes:
Attribute Name	Attribute Type	Attribute Value
Artist	String	John Lennon
Song	String	Imagine
Album	String	Imagine
Year	Number	1971
Genre	String	Soft rock
Note that this item has an additional attribute called genre. This is an example of each item being capable of having different attributes without having to pre-define a table schema.

Create a third Item, using these attributes:
Attribute Name	Attribute Type	Attribute Value
Artist	String	Psy
Song	String	Gangnam Style
Album	String	Psy 6 (Six Rules), Part 1
Year	Number	2011
LengthSeconds	Number	219
Once again, this item has a new LengthSeconds attribute identifying the length of the song. This demonstrates the flexibility of a NoSQL database.

There are also faster ways to load data into DynamoDB, such as using AWS Data Pipeline, programmatically loading data or using one of the free tools available on the Internet.

# Task 3: Modify an Existing Item
You now notice that there is an error in your data. In this task, you will modify an existing item.

Click Psy.

Change the Year from 2011 to 2012.

Click Save.

The item is now updated.

# Task 4: Query the Table
There are two ways to query a DynamoDB table: Query and Scan.

A query operation finds items based on Primary Key and optionally Sort Key. It is fully indexed, so it runs very fast.

Click the drop-down list showing Scan (located below the Create item button) and change it to Query.
Fields for the Partition Key (which is the same as Primary Key) and Sort Key are now displayed.

Enter these details:
Partition key: 
Psy
Sort key: 
Gangnam Style
Click Start search. (You might need to scroll down to see it.)
The song quickly appears in the list. A query is the most efficient way to retrieve data from a DynamoDB table.

Alternatively, you can scan for an item. This involves looking through every item in a table, so it is less efficient and can take significant time for larger tables.

Click the drop-down list showing Query and change it back to Scan.

Click  Add filter, then:

Scan

For Enter attribute, type: 
Year
Change String to Number
For Enter value, type: 
1971
Click Start search
Only the song released in 1971 is displayed.

# Task 5: Delete the Table
In this task, you will delete the Music table, which will also delete all the data in the table.

Click Delete table. On the confirmation panel, type Delete and then click on Delete
The table will be deleted.

End Lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

On the navigation bar, choose AWSLabsUser, and then choose Sign Out.

Choose End lab and then confirm that you want to end your lab.

Conclusion
 Congratulations! You have now successfully learned how to:

Create an Amazon DynamoDB table
Enter data into an Amazon DynamoDB table
Query an Amazon DynamoDB table
Delete an Amazon DynamoDB table
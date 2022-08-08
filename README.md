### DATA FLOW -- PYTHON


In the chart shown, 1 is the request to the internet to retrieve the data, 2 is the recording of the result of the request in the database, 3 is the request to the database in line with the analysis, and finally 4 is the result of the optional query from the database.

Let us now consider these stages one by one.

1) Making a request to the website

In order to make a request to the website, first of all, there is a need for a driver that the internet system can understand. Since we will use Google as the internet environment here, we first need to import the ChromeDriverManager into our working environment.

Afterwards, we need the host name of the website that we have specified specifically because the driver will first access the site from there.
For example 'https://www.worlddata.info/richest-countries.php'

There is only one step left to pull the data from the website. That is, we find the XPath information of the data we want to extract. After clicking "inspect" the website for the XPath information, you will have access to the necessary information when you click "copy" in the window that opens.

After completing these operations, you can run the script you wrote to extract the data.

Now we have data and we need to convert it to a dataframe to make it more readable.
2) Saving the captured data to the database

In order to start this process, you must first make the necessary settings to connect to the database or write it as a script.

As it is known, data is saved in rows in databases such as MySQL. For this, a method must be written in order to read the data we have previously taken from the internet as row-row. You can easily find this method on places like stackoverflow.

Afterwards, the Schema, in which the data will be recorded, must be created in the required database. As at the point of connecting to the database, you can handle the operations here by writing a script.

Now that you have a Schema where you can save the data, all that remains is to create a new table and transfer the data there with the necessary steps. Again, you can learn and apply the "CREATE" and "INSERT INTO" operations that need to be done in this step, from the internet.

After the last "INSERT" operation, all of your data will be saved in your database.

3) Sending a request in line with the analysis to be made to the database

In order to start this process, you must first make the necessary settings to connect to the database or write it as a script.

Then you can make different queries to the database in line with the features you want to analyze.


4) Evaluation of query results
It can be used in analysis operations as desired by converting query results to dataframe.



Finally 

Different technologies are used in order to periodically renew the processes from data flow to analysis and to constantly update the analyzes.

As an example, Python's schedule library is used here.


Soon 
After reading this document and going through the keywords in it once again, you have learned how to make a data flow on your own. If you've read this far, THANKS...

